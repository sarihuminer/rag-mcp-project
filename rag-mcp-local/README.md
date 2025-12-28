# מערכת RAG עם MCP ו-Ollama

מערכת Retrieval-Augmented Generation (RAG) המשתמשת בכלי MCP לעיבוד מסמכים ובמודל שפה פתוח (Ollama) ליצירת תשובות חכמות על בסיס מסמכים.

## ארכיטקטורה

המערכת מורכבת מהרכיבים הבאים:

1. **ממשק משתמש (User Interface)** - `main.py` - נקודת הכניסה למערכת
2. **מערכת RAG** - `rag_agent.py` - הסוכן הראשי המתאם בין הרכיבים
3. **סוכן MCP** - `tools.py` - שלושה כלים עיקריים:
   - קריאת קובץ טקסט
   - חלוקת טקסט לקטעים קטנים (chunks)
   - חיפוש קטעים דומים לשאלה
4. **מנוע Embeddings** - `embeddings.py` - יצירת וקטורים מטקסט
5. **מודל שפה** - Ollama (llama3.2:3b) - יצירת תשובות

## דרישות מערכת

- Python 3.8+
- Ollama מותקן ופועל
- 4GB RAM לפחות
- חיבור לאינטרנט (להורדת מודלים)

## התקנה

### 1. התקנת Ollama

```bash
# Windows
winget install Ollama.Ollama

# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. הורדת מודל השפה

```bash
ollama pull llama3.2:3b
```

### 3. התקנת תלויות Python

```bash
pip install -r requirements.txt
```

## הפעלה

### 1. הפעלת Ollama

```bash
ollama serve
```

### 2. הרצת המערכת

```bash
python main.py
```

## מבנה הפרויקט

```
rag-mcp-local/
├── main.py              # נקודת כניסה למערכת
├── rag_agent.py         # סוכן RAG ראשי
├── tools.py             # כלי MCP
├── embeddings.py        # מודל embeddings
├── requirements.txt     # תלויות Python
├── data/
│   └── document.txt     # מסמך לדוגמה
└── db/
    └── chroma/          # מאגר וקטורים (נוצר אוטומטית)
```

## כיצד זה עובד

1. **קריאת מסמך**: הכלי הראשון קורא קובץ טקסט מהדיסק
2. **חלוקה לקטעים**: הכלי השני מחלק את הטקסט לקטעים קטנים בלי לשבור מילים
3. **יצירת וקטורים**: המערכת יוצרת embeddings לכל קטע
4. **שמירה במאגר**: הקטעים נשמרים במאגר וקטורים מקומי (ChromaDB)
5. **חיפוש**: בהינתן שאלה, המערכת מוצאת את הקטעים הרלוונטיים ביותר
6. **יצירת תשובה**: מודל השפה מקבל את הקטעים הרלוונטיים ויוצר תשובה

## דוגמת שימוש

המערכת תקרא את הקובץ `data/document.txt` ותענה על שאלות לגביו:

```python
query = """
קרא את הקובץ data/document.txt,
חלק אותו לקטעים,
חפש חלקים רלוונטיים,
ועענה על השאלה:
מה הם הסוגים השונים של בינה מלאכותית?
"""
```

## פתרון בעיות

### Ollama לא מגיב
```bash
# בדוק שהשירות פועל
ollama list

# הפעל מחדש
ollama serve
```

### שגיאות Python
```bash
# התקן מחדש תלויות
pip install --upgrade -r requirements.txt
```

### בעיות זיכרון
- השתמש במודל קטן יותר: `ollama pull llama3.2:1b`
- עדכן את `rag_agent.py` לשנות את שם המודל

## התאמה אישית

### שינוי מודל השפה
ערוך את `rag_agent.py`:
```python
llm = Ollama(model="llama3.2:1b")  # מודל קטן יותר
```

### שינוי גודל קטעים
ערוך את `main.py` בקריאה לכלי:
```python
chunk_text_word_aware(text, max_chars=300)  # קטעים קטנים יותר
```

## רישיון

פרויקט זה הוא קוד פתוח לשימוש חינמי.