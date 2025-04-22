class Student:
    """This class contains all the fields found in FakeNames.txt."""
    
    def __init__(self, last, first, ss, email, age):
        self.last = last
        self.first = first
        self.email = email
        self.ss = ss
        #self.dob = dob
        self.age = age

    def __eq__(self, rhs):
        if not isinstance(rhs, Student):
            return False
        return self.ss == rhs.ss

    def __repr__(self):
        return f"Student({self.first} {self.last}, SSN: {self.ss})"
    
    def __lt__(self, rhs):
        return self.ss < rhs.ss

    def __gt__(self, rhs):
        return self.ss > rhs.ss

    def __hash__(self):                     # added with hash
        return int(self.ss.replace("-",""))
