def fifthchar(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) >= 5:
                result.append(line[4])
    return ''.join(result)
