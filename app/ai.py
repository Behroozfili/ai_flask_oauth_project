from transformers import pipeline


classifier=pipeline("zero-shot-classification",model="facebook/bart-large-mnli")

CANDIDATE_LABLS=["Login","Sign up","Support","Question","Logout"]

def analyze_text(text:str):
  result = classifier(text,candidate_labels=CANDIDATE_LABLS)
  return result["labels"][0]

