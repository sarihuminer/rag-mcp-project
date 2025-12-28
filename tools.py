from langchain_core.tools import tool
from embeddings import LocalEmbeddingModel
import chromadb
import uuid
import os

# יצירת מודל embeddings מקומי
embedding_model = LocalEmbeddingModel()

# יצירת מאגר וקטורים מקומי
os.makedirs("./db/chroma", exist_ok=True)
chroma_client = chromadb.PersistentClient(path="./db/chroma")
collection = chroma_client.get_or_create_collection("documents")

@tool
def read_file(path: str) -> str:
    """כלי MCP לקריאת קובץ טקסט מהדיסק"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"✓ קובץ {path} נקרא בהצלחה ({len(content)} תווים)")
        return content
    except Exception as e:
        return f"שגיאה בקריאת הקובץ: {str(e)}"

@tool
def chunk_text_word_aware(text: str, max_chars: int = 500) -> list[str]:
    """כלי MCP לחלוקת טקסט לקטעים קטנים בלי לשבור מילים"""
    chunks = []
    start = 0
    
    while start < len(text):
        end = min(start + max_chars, len(text))
        
        # מחפש רווח אחרון כדי לא לשבור מילים
        if end < len(text):
            space = text.rfind(" ", start, end)
            if space > start:
                end = space
        
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end + 1
    
    print(f"✓ הטקסט חולק ל-{len(chunks)} קטעים")
    return chunks

@tool
def store_and_search_chunks(question: str, chunks: list[str], k: int = 3) -> str:
    """כלי MCP לשמירת קטעים וחיפוש דומים לשאלה"""
    try:
        # יצירת embeddings לקטעים
        embeddings = embedding_model.embed(chunks)
        ids = [str(uuid.uuid4()) for _ in chunks]
        
        # שמירה במאגר וקטורים
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids,
        )
        
        # יצירת embedding לשאלה
        query_embedding = embedding_model.embed([question])[0]
        
        # חיפוש קטעים דומים
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
        )
        
        relevant_chunks = "\n\n".join(results["documents"][0])
        print(f"✓ נמצאו {len(results['documents'][0])} קטעים רלוונטיים")
        
        return relevant_chunks
        
    except Exception as e:
        return f"שגיאה בחיפוש: {str(e)}"