import random


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
    for i in range(4):
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
    if len(ans_list) == 0:
        return print("ans_list should have at least one element.")
    ans_index = int(random.uniform(0, len(ans_list) - 1))
    # print("ans_index: ", ans_index)
    new_guess = ans_list[ans_index]
    print("guess: ", new_guess)
    count_list[0] += 1
    print("count: ", count_list[0])
    AB_str = input()

    if AB_str == "4A0B":
        return

    filtered_answers = filter_answers(ans_list, new_guess, AB_str)
    # print("filtered_answers: ", filtered_answers)

    if count_list[0] == 6:
        return
    elif len(filtered_answers) == 0:
        return print("no answer available")

    return guess(filtered_answers, count_list)


def main():
    ans_list = []
    generate_all_possible_permutations(ans_list, "", 4)
    # print(ans_list)
    guess(ans_list, [0])


main()