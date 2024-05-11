import random, sys
import pyinputplus as pyip

def random_word():
    words = ['tempt', 'essay', 'public', 'rage', 'pocket', 'occupy', 'judge',
         'quote', 'climb', 'rack', 'move', 'relax', 'string', 'narrow', 
         'spine', 'brain', 'sun', 'garage', 'jam', 'good', 'awful', 
         'weigh', 'Bible', 'press', 'step', 'lay', 'bride', 'care', 
         'layout', 'fix', 'grave', 'attack', 'shout', 'week', 'pray', 
         'egg', 'prey', 'herb', 'open', 'cancer', 'organ', 'forbid', 
         'wrong', 'hay', 'pity', 'mayor', 'result', 'link', 'grain', 'eject']
    return random.choice(words)

boards = {0: '''
    ---------
    |       |
    |      
    |     
    |     
    |     
    |      
    |     
    |
_________

''',
1: '''
    ---------
    |       |
    |       O
    |    
    |     
    |  
    |    
    |     
    |
_________

''',
2: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     
    |  
    |    
    |     
    |
_________

''',
3: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     / | \\
    |  
    |    
    |     
    |
_________

''',
4: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     / | \\
    |       |
    |     
    |    
    |
_________

''',
5: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     / | \\
    |       |
    |      / \\
    |    
    |
_________

''',
6: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     / | \\
    |       |
    |      / \\
    |     /   \\
    |
_________

''',
7: '''
    ---------
    |       |
    |       O
    |      /|\ 
    |     / | \\
    |       |
    |      / \\
    |    _/   \\_
    |
_________

'''
}

def is_single_char(string):
    if len(string) != 1:
        raise Exception('Please only guess one character at a time')
    if not string.isalpha():
        raise Exception('Please only guess letters')
    return string

def hangman_game(word):
    print('Welcome to Hangman')
    guesses = ''
    wrong = 0
    correct = 0
    while wrong < 7:
        user_guess = (pyip.inputCustom(is_single_char,'\n\nGuess a letter: ')).lower()
        if user_guess in guesses:
            print('Letter has already been guessed')
            continue
        guesses += user_guess
        if user_guess not in word:
            wrong += 1
        else:
            correct += 1
        print(boards[wrong])
        for i in word:
            if i in guesses:
                print(i,end=' ')
            else:
                print('_',end=' ')
        print(f'\n\nLetters guessed: {guesses}')
        if correct == len(word):
            print('\nYou Won!')
            break
        if wrong == 7:
            print('\n\nnice try, maybe next time')

hangman_game(random_word())





