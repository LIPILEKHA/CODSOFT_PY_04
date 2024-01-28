import random
from django.shortcuts import render
from django.http import HttpResponse

def play_game(request):
    choices = ['rock', 'paper', 'scissors']
    user_choice = request.POST.get('user_choice')
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    return render(request, 'rps_app/game.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
    })

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'You win!'
    else:
        return 'Computer wins!'

