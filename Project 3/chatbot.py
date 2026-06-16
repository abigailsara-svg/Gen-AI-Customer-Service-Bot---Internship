import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/medquad.csv")

questions = df["question"].tolist()
answers = df["answer"].tolist()

model = SentenceTransformer('all-MiniLM-L6-v2')

question_embeddings = model.encode(questions)

def get_answer(user_question):

    user_embedding = model.encode([user_question])

    similarity = cosine_similarity(
        user_embedding,
        question_embeddings
    )

    index = similarity.argmax()

    return answers[index]