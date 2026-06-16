import os
import xml.etree.ElementTree as ET
import pandas as pd

data = []

folder = "MedQuAD"

for root_dir, dirs, files in os.walk(folder):

    for file in files:

        if file.endswith(".xml"):

            path = os.path.join(root_dir, file)

            try:
                tree = ET.parse(path)
                root = tree.getroot()

                for qa in root.findall(".//QAPair"):

                    question = qa.findtext("Question")
                    answer = qa.findtext("Answer")

                    if question and answer:
                        data.append([question, answer])

            except Exception as e:
                print("Error:", e)

df = pd.DataFrame(data, columns=["question", "answer"])

os.makedirs("data", exist_ok=True)

df.to_csv("data/medquad.csv", index=False)

print("Dataset prepared successfully!")
print("Total Q&A pairs:", len(df))