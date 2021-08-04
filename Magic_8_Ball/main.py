"""Simulate a magic 8-ball in the terminal"""

import time
import random

# response= [
#     'I have absolutely no idea',
#     'Good Fortune awaits you',
#     'You are very fortunate this week',
#     'Disaster awaits you',
#     'Be careful what you wish for',
#     'Your true goal is in front of you',
#     'Yes','Maybe','No','Absolutely','Very Good'
# ]
with open('data/responses.txt') as file:
    responses = file.readlines()
    response = [i.replace('\n','').strip("' ") for i in responses]
    

def userAsk():
    questionPrompt = 'What is in your mind? '
    question = input(questionPrompt)
    return question

def thinking():
    print('I am thinking...')
    time.sleep(3)
    

def pickAnswer():
    return random.choice(response)


if __name__ == '__main__':
    while True:
        user_q = userAsk()

        thinking()
        print(pickAnswer())
        if input('Do you want quit? "q" to quit:    ') == 'q'.lower():
            break
        else:
            print('great')
            time.sleep(1)

