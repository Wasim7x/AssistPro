import time
from typing import List
from langchain_core.embeddings import Embeddings


class RateLimitedEmbeddings(Embeddings):
    """
    Wraps any embedding model and slows down requests
    to avoid Gemini free-tier rate limits.
    """

    def __init__(self, base_embeddings, delay: float = 1.1):
        self.base_embeddings = base_embeddings
        self.delay = delay  # seconds between API calls

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        results = []
        for text in texts:
            results.extend(self.base_embeddings.embed_documents([text]))
            time.sleep(self.delay)  # <-- prevents 429
        return results

    def embed_query(self, text: str) -> List[float]:
        time.sleep(self.delay)
        return self.base_embeddings.embed_query(text)