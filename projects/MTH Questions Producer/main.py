import random


def endProgram(message = "You entered the wrong value. Ending the program."):
    print(message)
    quit() 
# end of "endProgram" function   
    
    
def isFloat(number): # function checking if value is a float
    # checking int value
    if isinstance(number, int):
        return False
    # checking float value
    if isinstance(number, float):
        return True
    # checking string value
    if number[0].isnumeric() or number[len(number) - 1].isnumeric(): # checking if fist value or last value is numeric 
        if '.' in number: 
            return True
        else:
            return False
    else:
        return False
# end of "isFloat" function

def removeDuplicates(listOfItemsToBeRemoved, listOfItemsBeingComparedWith): 
    for i in listOfItemsBeingComparedWith:
        if i in listOfItemsToBeRemoved:
            listOfItemsToBeRemoved.remove(i)
    # end of for loop (i)
    return listOfItemsToBeRemoved
# end of "removeDuplicates" function    
            
    
def expandRange(beginRange, endRange): # takes in two values and outputs the range
    rangeItems = []
    for i in range(int(beginRange),int(endRange) + 1):
        rangeItems.append(i)
    return rangeItems
# end of "expandRange" function        
        
        
def sortProblemsIntoList(problems):
    newProblems = []
    
    for arrayItem in problems:
        # variables
        beginNumberIndex = 0
        beginNumberIndexFound = False
        endIndex = 0
        endIndexFound = False
        rangeFound = False
        rangeIndex = 0
        unitFound = False
        
        for iterator, stringItem in enumerate(arrayItem):
            # ASSESSING THE CHARACTERS IN THE STRING
            if stringItem == ':' and not beginNumberIndexFound:
                unitFound = True
                unit = arrayItem[beginNumberIndex : iterator]
                
            elif not beginNumberIndexFound and stringItem.isnumeric() and (unitFound or ':' not in arrayItem): # Tracking beginNumberIndex
                beginNumberIndex = iterator
                beginNumberIndexFound = True
            
            elif stringItem == '-':
                rangeFound = True
                rangeIndex = iterator
                
            elif stringItem == ',' and not endIndexFound: # Tracking endIndex when comma found.
                endIndex = iterator - 1
                endIndexFound = True
                
            elif iterator == len(arrayItem) - 1 and not endIndexFound: # Tracking endIndex when length reached and no comma found.
                endIndex = iterator 
                endIndexFound = True
            
            
            # APPENDING ITEMS
            if not rangeFound and beginNumberIndexFound and endIndexFound: # appending value with no range
                # Appending the item to the newProblems list
                newProblems.append(arrayItem[beginNumberIndex : endIndex + 1]) 
                
                # resetting variables
                endIndexFound = False 
                beginNumberIndexFound = False
                
            elif rangeFound and beginNumberIndexFound and endIndexFound: # appending values with range
                # assigning the list from expandRange function to a new variable
                rangeItems = []
                rangeItems = expandRange(int(arrayItem[beginNumberIndex : rangeIndex].strip()), int(arrayItem[rangeIndex + 1 : endIndex + 1].strip()))
                
                for i in rangeItems: # looping through the range items to they can be added one-by-one
                    newProblems.append(str(i))
                    
                # resetting variables
                endIndexFound = False 
                beginNumberIndexFound = False
                rangeFound = False
                
    return newProblems
# end of "sortProblemsIntoList" function


def produceProblems(problems, uniqueProblemsDesired):  
    newProblems = []
    i = 0 # counter for while loop
    while i < uniqueProblemsDesired:
        randomIndex = random.randint(0, len(problems) - 1)
        if problems[randomIndex] not in newProblems: # asking for only unique values  
            newProblems.append(problems[randomIndex]) # appending values at random index
            i = i + 1 # only iterating if unique value was added     
    
        # end of while loop    
         
    return newProblems
# end of "produceProblem" function


def convertFromStringToDouble(problems):
    return problems
# end of "convertFromStringToDouble" function


def randomizeList(listOfProblems):
    return random.sample(listOfProblems, len(listOfProblems))
# end of "randomizeList" function


def printList(problemsToPrint, numberOfItemsForPrint = None): # prints the values in the list and returns the amount of values that were printed yet desired
    numberOfProblemsDesiredAndNotPrinted = 0 
    if numberOfItemsForPrint > 0: # only printing values if the number of items to print is greater than zero
        numberOfItemsForPrint = int(numberOfItemsForPrint) # changing numberOfItemsForPrint variable to a integer
        if numberOfItemsForPrint != None: # only printing the number of items specified if there are enough in the list # changing my return value
            if numberOfItemsForPrint > len(problemsToPrint): # if the number of problems desired exceeds the length of the list, update it
                numberOfProblemsDesiredAndNotPrinted = numberOfItemsForPrint - len(problemsToPrint)
                numberOfItemsForPrint = len(problemsToPrint)
            for i in range(0,numberOfItemsForPrint): # looping through each item and printing
                print(problemsToPrint[i], end = " ") 
            # end of for loop (i)
        elif numberOfItemsForPrint == None: # if the number of items was not specified, printing the entire list and returning zero
            for j in problemsToPrint:
                print(j , end = " ")
            return 0
            # end of for loop (j)
    return numberOfProblemsDesiredAndNotPrinted # returning number of items desired but not printed due to smaller list size
# end of "printList" function


def getInputFromUser(allProblems, problemsMarkedForReview):
    # Taking input from the user
    problemSelection = input("What database do you wish to study from? (enter 0 for review and non-review or 1 for review only): ")
    numberOfProblems = input("Please enter the number of problems you would like: ")
    
    if isFloat(numberOfProblems): # alerting user if float was entered
        print("You entered a float. Changing ", float(numberOfProblems), " to int: " , int(float(numberOfProblems))) 
         
    numberOfProblems = int(float(numberOfProblems)) # Changing number of Problems to integer
    
    if numberOfProblems <= 0: # ensuring that the value entered is larger than 0 and not a float
        endProgram("Must enter a positive numberer of problems as integer. Ending Program.")
    
    
    # using the "sortProblemsIntoList" function to isolate each problem from the string
    allProblems = sortProblemsIntoList(allProblems)
    problemsMarkedForReview = sortProblemsIntoList(problemsMarkedForReview)

    # shuffling values in the lists to random locations
    allProblemsRandomized = randomizeList(allProblems)
    problemsMarkedForReviewRandomized = randomizeList(problemsMarkedForReview)

    # Printing List to User
    if problemSelection == '0': # user wants all problems
        removeDuplicates(allProblemsRandomized, problemsMarkedForReviewRandomized) # removing any values that exist in problems marked for review out of the all problems list so that the user is receiving unique problems from both lists
        print("\n------------------------------------------\n")
        numberOfProblems = printList(problemsMarkedForReviewRandomized, numberOfProblems)
        numberOfProblems = printList(allProblemsRandomized, numberOfProblems)
        print("\n\n------------------------------------------\n")
        if numberOfProblems > 0:
                print("Sorry. Number of problems desired is greater than the amount available. We printed what we could.") 
    elif problemSelection == '1': # user wants only problems marked for review
        if len(problemsMarkedForReviewRandomized) > 0:
            numberOfProblems = printList(problemsMarkedForReview, numberOfProblems)
            if numberOfProblems > 0:
                print("Sorry. Number of problems desired is greater than the amount marked for review. We printed what we could.") 
        else:
            endProgram("Sorry; there are no review problems.")      
   
    else: 
        endProgram("You must enter either a 0 or 1; ending program.")
# end of "getInputFromUser" function       

#"4.10: 470-472, 474-477, 479, 481, 484, 490-497, 499-503", "1.1: 2-11, 42-43", "1.1: 12-15, 20-21, 24-26"
# String Array of Homework Problems    
allproblems = ["4.10: 470-472, 474-477, 479, 481, 484, 490-497, 499-503", "1.1: 2-11, 42-43", "1.1: 12-15, 20-21, 24-26", "Quiz3: 100-120"]
problemsMarkedForReview = ["Quiz3: 100-120"]
newProblems = sortProblemsIntoList(allproblems)
getInputFromUser(allproblems, problemsMarkedForReview)
