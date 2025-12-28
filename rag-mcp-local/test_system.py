#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
סקריפט בדיקה מהירה למערכת RAG
"""

import sys
import subprocess
import requests
import time

def check_ollama():
    """בודק אם Ollama פועל ומודל זמין"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [model["name"] for model in models]
            print(f"✓ Ollama פועל. מודלים זמינים: {model_names}")
            
            if "llama3.2:3b" in model_names:
                print("✓ מודל llama3.2:3b זמין")
                return True
            else:
                print("✗ מודל llama3.2:3b לא זמין")
                print("הרץ: ollama pull llama3.2:3b")
                return False
        else:
            print("✗ Ollama לא מגיב")
            return False
    except Exception as e:
        print(f"✗ שגיאה בחיבור ל-Ollama: {e}")
        print("וודא ש-Ollama מותקן ופועל: ollama serve")
        return False

def check_dependencies():
    """בודק תלויות Python"""
    required_packages = [
        "langchain",
        "langchain_community", 
        "sentence_transformers",
        "chromadb",
        "torch"
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package}")
            missing.append(package)
    
    if missing:
        print(f"\nחסרות חבילות: {missing}")
        print("הרץ: pip install -r requirements.txt")
        return False
    
    return True

def test_system():
    """בדיקה מהירה של המערכת"""
    print("בודק מערכת RAG...")
    print("=" * 40)
    
    # בדיקת תלויות
    print("\n1. בודק תלויות Python:")
    if not check_dependencies():
        return False
    
    # בדיקת Ollama
    print("\n2. בודק Ollama:")
    if not check_ollama():
        return False
    
    # בדיקת קבצים
    print("\n3. בודק קבצים:")
    import os
    required_files = [
        "main.py",
        "rag_agent.py", 
        "tools.py",
        "embeddings.py",
        "data/document.txt"
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file}")
            return False
    
    print("\n✓ כל הבדיקות עברו בהצלחה!")
    print("המערכת מוכנה לשימוש. הרץ: python main.py")
    return True

if __name__ == "__main__":
    if test_system():
        sys.exit(0)
    else:
        print("\n✗ יש בעיות במערכת. תקן אותן לפני המשך.")
        sys.exit(1)