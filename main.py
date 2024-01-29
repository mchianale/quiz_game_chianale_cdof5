# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:10:23 2024

@author: Matteo
"""

score = 0
questions  = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Neptune"],
        "answer": 1
    },
    {
        "question": "What galaxy is Earth located in?",
        "options": ["Andromeda Galaxy", "Whirlpool Galaxy", "Milky Way Galaxy"],
        "answer": 3
    },
    {
        "question": "What is the name of the red planet?",
        "options": ["Mars", "Venus", "Mercury"],
        "answer": 1
    },
    {
        "question": "How many moons does Earth have?",
        "options": ["1", "2", "3"],
        "answer": 1
    },
    {
        "question": "What is the hottest planet in our solar system?",
        "options": ["Mercury", "Venus", "Mars"],
        "answer": 2
    },
    {
        "question": "What planet is known as the 'Ringed Planet'?",
        "options": ["Jupiter", "Saturn", "Uranus"],
        "answer": 2
    },
    {
        "question": "Which planet is known for its Great Red Spot?",
        "options": ["Jupiter", "Mars", "Neptune"],
        "answer": 1
    },
    {
        "question": "Which is the closest star to Earth?",
        "options": ["Proxima Centauri", "Sirius", "The Sun"],
        "answer": 3
    },
    {
        "question": "What is the term for a year on Mars?",
        "options": ["Solar Year", "Martian Year", "Red Year"],
        "answer": 2
    },
    {
        "question": "Which of these is not a dwarf planet?",
        "options": ["Pluto", "Eris", "Neptune"],
        "answer": 3
    }
]

for i,q in enumerate(questions):
    print('Question {}, {}'.format(i+1, questions[i]['question']))
    for j,o in enumerate(questions[i]['options']):
        print('{} - {}'.format(j+1, o))
    a = input('Please select the rigth answer : ')
    if a == str(questions[i]['answer']):
        score += 1
        print('Good ! current score : {}/{}\n'.format(score, len(questions)))
    else:
        print('False ! current score : {}/{}\n'.format(score, len(questions)))

print('Final score : {}/{}'.format(score, len(questions)))
    