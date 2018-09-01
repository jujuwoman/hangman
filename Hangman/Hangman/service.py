import requests
import random

# -------------------------------------------------------- #
# custom modules
# -------------------------------------------------------- #
from . import config

# -------------------------------------------------------- #
# helper functions
# -------------------------------------------------------- #

# select random word from API
# (used by views.index)
def select_word():
    response = requests.get(config.DICTIONARY_API)
    dictionary = response.text.split()
    word = random.choice(dictionary)
    return word

# update game data
# (used by views.index, views.session)
def process_player_input(request):
    # player input
    letter = request.POST['letter'].lower()

    # update data
    request.session['progress'] = update_progress(request.session['word'], request.session['progress'], letter)

    if letter not in request.session['incorrect_guesses']:
        if letter not in request.session['word']:
            request.session['incorrect_guesses'] += ' {} '.format(letter)
        if letter not in request.session['word']:
            request.session['free_guesses_remaining'] -= 1

    # check if player meets conditions for win or loss
    if request.session['word'] == request.session['progress']:
        request.session['result'] = 1
    elif request.session['free_guesses_remaining'] <= 0:
        request.session['result'] = -1

# construct string that shows player's progress;
# letters guessed are revealed, letters not guessed are masked by asterisks
# (used by process_player_input)
def update_progress(word, progress, letter):
    for i, e in enumerate(word):
        if e == letter:
            progress = '{}{}{}'.format(progress[:i], e, progress[i + 1:])
    return progress