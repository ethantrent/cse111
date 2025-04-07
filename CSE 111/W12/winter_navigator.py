import math
from datetime import datetime

def get_weather_data():
    """Return current weather data (mock data for demonstration)."""
    return {
        'condition': 'snow',
        'temperature': 25,
        'wind_speed': 15,
        'precipitation': 0.5
    }

def get_campus_data():
    """Return campus routes and locations."""
    return {
        'routes': {
            ('MC', 'Hart'): [
                {'path': 'MC -> Manwaring -> Hart', 'distance': 0.3, 'sheltered': True},
                {'path': 'MC -> Library -> Hart', 'distance': 0.4, 'sheltered': True},
                {'path': 'MC -> Crosswalk -> Hart', 'distance': 0.2, 'sheltered': False}
            ],
            ('Hart', 'Taylor'): [
                {'path': 'Hart -> Manwaring -> Taylor', 'distance': 0.4, 'sheltered': True},
                {'path': 'Hart -> Crosswalk -> Taylor', 'distance': 0.3, 'sheltered': False}
            ]
        },
        'parking_lots': {
            'morning': {
                'clear': ['MC Lot', 'Hart Lot', 'Taylor Lot'],
                'snow': ['MC Lot', 'Hart Lot'],
                'ice': ['MC Lot'],
                'blizzard': ['MC Lot']
            },
            'afternoon': {
                'clear': ['Hart Lot', 'Taylor Lot', 'Library Lot'],
                'snow': ['Hart Lot', 'Library Lot'],
                'ice': ['Hart Lot'],
                'blizzard': ['Hart Lot']
            },
            'evening': {
                'clear': ['Taylor Lot', 'Library Lot', 'MC Lot'],
                'snow': ['Library Lot', 'MC Lot'],
                'ice': ['Library Lot'],
                'blizzard': ['Library Lot']
            }
        }
    }

def calculate_commute_time(distance, weather):
    """Calculate commute time based on distance and weather."""
    # Speed limits for different weather conditions
    speeds = {
        'clear': 35,
        'snow': 20,
        'ice': 15,
        'blizzard': 10
    }
    
    # Extra time to add based on weather
    extra_time = {
        'clear': 5,
        'snow': 10,
        'ice': 10,
        'blizzard': 15
    }
    
    # Calculate base time
    speed = speeds.get(weather, speeds['clear'])
    time = (distance / speed) * 60
    
    # Add extra time
    buffer = extra_time.get(weather, extra_time['clear'])
    
    return math.ceil(time) + buffer

def find_safe_routes(start_location, end_location, weather):
    """Find safe routes between locations."""
    campus_data = get_campus_data()
    routes = campus_data['routes']
    
    # Get available routes
    available_routes = routes.get((start_location, end_location), [])
    
    # In bad weather, only return sheltered routes
    if weather in ['snow', 'ice', 'blizzard']:
        return [route for route in available_routes if route['sheltered']]
    return available_routes

def get_parking_recommendations(weather, time_of_day):
    """Get parking recommendations based on weather and time."""
    campus_data = get_campus_data()
    lots = campus_data['parking_lots']
    
    if time_of_day in lots and weather in lots[time_of_day]:
        return lots[time_of_day][weather]
    return []

def get_winter_preparation_checklist(weather):
    """Get a checklist of items to prepare for winter weather."""
    # Base checklist for all weather
    checklist = [
        "Wear warm winter coat",
        "Bring gloves and hat",
        "Wear waterproof boots",
        "Check BYUI alerts"
    ]
    
    # Add items based on weather
    if weather == 'snow':
        checklist.extend([
            "Bring snow scraper",
            "Allow extra time for commute",
            "Check tire pressure"
        ])
    elif weather == 'ice':
        checklist.extend([
            "Wear ice cleats",
            "Allow extra time for commute",
            "Check tire pressure"
        ])
    elif weather == 'blizzard':
        checklist.extend([
            "Bring snow scraper",
            "Allow extra time for commute",
            "Check tire pressure",
            "Bring emergency kit"
        ])
    
    return checklist

def get_user_input():
    """Get user input for the program."""
    print("\nBYUI Winter Weather Navigator")
    print("-" * 30)
    
    # Get distance
    while True:
        try:
            distance = float(input("\nEnter your commute distance (miles): "))
            if distance > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get weather condition
    while True:
        weather = input("\nEnter weather condition (clear/snow/ice/blizzard): ").lower()
        if weather in ['clear', 'snow', 'ice', 'blizzard']:
            break
        print("Please enter a valid weather condition.")
    
    # Get time of day
    while True:
        time_of_day = input("\nEnter time of day (morning/afternoon/evening): ").lower()
        if time_of_day in ['morning', 'afternoon', 'evening']:
            break
        print("Please enter morning, afternoon, or evening.")
    
    return distance, weather, time_of_day

def main():
    """Main function to run the Winter Weather Navigator."""
    try:
        # Get current weather
        weather_data = get_weather_data()
        
        # Get user input
        distance, weather, time_of_day = get_user_input()
        
        # Calculate commute time
        commute_time = calculate_commute_time(distance, weather)
        
        # Get preparation checklist
        checklist = get_winter_preparation_checklist(weather)
        
        # Get parking recommendations
        parking_lots = get_parking_recommendations(weather, time_of_day)
        
        # Display results
        print("\nResults:")
        print("-" * 30)
        print(f"\nCurrent Weather:")
        print(f"- Condition: {weather_data['condition']}")
        print(f"- Temperature: {weather_data['temperature']}°F")
        print(f"- Wind Speed: {weather_data['wind_speed']} mph")
        
        print(f"\nEstimated Commute Time: {commute_time} minutes")
        
        print("\nPreparation Checklist:")
        for item in checklist:
            print(f"- {item}")
        
        print("\nRecommended Parking Lots:")
        if parking_lots:
            for lot in parking_lots:
                print(f"- {lot}")
        else:
            print("No parking recommendations available")
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please try again.")

if __name__ == "__main__":
    main()