#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
מערכת RAG (Retrieval-Augmented Generation) עם כלי MCP
משתמשת במודל שפה מקומי (Ollama) ליצירת תשובות חכמות
"""

from rag_agent import build_agent
import sys

def main():
    """פונקציה ראשית להרצת המערכת"""
    print("מערכת RAG עם MCP ו-Ollama")
    print("=" * 40)
    
    try:
        # בניית הסוכן
        print("בונה סוכן RAG...")
        agent = build_agent()
        
        # שאלה לדוגמה
        query = """
        קרא את הקובץ data/document.txt,
        חלק אותו לקטעים,
        חפש חלקים רלוונטיים,
        וענה על השאלה:
        מה הם הסוגים השונים של בינה מלאכותית?
        """
        
        print("\nמעבד שאלה...")
        print("-" * 40)
        
        # הרצת הסוכן
        response = agent.run(query)
        
        print("\n" + "=" * 40)
        print("תשובה סופית:")
        print("=" * 40)
        print(response)
        
    except Exception as e:
        print(f"שגיאה: {str(e)}")
        print("ודא ש-Ollama רץ ושהמודל llama3.2:3b מותקן")
        sys.exit(1)

if __name__ == "__main__":
    main()