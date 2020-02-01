import random

game_is_playing = True
secret_number = random.randint(1, 10)
attempts = 0
best_score = None


def read_best_score():
    with open("score.txt", "r") as score_file:
        best_score = int(score_file.read())
        return best_score


def write_best_score():
    with open("score.txt", "w") as score_file:
        score_file.write(str(attempts))

read_best_score()
print("Top score: {}".format(best_score))


while game_is_playing:
    guessed_number = int(input("Please insert number from 1 to 10: "))
    attempts+=1

    if secret_number == guessed_number:
        print("You guessed the number, it was {}, you have {} attempts!".format(secret_number, attempts))
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guessed_number == None or guessed_number == 0:
        print("Please, insert valid number!")
        break
    elif attempts <= 0:
        print("No attempts left, start again!")
        break
    else:
        attempts-=1
        print("Incorrect number, the real number was {} you have {} attempts left!".format(secret_number, attempts))




print(attempts)
# for loop

#for x in range(5) #5x loop


