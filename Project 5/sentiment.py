from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    print(polarity)

    if polarity > 0.2:
        return "Positive"
    elif polarity < -0.2:
        return "Negative"
    else:
        return "Neutral"