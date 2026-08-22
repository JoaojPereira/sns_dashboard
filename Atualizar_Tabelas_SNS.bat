@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "PYTHON_EXE=%PROJECT_DIR%BiEnv\Scripts\python.exe"
set "DOWNLOAD_SCRIPT=%PROJECT_DIR%scripts_historico\atualizar_dados_sns.py"
set "FACT_SCRIPT=%PROJECT_DIR%scripts_historico\atualizar_tabelas_fact.py"
set "MONTHLY_SCRIPT=%PROJECT_DIR%scripts_historico\gerar_valores_mensais.py"

cd /d "%PROJECT_DIR%"

echo ================================================================
echo ATUALIZACAO DAS TABELAS SNS
echo ================================================================
echo.
echo Portal: https://transparencia.sns.gov.pt
echo Pasta de destino: %PROJECT_DIR%
echo.

if not exist "%PYTHON_EXE%" (
    echo ERRO: Python do ambiente BiEnv nao foi encontrado:
    echo %PYTHON_EXE%
    echo.
    pause
    exit /b 1
)

if not exist "%DOWNLOAD_SCRIPT%" (
    echo ERRO: Script de download nao foi encontrado:
    echo %DOWNLOAD_SCRIPT%
    echo.
    pause
    exit /b 1
)

if not exist "%FACT_SCRIPT%" (
    echo ERRO: Script das tabelas Fact nao foi encontrado:
    echo %FACT_SCRIPT%
    echo.
    pause
    exit /b 1
)

if not exist "%MONTHLY_SCRIPT%" (
    echo ERRO: Script da tabela mensal nao foi encontrado:
    echo %MONTHLY_SCRIPT%
    echo.
    pause
    exit /b 1
)

echo [1/3] A descarregar dados do Portal SNS...
"%PYTHON_EXE%" "%DOWNLOAD_SCRIPT%"
set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" goto :failed

echo.
echo [2/3] A reconstruir as tabelas Fact...
"%PYTHON_EXE%" "%FACT_SCRIPT%"
set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" goto :failed

echo.
echo [3/3] A gerar a tabela mensal usada pelo Power BI...
"%PYTHON_EXE%" "%MONTHLY_SCRIPT%"
set "EXIT_CODE=%ERRORLEVEL%"
if not "%EXIT_CODE%"=="0" goto :failed

echo.
echo Atualizacao concluida. Abra o Power BI e clique em Atualizar.
goto :end

:failed
echo.
echo A atualizacao terminou com erros. Codigo: %EXIT_CODE%

:end
echo.
pause
exit /b %EXIT_CODE%
