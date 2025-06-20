import string
from jiwer import wer
from difflib import SequenceMatcher

def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = " ".join(text.strip().split())
    return text

ref = "Hello, my name is John. I am learning English!"
hyp = "hello my name is john i am learning english"

ref_clean = normalize(ref)
hyp_clean = normalize(hyp)

wer_score = round((1 - wer(ref_clean, hyp_clean)) * 100, 2)
sim_score = round(SequenceMatcher(None, ref_clean, hyp_clean).ratio() * 100, 2)

print(f"WER评分: {wer_score}/100")
print(f"相似度评分: {sim_score}/100")
