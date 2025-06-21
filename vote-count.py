countV = int(input("Enter Total Number of Votes: "))  
countAB = input("Enter Sequence of A or B in par with Total Number of votes represented above: \n").lower()

def counting_vote(countV, countAB):  
    countABList = [i for i in countAB]
    
    if countV == len(countABList) and len(countABList) <= 15:  
        countA = countABList.count('a')  
        countB = countABList.count('b')  
        if countA > countB:
            return "A"
        elif countA < countB:
            return "B"
        elif countA == countB:
            return "Tie"
        else:
            return "Error make sure its either A or B only"
    else:  
        return "Error: Your votes don't match the total number of votes represented above or you have given a count greater than 15"  

print(counting_vote(countV, countAB))