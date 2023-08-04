import glob
import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

neg = []
pos = []
pages = sorted(glob.glob("data/*.txt"))

analyzer = SentimentIntensityAnalyzer()

for page in pages:
    with open(page, "r") as file:
        content = file.read()
    score = analyzer.polarity_scores(content)
    neg.append(score["neg"])
    pos.append(score["pos"])

dates = [page.strip(".txt").strip("data\\") for page in pages]

print(dates)
print(neg)
print(pos)

st.title("Diary Tone")
st.subheader("Positivity")
pos_fig = px.line(x=dates, y=pos, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_fig)

st.subheader("Negativity")
neg_fig = px.line(x=dates, y=neg, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_fig)