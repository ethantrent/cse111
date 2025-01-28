# To declare a list, you use the square brackets []
movies = []

# If you want to start the list with items in it, you can put them inside the square brackets with commas
movies = ["The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"]

# You can also add items to the list using the append method
movies.append("The Matrix 4")

# iterate through the items of a list using the "for each"
for movie in movies:
    print(movie)

# add to a specific index in the list
movies.append(1, "The Matrix: Resurrections")

# remove an item from the list
movies.remove("The Matrix Reloaded")

# += is a shorthand way of adding to a variable
total = 0
total += 5
