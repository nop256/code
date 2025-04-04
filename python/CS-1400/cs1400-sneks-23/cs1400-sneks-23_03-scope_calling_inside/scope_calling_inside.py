def improve_message(a_string):
    return a_string.replace('dog', 'doggo')

def combine_messages(first, second, third):
    return improve_message(first + '\n' + second + '\n' + third)

first = 'That dog is cute.'
second = "I want to pet the dog."
third = "I will ask the dog's owner."
print(combine_messages(first, second, third))
