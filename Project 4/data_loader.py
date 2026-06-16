import pandas as pd

print("Loading dataset...")

df = pd.read_json(
    "ResearchPaperChatbot/arxiv-metadata-oai-snapshot.json",
    lines=True,
    nrows=5000
)

print("Filtering Computer Science papers...")

cs_papers = df[df['categories'].str.contains('cs', na=False)]

print("Selecting columns...")

cs_papers = cs_papers[['title', 'abstract', 'categories']]

print("Saving CSV...")

cs_papers.to_csv("data/arxiv_sample.csv", index=False)

print("Dataset prepared successfully!")
print(f"Total papers saved: {len(cs_papers)}")