from datetime import datetime

# Global list to store workouts
workouts = []

def add_workout(date, exercise, sets, reps, weight):
    """Add a workout entry to the list."""
    workout_entry = f"{date.strftime('%Y-%m-%d')},{exercise.lower()},{sets},{reps},{weight}"
    workouts.append(workout_entry)
    return True

def get_personal_best(exercise):
    """Return the highest weight lifted for an exercise."""
    exercise = exercise.lower()
    relevant_workouts = [w.split(',') for w in workouts if exercise in w]
    
    if not relevant_workouts:
        return None
        
    max_weight_entry = max(relevant_workouts, key=lambda x: int(x[4]))
    return int(max_weight_entry[4])  # Just the weight

def calculate_progress(exercise):
    """Check if weight is increasing for an exercise."""
    exercise = exercise.lower()
    relevant_workouts = [w.split(',') for w in workouts if exercise in w]
    
    if len(relevant_workouts) < 2:
        return "Not enough data"
    
    weights = [int(w[4]) for w in relevant_workouts]
    return "Increasing" if weights[-1] > weights[0] else "Stable or Decreasing"

def save_workouts(filename):
    """Save workout data to a text file."""
    with open(filename, 'w') as f:
        for workout in workouts:
            f.write(workout + '\n')
    return True

def main():
    """Basic interface to use the tracker."""
    print("Welcome to Workout Tracker!")
    while True:
        print("\n1. Add workout\n2. Check personal best\n3. Check progress\n4. Save and quit")
        choice = input("What do you want to do? (1-4): ")
        
        if choice == "1":
            exercise = input("Exercise name: ")
            sets = int(input("Number of sets: "))
            reps = int(input("Number of reps: "))
            weight = int(input("Weight lifted (lbs): "))
            date = datetime.now()  # Use current date for simplicity
            add_workout(date, exercise, sets, reps, weight)
            print(f"Added {exercise} workout!")
        
        elif choice == "2":
            exercise = input("Exercise name: ")
            pb = get_personal_best(exercise)
            if pb is None:
                print(f"No data for {exercise} yet.")
            else:
                print(f"Personal best for {exercise}: {pb} lbs")
        
        elif choice == "3":
            exercise = input("Exercise name: ")
            progress = calculate_progress(exercise)
            print(f"Progress for {exercise}: {progress}")
        
        elif choice == "4":
            save_workouts("workouts.txt")
            print("Workouts saved to workouts.txt. Goodbye!")
            break
        
        else:
            print("Pick 1-4, try again.")

if __name__ == "__main__":
    main()