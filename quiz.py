import pyfiglet
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def display_result(score, total_questions):
    result_text = f"Your Score: {score}/{total_questions}"
    ascii_art = pyfiglet.figlet_format(result_text, font="standard")
    print(Fore.YELLOW + ascii_art)  

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ("A) Paris", "B) London", "C) Rome", "D) Berlin"),
        "answer": "A"
    },
    {
        "question": "Which programming language is known as the language of Artificial Intelligence?",
        "options": ("A) C", "B) Python", "C) Java", "D) Ruby"),
        "answer": "B"
    },
    {
        "question": "Who is known as the father of computers?",
        "options": ("A) Charles Babbage", "B) Alan Turing", "C) Bill Gates", "D) Steve Jobs"),
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ("A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"),
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ("A) 5", "B) 6", "C) 7", "D) 8"),
        "answer": "C"
    }
]

print(Fore.BLUE + pyfiglet.figlet_format("Welcome to the Quiz Game!", font="slant"))
print(Fore.CYAN + "=" * 60)  
score = 0
total_questions = len(quiz)


for idx, q in enumerate(quiz, start=1):
    print(Fore.MAGENTA + f"\nQuestion {idx}: {q['question']}")
    print(Fore.CYAN + "-" * 50)
    
    for option in q['options']:
        print(Fore.LIGHTWHITE_EX + f"    {option}")
    
    answer = input(Fore.YELLOW + "\nEnter your answer (A, B, C, or D): ").upper()
    
    if answer == q["answer"]:
        print(Fore.GREEN + pyfiglet.figlet_format("Correct!", font="small"))
        score += 1
    else:
        print(Fore.RED + pyfiglet.figlet_format("Incorrect", font="small"))
        print(Fore.RED + f"The correct answer was {q['answer']}.")

    print(Fore.CYAN + "=" * 60)

display_result(score, total_questions)
