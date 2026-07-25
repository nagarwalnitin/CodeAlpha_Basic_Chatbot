import random
from datetime import datetime

quotes = [
    "Success is the sum of small efforts, repeated day in and day out.",
    "Believe in yourself.",
    "Never stop learning.",
    "Dream big, work hard.",
    "Every expert was once a beginner."
]

basic_responses = {
    "how are you": "I am doing great. Thanks for asking!",
    "who are you": "I am Nexa AI Assistant created using Python.",
    "your name": "My name is Nexa.",
    "what is python": "Python is a high-level programming language used for AI, automation and web development.",
    "what is ai": "AI stands for Artificial Intelligence. It allows machines to perform intelligent tasks.",
    "who created python": "Python was created by Guido van Rossum.",
    "what is your purpose": "My purpose is to assist users with basic tasks."
}


def get_response(user):

    if user in ["hello", "hi", "hey"]:
        return random.choice([
            "Hello! Welcome to Nexa AI Assistant.",
            "Hi! Nice to meet you.",
            "Hey! How can I help you?"
        ])

    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"Current Time: {current_time}"

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's Date: {current_date}"

    elif user == "day":
        current_day = datetime.now().strftime("%A")
        return f"Today is {current_day}"

    elif user == "help":
        return """
========== NEXA AI ASSISTANT ==========

Available Commands:

• hello
• hi
• hey
• how are you
• who are you
• your name
• what is python
• what is ai
• who created python
• what is your purpose
• date
• time
• day
• calculator
• quote
• dice
• flip
• bye
"""

    elif user in basic_responses:
        return basic_responses[user]

    elif user == "quote":
        return random.choice(quotes)

    elif user == "dice":
        return f"🎲 You rolled a {random.randint(1, 6)}"

    elif user == "flip":
        return f"🪙 {random.choice(['Heads', 'Tails'])}"

    elif user == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."