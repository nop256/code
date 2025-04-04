#from bag import bag
from linkedlist import bag
from student import Student

def main():
    b = bag()
    try:
        with open ("FakeNames.txt", "r") as file:
            for line in file:
                words = line.split()
                l,f,ss,e,a = words
                student = Student(l,f,ss,e,a)
                if not b.insert(student):
                    print(f"Duplicate detected: {student}")
    except FileNotFoundError:
        print("Error: FakeNames.txt not found. Make sure the file is in the correct directory.")
        return
    file.close()
    print(f"Total students added: {b.size()}")

main()
