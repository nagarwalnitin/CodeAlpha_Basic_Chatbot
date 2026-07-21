import random
words = [
    "python",
    "computer",
    "programming",
    "keyword",
    "developer"
]

secret_word = random.choice(words)


display = []
for letter in secret_word:
    display.append("_")

chances = 6

while chances > 0:
     
     print("Word:", " ".join(display))
     print("Remaining Chances:", chances)
     guess = input("Enter a letter : ").lower()

     if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one alphabet.")
        continue

     if guess in secret_word:
      
      for index in range(len(secret_word)):
        if secret_word[index] == guess:
            display[index] = guess

      print("✅Correct Guess!")

      if "_" not in display:
       print("🎉congratulations! you won!")
       break

     else:
        chances -= 1
        print("Wrong Guess❌")
        print("Remainging Chances:",chances)

if chances == 0:
   print("😔 You Lost!")
   print("Correct Word:",secret_word)



