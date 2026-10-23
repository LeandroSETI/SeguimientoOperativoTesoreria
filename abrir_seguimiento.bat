@echo off
cd /d "%~dp0"

where py >nul 2>1
if not errorlevel 1 (
    py -3.12 servir_seguimiento.py --open
    exit /b %errorlevel%
)

where python >nul 2>1
if not errorlevel 1 (
    python servir_seguimiento.py --open
    exit /b %errorlevel%
)

echo No se encontró Python en el sistema.
echo Instala Python 3.12 o usa el launcher 'py'.
pause
exit /b 1
