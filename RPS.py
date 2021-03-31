import random
while True :

    print("\n Welcome to RPS game \n")
    print("\n 1.Rock \n 2.Paper \n 3.Scissor \n")

    user_choice = int(input("\n Please Enter Your Choice \n"))

    if user_choice > 3 or user_choice < 1 :
        print("\n Please Enter A Valid Choice \n")
        user_choice = int(input())
    else:
        if user_choice == 1 :
            x = "Rock"
        elif user_choice == 2:
            x = "Paper"
        else:
            x = "Scissor"
    print("\n Your Choice Is \n", x)

    possible_selections = ["Rock", "Paper", "Scissor"]
    comp_choice = random.choice(possible_selections)

    print("\n Computer Choice is ", comp_choice)

    if x == comp_choice:
        print("\n Match Tied \n")
    elif x == "Rock" :
        if comp_choice == "Scissor":
            print("\n Rock Smashed Scissor ... You Win The Game!!..\n ")
        else:
            print("\n Rock Covered by Paper... Computer Win The Game!!..\n")
    elif x == "Paper":
        if comp_choice == "Rock":
            print("\n Paper Covered The Rock... You Win The Game!!..\n")
        else:
            print("\n Scissor cutted The Paper... Computer Win The Game!!..\n")
    else :
        if comp_choice == "Paper":
            print("\n Scissor Cutted The Paper... You Win The Game!!.. \n")
        else:
            print("\n Rock Smashed Scissor... Computer Win The Game!!.. \n")
    play_again = input("Play again ? (y/n) : \n")
    if play_again.lower() != "y":
        break

