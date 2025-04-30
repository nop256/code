import random

questions = {
    "Appending to the end of a Python list": "1",
    "Removing from the beginning of a Python list": "n",
    "Traveling Salesperson by trying all paths (brute force)": "n!",
    "Adding two numbers of N digits each": "n",
    "Linear Search": "n",
    "Towers of Hanoi": "2^n",
    "Factoring a number": "sqrtn",
    "Matrix Multiplication": "n^3",
    "Binary Search": "logn",
    "SAT Problem (brute force)": "2^n",
    "Multiplying two N-digit numbers": "n^2",

    "Bubble Sort (random data)": "n^2",
    "Bubble Sort (mostly sorted data)": "n^2",
    "Shaker Sort (random data)": "n^2",
    "Shaker Sort (mostly sorted data)": "n",
    "Counting Sort (random data)": "n",
    "Counting Sort (mostly sorted data)": "n",
    "Merge Sort (random data)": "nlogn",
    "Merge Sort (mostly sorted data)": "nlogn",
    "Quick Sort (random data)": "nlogn",
    "Quick Sort (mostly sorted data, median-of-three pivot strategy)": "nlogn",
    "Quick Sort (mostly sorted data, naive (1st or last) pivot strategy)": "n^2",
    "Modified Quick Sort (random data)": "nlogn",
    "Modified Quick Sort (mostly sorted data)": "nlogn"
}

question_list = list(questions.items())
random.shuffle(question_list)

score = 0
total_questions = len(question_list)

print("\n💡 Welcome to the Big-O Complexity Quiz! 💡\n")
print("You'll be asked a series of questions about algorithm complexity.")
print("Enter your answer (e.g., n, n log n, 2^n, n^2, n^3, sqrt n, etc.)\n")

for i, (question, correct_answer) in enumerate(question_list, start=1):
    user_answer = input(f"Q{i}/{total_questions}: What is the Big-O complexity of {question}? ").strip()

    if user_answer.lower() == correct_answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is: {correct_answer}\n")

print(f"🎯 Quiz Complete! Your score: {score}/{total_questions} ({(score/total_questions)*100:.2f}%)")

if score == total_questions:
    print("🏆 Perfect score! You're a Big-O master!")
elif score > total_questions * 0.75:
    print("🔥 Great job, you're grasping the fundamentals!")
elif score > total_questions * 0.5:
    print("👍 Not bad, but keep practicing.")
else:
    print("📚 Keep studying! Algorithm complexity is a key concept in CS.")


