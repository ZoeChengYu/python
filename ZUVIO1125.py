def generate_all_possible_permutations(ans_list, s: str, p_len: int):
    if len(s) == p_len:
        ans_list.append(s)
        return
    else:
        for i in range(10):
            if str(i) not in s:
                generate_all_possible_permutations(ans_list, s + str(i), p_len)


def match(answer: str, guess: str) -> str:
    a, b = 0, 0
    for i in range(5):
        if guess[i] == answer[i]:
            a += 1
        elif guess[i] in answer:
            b += 1
    AB_str = str(a) + "A" + str(b) + "B"
    return AB_str


def filter_answers(ans_list: list, last_guess: str, AB_str: str):
    possible_answers = []

    # find all permutation that match 3A0B:
    for i in range(len(ans_list)):
        if match(ans_list[i], last_guess) == AB_str:
            possible_answers.append(ans_list[i])
    return possible_answers


def guess(ans_list, count_list):
    new_guess = ans_list[0]
    print("\033[30;43mguess: ", new_guess,'\033[0m')
    count_list[0] += 1
    print("\033[37;44mcount: ", count_list[0],'\033[0m')
    AB_str = input()

    if AB_str == "5A0B":
        print('\033[30;42mans:'+new_guess+'\033[0m')
        return 

    filtered_answers = filter_answers(ans_list, new_guess, AB_str)
    # print("filtered_answers: ", filtered_answers)

    if count_list[0] == 99:
        return
    elif len(filtered_answers) == 0:
        return print("\033[30;41mno answer available\033[0m")

    return guess(filtered_answers, count_list)


def main():
    ans_list = []
    generate_all_possible_permutations(ans_list, "", 5)
    #print(ans_list)
    guess(ans_list, [0])


main()