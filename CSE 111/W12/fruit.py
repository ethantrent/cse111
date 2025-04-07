"""Write a small Python program named fruit.py that demonstrates object oriented programming by modifying a list. Do the following:

Open a new blank file in VS Code and save it as fruit.py
Copy and paste this code at the top of your fruit program:
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
Add code to reverse and print fruit_list.
Add code to append "orange" to the end of fruit_list and print the list.
Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
Add code to remove "banana" from fruit_list and print the list.
Add code to pop the last element from fruit_list and print the popped element and the list.
Add code to sort and print fruit_list.
Add code to clear and print fruit_list.
At the bottom of your program write a call to the main function."""

def main ():
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"append: {fruit_list}")

    i = fruit_list.index("apple")
    fruit_list.insert(i, "cherry")
    print(f"insert: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove: {fruit_list}")

    last_item = fruit_list.pop()
    print(f"pop: {last_item} {fruit_list}")

    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    fruit_list.clear()
    print(f"cleared: {fruit_list}")

if __name__ == "__main__":
    main()