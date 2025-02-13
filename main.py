from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

# Function to generate random lottery numbers
def generate_lottery_numbers():
    return sorted(random.sample(range(1, 50), 6))  # 6 numbers from 1-49

# Function to get a random joke
def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke_data = response.json()
        return f"{joke_data['setup']} {joke_data['punchline']}"
    except:
        return "Why don’t skeletons fight each other? They don’t have the guts!"

@app.route("/")
def home():
    lottery_numbers = generate_lottery_numbers()
    joke = get_random_joke()
    return render_template("index.html", numbers=lottery_numbers, joke=joke)

if __name__ == "__main__":
    app.run(debug=True)
