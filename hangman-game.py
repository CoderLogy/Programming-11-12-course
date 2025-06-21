import requests
import os
import random
import time
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

HANGMAN_ART = r'''
                                                                                                                                                                                                                                                                                                
 o         o                                        o          o                              
<|>       <|>                                      <|\        /|>                             
< >       < >                                      / \\o    o// \                             
 |         |      o__ __o/  \o__ __o     o__ __o/  \o/ v\  /v \o/     o__ __o/  \o__ __o      
 o__/_ _\__o     /v     |    |     |>   /v     |    |   <\/>   |     /v     |    |     |>     
 |         |    />     / \  / \   / \  />     / \  / \        / \   />     / \  / \   / \     
<o>       <o>   \      \o/  \o/   \o/  \      \o/  \o/        \o/   \      \o/  \o/   \o/     
 |         |     o      |    |     |    o      |    |          |     o      |    |     |      
/ \       / \    <\__  / \  / \   / \   <\__  < >  / \        / \    <\__  / \  / \   / \     
                                               |                                              
                                       o__     o                                              
                                       <\__ __/>                                              
'''
hangmanWords = [
    "zimmerman", "rai", "kwantlen", "python", "code", "university", "student",
    "algorithm", "data", "science", "function", "variable", "loop", "dictionary",
    "array", "list", "tuple", "string", "boolean", "object", "class", "method"
]
def play_again():
    print(center_text(text=HANGMAN_ART))
    playAgain = input("Do you wanna play again (yes or no): ").lower()
    if playAgain == "yes":
        main_game()

def center_text(text, width=120):
    centered_art = []
    for line in text.split('\n'):
        padding = (width - len(line)) // 2
        centered_line = ' ' * padding + line
        centered_art.append(centered_line)
    return '\n'.join(centered_art)

def delay():
    time.sleep(1)
    os.system("cls")

def hangman(secretWord):
    maxWrong = len(HANGMANPICS) - 1
    correctGuess = ''
    wrongGuess = ''
    secretWord = secretWord.lower()
    print("🎉 Welcome to Hangman!")
    while True:
        print(HANGMANPICS[len(wrongGuess)])
        displayWord = [letter if letter in correctGuess else '_' for letter in secretWord]
        print("Word: " + ' '.join(displayWord))
        print("Missed letters:", wrongGuess)
        guess = input("Guess a letter: ").lower()
        delay()
        if not guess.isalpha() or len(guess) != 1:
            print("❗ Enter only one letter.")
            delay()
            continue
        elif guess in correctGuess + wrongGuess:
            print("❗ You already guessed that letter.")
            delay()
            continue
        elif guess in secretWord:
            correctGuess += guess
            if all(letter in correctGuess for letter in secretWord):
                print("🎉 You guessed the word:", secretWord)
                delay()
                play_again()
                break
        else:
            wrongGuess += guess
            if len(wrongGuess) == maxWrong:
                print(HANGMANPICS[-1])
                print("💀 You lost! The word was:", secretWord)
                delay()
                play_again()
                break

def genrative_api(message):
    url = "https://ai.hackclub.com/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": message}]
    }

    # Define headers
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url,json=payload,headers=headers)
    if response.status_code == 200:
        response_content = response.json()
        reply = response_content["choices"][0]["message"]["content"]
        return reply.strip()

def create_random_word(choice):
    if choice == "yes":
        message = (
            "give me a unique english word from dictionary every time don't store it in your server etc and also make sure it doesn't contains any kind of symbols. Remember 'word' not a sentence."
        )
        word = genrative_api(message)
        print(word)
        return word
    else:
        hangmanWordExcluding = {"zimmerman","rai"}
        hangmanWordIncluding = [hangmanWord for hangmanWord in hangmanWords if hangmanWord not in hangmanWordExcluding ]
        hangmanWordRandom = random.choice(hangmanWordIncluding)
        return hangmanWordRandom

if __name__ == "__main__":
    def main_game():
        os.system('cls')
        print(center_text(text=HANGMAN_ART))
        choice = input("Wanna play Ai Generated Hangman game or not (yes or no): ")
        hangman(create_random_word(choice=choice))
    main_game()