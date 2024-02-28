from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

comment = "This is a great product, I highly recommend it!"

sentiment = SentimentIntensityAnalyzer()
result = sentiment.polarity_scores(comment)

print("Sentiment of the comment: ", result)