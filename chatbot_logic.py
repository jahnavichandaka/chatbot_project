from utils import get_joke, calculate_expression, get_weather,get_news
from utils import get_news_by_country_and_category
from datetime import datetime
import wikipedia
from utils import play_rps
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Did you mean: {e.options[:5]}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any page matching your query."
    except Exception:
        return "Oops! Something went wrong with Wikipedia search."
def get_bot_response(user_input):
    user_input = user_input.lower()
    if (user_input.startswith("wiki ") or user_input.startswith("wikipedia ") or
        user_input.startswith("what is ") or user_input.startswith("tell me about ") or
        user_input.startswith("who is ")):
        for phrase in ["wiki ", "wikipedia ", "what is ", "tell me about ", "who is "]:
            if user_input.startswith(phrase):
                topic = user_input[len(phrase):].strip()
                break       
        response = get_wikipedia_summary(topic)
        return response
    if "hi" in user_input or "hello" in user_input:
        return "Hey there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm ChatPy, your virtual assistant."
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking!"
    elif "help" in user_input:
        return "Try asking me: 'tell me a joke', 'your name', 'how are you', 'calculate <expression>', 'weather in <city>', or 'wiki <topic>'."
    elif "joke" in user_input:
        return get_joke()
    elif "bye" in user_input:
        return "Goodbye! Have a nice day. 👋"
    elif "calculate" in user_input:
        expr = user_input.replace("calculate", "").strip()
        return calculate_expression(expr)
    elif "weather in" in user_input:
        city = user_input.split("weather in")[-1].strip()
        return get_weather(city)
        # Time and Date feature
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")  
        return f"The current time is {current_time}."   
    elif "date" in user_input:
        current_date = datetime.now().strftime("%A, %B %d, %Y")  
        return f"Today’s date is {current_date}."
    elif "news" in user_input or "headlines" in user_input:
        # Detect category and country
        categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        countries = ["india", "us", "usa", "uk", "united kingdom", "canada", "australia", "germany", "france"]

        category = None
        country = "india"  # Default

        for word in user_input.split():
            if word in categories:
                category = word
            elif word in countries:
                country = word

        return get_news_by_country_and_category(country, category)
    elif "play rock paper scissors" in user_input or "rps" in user_input:
        return "Sure! Type 'rock', 'paper', or 'scissors' to play."

    elif user_input in ["rock", "paper", "scissors"]:
        return play_rps(user_input)

    else:
        return "Sorry, I didn't understand that. Try asking something else."