lowest = 999999999
highest = 0
average_expectancy = 0
total_expectancy = 0
count = 0

# Variables to track the lowest/highest for the year of interest
lowest_year_country = ""
highest_year_country = ""
lowest_year_expectancy = 999999999
highest_year_expectancy = 0

interest_year = int(input('Enter a year of interest: '))

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
        
        # Check for overall lowest and highest life expectancy
        if expectancy < lowest:
            lowest = expectancy
            lowest_country = country
            lowest_year = year
        
        if expectancy > highest:
            highest = expectancy
            highest_country = country
            highest_year = year
        
        # Check for lowest and highest life expectancy in the interest year
        if year == interest_year:
            total_expectancy += expectancy
            count += 1
            
            if expectancy < lowest_year_expectancy:
                lowest_year_expectancy = expectancy
                lowest_year_country = country
            
            if expectancy > highest_year_expectancy:
                highest_year_expectancy = expectancy
                highest_year_country = country

# Calculate average expectancy for the year of interest
if count > 0:
    average_expectancy = total_expectancy / count
else:
    average_expectancy = 0

# Output results
print(f'\nThe overall lowest life expectancy was {lowest} from {lowest_country} in {lowest_year}.')
print(f'The overall highest life expectancy was {highest} from {highest_country} in {highest_year}.')

print(f'\nFor the year {interest_year}:')
if count > 0:
    print(f'\nThe average life expectancy across all countries was {average_expectancy:.2f}.')
    print(f'The lowest life expectancy was {lowest_year_expectancy} from {lowest_year_country}.')
    print(f'The highest life expectancy was {highest_year_expectancy} from {highest_year_country}.')
else:
    print("No data available for the specified year.")
