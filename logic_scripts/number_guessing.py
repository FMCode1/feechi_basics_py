stage1_completed = stage2_completed = False


def high_or_low(users_guess, right_answer):
    # if what they guessed is greater than the right answer print "too high"
    if users_guess > right_answer:
        print("Your guess was too high")
    # else, "too low"
    else:
        print("Your guess was too low")


def how_far_off(users_guess, right_answer):
    # if what they guessed is greater than the right answer print "too high"
    if users_guess != right_answer:
        print(f"Your guess was {abs(users_guess-right_answer)} points off")


def stage1():
    # there is a predefinded number
    right_answer = 34

    # prompt the user to enter a number
    users_guess = int(
        input("Welcome to Stage 1 of Guessing Game, please enter a number: ")
    )

    # while users guess is not the right answer, the user will be allowed to retry
    while users_guess is not right_answer:
        high_or_low(users_guess, right_answer)
        users_guess = int(input("Please try again: "))

    if users_guess == right_answer:
        print("You Got it! Moving to Stage 2")
        return stage1_completed is True


def stage2():
    # using a fixed number of tries and telling the user how far off they were
    right_answer = 45
    # prompt the user to enter a number
    users_guess = int(
        input(
            "Stage 2: You will now also be told how far off your guess was, please enter a number: "
        )
    )

    # while users guess is not the right answer, the user will be allowed to retry
    while users_guess is not right_answer:
        high_or_low(users_guess, right_answer)
        how_far_off(users_guess, right_answer)
        users_guess = int(input("Please try again now you know how far off you were: "))

    if users_guess == right_answer:
        print("You Got it! Moving to Stage 3")
        return stage2_completed is True


def stage3():
    right_answer = 67
    users_guess = int(
        input("This is the final stage of Guessing Game, please enter a number: ")
    )

    match users_guess:
        case greater_than if users_guess > right_answer:
            print(f"Your guess was too high. {how_far_off}")
        case less_than if users_guess > right_answer:
            print(f"Your guess was too low. {how_far_off}")
        case equal_to if users_guess == right_answer:
            print("You win!!!")


if stage1_completed == True and stage2_completed == True:
    stage3()
elif stage1_completed == True and stage2_completed == False:
    stage2()
    stage3()
elif stage1_completed == False:
    stage1()
    stage2()
    stage3()
else:
    print("You must complete stage 1 and stage 2 first before stage 3")
