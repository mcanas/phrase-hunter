# Create your Game class logic in here.

# Create a Game class

# has an __init()__ method
#   sets missed attribute to initial value of 0
#   sets phrases attribute that will hold a list of Phrase instances
#     a phrase should only contain spaces and letters
#   sets an active_phrase attribute with initial value of None
#   sets a guesses attribute that will hold a list of guessed letters


# has a start() method
#   calls welcome()
#   starts game loop
#     calls get_guess()
#     adds guess to guesses list
#     increments missed when guess is incorrect
#     calls game_over() when missed equals 5


# has a get_random_phrase() method
#   returns a random Phrase from phrases list

# has a welcome() method
#   prints a welcome message

# has a get_guess() method
#   retreives and validates user input as a single letter guess
#   store guess in guesses list

# has a game_over() method
#   prints a win or lose message
