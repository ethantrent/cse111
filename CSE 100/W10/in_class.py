# Create a program that allows a user to input and rank their top 5 favorite movies.
# The program should:
# Prompt the user to enter the names of movies.
# Display the list of movies in the order they were entered, numbered from 1 to n.
# Allow the user to swap the rankings of movies if they wish to change the order.
# Continue allowing rank changes until the user is satisfied with the order.
# Finally, display the updated list of favorite movies in their new ranked order.
 
# Requirements:
# 1.Use a list to store the movie titles.
# 2.Implement input validation to ensure only valid ranking positions (1-n)
# are accepted when swapping positions.
# 3.The program should allow multiple changes to the rankings.
# 4.For this program, use the enumerate to loop through the lists

movies = []
movie = ''
print("Top 5 favorite movies ")

for i in range(5):
# List to store the movie titles
    movie = input('Enter movie: ').strip()
    movies.append(movie)

print("\nYour top 5 favorite movies are: ")

# Use enumerate to loop through the lists
for i, movie in enumerate(movies, 1):
    print(f'{i}. {movie}')

# Continue allowing rank changes until the user is satisfied with the order
swap = input(f"Would you like to swap the ranking? (y/n): ")
while swap == 'y':
    old_rank = int(input("Enter the ranking of the movie you would like to switch: "))
    new_rank = int(input("Enter the new ranking of the movie: "))
    # Implement input validation to ensure only valid ranking positions (1-n)
    if old_rank > 0 and old_rank <= 5 and new_rank > 0 and new_rank <= 5:
        movies[old_rank - 1], movies[new_rank - 1] = movies[new_rank - 1], movies[old_rank - 1]
        # Updated list of favorite movies
        print("\nUpdated list of favorite movies: ")
        for i, movie in enumerate(movies, 1):
            print(f'{i} - {movie}')
        swap = input(f"Would you like to swap the ranking again? (y/n): ")
    else:
        print("Invalid ranking position.")
else:
    print("\nFinal list of favorite movies: ")
    for i, movie in enumerate(movies, 1):
        print(f'{i} - {movie}')
