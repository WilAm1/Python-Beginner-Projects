"""Rock Paper Scissors Game"""

import random

hand_move = ['rock', 'paper', 'scissors']
move_dic = {move:count-1 for count, move in enumerate(hand_move)}

def compare_hands(name,user,comp):
    if user == comp:
        return f'Draw. Both have {user} hand' 
    elif (move_dic[user] == -1 and move_dic[comp] == 1) or (move_dic[user]==0 and move_dic[comp]==-1) or (move_dic[user]==1 and move_dic[comp]==0):
        return f"{name} wins. computer's move is  {comp}"

    return f"{name} lose. computer's move is {comp}"


score = 0
uName = input("What is your name?  ")

while True:

    user_choice = ''
    while user_choice not in hand_move:
        user_choice = input('Rock Paper or Scissors?  ').lower()

    bot_choice = random.choice(hand_move)

    result = compare_hands(name=uName,user=user_choice,comp=bot_choice)
    print('\n',result)
    if 'wins' in result:
        score +=1

    print(f'Your score: {score}')
    if input('Do you want to continue? type "n" to stop else press any key. ') == 'n':
        break
