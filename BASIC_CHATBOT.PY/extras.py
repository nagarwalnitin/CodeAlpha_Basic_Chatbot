import random

def get_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Python developers don't bite, they just debug.",
        "A computer once beat me at chess, but it was no match for me at boxing."
    ]

    return random.choice(jokes)


def get_fact():
    facts = [
        "Python was created by Guido van Rossum.",
        "The first computer bug was an actual moth.",
        "AI stands for Artificial Intelligence."
    ]

    return random.choice(facts)