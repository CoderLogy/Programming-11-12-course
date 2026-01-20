countHappyOrSad = input("Type happy or sad faces: \n")
def happy_or_sad(countHappyOrSad):
    countHappyFaces = countHappyOrSad.count(":-)")
    countSadFaces = countHappyOrSad.count(":-(")
    if countHappyFaces == countSadFaces:
        return "unsure"
    elif countHappyFaces > countSadFaces:
        return "happy"
    elif countHappyFaces < countSadFaces:
        return "sad"
    else:
        return "happy_or_sad error"
print(happy_or_sad(countHappyOrSad))


