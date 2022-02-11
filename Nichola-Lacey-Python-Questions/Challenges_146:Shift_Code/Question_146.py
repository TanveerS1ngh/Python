# In this challenge you will need to use the following skills:
# -input and display data;
# -lists;
# -splitting and joining strings;
# -if statements;
# -loops (while and for);
# -subprograms.

# The Challenge

# A shift code is where a message can be easily encoded and is one of the simplest codes to use. Each letter is moved forwards through the alphabet a set number of letters to be represented by a new letter. For instance, “abc” becomes “bcd” when the code is shifted by one (i.e. each letter in the alphabet is moved forward one character).

# You need to create a program which will display the following menu:
#	1) Make a code
#	2) Decode a message
#	3) quit
#	enter your selection:

# If the user selects 1, they should be able to type in a message (including spaces) and then enter a number. Python should then display the encoded message once the shift code has been applied.
# If the user selects 2, they should enter an encoded message and the correct number and it should display the decoded message (i.e.move the correct number of letters backwards through the alphabet).
# If they select 3 it should stop the program from running.

# After they have encoded or decoded a message the menu should be displayed to them again until they select quit.


# Problems You Will Have to Overcome
# - Decide if you want to allow both upper and lower case letters or if you want to convert all the data into one case.
# - Decide if you are allowing punctuation.
# - If the shift makes the letter go past the end of the alphabet it should start again; i.e. if the user enters “xyz” and 5 is entered as the shift number, it should display “bcd”. This should work the opposite way for decoding a message, so if the value gets to “a” it will go back to “w”.
# - Make sure that suitable messages are displayed if the user selects an inappropriate option on the menu or selects an inappropriate number to make the shift code.

# Test out your decode option by decoding the message “we ovugjohsslunl”, which was created with the number 7 when the code only uses “abcdefghijklmnopqrstuvwxyz ” (note the space at the end).
