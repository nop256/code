class Student:
    def __init__(self, last, first, ss, email, age):
        self.last = last
        self.first = first
        self.ss = ss
        self.email = email
        self. age = age
    
    def __eq__(self, rhs):
        self.ss == rhs.ss

    def __repr__(self):
        return f"Student({self.first} {self.last}, SSN: {self.ss})"

    def __lt__(self, rhs):
        return self.ss < rhs.ss

    def __gt__(self, rhs):
        return self.ss > rhs.ss
