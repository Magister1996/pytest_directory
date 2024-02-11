def add_five(num):
    return num + 5

def greet(name):
    return f"Hello, {name}!"

def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"
    
def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."

class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."
    
class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str

class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
    


# class Reminder:
#     def __init__(self, name):
#         self.name = name
#         self.task = None

#     def remind_me_to(self, task):
#         self.task = task

#     def remind(self):
#         # Look here! We want to fail if there is no reminder yet.
#         if self.task is None:
#             raise Exception("No reminder set!")
#         return f"{self.task}, {self.name}!"


# def test_reminder():
#     reminder = Reminder("Kay")
#     with pytest.raises(Exception) as e: # <-- New code
#         reminder.remind()
#     error_message = str(e.value) # <-- New code
#     assert error_message == "No reminder set!"


class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents
    
class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
        
