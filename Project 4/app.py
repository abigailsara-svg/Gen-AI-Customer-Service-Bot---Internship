import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import ollama

# ---------------- PAGE SETTINGS ---------------- #

st.set_page_config(
    page_title="AI Research Paper Assistant",
    layout="wide"
)

# ---------------- TITLE ---------------- #

st.title("📚 AI Research Paper Assistant")

st.write(
    "Ask research-related questions and get AI-powered explanations."
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("About")

st.sidebar.info(
    """
    AI Research Assistant built using:

    • arXiv Dataset  
    • Sentence Transformers  
    • FAISS Vector Database  
    • Phi-3 Open Source LLM  
    • Streamlit  
    """
)

# ---------------- SEARCH HISTORY ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- LOAD MODELS ---------------- #

@st.cache_resource
def load_models():

    # Load FAISS index
    index = faiss.read_index(
        "models/arxiv_index.faiss"
    )

    # Load papers dataframe
    with open("models/papers.pkl", "rb") as f:
        df = pickle.load(f)

    # Load embedding model
    model = SentenceTransformer(
        'all-MiniLM-L6-v2'
    )

    return index, df, model


index, df, model = load_models()

# ---------------- PAPER SEARCH FUNCTION ---------------- #

def search_papers(query, top_k=3):

    # Convert query to embeddings
    query_embedding = model.encode([query])

    # Search FAISS index
    distances, indices = index.search(
        np.array(query_embedding),
        top_k
    )

    results = []

    for idx in indices[0]:

        paper = df.iloc[idx]

        results.append({
            "title": paper['title'],
            "abstract": paper['abstract'],
            "category": paper['categories']
        })

    return results


# ---------------- AI EXPLANATION FUNCTION ---------------- #

def generate_explanation(query, papers):

    context = ""

    for paper in papers:

        context += f"""
Title: {paper['title']}

Abstract:
{paper['abstract']}

"""

    prompt = f"""
You are an expert AI Research Assistant.

Your task is to explain research topics in a simple, clean, and student-friendly way.

Use the research papers below as context.

User Question:
{query}

Research Papers:
{context}

Instructions:
- Give a short and clear explanation
- Explain important concepts simply
- Avoid overly technical language
- Summarize the research insights
- Keep the response well-structured

Format:

1. Overview
2. Key Concepts
3. Research Insights
4. Real-World Applications
"""

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response['message']['content']


# ---------------- USER INPUT ---------------- #

query = st.text_input(
    "Enter your research question:"
)

# ---------------- SEARCH BUTTON ---------------- #

if st.button("Search"):

    if query:

        # Save history
        st.session_state.history.append(query)

        # Search papers
        with st.spinner(
            "Searching research papers..."
        ):

            papers = search_papers(query)

        # Display papers
        st.subheader(
            "📄 Relevant Research Papers"
        )

        for i, paper in enumerate(papers, 1):

            st.write(
                f"### {i}. {paper['title']}"
            )

            st.write(
                f"**Category:** {paper['category']}"
            )

            st.text_area(
                "Abstract",
                paper['abstract'],
                height=180,
                key=i
            )

            st.write("---")

        # Generate explanation
        with st.spinner(
            "Generating AI explanation..."
        ):

            answer = generate_explanation(
                query,
                papers
            )

        # Display AI explanation
        st.subheader(
            "🤖 AI Explanation"
        )

        st.write(answer)

# ---------------- SIDEBAR SEARCH HISTORY ---------------- #

st.sidebar.subheader("Search History")

for item in st.session_state.history:
    st.sidebar.write(f"• {item}")