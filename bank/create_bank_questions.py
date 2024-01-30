# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:27:27 2024

@author: Matteo
"""

import json
 

#get first questions 
file = open('questions0.json', 'r')
questions = json.load(file)
file.close()


#get second bank of questions
file = open('questions1.json', 'r')
questions1 = json.load(file)
equivalent_answer = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4}
 
for question in questions1:
    q = {}
    new_question = {
        'question' : question['question'],
        'options' : [question['A'],question['B'],question['C'],question['D']],
        'answer' : equivalent_answer[question['answer']],
        'category': ''
    }
    questions.append(new_question)
file.close()


#save all
print(questions)
file = open('all_questions.json', 'w')
json.dump(questions, file, indent=4)
file.close()

#update Read me
file = open('../README.md', 'r')
lines = file.readlines()
arr = lines[4].split('**')
arr[1] = len(questions)
lines[4] = arr[0] + '**' + str(arr[1]) + '**' + arr[2]
file.close()

file = open('../README.md', 'w')
file.writelines(lines)
file.close()
