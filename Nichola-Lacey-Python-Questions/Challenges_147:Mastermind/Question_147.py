# In this challenge you will need to use the following skills:
# - input and display data;
# - lists;
# - random choice from a list;
# - if statements;
# - loops (while and for);
# - subprograms.

# The Challenge

# You are going to make an on-screen version of the board game “Mastermind”. The
computer
will
automatically
generate
four
colours
from a list

of
possible
colours(it
should
be
possible
for the computer to randomly select the same colour more than once).For instance, the computer may choose “red”, “blue”, “red”, “green”.This sequence should n ot be displayed to the user.
# After this is done the user should enter their choice of four colours from the same list the computer used. For instance, they may choose “pink”, “blue”, “yellow” and “red”.
# After the user has made their selection, the program should display how many colours they got right in the correct position and how many colours they got right but in the wrong position. In the example above, it should display the message “Correct colour in the correct place: 1” and “Correct colour but in the wrong place: 1”.

# The user continues guessing until they correctly enter the four colours in the order they should be in. At the end of the game it should display a suitable message and tell them how many guesses they took.



# Problems You Will Have to Overcome


# The hardest part of this game is working out the logic for checking how many the user has correct and how many are in the wrong place. Using the example above, if the user enters “blue”, “blue”, “blue”, “blue” they should see the messages, “Correct colour in the correct place: 1” and “Correct colour but in the wrong place: 0”.

# Decide if there is an easier way of allowing the user to enter their selection (e.g. using a code or a single letter to represent the colour). If using the first letter, make sure you only use colours that have a unique first letter (i.e. avoid using blue, black and brown as options and select just one of these as a possibility). Make your instructions clear to the user.

# Decide if you want to allow upper and lower case or if it is easier to convert everything to the same case.

# Make sure you build in validation checks to make sure the user is only entering valid data and display a suitable message if they make an incorrect selection. If they do make an incorrect selection you may want to allow them to enter the data again, rather than class it as an incorrect guess.
