#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

# ^^^ I had to add the first 3 lines because
# I got the following error when I added the hard questions to the list:
#Non-ASCII character '\xe2' in file firstStep.py on line 8, but no encoding declared;
# see http://python.org/dev/peps/pep-0263/ for details


# Quiz lists:

quiz_level =[ "easy", "intermediate", "hard"]

quiz_q = [" 3 + 5 = __1__ | 3*5= __2__ | 4/2 = __3__ | 5*4= __4__",
"(2+4)*10= __1__ | (0+1)*100= __2__ | (3+6)*10=__3__ | (7*8)+5= __4__ " ,
 "9-3 / 1/3 + 1 =__1__ | (3 + 3 * 3 – 3 + 3) =__2__ | (7+7 / 7+7 * 7-7) =__3__ | 6^2 / 2(3) + 4 = __4__ "]



quiz_answers=[[8,15,2,20],[60, 100,90, 61],[1,12,50,58]]

parts_of_speech1=["__1__","__2__", "__3__", "__4__" ]



class style:
    #code Source: https://stackoverflow.com/questions/24834876/how-can-i-make-text-bold-in-python
   BOLD = '\033[1m'
   END = '\033[0m'

def text_format(a):
    #Adding lines to text
    return style.BOLD + "\n" + a + "\n" + style.END


#I used the same functions explained in lesson 13 ( Mad Libs Continued )
def word_in_pos(word, parts_of_speech):
    #Checking each word in list of strings to see if it matches
    # the part of speech we want to replace
    #The inputs are words in string list and parts of speech list
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None


def Check_input(u_input, replacement, correct_answer, word, l):
    # This function will check the user input to make sure it is an integer
    #also it will check if it matches the correct answer
    #Inputs: user input - replacement (matching part of speech ) and word to be replaced - Replaced string list to be updated

    try:
        user_input = int(u_input)
    except:
        #In case of value error
        print text_format("Please, enter a number!")
        return False
    else:
        if user_input != correct_answer:
            print text_format("Incorrect answer.. Try again!")
            return False
        else:
            print text_format("Correct answer!")
            word = word.replace(replacement, str(user_input))
            l.append(word)
            return True
#learned about try , except from:
# http://geek-university.com/python/the-try-except-else-statements/
# checking if the input is a number


def start_program(user_input, level, questions, answers):
# This function will start the program, it takes the following inputs:
# user choice - quiz level - questions and answers to match them with the chosen quiz level.
#It validate the input ( if it exist in the list of levels) and return the needed values to
#start the quiz.


    if user_input != None:

        if user_input in level:

            #Matching the user input with the correct quiz level string
            u_input = level.index(user_input1)
            Question_str = questions[u_input]
            Answers = answers[u_input]

            return  Question_str ,  Answers


        else:
            #In case user input is incorrect
            print ("Invalid Input")
            return False





def do_quiz(q_str, parts_of_speech, correct_answers):
    #Function to perform the conditions of the quiz
    #Its inputs are: the selected question str- list of parts of speech we want to replace
    # and the correct answers for comparison
    #It checks every word in the question string list, if it matches a "part of speech" it will evaluate the
    #entered answer and replace it when it is correct.
    #Its output: the new str with the correct answers.
    #I started with the same concepts explained in lesson 13 and built upon it


    print text_format(" List of correct answers" + str(correct_answers))

    replaced= []
    q_str = q_str.split()


    for word in q_str:

        replacement = word_in_pos(word, parts_of_speech)
        while replacement != None:
            index= parts_of_speech.index(replacement)
             #returns index number for comparing user input with the
             #correct answer
            correct_answer = correct_answers[index]
            # For displaying the new string of quiz with the entered answers
            starting_point= len(replaced)
            new_str = replaced + q_str[starting_point: ]
            print " ".join(new_str)


            #User input
            user_input2 = raw_input("Your answer for "+ replacement + " is... " )
            if Check_input(user_input2, replacement, correct_answer, word, replaced) == True:
                break

        else:
            replaced.append(word)

    replaced = " ".join(replaced)
    return text_format("You have just completed the following string:")+ "\n" + replaced + "\n\n"+text_format("Thank you for completing the quiz :)")






while True:
    #returning user_input1 in lowercase letters
    user_input1= (raw_input("Hello user, please select a quiz level : easy - intermediate - hard" )).lower()
    if start_program(user_input1, quiz_level, quiz_q, quiz_answers):

        Question_str , Answers = start_program(user_input1, quiz_level, quiz_q, quiz_answers)
        print  do_quiz(Question_str, parts_of_speech1, Answers)
        break

#Concept for this loop learned from
# www.youtube.com/watch?v=yEST0vy2UBE
#Returning multiple values using a function
#https://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-in-python
