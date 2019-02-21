#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os
import sys

quizQuestion = {"easy":
                ["3 + 5 = __1__ | 3*5= __2__ | 4/2 = __3__ | 5*4= __4__",
                 [8, 15, 2, 20]],
                "intermediate":
                ['''(2+4)*10= __1__ | (0+1)*100= __2__ |
                (3+6)*10=__3__ | (7*8)+5= __4__''',
                 [60, 100, 90, 61]],
                "hard":
                ['''9-3 / 1/3 + 1 =__1__ | (3 + 3 * 3 – 3 + 3) =__2__ |
                (7+7 / 7+7 * 7-7) =__3__ | 6^2 / 2(3) + 4 = __4__''',
                 [1, 12, 50, 58]]}

parts_of_speech1 = ["__1__", "__2__", "__3__", "__4__"]


class style:
    BOLD = '\033[1m'
    END = '\033[0m'


def text_format(a):
    # Adding lines to text
    return style.BOLD + "\n" + a + "\n" + style.END


def ClosingText(results):
    output = ""
    output += text_format("You have just completed the following string:\n")
    output += results
    output += text_format("\n\n Thank you for completing the quiz :)")
    return output


def word_in_pos(word, parts_of_speech):
    ''' Checking each word for a match for
    the part of speech to be replaced.'''

    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


def Check_input(u_input, replacement, correct_answer, word, l):
    ''' Checking the user input to make sure it is an integer,
    matches the correct answer.'''
    # user_input = int(u_input)
    if u_input.isdigit():
        x = int(u_input)
        if x != correct_answer:
            print(text_format("Incorrect answer.. Try again!"))
            return False
        else:
            print(text_format("Correct answer!"))
            word = word.replace(replacement, str(u_input))
            l.append(word)
            return True
    else:
        print(text_format("Please, enter a number!"))
        return False


def start_program(user_input, questions):
    ''' Matching the user chosen level and returnin its questions'''

    if user_input is not None:
        if user_input in questions.keys():
            Question_str = questions[user_input][0]
            Answers = questions[user_input][1]
            return Question_str, Answers
        else:
            print("Invalid Input")
            return False


def do_quiz(q_str, parts_of_speech, correct_answers):
    ''' Comparing the users answers to the correct ones.
        Replacing th parts of speech with the correct asnwers.
        Ending the quiz '''

    print(text_format(" List of correct answers" + str(correct_answers)))

    replaced = []
    q_str = q_str.split()

    for word in q_str:

        replacement = word_in_pos(word, parts_of_speech)
        while replacement is not None:
            index = parts_of_speech.index(replacement)
            # Returns index number of correct answer
            correct_answer = correct_answers[index]
            # Displaying the new string of quiz with the entered answers
            starting_point = len(replaced)
            new_str = replaced + q_str[starting_point:]
            print(" ".join(new_str))

            # User input
            usr_input2 = input("Your answer for " + replacement + " is...")
            if Check_input(usr_input2, replacement,
                           correct_answer, word, replaced):
                break
        else:
            replaced.append(word)

    replaced = " ".join(replaced)
    return ClosingText(replaced)


while True:
    # Returning user_input1 in lowercase letters
    user_input1 = (input('''Hello user, please select a quiz level:
                    easy - intermediate - hard''')).lower()
    if start_program(user_input1, quizQuestion):

        Question_str, Answers = start_program(user_input1, quizQuestion)
        print(do_quiz(Question_str, parts_of_speech1, Answers))
        break
