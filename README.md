# Hangman

This project uses Django to implement a simple web interface that invites visitors to play the word guessing game of [hangman] (https://en.wikipedia.org/wiki/Hangman_(game)). The interface aspires to a minimalist design so that the player can focus on gameplay.

## Requirements
The game was  implemented using Python 3.7, Django 2.1, Pipenv, pip, and pip3 on macOS High Sierra 10.13.6. The player can run the game by using an IDE that supports Django (e.g. PyCharm, Heroku) or from command line. If the IDE does not work, use command line.

### PyCharm Professional 2018.2
1. Start PyCharm and close any existing projects. Click Open on the Welcome Screen. Open the project folder Hangman.
2. Set up a virtual environment. Since the project was constructed using Pipenv, it is likely the safest option. If Pipenv is not already available, install by entering "pip install pipenv" in the terminal.
3. Go to PyCharm | Preferences | Project:Hangman | Project Interpreter. Click on the cog near the top right and choose Add... In the Add Python Interpreter window, choose Pipenv Environment. Make sure the "Install packages from Pipfile" box is checked and click OK. Click OK in the Preferences window.  
4. In the dropdown menu near the top right in the Navigation Bar (check View | Navigation Bar), select Hangman. Click the triangular Run button to the immediate right.
5. If the run console indicates that the port 8000 is already in use, free the port by entering "lsof -i :8000" in the terminal, copy the process ID (PID) associated with port 8000, and enter "kill -9 PID". Repeat Step 4.

### Command line
1. Install Python 3.7 (https://www.python.org/downloads/).
2. Install Django 2.1 (https://www.djangoproject.com/download/).
3. Install Pipenv (enter "pip install pipenv").
4. Navigate to the Hangman directory. Create a virtual environment by entering "pipenv install --dev".
5. Enter "pipenv shell" to activate the virtual environment.
6. Enter "python manage.py runserver" ("python3 manage.py runserver" on some machines).
7. If the terminal indicates that the port 8000 is already in use, free the port by entering Control-C. Repeat Step 6.

Visit Django's development server at http://127.0.0.1:8000 in a web browser to play hangman.

## Design
The web interface has four variable components. The graphical components are fixed to their absolute positions so changes in text do not alter the interface's look among different pages. The goal is to provide a seamless gameplay experience.
1. The web interface selects a word at random from a dictionary API. The word is hidden until the player wins or loses. Underneath the word is a string of asterisks having the same number of characters as the the word does.
2. The player enters a guess into an input form, which records uppercase or lowercase letters and ignores all other symbols as well as letters already entered. Ignoring the invalid inputs spares the player from the distraction of error messages and steers the player to adopt valid input in an intuitive way. The cursor stays in the input form so that the player can enter successive guesses efficiently. 
3. A correct guess reveals the letter(s) in the masked word. The interface displays the incorrect guesses and the number of free guesses remaining. The incorrect guesses and the number of free guesses under three are shown in red to alert the player to guess more carefully. 
4. A reset button below allows the player to restart the game with a new word. 

## Code
The Django project structure follows the namespacing convention in which templates and static files (stylesheet and image) are stored in project/templates_or_static/project. To allow for easy modification of the game's parameters, the following variables are declared in config.py: the number of free guesses (default six), dictionary API (default http://app.linkedin-reach.io/words), winning message, and losing message. The module service.py contains all the helper functions and forms.py handles the input form so that views.py does not need to contain functions that do not correspond to an HTML file. The entire interface is encapsulated by three HTML files: index, session, and game_over. They each handle game initialization, in-game behavior, and game termination, respectively. By design, index.html and session.html look nearly identical so that the player can jump right into the game without extra steps to instantiate a session.  

## Ideas for extensions
Here are some ideas for extending the program in order of increasing complexity.
1. Sound prompts to indicate correct or incorrect guesses
2. Draw part of the traditional hangman stick figure after each incorrect guess
3. Implement database to keep track of each player's record
4. Award credits to the player for each correct guess to buy letters in future games
5. Set a timer after the player enters first guess so that player could be rewarded for identifying a word quickly
6. Introduce difficulty levels (e.g. for easier levels trim words to stem form, for harder levels include conjugated words)
7. Modify number of free guesses with respect to difficulty level to accommodate faster style of gameplay

---
Judy Wang  
jwang@alumnae.smith.edu  
https://www.linkedin.com/in/jujuwoman  
https://github.com/jujuwoman  

Last revised: August 31, 2018
