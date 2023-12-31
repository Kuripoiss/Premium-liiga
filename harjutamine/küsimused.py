def new_game():

    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in küsimused:
        print("-------------------------------------")
        print(key)
        for i in valikud[question_number-1]:
            print(i)
        guess = input("Mis on teie valik (A, B, C, D)? ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(küsimused.get(key),(guess))
        question_number += 1
    display_score(correct_guesses, guesses)
def check_answer(answer, guess):

    if answer == guess:
        print("Õige!")
        return 1
    else:
        print("Vale!")
        return 0


def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("Tulemused")
    print("---------------------------")
    print("Vastused: ", end="")
    for i in küsimused:
        print(küsimused.get(i), end=" ")
    print()

    print("Sinu valikud: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(küsimused))*100)
    print("Sinu skoor on: "+str(score)+"%")


def play_again():

    response = input("Kas sa tahad uuesti mängida? (jah või ei): ").upper()

    if response == "JAH":
        return True
    else:
        return False



küsimused = {
    "Kes võitis Eesti Premium liiga? ": "A",
    "Mis on Marten Alvini lemmik klubi? ": "B",
    "Kes on FC FLora kapten? ": "C",
    "Kes saavutas Eesti Premium liigas teise koha? ": "A"
}
valikud = [["A: FC Flora", "B: Tallinna FCI Levadia", "C: JK Tallinna Kalev", "D: Paide Linnameeskond"],
           ["A: Bayer 04 Leverkusen", "B: FC Bayern München", "C: Borussia Dortmund", "D: RB Leipzig"],
           ["A: Martin Miller", "B: Sergei Zenjov", "C: Henrik Ojamaa", "D: Ken Kallaste"],
           ["A: FCI Levadia", "B: FC Flora", "C: JK Tallinna Kalev", "D: Paide Linnameeskond"]]

new_game()

while play_again():
    new_game()

print('Head aega!')