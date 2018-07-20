# Michaelmas Lesson 1: Hello World
#
# The first part of this lesson teaches some very basics of input and output using Python.
#
# For license see LICENSE

# Welcome! These example files are here to help you if you get stuck.
# DON'T JUST COPY AND PASTE, if you do this it is very unlikely you'll understand
#  what's going on. If you don't *understand* after reading this example file
#  ASK A DEMONSTRATOR. It's better to ask now and grasp the basics than
#  be so stumped later that you give up the course...
#
# Have fun...

# The first thing we can do is to print something to the output.
print("Hello World!")

# But that's not very interesting...
# Let's get the user's name in there too!

# We declare a variable to store shit in and give it a name "user_name"
# They're called variables because, they, well vary. They can change
# and that's why they're so useful. Think of them like boxes to put
# things to remember in.

# We can then get some input for the user and give them a prompt...
users_name = input("What is your name?")
print("Hello there " + users_name)

# I wonder how old they are?
some_number_string = input("Give me a number")

# Hang on: what the fuck are we doing here with int(some_number_string)?

# So we need a brief introduction into types. Not romantic ones,
#  but computationally. Arguably more exciting? Definitely more exciting!

# Let's think about it like types of alcohol you can drink on a night out.
#  If you mix drinks: bad things happen. Same with computers and types:
#  much like you crash, your program will crash if you mix types.

# What types have we got then?
# 'string' - a series of letters, numbers and symbols (words basically)
# 'int' - a whole number

# Luckily unlike mixing drinks, you can magic the types into each other
#  so long as it's a valid conversion. We can change 8782 (int) to "8782" (string)
#  or we can do "9312" (string) to 9312 (int). But not "8s7sabcs" (string) to an int
some_number = int(some_number_string)
added_ten = 10 + some_number

# You should know what's going on here now,
added_ten_string = str(added_ten)

# and here...
print("So at some point this year you're " + added_ten_string + "!")