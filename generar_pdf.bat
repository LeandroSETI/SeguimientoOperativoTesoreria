@echo off
cd /d "%~dp0"

set "JSON_FILE=Contexto_HAs_JSON.json"
set "JSON_EXAMPLE=Contexto_HAs_JSON_Ejemplo.json"

if not exist "%JSON_FILE%" if exist "%JSON_EXAMPLE%" (
    set "JSON_FILE=%JSON_EXAMPLE%"
)

where py >nul 2>1
if not errorlevel 1 (
    py -3.12 "Generar_Seguimiento_PDF.py" --json "%JSON_FILE%"
    exit /b %errorlevel%
)

where python >nul 2>1
if not errorlevel 1 (
    python "Generar_Seguimiento_PDF.py" --json "%JSON_FILE%"
    exit /b %errorlevel%
)

echo No se encontró Python en el sistema.
echo Instala Python 3.12 o usa el launcher 'py'.
pause
exit /b 1
