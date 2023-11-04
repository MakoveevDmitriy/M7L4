from speach import speach
import speech_recognition as speech_recog
from random import choice
import time


levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}



def play_game(level):
    words = levels[level]
    score = 0
    
    for i in range(len(words)):
        random_word = choice(words)
        print(f'произнесите слово {random_word} ')
        recog_word = speach()
        print(recog_word)
        
        if random_word == recog_word:
            print('Молодец!!! Ты назвал слово верно')
            score += 1
        else:
            print('У тебя не получилось попробуй снова.')
            print(f'произнесите слово {random_word} ')
            recog_word = speach()
            if random_word == recog_word:
                print('Молодец!!! Ты назвал слово верно')
                score += 1
            else:
                print('Ты не смог произнести это слово, делай дальше.')
    print('Твой счёт', score)
selected_level = input('выберете уровень сложности: easy, medium, hard ').lower()

play_game(selected_level)

