speedLimit = int(input("Enter the speed limit: "))
recordedSpeed = int(input("Enter the recorded speed of the car: "))
limits = {"1-20": "$100", "21-30": "$270", "31<": "$500"}
messages = ["Congratulations, you are within the speed limit!","You are speeding and your fine is "]
formula = (recordedSpeed - speedLimit)
def speeding_ticket():
    if formula <= 0:
         return messages[0]
    elif formula <= 20:
         return messages[1]+limits["1-20"]
    elif formula <= 30:
         return messages[1]+limits["21-30"]
    else:
         return messages[1]+limits["31<"]

print(speeding_ticket())