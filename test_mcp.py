#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
בדיקת כלי MCP ללא Ollama
"""

from tools import read_file, chunk_text_word_aware, store_and_search_chunks

def test_mcp_tools():
    """בדיקת כלי MCP בלבד"""
    print("בודק כלי MCP...")
    print("=" * 40)
    
    try:
        # בדיקת קריאת קובץ
        print("1. בודק קריאת קובץ...")
        content = read_file.run("data/document.txt")
        if content.startswith("שגיאה"):
            print(f"❌ {content}")
            return False
        
        # בדיקת חלוקה לקטעים
        print("2. בודק חלוקה לקטעים...")
        chunks = chunk_text_word_aware.run({"text": content, "max_chars": 300})
        if not chunks:
            print("❌ לא נוצרו קטעים")
            return False
        
        # בדיקת חיפוש
        print("3. בודק חיפוש...")
        question = "מה זה בינה מלאכותית?"
        results = store_and_search_chunks.run({"question": question, "chunks": chunks, "k": 2})
        if results.startswith("שגיאה"):
            print(f"❌ {results}")
            return False
        
        print("\n✅ כל הכלי MCP עובדים!")
        print("\nתוצאות חיפוש:")
        print("-" * 30)
        print(results)
        
        return True
        
    except Exception as e:
        print(f"❌ שגיאה: {str(e)}")
        return False

if __name__ == "__main__":
    test_mcp_tools()