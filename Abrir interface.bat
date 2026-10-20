@echo off
rem Abre a interface do Monitor de Promessas no navegador.
rem Atualiza os dados (scripts\build.py), liga o servidor local e abre http://localhost:8765/.
rem Para desligar, feche esta janela.
chcp 65001 >nul
title Monitor de Promessas - interface
cd /d "%~dp0"

echo Atualizando os dados...
python -I scripts\build.py
if errorlevel 1 (
  echo.
  echo A validacao dos dados falhou; veja a mensagem acima. A interface abre com os dados anteriores.
  echo.
)

netstat -ano | findstr /r /c:":8765 .*LISTENING" >nul
if not errorlevel 1 (
  echo A interface ja esta ligada. Abrindo no navegador...
  start "" http://localhost:8765/
  timeout /t 3 >nul
  exit /b
)

echo Ligando a interface em http://localhost:8765/ ...
rem abre o navegador 2 segundos depois, quando o servidor ja respondeu
start "" /min cmd /c "timeout /t 2 >nul & start "" http://localhost:8765/"
echo Deixe esta janela aberta enquanto usa a interface. Para desligar, feche a janela.
python -m http.server 8765 --bind 127.0.0.1 --directory web
