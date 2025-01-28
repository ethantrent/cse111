# Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format:

# Scripture: Old Testament, Book: Genesis, Chapters: 50

# Find the largest number of chapters in the scriptures.

# Find the book that has the largest number of chapters in the scriptures.

# Change your program so that it only prints the books in the Book of Mormon.

# Find the book in the Book of Mormon that has the largest number of chapters.

# At the beginning of the program, ask the user which volume of scriptures they would like to learn about
# Then, find the book in that volume of scripture that has the largest number of chapters

largest_chapters = 0
largest_book = ''

# open file, read through it line by line, separate the line into the appropriate pieces and display each book in this format
with open('books_and_chapters.txt') as f:
    for line in f:
        line_parts = line.split(':')
        book = line_parts[0]
        chapters = int(line_parts[1])
        scripture = line_parts[2].strip()
        print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapters}')

        if chapters > largest_chapters:
            largest_chapters = chapters
            largest_book = book
print(f'The book with the largest number of chapters is {largest_book} with {largest_chapters} chapters.')

