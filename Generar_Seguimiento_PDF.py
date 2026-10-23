"""Genera un PDF desde SeguimientoOperativo.html usando un JSON actualizado.

Instalación inicial:
    pip install playwright
    playwright install chromium

Uso normal:
    python Generar_Seguimiento_PDF.py

Uso con rutas personalizadas:
    python Generar_Seguimiento_PDF.py --json Contexto_HAs_JSON_Ejemplo.json --output Reporte.pdf
"""
from __future__ import annotations
import argparse, json
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
ROOT=Path(__file__).resolve().parent
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None: pass

def parse_args():
    default_json=ROOT/"Contexto_HAs_JSON.json"
    example_json=ROOT/"Contexto_HAs_JSON_Ejemplo.json"
    if not default_json.exists() and example_json.exists():
        default_json=example_json
    p=argparse.ArgumentParser(description="Genera el seguimiento operativo en PDF")
    p.add_argument("--html",type=Path,default=ROOT/"SeguimientoOperativo.html")
    p.add_argument("--json",type=Path,default=default_json)
    p.add_argument("--output",type=Path,default=None)
    return p.parse_args()

def validate(path:Path):
    data=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data.get("sprint"),dict): raise ValueError("Falta el objeto sprint")
    if not isinstance(data.get("items"),list): raise ValueError("Falta la lista items")
    for n,item in enumerate(data["items"],1):
        if not item.get("id"): raise ValueError(f"El elemento {n} no tiene id")
    return data

def default_output_path(data:dict)->Path:
    sprint=data["sprint"].get("numero")
    sprint_name=str(sprint).strip() if sprint is not None and str(sprint).strip() else "-"
    return ROOT/f"Reporte Seguimiento Operativo {sprint_name}.pdf"

def next_output_path(path:Path)->Path:
    path.parent.mkdir(parents=True,exist_ok=True)
    sequence=1
    while True:
        candidate=path.with_name(f"{path.stem}_{sequence:03d}{path.suffix}")
        try:
            candidate.touch(exist_ok=False)
            return candidate
        except FileExistsError:
            sequence+=1

def main():
    a=parse_args();html=a.html.resolve();js=a.json.resolve()
    for f in (html,js):
        if not f.is_file(): print(f"Error: no existe {f}");return 1
    try:
        data=validate(js)
        out=(a.output or default_output_path(data)).resolve()
    except Exception as e: print(f"JSON inválido: {e}");return 1
    expected=html.parent/"Contexto_HAs_JSON.json"
    backup=None
    if js!=expected and expected.exists() and js.name != expected.name:
        backup=expected.read_bytes()
    if js!=expected and not expected.exists() and js.name=="Contexto_HAs_JSON_Ejemplo.json":
        expected.write_bytes(js.read_bytes())
    elif js!=expected and js.name != expected.name:
        if expected.exists(): backup=expected.read_bytes()
        expected.write_bytes(js.read_bytes())
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
    except ImportError:
        print("Falta Playwright. Ejecuta: pip install playwright && playwright install chromium");return 1
    server=ThreadingHTTPServer(("127.0.0.1",0),partial(QuietHandler,directory=str(html.parent)))
    Thread(target=server.serve_forever,daemon=True).start()
    output_created=False
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch()
            page=browser.new_page(viewport={"width":1200,"height":1600})
            page.goto(f"http://127.0.0.1:{server.server_port}/{html.name}",wait_until="domcontentloaded")
            try: page.wait_for_function("document.body.dataset.reportReady === 'true' || document.body.dataset.reportReady === 'error'",timeout=30000)
            except PlaywrightTimeoutError: raise RuntimeError("El reporte no terminó de cargar")
            if page.locator("body").get_attribute("data-report-ready")!="true": raise RuntimeError(page.locator(".empty").first.inner_text())
            out=next_output_path(out)
            output_created=True
            page.pdf(path=str(out),format="A4",print_background=True,prefer_css_page_size=True,margin={"top":"0","right":"0","bottom":"0","left":"0"})
            browser.close()
    except Exception as e:
        if output_created:
            out.unlink(missing_ok=True)
        print(f"Error al generar PDF: {e}");return 1
    finally:
        server.shutdown();server.server_close()
        if js!=expected:
            if backup is None: expected.unlink(missing_ok=True)
            else: expected.write_bytes(backup)
    print(f"PDF generado: {out}");return 0
if __name__=="__main__": raise SystemExit(main())
