@echo off
chcp 65001 > nul
echo מערכת RAG עם MCP ו-Ollama
echo ========================

echo בודק מערכת...
python test_system.py

if %errorlevel% equ 0 (
    echo.
    echo מפעיל מערכת RAG...
    python main.py
) else (
    echo.
    echo יש בעיות במערכת. בדוק את ההודעות למעלה.
    pause
)