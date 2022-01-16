
from questions import questions_list0, questions_list1, questions_list2, questions_list3, questions_list4
from questions import questions_list5, questions_list6, questions_list7, questions_list8, questions_list9
from cl_Test import Test
from random import randint


def main():
    tests_list = [
        Test(questions_list0),
        Test(questions_list1),
        Test(questions_list2),
        Test(questions_list3),
        Test(questions_list4),
        Test(questions_list5),
        Test(questions_list6),
        Test(questions_list7),
        Test(questions_list8),
        Test(questions_list9)
    ]
    score = 0
    for question in tests_list[randint(0, 9)].question_list:
        otvet = input(question.ques)
        if otvet == question.answer:
            score += 1
    print("Правильных ответов " + str(score) + " из " + str(len(questions_list0)))








