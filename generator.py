from transformers import pipeline

class Generator:
    def __init__(self, model="google/flan-t5-base"):
        self.generator = pipeline("text2text-generation", model=model)

    def generate(self, context, query):
        prompt = f"Context: {context}\nQuestion: {query}"
        return self.generator(prompt, max_length=256)[0]['generated_text']
