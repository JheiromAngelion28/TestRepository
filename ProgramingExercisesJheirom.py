#Print Hello world  works by placing a print command, then place quotes on the word on either side along with parenthesis will cause python to treat the word as a string. 
print("Hello, World!")

#From what I have observed, you can also add numbers using the print fuction, just place the numbers you want to add, then the parenthesis then it will add both numbers together.
print(5 + 3)

#Python can also accept for multiple strings to be excecuted.
print("Python", "is", "fun!")

#I have observed that a slash is a way to add quotation marks within a string.
print("She said, \"Hello!\"")

# The \n acts like an enter button to shift the string down a bar.
print("First line\nSecond line")

# According to htts://realpython.com The slash allows us to force arguments into postition.
print("Item 1\tItem 2\tItem 3")


print("The result is", 42)


print(12345)


print(3.14159)


print("Dollar sign: $")


#This lets you modify or add additional strings or characters in a string.
print("apple", "banana", "cherry", sep=", and ")

#This lets you place additional characters into the middle of a string. Here, I placed the word "my" so that it says "Hello my world".
print("Hello,", end=" my ")
print("World!")

#This one multiplies the code by this symbol * depending on the vaule entered. Here I entered a value of 10.
print("Python! " * 10)

# When a unicode hex vaule for a character is emtered, then it will display the special character/symbol.
print("\u2764") # Prints a heart symbol

print()

print(True)
print(False)

print(1.2e3) # Prints 1200.0

#Python allows a triple quotation mark to turn a word into a string.
print("""This is a multiline
print statement.""")

print("This is a backslash: \\")
