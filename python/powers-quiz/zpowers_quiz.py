import random, time, os
from datetime import datetime


superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
def to_superscript(n):
    return str(n).translate(superscript_map)

def saveStats(score, number_of_questions, num_incorrect, incorrect_answers, elapsed_time):
    """Save game stats to a text file to track your progress."""
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    #print(scriptDir) # for testing
    fileName = os.path.join(scriptDir, "powers_quiz_stats.txt")
    
    if not os.path.exists(fileName):
        with open(fileName, "w", encoding="utf-8") as file:
            file.write("Powers of Two Quiz - Game Statistics\n")
            file.write("="*40 + "\n")
    
    with open(fileName, "a", encoding="utf-8") as file:
        file.write("\n" + "="*40 + "\n")  
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Total Questions: {number_of_questions}\n")
        file.write(f"Correct Answers: {score}\n")
        file.write(f"Incorrect Answers: {num_incorrect}\n")
        file.write(f"Time Taken: {round(elapsed_time, 2)} seconds\n")
        
        if num_incorrect > 0:
                file.write("Incorrect Responses:\n")
                for key, (expected, given) in incorrect_answers.items():
                    exponent = to_superscript(key)
                    file.write(f"  2{exponent} = {expected}  -  You answered: {given}\n")

        file.write("="*40 + "\n")

def exponentQuiz():
    alive = True
    while alive:
        powers = []
        number_of_questions = int(input("\nEnter a number of questions (1-50): "))
        while number_of_questions < 0 or number_of_questions > 50:
            number_of_questions = int(input("Please pick a number between (1-50): "))
        for number in random.sample(range(50), number_of_questions):
            powers.append(number)
            
        #print(powers) # for testing
        incorrect = {}
        score = 0
        num_incorrect = 0
        start = time.time()
        
        for i in powers:
            correct_answer = 2**i
            exponent = to_superscript(i)
            
            # optimized lookup table
            suffixes = ["","K","M","B","T"]
            exponentGroup = min(i // 10, len(suffixes) - 1)
            expected_answer = str(correct_answer // (1024 ** exponentGroup)) + suffixes[exponentGroup]
            
            # original, unoptimized lookup table
            # if 0 <= i < 10:
            #     expected_answer = str(correct_answer)
            # elif 10 <= i < 20:
            #     expected_answer = str(correct_answer // 1024) + "K"
            # elif 20 <= i < 30:
            #     expected_answer = str(correct_answer // (1024 ** 2)) + "M"
            # elif 30 <= i < 40:
            #     expected_answer = str(correct_answer // (1024 ** 3)) + "B"
            # elif 40 <= i <= 50:
            #     expected_answer = str(correct_answer // (1024 ** 4)) + "T"
                
            while True:
                try:
                    question = str(input(f"2{exponent} = ")).strip().upper()
                    #print(expected_answer) # for testing
                    if question == expected_answer:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print(f"Incorrect. The correct answer was {expected_answer}")
                        incorrect[i] = (expected_answer, question)
                        num_incorrect += 1
                        break
                except ValueError:
                    print("Invalid input. Please enter your answer in the correct format.")
        
        end = time.time()
        elapsed_time = end - start
        
        print(f"\nQuiz completed. Score: {score}/{number_of_questions}")
        print(f"Time taken: {round(elapsed_time, 2)} seconds.")
        
        if num_incorrect > 0:
            print(f"\nIncorrect Answers:")
            for index, (key,(expected, given)) in enumerate(incorrect.items(), start=1):
                exponent = to_superscript(key)
                #print(f"key: {key}") # for testing
                print(f"{index}. 2{exponent} = {expected}  -  You answered: {given}")
        
        saveStats(score, number_of_questions, num_incorrect, incorrect, elapsed_time)
        print("\nGame stats saved to quiz_stats.txt")
        
        while True:
            try:
                valid = ["Y","N"]
                new_game = str(input("\nPlay Again? (Y/N) ")).upper()
                if new_game == "N":
                    print("\nThanks for playing!")
                    alive = False
                    break
                elif new_game == "Y":
                    break
            except ValueError:
                    print("Invalid input. Please select (Y/N) ")
    
def main():
    exponentQuiz()

if __name__ == "__main__":
    main()
