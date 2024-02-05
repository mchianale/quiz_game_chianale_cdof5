## Quiz Game
Welcome to this simple yet engaging Python quiz game. Challenge your knowledge across a vast array of topics with a dynamic question bank.
### Key Features
- **Dynamic Question Bank:** With **1558** diverse questions, test your knowledge across various categories.
- **Customizable Sessions:** Each session presents 10 questions, allowing for a quick yet engaging quiz experience.
- **Multiple Choice Questions:** For every question, choose your answer from multiple options, ensuring a challenging and fun gameplay.

## Getting Started

This repository hosts `main.py`, the main script for running the Quiz Game, which offers an intuitive command-line interface for users.

### Prerequisites

Ensure Python 3.x is installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

### Running the Quiz Game

1. **Clone the Repository:** Use Git to clone the repository to your local machine.
   ```shell
   git clone https://github.com/mchianale/quiz_game_chianale_cdof5.git
   ```
2. **Navigate to the Repository:** Change your working directory to the cloned repository.
   ```shell
   cd [your-repo-name]
   ```
3. **Launch the Game:** Execute `main.py` with Python.
   ```shell
   python main.py
   ```

### Troubleshooting

Encountering issues? Ensure Python is properly installed and that you're in the correct directory. For further assistance, open an issue in this repository.

## Expanding the Question Bank

To add new questions, modify and execute `create_bank_questions.py` found in the bank folder. This updates the total count of questions in `all_questions.json` and the README documentation.

### Question Format

Add questions using the following JSON structure:

```json
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

### Question Sources

- `question0.json`: Manually curated.
- `question1.json`: [View Source](https://gist.github.com/cmota/f7919cd962a061126effb2d7118bec72).
- `question2.json`: [View Source](https://github.com/Eromnoj/quizAPI/blob/main/quiz.json). Translated from French using Google Translator.
- `questions3.txt`: [View Source](https://raw.githubusercontent.com/curiousily/simple-quiz/master/script/statements-data.json).
- `questions4.json`: Generated using GPT.

## Future Enhancements

We're exploring ways to enrich your quiz experience:
- **Customizable Quiz Sessions:** A proposed feature to let players select their preferred categories and the number of questions per session. Track our progress and share your thoughts on this [issue](https://github.com/mchianale/quiz_game_chianale_cdof5/issues/5).

## Contribution

Your contributions are welcome! Whether it's adding new questions, enhancing the game's features, or reporting issues, every effort helps improve the quiz game for everyone.
