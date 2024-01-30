## Quiz Game
Hi, this is a simple Python quiz game.
- You have to answer to 10 questions per session.
- For each question, you have to chose just one answer from multiple options.
- There are actually **1550** questions.

## Running the Quiz Game Script

This repository contains a simple Python quiz game, `main.py`, which can be run easily on any system with Python installed.

### Prerequisites

Before you run the script, ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/). This script is compatible with Python 3.x.

### Steps to Run the Script

1. **Clone the Repository**: First, clone this repository to your local machine using Git. If you have Git installed, you can run the following command:

   ```
   git clone https://github.com/mchianale/quiz_game_chianale_cdof5.git
   ```

2. **Navigate to the Repository Directory**: Change your directory to the folder containing the cloned repository.

   ```
   cd [your-repo-name]
   ```

3. **Run the Script**: Run `main.py` using Python. In your terminal or command prompt, execute the following command:

   ```
   python main.py
   ```

   This will start the quiz game in your command line interface.

### Troubleshooting

- If you encounter any issues while running the script, ensure that Python is correctly installed on your system and that you're running the script in the right directory. For more support, feel free to raise an issue in this repository.

## Add questions to the actual bank

If you want to add new questions, you have to update and run `create_bank_questions.py` located the bank folder.

When you run the script it will also update README by change the total of existing questions in `all_questions.json`.


### Format of question

```
{
        "question": "What is the largest planet in our solar system?",
        "options": [
            "Jupiter",
            "Saturn",
            "Neptune"
        ],
        "answer": 1,
        "category": "astronomy"
    }
```



## All data

- `question0.json`: Manually created.

- `question1.json`: Available [here](https://gist.github.com/cmota/f7919cd962a061126effb2d7118bec72).

- `question2.json`: Available [here](https://github.com/Eromnoj/quizAPI/blob/main/quiz.json). The original data was in French and has been translated to English using Google Translator.

- `questions3.txt`: Available [here](https://raw.githubusercontent.com/curiousily/simple-quiz/master/script/statements-data.json)

