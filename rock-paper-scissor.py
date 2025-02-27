import random
rock='🪨'
paper='📜'
scissor="✂️"
choose=['rock','paper','scissor']
graphic = {'rock':'🪨','paper':'📜','scissor':'✂️'}
on=True
user_score = total = comp_score = 0
games=[rock,paper,scissor]
print('\n\n============================================\n\nWelcome to Virtual Rock Paper scissor.',rock,paper,scissor)
while on:
    user=input(f'Rock{rock} ,Paper{paper} Scissors{scissor}.\n Please enter your choice:- ')
    if user not in choose:
        print("You chose an invalid input.Please enter a Valid Choice: ")
    else:
        total += 1
        comp=random.choice(choose)
        print(f"You Choose",graphic[user],end=" ")
        print(f"Computer choose ",graphic[comp])
        if user==comp:
            print('It is a Draw.')
            total -= 1
        elif user=='rock':
            if comp=='paper':
                print("Computer Wins.")
                comp_score += 1
            elif comp=='scissor':
                print("You Win.")
                user_score += 1
        elif user=='paper':
            if comp=='rock':
                print("You Win.")
                user_score += 1
            elif comp=='scissor':
                print("Computer Wins.")
                comp_score += 1
        elif user=='scissor' and comp=='rock':
            print("Computer Wins.")
            comp_score += 1
        elif user=='scissor' and comp=='paper':
            print("You Win.")
            user_score += 1
        choice=input("Do you wanna play again? y/n : ")
        if choice =='n':
            on=False
            print(f'Your Total Score: {user_score}/{total}.'
                  f'Computer\'s total score: {comp_score}/{total}.')
            continue
        print(f'Your current Score is {user_score}/{total}.')
        # print("computer's score",comp_score,'/',total)
