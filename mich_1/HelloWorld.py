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
users_name = input("What is your name?")
print("Hello there " + users_name)

# I wonder how old they are
some_number_string = input("Give me a number")

# hang on, what the fuck are we doing here?
#  Turns out that everything in Python has a "type". Words have a type of "string"
#  and whole numbers (or integers to use the maths term) the type "int". We can't
#  mix and match. Much like in real life we can't add words or make sentances using
#  just numbers...
some_number = int(some_number_string)
added_ten = 10 + some_number

# You should know what's going on here now...
added_ten_string = str(added_ten)

print("So at some point this year you're " + added_ten_string + "!")

# testing branching in GitHub