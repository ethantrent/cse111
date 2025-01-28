# Variables to track the lowest, highest, and average life expectancy for the selected country
lowest = 999999999
highest = 0
average_expectancy = 0
total_expectancy = 0
count = 0

# Variables to track the lowest/highest for the selected country
lowest_year_country = ""
highest_year_country = ""
lowest_year_expectancy = 999999999
highest_year_expectancy = 0

# Get user input for the country
selected_country = input('Enter the country you want to analyze: ').strip()

# Load data set
with open('life-expectancy.txt') as f:
    # Iterate through each line
    for line in f:
        # Remove any whitespace
        clean_line = line.strip()
        # Split each line into parts
        line_parts = clean_line.split(',')
        country = line_parts[0]
        year = int(line_parts[2])
        expectancy = float(line_parts[3])
        
        # Process data only for the selected country
        if country.lower() == selected_country.lower():
            total_expectancy += expectancy
            count += 1

            # Check for lowest and highest life expectancy for this country
            if expectancy < lowest:
                lowest = expectancy
                lowest_year_country = country
                lowest_year = year

            if expectancy > highest:
                highest = expectancy
                highest_year_country = country
                highest_year = year

# Calculate average expectancy for the selected country
if count > 0:
    average_expectancy = total_expectancy / count
else:
    average_expectancy = 0

# Output results for the selected country
if count > 0:
    print(f'\nFor the country "{selected_country}":')
    print(f'The lowest life expectancy was {lowest} in {lowest_year}.')
    print(f'The highest life expectancy was {highest} in {highest_year}.')
    print(f'The average life expectancy across all years was {average_expectancy:.2f}.')
else:
    print(f'\nNo data available for the country "{selected_country}".')
