import random
from datetime import datetime, time
import math

def get_base_wait_time(current_time):
    """Calculate base wait time based on time of day.
    
    Args:
        current_time (time): Current time of day
        
    Returns:
        int: Base wait time in minutes
    """
    # Peak hours (11:30 AM - 1:30 PM)
    peak_start = time(11, 30)
    peak_end = time(13, 30)
    
    # Convert current time to minutes since midnight for easier comparison
    current_minutes = current_time.hour * 60 + current_time.minute
    peak_start_minutes = peak_start.hour * 60 + peak_start.minute
    peak_end_minutes = peak_end.hour * 60 + peak_end.minute
    
    if peak_start_minutes <= current_minutes <= peak_end_minutes:
        return 15  # Peak time base wait
    elif current_minutes < peak_start_minutes:
        # Calculate how close we are to peak time
        minutes_to_peak = peak_start_minutes - current_minutes
        if minutes_to_peak <= 30:  # Within 30 minutes of peak
            return 10 + (30 - minutes_to_peak) // 6  # Gradually increases
        return 10  # Regular time
    else:
        # After peak time
        minutes_from_peak = current_minutes - peak_end_minutes
        if minutes_from_peak <= 30:  # Within 30 minutes of peak end
            return 15 - (minutes_from_peak // 6)  # Gradually decreases
        return 10  # Regular time

def add_random_variation(base_time):
    """Add random variation to base wait time.
    
    Args:
        base_time (int): Base wait time in minutes
        
    Returns:
        int: Wait time with random variation
    """
    variation = random.randint(-3, 3)
    return max(5, base_time + variation)  # Ensure minimum 5-minute wait

def calculate_wait_time():
    """Calculate total wait time based on current conditions.
    
    Returns:
        tuple: (total_wait_time, breakdown)
    """
    current_time = datetime.now().time()
    base_time = get_base_wait_time(current_time)
    
    # Add random variation
    final_time = add_random_variation(base_time)
    breakdown = f"Base time: {base_time} minutes"
    breakdown += f"\nRandom variation: {final_time - base_time} minutes"
    
    return final_time, breakdown

def format_wait_time(minutes):
    """Format wait time into a human-readable string.
    
    Args:
        minutes (int): Wait time in minutes
        
    Returns:
        str: Formatted wait time
    """
    if minutes < 60:
        return f"{minutes} minutes"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes == 0:
            return f"{hours} hour{'s' if hours != 1 else ''}"
        return f"{hours} hour{'s' if hours != 1 else ''} and {remaining_minutes} minutes"

def main():
    """Main function to demonstrate the wait time calculator."""
    print("Chick-fil-A Wait Time Estimator")
    print("===============================")
    
    while True:
        print("\nOptions:")
        print("1. Get Wait Time Estimate")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == "2":
            break
        elif choice != "1":
            print("Invalid choice. Please try again.")
            continue
        
        wait_time, breakdown = calculate_wait_time()
        
        print("\nWait Time Estimate:")
        print("-------------------")
        print(f"Estimated wait time: {format_wait_time(wait_time)}")
        print("\nBreakdown:")
        print(breakdown)
        print(f"Total wait time: {format_wait_time(wait_time)}")

if __name__ == "__main__":
    main() 