from sentence_transformers import SentenceTransformer
import torch

MODEL_NAME = "all-MiniLM-L6-v2"

class LocalEmbeddingModel:
    """מודל embeddings מקומי ליצירת וקטורים מטקסט"""
    
    def __init__(self):
        print(f"טוען מודל embeddings: {MODEL_NAME}")
        self.model = SentenceTransformer(MODEL_NAME)
        
        # בדיקת זמינות GPU
        if torch.cuda.is_available():
            self.model = self.model.cuda()
            print("משתמש ב-GPU")
        else:
            print("משתמש ב-CPU")

    def embed(self, texts: list[str]) -> list[list[float]]:
        """ממיר רשימת טקסטים לוקטורים"""
        embeddings = self.model.encode(texts, convert_to_tensor=False)
        return embeddings.tolist()