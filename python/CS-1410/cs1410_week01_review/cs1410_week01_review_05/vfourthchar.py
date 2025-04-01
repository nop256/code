


def fourthchar(filename,lines):
    result = ""

    for line in lines:
        if len(line) >= 4:
            result += line[3]
        else:
            result += 'x'


    with open(filename, 'w') as file:
        file.write(result + '\n')





fourthchar("output.txt", ["abcde", "ghi", "jklm"])
