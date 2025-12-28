@echo off
chcp 65001 > nul
echo מערכת RAG מקצועית עם MCP ו-Ollama
echo =====================================

echo מתקין תלויות...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo מפעיל מערכת RAG...
    python main.py
) else (
    echo.
    echo שגיאה בהתקנת תלויות. בדוק את החיבור לאינטרנט.
    pause
)