# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:27:27 2024

@author: Matteo
"""

import json
 

#get first questions 0
file = open('questions0.json', 'r')
questions = json.load(file)
file.close()


#get second bank of questions 1
file = open('questions1.json', 'r')
questions1 = json.load(file)
equivalent_answer = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4}
 
for question in questions1:
    new_question = {
        'question' : question['question'],
        'options' : [question['A'],question['B'],question['C'],question['D']],
        'answer' : equivalent_answer[question['answer']],
        'category': ''
    }
    questions.append(new_question)
file.close()

#get questions 2
file = open('questions2.json', 'r')
questions +=  json.load(file)
file.close()


#get questions 3
file = open('questions3.txt', 'r')
#format 
lines = file.readlines()
parts = lines[0].split('[')
joined = ''.join(parts)  # Joining parts without any separator
final_parts = joined.split(']')
final_string = ''.join(final_parts)
final_parts = final_string.split('",')
final_string = ''.join(final_parts)
list_questions3 = final_string.split(', "')

def getQuestion(str1):
    res = ""
    for c in str1:
        if c != '"':
            res += c
    return res + '.'

def getAnswer(str2):
    if 'true' in str2.lower():
        return 1 
    else:
        return 2 
 
def getInfo(str1):
    parts = str1.split('.')
    question = getQuestion(''.join(parts[:len(parts)-1]))
    answer = getAnswer(parts[len(parts)-1])
    return {
        'question' : question,
        'options' : ['True', 'False'],
        'answer' : answer,
        'category': 'general culture'
    }
    
 
for i in range(len(list_questions3)):
    questions.append(getInfo(list_questions3[i]))
    
file.close()

#get questions 4
file = open('questions4.json', 'r')
questions +=  json.load(file)
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
