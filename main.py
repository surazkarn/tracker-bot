import requests
from textbase import bot, Message
from typing import List
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Replace 'NEWS_API_KEY' with your actual News API key
NEWS_API_KEY = ""

# NewsAPI URL for top headlines
NEWS_API_TOP_URL = "https://newsapi.org/v2/top-headlines"
NEWS_API_EVERYTHING_URL = "https://newsapi.org/v2/everything"


# System prompt for your bot
SYSTEM_PROMPT = """Hello 👋 Type '!news [category]' (e.g., '!news technology') for clickable news links with sentiment labels: 'positive,' 'negative,' or 'neutral'.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):
    
    # Ensure there are messages in the history
    if not message_history:
        return {
            "status_code": 200,
            "response": {
                "data": {
                    "messages": ["No messages available."],
                    "state": state
                },
                "errors": [{"message": ""}]
            }
        }

    # Get the user's most recent message
    user_message = message_history[-1]["content"][0]["value"].strip()

    # Check if the user is requesting news
    if user_message.startswith("!news"):
        # Extract the news category from the user's message, default to 'general'
        parts = user_message.split()
        if len(parts) > 1:
            news_category = parts[1]
        else:
            news_category = 'general'
        #print("News Category:", news_category)

        #print("User Message:", user_message)

        # Fetch news articles from the chosen category
        news_articles = get_news(news_category)
        
        # Analyze sentiment for each article
        for article in news_articles:
            article['sentiment'] = analyze_sentiment(article['description'])  # Add this line

        # Generate a response with news articles
        if news_articles:
            formatted_articles = format_news_articles(news_articles)
            response_message = "Here are the latest "+ news_category +" news articles: \n\n" + '\n\n'.join(formatted_articles)
        else:
            response_message = "Sorry, I couldn't find any news articles for that category."
        #print("Response Message:", response_message)
        response = {
            "data": {
            "messages": [
                {
                    "data_type": "HTML",
                    "value": response_message
                },
                {
                    "data_type": "STRING",
                    "value": "To get the latest news, type '!news [category]'."
                },
                {
                    "data_type": "STRING",
                    "value": "Replace `[category]` with your desired news category (e.g., technology, business, entertainment, general, health, science, sports)."
                }
            ],
            "state": state
        },
            "errors": [
                {
                    "message": ""
                }
            ],
        }
    else:
        # If the user's message is not related to news, respond with the system prompt
        response = {
            "data": {
                "messages": [
                    {
                        "data_type": "STRING",
                        "value": SYSTEM_PROMPT
                    }
                ],
                "state": state
            },
            "errors": [
                {
                    "message": ""
                }
            ]
        }

    return {
        "status_code": 200,
        "response": response
    }

def format_news_articles(articles):
    formatted_articles = []
    for index, article in enumerate(articles, start=1):
        title = article['title']
        description = article['description']
        link = article['url']
        sentiment = article['sentiment']  # Add this line

        # Create a formatted string for each article
        formatted_article = f"📌 [{title}]({link}) 🔊Sentiment ➡ {sentiment}\n\n"
        formatted_article += f"{description}\n\n"

        formatted_articles.append(formatted_article)

    return formatted_articles



def get_news(query=None, category=None):
    params = {
        'apiKey': NEWS_API_KEY,
        'pageSize': 5,  # Adjust the number of articles to fetch as needed,
        'language': 'en'
    }

    if query:
        params['q'] = query
    elif category:
        params['category'] = category
    else:
        return []

    response = requests.get(NEWS_API_EVERYTHING_URL if query else NEWS_API_TOP_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        return articles
    else:
        return []

def analyze_sentiment(article_text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(article_text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'
