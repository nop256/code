import random, time, os, re
from datetime import datetime

OPERATORS = ['+', '-', '*', '/']
DIGITS = list('123456789')  #zero not included to avoid division by zero
PARENTHESES = ['(', ')']

def generate_infix_expression(min_length=15, max_depth=3):
    """dynamically generates a random infix expression with controlled depth."""
    def build_expr(depth):
        if depth == 0:
            return str(random.randint(1, 9))  #always single-digit for now
        
        if random.random() < 0.3:
            return build_expr(depth - 1)  #bias toward simpler expressions

        op = random.choice(OPERATORS)
        left = build_expr(depth - 1)
        right = build_expr(depth - 1)
        
        #integer division safety net
        if op == '/': 
            try: #make sure right is non-zero
                right_val = eval(right)
                if right_val == 0:
                    right_val = 1
                #left value = multiple of right value
                left_val = right_val * random.randint(1, 5)
                left = str(left_val)
                right = str(right_val)
            except:
                left, right = '8', '2'  #fallback values
        
        expr = f"{left}{op}{right}"
        if random.random() < 0.5:
            return f"({expr})"
        return expr

    #retry until expression meets the minimum length
    while True:
        expr = build_expr(max_depth)
        if len(expr) >= min_length:
            return expr

def tokenize(expr):
    return re.findall(r'\d+|[()+\-*/]', expr)

def infix_to_postfix(expr):
    '''converts infix to postfix using shunting yard algorithm'''
    tokens = tokenize(expr)
    output = []
    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in OPERATORS:
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

def evaluate_postfix(postfix_expr):
    """evaluates the postfix expression"""
    stack = []
    tokens = postfix_expr.strip().split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in OPERATORS:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a // b)
    return stack[0] if stack else 0

# def space_postfix(expr):
#     spaced = []
#     i = 0
#     while i < len(expr):
#         if expr[i].isdigit():
#             num = expr[i]
#             while i + 1 < len(expr) and expr[i + 1].isdigit():
#                 i += 1
#                 num += expr[i]
#             spaced.append(num)
#         else:
#             spaced.append(expr[i])
#         i += 1
#     return ' '.join(spaced)

def save_stats(incorrect_responses):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    fileName = os.path.join(scriptDir, "infix_postfix_quiz_stats.txt")

    if not os.path.exists(fileName):
        with open(fileName, "w", encoding="utf-8") as file:
            file.write("Infix to Postfix Quiz - Incorrect Responses\n")
            file.write("="*40 + "\n")

    with open(fileName, "a", encoding="utf-8") as file:
        file.write(f"\nSession: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for infix, correct_postfix, user_postfix, postfix_eval, user_eval in incorrect_responses:
            file.write(f"Infix: {infix}\n")
            file.write(f"Expected Postfix: {correct_postfix} | Your Answer: {user_postfix}\n")
            file.write(f"Postfix Eval: {postfix_eval} | Your Eval Answer: {user_eval}\n")
            file.write("-"*40 + "\n")

def quiz():
    number_of_questions = int(input("How many questions? (1–20): "))
    incorrect = []

    for _ in range(number_of_questions):
        infix = generate_infix_expression()
        correct_postfix = infix_to_postfix(infix)
        try:
            postfix_eval = evaluate_postfix(correct_postfix)
        except ZeroDivisionError:
            print("\n⚠️ Skipping this question due to division by zero.")
            continue  #skip to next question
        #postfix_spaced = space_postfix(correct_postfix)
        
        print("\n🔔 Use spaces between **all** numbers and operators — especially for multi-digit numbers!")
        print("🔔 Enter the postfix expression with spaces between all numbers and operators (e.g., 2 3 + 4 * )")
        print(f"\nConvert the infix expression to postfix: {infix}")
        #print(f"Expected: {correct_postfix}") #for debugging
        user_postfix = input("Postfix: ")
        user_postfix = ' '.join(user_postfix.strip().split())
        if user_postfix == correct_postfix:
            print("✅ Correct postfix!")
        else:
            print(f"❌ Incorrect. Expected: {correct_postfix}")

        print(f"\nNow evaluate the correct postfix expression (with spaces): {correct_postfix}")
        #print(f"Expected result: {postfix_eval}") #for debugging
        try:
            user_eval = int(input("Result: "))
        except ValueError:
            user_eval = None

        if user_eval == postfix_eval:
            print("✅ Correct evaluation!")
        else:
            print(f"❌ Incorrect. Expected result: {postfix_eval}")
            incorrect.append((infix, correct_postfix, user_postfix, postfix_eval, user_eval))

    if incorrect:
        save_stats(incorrect)
        print(f"\nStats saved for {len(incorrect)} incorrect responses.")
    else:
        print("\nAll answers were correct! 🎉")

def main():
    quiz()

if __name__ == "__main__":
    main()
