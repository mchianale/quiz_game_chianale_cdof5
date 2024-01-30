# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:10:23 2024

@author: Matteo
"""
 
import json
import random

#quetsions informations
file = open('bank/all_questions.json', 'r')
questions = json.load(file)
TOTAL_QUESTIONS = len(questions)
id_questions = [i for i in range(0, TOTAL_QUESTIONS)]
selected_questions = random.sample(id_questions, 10)
print(selected_questions)

#user 
score = 0
 
 
for k,i in enumerate(selected_questions):
    print('Question {}, {}'.format(k+1, questions[i]['question']))
    for j,o in enumerate(questions[i]['options']):
        print('{} - {}'.format(j+1, o))
    a = input('Please select the rigth answer : ')
    if a == str(questions[i]['answer']):
        score += 1
        print('Good ! current score : {}/{}\n'.format(score, 10))
    else:
        print('False ! current score : {}/{}\n'.format(score, 10))

print('Final score : {}/{}'.format(score, 10))

file.close()