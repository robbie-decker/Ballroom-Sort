import json

# Read list, if it does not exist create it
# Using a context manager :O
with open("recording_list.json", 'a+') as myFile:
    oldDict = {}
    # Get first char from file
    myFile.seek(0)
    first_char = myFile.read(1)
    myFile.seek(0)

    # If file is not empty
    if first_char:
        oldDict = json.load(myFile)

    # Ask the user for name of lead and number
    leadName = input("What is the name of the lead? ")
    leadNum = input("What is the back number of the lead? ")
    leadInfo = leadName + leadNum
    heatDict = {}

    # Ask the user to input heat number (type q to quit)
    print("Write down a heat number and press enter (non numbers will quit)")
    while(True):
        try:
            heatNum = int(input())
            if isinstance(heatNum, int):
                # Heat numbers should be keys, names can be in an array 
                heatDict[heatNum] = [leadInfo]

        except ValueError:
            break

    # Compare old info against new stuff
    if oldDict:
        for oldKey, oldValue in oldDict.items():
            oldKey = int(oldKey)
            matchingKey = oldKey in heatDict
            # Check if there are mutliple people in the same round
            if matchingKey:
                for value in oldValue:
                    heatDict[oldKey].append(value)
            else:
                heatDict[oldKey] = oldValue

    # Clear info in file
    myFile.truncate(0)
    # Put info into the file
    json.dump(heatDict, myFile, sort_keys=True, indent = 2)