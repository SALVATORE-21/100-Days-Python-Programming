![# Day-017: Quiz Game

## Overview
A Python-based quiz game application that demonstrates object-oriented programming concepts. The program loads questions from a data source, presents them to the user, tracks scores, and provides feedback on answers.

## Project Structure

### Files
- **main.py** - Entry point that initializes the quiz and manages the game loop
- **question_model.py** - Defines the `Question` class to represent individual quiz questions
- **quiz_brain.py** - Defines the `QuizBrain` class to manage quiz logic and scoring
- **data.py** - Contains the question bank (list of question/answer pairs)
- **practice.py** - Additional practice/test file

## How It Works

### QuizBrain Class
Manages the overall quiz flow:
- Tracks the current question number
- Maintains the score
- Presents questions to the user
- Checks answers (case-insensitive)
- Determines if more questions remain

### Question Class
Represents a single quiz question with:
- Question text
- Correct answer

### Game Flow
1. Load questions from the data source
2. Create Question objects for each question
3. Initialize QuizBrain with the question list
4. Loop through questions until none remain
5. Get user input and check correctness
6. Display feedback and final score

## Running the Game

```bash
python main.py
```

The quiz will prompt you with each question in sequence. Answer each question when prompted, and receive immediate feedback. Your final score will be displayed at the end.

## Learning Concepts
- Object-oriented programming (classes and objects)
- List operations and iteration
- String methods (`.lower()` for case-insensitive comparison)
- While loops and conditional logic
- User input handling](image.png)