from TextBlob import TextBlob
import json

def analyze_sentiment(comments):
# Create a TextBlob object
blob = TextBlob(comments)

# Perform sentiment analysis
result = blob.sentiment.polarity

# Return the result as a JSON object
return json.dumps({ 'result': result })

# Get the comments from the request
comments = request.GET.get('comments')

# Perform sentiment analysis on the comments
result = analyze_sentiment(comments)

# Return the result as a JSON object
return HttpResponse(result, content_type='application/json')