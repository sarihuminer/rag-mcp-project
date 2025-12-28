# מערכת RAG עם MCP ו-Ollama

מערכת Retrieval-Augmented Generation (RAG) המשתמשת בכלי MCP לעיבוד מסמכים ובמודל שפה פתוח (Ollama) ליצירת תשובות חכמות על בסיס מסמכים.

## ארכיטקטורה

המערכת מורכבת מהרכיבים הבאים:

1. **ממשק משתמש (User Interface)** - `main.py` - נקודת הכניסה למערכת
2. **מערכת RAG** - `SimpleRAGSystem` - הסוכן הראשי המתאם בין הרכיבים
3. **סוכן MCP** - `SimpleMCPTools` - שלושה כלים עיקריים:
   - קריאת קובץ טקסט
   - חלוקת טקסט לקטעים קטנים (chunks)
   - חיפוש קטעים דומים לשאלה
4. **מנוע Embeddings** - SentenceTransformers - יצירת וקטורים מטקסט
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

### או בWindows:

```bash
run.bat
```

## מבנה הפרויקט

```
rag-mcp-local/
├── main.py                  # מערכת RAG מלאה עם MCP
├── requirements.txt         # תלויות Python
├── run.bat                  # הפעלה מהירה ב-Windows
├── architecture_diagram.md  # תרשים ארכיטקטורה
├── README.md               # מדריך זה
├── data/
│   └── document.txt        # מסמך לדוגמה
└── db/                     # מאגר וקטורים (נוצר אוטומטית)
```

## כיצד זה עובד

1. **קריאת מסמך**: הכלי הראשון קורא קובץ טקסט מהדיסק
2. **חלוקה לקטעים**: הכלי השני מחלק את הטקסט לקטעים קטנים בלי לשבור מילים
3. **יצירת וקטורים**: המערכת יוצרת embeddings לכל קטע
4. **שמירה במאגר**: הקטעים נשמרים במאגר וקטורים פשוט
5. **חיפוש**: בהינתן שאלה, המערכת מוצאת את הקטעים הרלוונטיים ביותר
6. **יצירת תשובה**: מודל השפה מקבל את הקטעים הרלוונטיים ויוצר תשובה

## דוגמת שימוש

המערכת תקרא את הקובץ `data/document.txt` ותענה על שאלות לגביו:

```python
file_path = "data/document.txt"
question = "מה הם הסוגים השונים של בינה מלאכותית?"
```

## פתרון בעיות

### Ollama לא מגיב
```bash
# בדוק שהשירות פועל
ollama list

# הפעל מחדש
ollama serve
```

### שגיאות התקנה
```bash
# התקן מחדש תלויות
pip install --upgrade -r requirements.txt
```

### בעיות זיכרון
- השתמש במודל קטן יותר: `ollama pull llama3.2:1b`
- עדכן את `main.py` לשנות את שם המודל

## התאמה אישית

### שינוי מודל השפה
ערוך את `main.py`:
```python
model = "llama3.2:1b"  # מודל קטן יותר
```

### שינוי גודל קטעים
```python
chunks = chunk_text(text, max_chars=300)  # קטעים קטנים יותר
```

## רישיון

פרויקט זה הוא קוד פתוח לשימוש חינמי.