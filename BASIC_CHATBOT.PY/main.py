from memory import save_name, get_name
from calculator import calculate
from responses import get_response
from extras import get_joke, get_fact


print("=" * 40)
print("      🤖 NEXA AI ASSISTANT")
print("=" * 40)
print("Type 'help' to see commands")
print("Type 'bye' to exit\n")


while True:

    user = input("You : ").lower().strip()


    if user == "calculator":
        calculate()
        continue


    if user == "joke":
        print("Nexa :", get_joke())
        continue


    if user == "fact":
        print("Nexa :", get_fact())
        continue


    if user.startswith("my name is"):

        name = user.replace("my name is", "").strip()

        save_name(name)

        print("Nexa: Nice to meet you " + name)
        continue


    if user == "what is my name":

        name = get_name()

        if name:
            print("Nexa: Your name is " + name)
        else:
            print("Nexa: I don't know your name yet.")

        continue


    response = get_response(user)

    print("Nexa :", response)


    with open("chat_history.txt", "a",encoding="utf-8") as file:
        file.write("User: " + user + "\n")
        file.write("Nexa: " + response + "\n\n")


    if user == "bye":
        break