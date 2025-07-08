import requests
import wikipedia
import random
def get_joke():
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if res.status_code == 200:
            return res.json()["joke"]
        else:
            return "Oops! I couldn't fetch a joke right now."
    except:
        return "Sorry! Something went wrong while getting a joke."
def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"The result is: {result}"
    except:
        return "Sorry! I couldn't calculate that. Please enter a valid expression."
API_KEY = "7c1906eb8e05051eb3a92db80244c848"
def get_weather(city):
    try:
        city = city.strip()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "Please enter a valid city name (not state or region)."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        return f"🌤️ The weather in {city.title()} is {temp}°C with {desc}."
    except Exception:
        return "⚠️ Couldn't fetch the weather. Please try again later."
def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)  # 2 sentences summary
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Did you mean: {e.options[:5]}?"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any page matching your query."
    except Exception as e:
        return "Oops! Something went wrong with Wikipedia search."
def get_news():
    api_key = "35d53f3043db467a8f98058c52d56a50"
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        print("DEBUG:", data)

        if data.get("status") == "ok" and data.get("articles"):
            articles = data["articles"][:5]
            news_list = [f"📰 {article['title']}" for article in articles if article.get("title")]
            return "\n\n".join(news_list)
        else:
            return "🛑 Still no headlines found. Try again later or use a different country/category."
    except Exception as e:
        return f"⚠️ Error fetching news: {str(e)}"
def get_news_by_country_and_category(country_name="india", category=None):
    api_key = "35d53f3043db467a8f98058c52d56a50"

    # Map country names to codes
    country_codes = {
        "india": "in",
        "us": "us",
        "usa": "us",
        "united states": "us",
        "uk": "gb",
        "united kingdom": "gb",
        "canada": "ca",
        "australia": "au",
        "germany": "de",
        "france": "fr"
    }

    # Map category if provided
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

    country_code = country_codes.get(country_name.lower(), "in")
    category_param = f"&category={category}" if category in categories else ""

    url = f"https://newsapi.org/v2/top-headlines?country={country_code}{category_param}&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok" and data.get("articles"):
            articles = data["articles"][:5]
            news_list = [f"📰 {article['title']}" for article in articles if article.get("title")]
            return "\n\n".join(news_list)
        else:
            return "🛑 Couldn't find any news articles for that category/location."
    except Exception as e:
        return f"⚠️ Error fetching news: {str(e)}"
import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Network error. Please check your internet."
def play_rps(user_choice):
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    result = f"You chose {user_choice}, I chose {bot_choice}. "

    if user_choice == bot_choice:
        return result + "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return result + "You win! 🎉"
    else:
        return result + "I win! 😄"
