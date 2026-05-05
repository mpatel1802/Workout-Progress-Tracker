# Workout Progress Tracker
# Name: Mann Patel
# Date: 2026-03-28

# Problem Decription: 

"""
I regularly go to the gym for workout sessions which includes 
strength training. I always find myself logging my progress in notes application (text format)
on my iPhone which at times can be very time consuming and hard to follow. 

Key challenges that I face everyday: 
1. Manual calculation of my training volume
2. Manually selecting my highest lift of the day 
3. Scrolling through pages of my logs to find a session on one particular date or exercise
4. There have been multiple instances where I have misred reps and forgotten sessions when calculating
   leading to incorrect results. 
5. No progress summary for me to review
Thus, my old method is very time consuming and error-prone. 

My solution to the above problem: 

A program which parses the data by ignoring unwanted lines and 
skipping empty/wrong data. 
It includes an interactive menu design implemented using while loop which validates the 
user's input, asks exercise name that the user wishes to view the data about. 
It loads the workouts/sessions using a function and uses other helper functions 
to calculate statistics, maximum weights lifted, number of sets, 
average number of repetitions per set. And finally, it creates a file which includes the 
summarized information based on the calculated stats. 
"""


def mainMenu(workouts): 

    '''
    This function uses a WHILE loop to prompt user a series of options 
    and continues prompting until user enters a valid choice (1-4). 
    I am using if/elif/else, it calls the revelant function, calculates the data and displays the 
    results in a well-formatted structure. 
    '''
     
    while True: 

        try:
            print("\n ============== WORKOUTS TRACKER ==============") 
            print("1. Exercise Statistics")
            print("2. Date Statistics")
            print("3. Save Summary")
            print("4. Exit")
            print("===============================================")


            user_input = input("Please select an option from 1-4: ").strip()

            if (user_input == '1'): 

                name = input("Enter exercise name: ").strip() # Removing leading/trailing whitespaces from user's input
                exercise_data = getExerciseStats(workouts, name)

                if (exercise_data):
                    print(f"\n{name.capitalize()} Data: ")
                    print(f"  Volume: {round(exercise_data['total_volume'])} kg")
                    print(f"  Max weight: {round(exercise_data['max_weight'])} kg") 
                    print(f"  Sets: {exercise_data['num_sets']}")
                    print(f"  Average reps per set: {exercise_data['avg_reps']} reps")
                else:
                    print("\nData does not exist for the given exercise!")

            elif (user_input == '2'): 

                date = input("Enter date (YYYY-MM-DD): ").strip()
                exercise_data = statsDate(workouts, date)

                if exercise_data:
                    print(f"\n Data on {date}")
                    print(f"  Volume: {round(exercise_data['total_volume'])} kg")
                    print(f"  Exercises: {exercise_data['total_exercises']}")
                    print(f"  Sets: {exercise_data['num_sets']}")
                else:
                    print("No workout on that date.")

            elif (user_input == '3'):
                saveSummary(workouts)

            elif (user_input == '4'): 
                print("\nThank you for using this program. Take care and Stay fit!\n")
                break

            else:
                print("\nInvalid entry! Please enter 1, 2, 3, or 4 (if you wish to exit)")

        except Exception as error: 
            print(f"Error occured: {error}") 


def loadWorkouts(filename):

    '''
    This function is the heart of the program. It opens the file (workouts.txt)
    and parses the data (comma separated) to store into a dictionary with same number of required key/value pairs. 
    It does robust error handling while opening the file and parsing the data to avoid crashes.
    It also skips comments, empty lines, strips empty whitespaces and returns a list of dictionaries. 
    '''
    workouts = [] 
    sub_part = [] # List to store comma separated elements from each line

    try: 
        
        f = open(filename, "r")
        line_number = 0

        for line in f: 
            line_number += 1 
            line = line.strip() 

            if (len(line) == 0 or line[0] == '#'): # Skipping empty and comment lines
                continue
             
            sub_part = line.split(',') 
            
            for sl in range(len(sub_part)): 
                sub_part[sl] = sub_part[sl].strip()

            if len(sub_part) != 5:
                print(f"Error occured on line {line_number}") # Added for debugging purposes
                continue
            
            try: 
                workout_dict = { # Storing each element of each line in a dictionary

                    "date": sub_part[0],
                    "exercise": sub_part[1],
                    "sets": int(sub_part[2]),
                    "reps": int(sub_part[3]),
                    "weight": float(sub_part[4]),                
                }

                workouts.append(workout_dict)

            except ValueError: 
                print(f"Error occured on line {line_number}") # Added for debugging purposes
                continue   

    except FileNotFoundError:  
        print(f"Unable to find {filename}!") # Added for debugging pruposes
        return []

    return workouts


def getExerciseStats(workouts, exercise_name): 

    '''
    This functions handles all the arithmetic calculations of the program. 
    It adds the matched exercise sessions based on what user inputs and calculates
    total volume, number of repetitions, maximum weight lifted, and average 
    reps per set and returns the result of type dictionary. 
    '''
    matched = [] 
    num_sets = 0
    max_weight = 0.0
    total_volume = 0.0
    repetitions = 0
    result = {}

    for i in workouts: 
        if (i['exercise'].lower() == exercise_name.lower()): 
            matched.append(i)

    if (not matched):
        return None
    
    for j in matched:  # This loop calculates total volume, reps, maximum weight and sets
        
        volume = j['sets'] * j['weight'] * j['reps']
        repetitions += j['reps'] * j['sets']
        total_volume += volume
        num_sets += j['sets']

        if (j['weight'] > max_weight):
            max_weight = j['weight']
        
    if (num_sets > 0): 
        avg_reps = repetitions / num_sets
    else: 
        avg_reps = 0

    result = {
        'total_volume': total_volume,
        'max_weight': max_weight,
        'num_sets': num_sets,
        'avg_reps': round(avg_reps)
    }

    return result


def statsDate(workouts, date): 

    '''
    This function does single training session analysis by date. It
    calculates session volume, exercise variety and total number of sets. 
    Returns a result of type dictionary with  key/value pairs of volume, exercises, and sets.
    '''

    matched = []
    total_volume = 0.0
    exercises_done = set() # I used set to make sure duplicate exercises are removed automatically
    num_sets = 0
    result = {}

    for i in workouts: 
        if (i['date'] == date): 
            matched.append(i)

    if (not matched): 
        return None
    
    for j in matched: 
        total_volume += j['sets'] * j['reps'] * j['weight']
        exercises_done.add(j['exercise']) # Avoiding duplicates
        num_sets += j['sets']

    result = {
        'total_volume': total_volume,
        'total_exercises': len(exercises_done),
        'num_sets': num_sets
    }

    return result


def saveSummary(workouts): 

    '''
    This function generates a summary report of the file data and saves the formatted 
    data into a file named workouts_summary.txt.
    '''

    added = []

    f = open("workouts_summary.txt", "w")
    f.write("==============================\n")
    f.write("Workout Summary Report\n")
    f.write("==============================\n")
    f.write(f"Total workouts: {len(workouts)}\n\n")

    for i in workouts:
        ex = i['exercise']
        if (ex not in added): 
            data = getExerciseStats(workouts, ex)
            if (data): 
                f.write(f"{ex.capitalize()}: \n")
                f.write(f"  Volume: {round(data['total_volume'])} kg\n")
                f.write(f"  Max: {round(data['max_weight'])} kg\n")
                f.write(f"  Sets: {data['num_sets']}\n")
                f.write(f"  Average reps per set: {data['avg_reps']}\n\n")
            added.append(ex)
    f.close()
    print("\nStatistics Summary saved to workouts_summary.txt!")


# ---- main ------
if __name__ == "__main__":

    workouts = loadWorkouts("workouts.txt") # Extracting workouts from file and saving the returned list of dictionaries into workouts

    if ((workouts) and (len(workouts) > 0)):
        print("\nNumber of workouts:", len(workouts))
    else:
        print("No workouts loaded.")

    mainMenu(workouts) # Passing workouts list as an argument to the main interative menu





