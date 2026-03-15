@echo off
chcp 65001 >nul
echo ================================================================================
echo ATUALIZAÇÃO AUTOMÁTICA DE DADOS DO SNS - POWER BI
echo ================================================================================
echo.
echo Iniciando atualização de dados...
echo.

cd /d "E:\Ambiente de trabalho\TransformacaoBi\Report de Ineficiências nas Urgências Hospitalares"

echo ────────────────────────────────────────────────────────────────────────────────
echo PASSO 1: Descarregando dados atualizados do Portal SNS
echo ────────────────────────────────────────────────────────────────────────────────
echo.

"E:\Ambiente de trabalho\TransformacaoBi\Report de Ineficiências nas Urgências Hospitalares\PyBi\Scripts\python.exe" "E:\Ambiente de trabalho\TransformacaoBi\Report de Ineficiências nas Urgências Hospitalares\scripts_historico\atualizar_dados_sns.py"

if %errorlevel% neq 0 (
    echo.
    echo ✗ ERRO ao descarregar dados do SNS!
    echo.
    pause
    exit /b 1
)

echo.
echo ────────────────────────────────────────────────────────────────────────────────
echo PASSO 2: Atualizando tabelas Fact do Power BI
echo ────────────────────────────────────────────────────────────────────────────────
echo.

"E:\Ambiente de trabalho\TransformacaoBi\Report de Ineficiências nas Urgências Hospitalares\PyBi\Scripts\python.exe" "E:\Ambiente de trabalho\TransformacaoBi\Report de Ineficiências nas Urgências Hospitalares\scripts_historico\atualizar_tabelas_fact.py"

if %errorlevel% neq 0 (
    echo.
    echo ✗ ERRO ao atualizar tabelas Fact!
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================================================
echo ✓ ATUALIZAÇÃO CONCLUÍDA COM SUCESSO!
echo ================================================================================
echo.
echo Próximos passos:
echo 1. Abrir o Power BI Desktop
echo 2. Ir em "Home" ^> "Atualizar" para recarregar os dados atualizados
echo 3. Verificar se as métricas foram atualizadas corretamente
echo.
echo ────────────────────────────────────────────────────────────────────────────────
echo Data da atualização: %date% %time%
echo ────────────────────────────────────────────────────────────────────────────────
echo.
pause
