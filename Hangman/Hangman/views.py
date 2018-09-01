from django.http import HttpResponseRedirect
from django.shortcuts import render

# -------------------------------------------------------- #
# custom modules
# -------------------------------------------------------- #
from . import config
from . import service
from .forms import InputForm

# -------------------------------------------------------- #
# views
# -------------------------------------------------------- #

# initialize game
def index(request):
    # initialize form
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # update data in response to player input
            service.process_player_input(request)
            # redirect player to appropriate page
            if request.session['result']:
                return HttpResponseRedirect('game_over')
            return HttpResponseRedirect('session')

    # initialize data
    word = service.select_word()
    progress = len(word) * '*'
    result = 0
    incorrect_guesses = ''
    free_guesses_remaining = config.FREE_GUESSES

    # record initialized data
    request.session['word'] = word
    request.session['progress'] = progress
    request.session['result'] = result
    request.session['incorrect_guesses'] = incorrect_guesses
    request.session['free_guesses_remaining'] = free_guesses_remaining

    return render(request, 'Hangman/index.html',
                  {
                      'word': '',
                      'progress': progress,
                      'form': InputForm(),
                      'incorrect_guesses': incorrect_guesses,
                      'free_guesses_remaining': free_guesses_remaining
                  })

# in-session game behavior
def session(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            service.process_player_input(request)
            if request.session['result']:
                return HttpResponseRedirect('/game_over')

    return render(request, 'Hangman/session.html',
                  {
                      'word': '',
                      'progress': request.session['progress'],
                      'form': InputForm(),
                      'incorrect_guesses': request.session['incorrect_guesses'],
                      'free_guesses_remaining': request.session['free_guesses_remaining']
                  })

# display appropriate game over message
def game_over(request):
    result = request.session['result']
    if result == 1:
        message = config.WINNING_MESSAGE
    else:
        message = config.LOSING_MESSAGE

    return render(request, 'Hangman/game_over.html',
                  {
                      'word': request.session['word'],
                      'progress': request.session['progress'],
                      'result': result,
                      'message': message,
                      'incorrect_guesses': request.session['incorrect_guesses'],
                      'free_guesses_remaining': request.session['free_guesses_remaining']
                  })
