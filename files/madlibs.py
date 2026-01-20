import requests
import os
import time


madlibs_art = '''
███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝
██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗
██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝
    '''

    # Grass ASCII art
grass_art = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣇⠀⣀⠀⠀⢀⣠⡶⢟⣩⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⢤⣤⣄⡀⠀⢀⡿⣿⣼⣻⢀⣴⠟⢥⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⢠⣾⡏⢀⣠⣾⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠻⣝⠳⣾⡇⣿⠃⣯⠞⠁⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢿⢧⣺⠉⣿⠞⣹⣏⣤⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⠀⠁⠈⠐⠏⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡾⠌⠳⠀⠈⠀⠙⠁⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⣷⠀⠀⠀⠀⡄⠀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣾⡿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⡿⠀⢹⠀⢀⣴⡾⢻⡆⠀⢸⡿⣆⠀⠀⢀⣠⢀⣴⠞⣩⡾⣁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⢦⣄⢸⡇⠀⢸⣶⢿⡿⠀⡌⠳⠀⣼⠇⣿⢠⡼⣿⣿⡟⠁⢠⣟⣥⣼⡿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢶⣦⣌⣷⠙⢿⡇⠀⢸⠇⣿⣠⡾⠻⡕⣴⡏⠀⣽⠏⠀⣿⠋⠀⠀⣿⡟⢩⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠙⡇⠀⠀⠀⠈⠀⠹⠏⠀⠀⠙⠟⠀⠀⠀⠀⠀⠉⠀⠀⠀⠸⠷⣾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''


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
        print(response_content["choices"][0]["message"]["content"])

def genrative_ai_stories(listOfDetails):
    message = f"Create me a random stories using {str(listOfDetails)}. Not more than 100 words. Make sure they sound perfectly like some real writer wrote it and story should sound meaningful irrespective what content i have put in it."
    genrative_api(message=message)

def standard_stories(listOfDetails):
    message = """
One evening, {name} was mining deep in the {place} when they heard a strange noise—clink! clank! A glimmering {noun} lay in the dirt, shining brightly. "What in the world is this?" {name} said, picking it up. The moment {name} touched it, the {noun} started {verb}, sending out flashes of light! Startled, {name} jumped back, only to spot a {noun} creeping up behind them, {verb} slowly.

"Not today!" shouted {name}, grabbing {noun} and sprinting through the {place}, leaping over {noun}s and dodging {noun}s. It was a wild chase—would for {name} to catch {noun} before it vanished forever?
"""
    placeholders = ['name', 'noun', 'partOfBody', 'number', 'place', 'verb']
    listOfDetailsAsDict = {placeholders[i]:listOfDetails[i] for i in range(len(placeholders))}
    print(message.format(**listOfDetailsAsDict))    


def madlibs(choice,listOfDetails):
    if choice == "GEN":
        genrative_ai_stories(listOfDetails)
    else:
        standard_stories(listOfDetails)

def center_text(text, width=120):
    centered_art = []
    for line in text.split('\n'):
        padding = (width - len(line)) // 2
        centered_line = ' ' * padding + line
        centered_art.append(centered_line)
    return '\n'.join(centered_art)

def main_game(choice = input("Type GEN to start generative ai story, press enter to continue with standard story: ").upper()):
    name = input("Tell me a name: ")
    noun = input("Tell me a noun: ")
    partOfBody = input("Tell me a part of body: ")
    number = input("Tell me a number: ")
    place = input("Tell me a place: ")
    verb = input("Tell me a verb ending with 'ing': ")
    listOfDetails = [name,noun,partOfBody,number,place,verb]
    os.system('cls')
    print(center_text(madlibs_art))
    time.sleep(1.5)
    madlibs(choice=choice,listOfDetails=listOfDetails)
    time.sleep(1.5)
    print(center_text(grass_art))

if __name__ == '__main__':
    main_game()