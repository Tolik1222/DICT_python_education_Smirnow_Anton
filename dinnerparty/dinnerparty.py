"""Practice_7_Dinnerparty: Writing a program for sharing common expenses"""

import random


def stage_3():
    try:
        num_of_friends = int(input("Enter the number of friends joining (including you):\n> "))
        if num_of_friends <= 0:
            print("No one is joining for the party")
            return

        friends = {}
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(num_of_friends):
            name = input("\n> ")
            friends[name] = 0

        if len(friends) <= 1:
            print("No one is joining for the party")
            return

        total_amount = float(input("Enter the total amount:\n> "))

        for friend in friends:
            friends[friend] = round(total_amount / len(friends), 2)

        choose_lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n> ")

        if choose_lucky.lower() == 'yes':
            lucky_friend = random.choice(list(friends.keys()))
            print(f"{lucky_friend} is the lucky one!")
            friends[lucky_friend] = 0
            amount_per_friend = round(total_amount / (num_of_friends - 1), 2)
            for friend_name in friends:
                if friends[friend_name] != 0:
                    friends[friend_name] = amount_per_friend
        else:
            print("No one is going to be lucky")
        print(friends)
    except ValueError:
        print("Please enter a number.")


stage_3()
