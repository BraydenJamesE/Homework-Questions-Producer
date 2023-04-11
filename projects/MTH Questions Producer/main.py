import numpy as np
import random
import math

# Global Variables
unit_dictionary = {} # Dictionary that tracks the unit assocaited with each problem

def End_program(message = "You entered the wrong value. Ending the program."): # this function ends the program with a default or specific message
    print(message)
    quit() 
# end of "End_program" function   
    
    
def Is_float(number): # function checking if value is a float
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
# end of "Is_float" function


def Remove_duplicates(list_of_items_to_be_removed, list_of_items_being_compared_with): # this function takes in two lists and removes the values that already exist in the second one out of the first. The second list does not lose any items, only the first.
    for i in list_of_items_being_compared_with:
        if i in list_of_items_to_be_removed:
            list_of_items_to_be_removed.remove(i)
    # end of for loop (i)
    return list_of_items_to_be_removed
# end of "Remove_duplicates" function


def Create_study_plan(number_of_days, number_of_problems, number_of_days_to_cover_each_problem = 1): # This function allows the user to create a study plan.
    if number_of_days_to_cover_each_problem != 1:
        number_of_problems_per_day = math.ceil((number_of_problems * number_of_days_to_cover_each_problem) / number_of_days)
        print("You must study", number_of_problems_per_day, "problems per day to be ready for your test if you do each problem", number_of_days_to_cover_each_problem, "times.")
    else:
        number_of_problems_per_day = math.ceil(number_of_problems / number_of_days)
        print("You must study", number_of_problems_per_day, "problems per day to be ready for your test.")
# end of "Create_study_plan" function
            
    
def Expand_range(begin_range, end_range): # takes in two values and outputs the range
    range_items = []
    for i in range(int(begin_range),int(end_range) + 1):
        range_items.append(i)
    return range_items
# end of "Expand_range" function        
        
       
        
        
def Sort_problems_into_list(problems):
    new_problems = []
    
    for array_item in problems:
        # variables
        begin_number_index = 0
        begin_number_index_found = False
        end_index = 0
        end_index_found = False
        range_found = False
        range_index = 0
        unit_found = False
        list_of_units = []
        
        for iterator, string_item in enumerate(array_item):
            # ASSESSING THE CHARACTERS IN THE STRING
            if string_item == ':' and not begin_number_index_found:
                unit_found = True
                unit = array_item[begin_number_index : iterator + 1] + " "
                if unit not in list_of_units: 
                    list_of_units.append(unit)

                
            elif not begin_number_index_found and string_item.isnumeric() and (unit_found or ':' not in array_item): # Tracking begin_number_index
                begin_number_index = iterator
                begin_number_index_found = True
            
            elif string_item == '-':
                range_found = True
                range_index = iterator
                
            elif string_item == ',' and not end_index_found: # Tracking end_index when comma found.
                end_index = iterator - 1
                end_index_found = True
                
            elif iterator == len(array_item) - 1 and not end_index_found: # Tracking end_index when length reached and no comma found.
                end_index = iterator 
                end_index_found = True
            
            
            # APPENDING ITEMS
            if not range_found and begin_number_index_found and end_index_found: # appending value with no range
                # Appending the item to the new_problems list
                new_problems.append(unit + array_item[begin_number_index : end_index + 1]) 
                
                # resetting variables
                end_index_found = False 
                begin_number_index_found = False
                
            elif range_found and begin_number_index_found and end_index_found: # appending values with range
                # assigning the list from Expand_range function to a new variable
                range_items = []
                range_items = Expand_range(int(array_item[begin_number_index : range_index].strip()), int(array_item[range_index + 1 : end_index + 1].strip()))
                
                for i in range_items: # looping through the range items to they can be added one-by-one
                    new_problems.append(unit + str(i))
                    
                # resetting variables
                end_index_found = False 
                begin_number_index_found = False
                range_found = False
                
    return new_problems
# end of "Sort_problems_into_list" function


def Produce_problems(problems, unique_problems_desired):  
    new_problems = []
    i = 0 # counter for while loop
    while i < unique_problems_desired:
        random_index = random.randint(0, len(problems) - 1)
        if problems[random_index] not in new_problems: # asking for only unique values  
            new_problems.append(problems[random_index]) # appending values at random index
            i = i + 1 # only iterating if unique value was added     
    
        # end of while loop    
         
    return new_problems
# end of "produceProblem" function


def Randomize_list(list_of_problems):
    return random.sample(list_of_problems, len(list_of_problems))
# end of "Randomize_list" function


def Print_list(problems_to_print, number_of_items_for_print = None): # prints the values in the list and returns the amount of values that were printed yet desired
    number_of_problems_desired_and_not_printed = 0 
    if number_of_items_for_print > 0: # only printing values if the number of items to print is greater than zero
        number_of_items_for_print = int(number_of_items_for_print) # changing number_of_items_for_print variable to a integer
        if number_of_items_for_print != None: # only printing the number of items specified if there are enough in the list # changing my return value
            if number_of_items_for_print > len(problems_to_print): # if the number of problems desired exceeds the length of the list, update it
                number_of_problems_desired_and_not_printed = number_of_items_for_print - len(problems_to_print)
                number_of_items_for_print = len(problems_to_print)
            for i in range(0,number_of_items_for_print): # looping through each item and printing
                print(problems_to_print[i]) 
            # end of for loop (i)
        elif number_of_items_for_print == None: # if the number of items was not specified, printing the entire list and returning zero
            for j in problems_to_print:
                print(j)
            return 0
            # end of for loop (j)
    return number_of_problems_desired_and_not_printed # returning number of items desired but not printed due to smaller list size
# end of "Print_list" function


def Get_intput_from_user(all_problems, problems_marked_for_review):
    
    # using the "Sort_problems_into_list" function to isolate each problem from the string
    all_problems = Sort_problems_into_list(all_problems)
    problems_marked_for_review = Sort_problems_into_list(problems_marked_for_review)

    # shuffling values in the lists to random locations
    all_problems_randomized = Randomize_list(all_problems)
    problems_marked_for_review_randomized = Randomize_list(problems_marked_for_review)
    
    # Taking input from the user
    problem_selection = input("What database do you wish to study from? (enter 0 for review and non-review, 1 for review only, and 2 for a study plan): ")
    
    if problem_selection == "2":
        number_of_days_until_exam = int(input("Enter the number of days you have to study: "))
        number_of_times_to_do_each_problem = int(input("Enter the number of times you want to do each problem: "))
        
        if number_of_times_to_do_each_problem <= 0 or number_of_days_until_exam <= 0:
            End_program("Error in the number you entered. Ending Program.")
        else:
            Create_study_plan(number_of_days_until_exam, len(all_problems), number_of_times_to_do_each_problem)
        End_program("Thank you!")
    
    number_of_problems = input("Please enter the number of problems you would like: ")
    
    if Is_float(number_of_problems): # alerting user if float was entered
        print("You entered a float. Changing ", float(number_of_problems), " to int: " , int(float(number_of_problems))) 
         
    number_of_problems = int(float(number_of_problems)) # Changing number of Problems to integer
    
    if number_of_problems <= 0: # ensuring that the value entered is larger than 0 and not a float
        End_program("Must enter a positive numberer of problems as integer. Ending Program.")
    

    # Printing List to User
    if problem_selection == '0': # user wants all problems
        Remove_duplicates(all_problems_randomized, problems_marked_for_review_randomized) # removing any values that exist in problems marked for review out of the all problems list so that the user is receiving unique problems from both lists
        print("\n------------------------------------------\n")
        number_of_problems = Print_list(problems_marked_for_review_randomized, number_of_problems)
        number_of_problems = Print_list(all_problems_randomized, number_of_problems)
        print("\n------------------------------------------\n")
        if number_of_problems > 0:
                print("Sorry. Number of problems desired is greater than the amount available. We printed what we could.") 
    elif problem_selection == '1': # user wants only problems marked for review
        if len(problems_marked_for_review_randomized) > 0:
            number_of_problems = Print_list(problems_marked_for_review, number_of_problems)
            if number_of_problems > 0:
                print("Sorry. Number of problems desired is greater than the amount marked for review. We printed what we could.") 
        else:
            End_program("Sorry; there are no review problems.")      
   
    else: 
        End_program("You must enter either a 0 or 1; ending program.")
# end of "Get_intput_from_user" function       


#"4.10: 470-472, 474-477, 479, 481, 484, 490-497, 499-503", "1.1: 2-11, 42-43", "1.1: 12-15, 20-21, 24-26"
# String Array of Homework Problems    
all_problems = ["3.7: 347-352, 355-363, 374-375,382, 384, 399", "5.1: 1-5, 8-15, 19-21, 27-30, 46-48", 
               "5.2: 67-69, 71-73, 83-85, 87, 89-91, 93-103", "5.3: 138-146, 152-162, 169-171"]
problems_marked_for_review = [""]

Get_intput_from_user(all_problems, problems_marked_for_review)
