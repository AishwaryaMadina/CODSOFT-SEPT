import time  # Import the time module for pausing the game and adding delays

# Define quiz questions as a list of dictionaries
questions = [
    {
        "question": "Which is the smallest bone in the human body?",
        "choices": ["a) Malleus", "b) Incus", "c) Stapes", "d) Femur"],
        "answer": "c",
    },
    {
        "question": "Which continent is known as the 'Dark' continent?",
        "choices": ["a) Antartica", "b) Australia", "c) Asia", "d) Africa"],
        "answer": "d",
    },
    {
        "question": "Who wrote 'Malgudi Days'?",
        "choices": ["a) RK Laxman", "b)  RK Narayan", "c) RK Kapoor", "d) Balaji Subramanium"],
        "answer": "b",
    },
    {
        "question": "Who discovered the X-rays first?",
        "choices": ["a) Becquerel", "b) Van lane", "c) Roentgen", "d) Curie"],
        "answer": "c",
    },
    {
        "question": "Name a natural satellite of Earth?",
        "choices": ["a) Moon", "b) Dione", "c) Titan", "d) Mimas"],
        "answer": "a",
    },
]

def present_question(question_data):
    # Display the question and answer choices
    print(question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    
    user_answer = input("Select your answer (a, b, c, or d): ")  # Prompt the user for an answer
    return user_answer

def evaluate_answer(question_data, user_answer):
    if user_answer == question_data["answer"]:
        print("Correct! Good Job.\n")  # Provide feedback for a correct answer
        return True
    else:
        print("Incorrect! The correct answer is", question_data["answer"], "\n\n")  # Provide feedback for an incorrect answer
        return False

def play_quiz(quiz_questions):
    score = 0  # Initialize the user's score
    total_questions = len(quiz_questions)  # Get the total number of questions

    print("Welcome to the Simple Quiz Game!")
    time.sleep(1)  # Pause for 1 second to display the welcome message
    print(f"You will have {total_questions} chances to answer correctly.")
    print("Please put the alphabet of the answer (e.g., 'a').\n")
    time.sleep(2)  # Pause for 2 seconds before starting the quiz

    for question_data in quiz_questions:
        user_answer = present_question(question_data)  # Present a question and get the user's answer
        if evaluate_answer(question_data, user_answer.lower()):  # Evaluate the user's answer
            score += 1  # Increment the score for a correct answer
        time.sleep(2)  # Pause for 2 seconds before the next question

    print(f"Your Score: {score}/{total_questions}")  # Display the user's final score
    if score >= 4:
        print("Well done!")  # Provide a congratulatory message for a high score
    else:
        print("Better luck next time!")  # Provide an encouraging message for a low score
    print("Thank you for playing the Simple Quiz Game!")

if __name__ == "__main__":
    play_quiz(questions)  # Start the quiz game when the script is executed
