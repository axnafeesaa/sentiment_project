import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

st.title("AI-Based Brand Reputation Monitoring System")

st.write("Enter customer reviews or tweets (one per line):")

user_input = st.text_area("Paste text here")

if st.button("Analyze Sentiment"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        reviews = user_input.split("\n")

        results = []
        positive = negative = neutral = 0

        for review in reviews:
            analysis = TextBlob(review)
            polarity = analysis.sentiment.polarity

            if polarity > 0:
                sentiment = "Positive"
                positive += 1
            elif polarity < 0:
                sentiment = "Negative"
                negative += 1
            else:
                sentiment = "Neutral"
                neutral += 1

            results.append([review, sentiment, round(polarity, 2)])

        df = pd.DataFrame(results, columns=["Text", "Sentiment", "Score"])

        st.subheader("Sentiment Analysis Results")
        st.dataframe(df)

        # Pie Chart
        st.subheader("Overall Brand Reputation")

        labels = ["Positive", "Negative", "Neutral"]
        sizes = [positive, negative, neutral]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        st.pyplot(fig)