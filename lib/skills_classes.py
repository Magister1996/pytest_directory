def say_hello(name):
    return (f"hello {name}")

def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
    print("".join(ciphertext_chars))
    return "".join(ciphertext_chars)

def decode(encrypted, key):
    cipher = make_cipher(key)
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) -65]
        plaintext_chars.append(plain_char)
    return "".join(plaintext_chars)

def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    alphabet.append(chr(32))
    print(alphabet)
    cipher_with_duplicates = list(key) + alphabet
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    return cipher 

class DiaryEntry:
    def __init__(self, title, contents):
        self.diary = {}
        self.title = title
        self.contents = contents

    def format(self):
        self.diary[self.title] = self.contents
        return self.diary

    def count_words(self):
        total_word_count = 0
        for title, entry in self.diary.items():
            combined_text = f'{title}: {entry}'
            word_count = len(combined_text.split())
            total_word_count += word_count
        return total_word_count


    def reading_time(self, wpm):
        word_count = self.count_words()
        answer = (word_count / wpm)
        return answer
    

    def reading_chunk(self, wpm, minutes):
        reading_chunk = f'{self.title}: {self.contents}'
        word_progress = wpm * minutes
        initial_list = reading_chunk.split()
        final_list = initial_list[:int(word_progress)]
        print(' '.join(final_list))
        return ' '.join(final_list)
    
    def get_most_common_letter(text):
        counter = {}
        for char in text:
            counter[char] = counter.get(char, 0) + 1
            letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
        return letter
    
class GrammarStats:
    def __init__(self):
        self.truecounter = 0
        self.falsecounter = 0

    def check(self, text):
        spag = '.?!'
        if text[0].isupper() and text[-1] in spag:
            self.truecounter += 1
            return True
        else:
            self.falsecounter += 1
            return False

    def percentage_good(self):
        total_checks = self.falsecounter + self.truecounter
        percentage_answer = (self.truecounter / total_checks) * 100
        return percentage_answer

class ToDoList():
    def __init__(self):
        self.task_list = []

    def see_list(self):
        return (f'This is your list of to do items: {self.task_list}')

    def add_task(self, task):
        self.task_list.append(task)

    def remove_completed_task(self, task):
        self.task_list.remove(task)

