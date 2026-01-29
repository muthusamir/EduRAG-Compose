from edurag.pipeline import EduRAGCompose
from edurag.embeddings import Embedder
from edurag.retriever import LightRAGRetriever
import numpy as np

texts = open("data/corpus.txt").read().split("\n")
embedder = Embedder()
embs = embedder.encode(texts)

retriever = LightRAGRetriever(np.array(embs), texts)
system = EduRAGCompose(retriever)

queries = ["Why does lightning appear before thunder?"]
for q in queries:
    print(system.answer(q, embedder))
