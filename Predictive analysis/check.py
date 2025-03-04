from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze sentiment of a sample text
text = "VADER is amazing for sentiment analysis!"
sentiment = analyzer.polarity_scores(text)

# Display sentiment scores
print(sentiment)
