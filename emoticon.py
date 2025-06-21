emoticon = {"CU":"see you",
            ":-)":"I'm happy",
            ":-(":"I am unhappy",
            ":-P":"stick out my tounge",
            "(`.`)":"sleepy",
            "TA":"totally awesome",
            "CCC":"Canadian Computing Competition",
            "CUZ":"because","TY":"thank-you",
            "YW":"you're welcome",
            "TTYL":"talk to you later"}

textInput = input("Enter Phrase> ").upper()

def emoticon_parsing():
        if textInput in emoticon:
            return emoticon[textInput]
        else:
            return emoticon["TTYL"]

while textInput != "TTYL":
    print(emoticon_parsing())
    textInput = input("Enter Phrase> ").upper()