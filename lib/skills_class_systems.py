class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        answer_list = (c for c in self.text if c not in self.vowels)
        return "".join(answer_list)

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count = counter[char]
        return [most_common_count, most_common]

class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)
        pass

    def all(self):
        return self.entry_list

    def count_words(self):
        word_count = 0
        for entry in self.entry_list:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        total_words = 0
        for entry in self.entry_list:
            total_words += entry.count_words()
        return total_words / wpm
        


    def find_best_entry_for_reading_time(self, wpm, minutes):
        total_words = wpm * minutes
        answer_list = (entry for entry in self.entry_list if entry.count_words() < total_words)
        sorted_answer_list = sorted(answer_list, key=lambda x: x.count_words(), reverse=True)
        print(sorted_answer_list[0].__dict__)
        return sorted_answer_list[0]

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        self.formatted_entry = f'{self.title}: {self.contents}'
        return self.formatted_entry

    def count_words(self):
        word_list = self.formatted_entry.split()
        return len(word_list)


    def reading_time(self, wpm):
        word_count = self.count_words()
        answer = (word_count / wpm)
        return answer
    

    def reading_chunk(self, wpm, minutes):
        word_progress = wpm * minutes
        initial_list = self.formatted_entry.split()
        final_list = initial_list[:int(word_progress)]
        return ' '.join(final_list)

class SecondDiary():
    def __init__(self):
        self.entry_list = []

    def add(self, subject):
        self.entry_list.append(subject)
    
    def show_entry(self, prompt):
        sorted_list = [i for i in self.entry_list if isinstance(i, EntryExperience)]
        answer_list = [i for i in sorted_list if prompt in i.title]
        return answer_list[0].formatted_entry

    def best_entry_for_time(self, wpm, minutes):
        sorted_list = [i for i in self.entry_list if type(i) == EntryExperience]
        total_words = wpm * minutes
        answer_list = (i for i in sorted_list if i.count_words() < total_words)
        sorted_answer_list = sorted(answer_list, key=lambda x: x.count_words(), reverse=True)
        print(sorted_answer_list[0].__dict__)
        return sorted_answer_list[0]
    
    def show_todo_list(self):
        todo_tasks = [task.task['task'] for task in self.entry_list if isinstance(task, EntryTask) and task.task['status'] == 'To Do']
        return todo_tasks
    
    def show_contact(self, name):
        answer = [i.number for i in self.entry_list if isinstance(i, EntryContact) and i.name == name]
        return str(answer[0])
    
    def show_number(self, number):
        answer = [i.name for i in self.entry_list if isinstance(i, EntryContact) and i.number == number]
        return str(answer[0])
    
class EntryExperience():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        self.formatted_entry = f'{self.title}: {self.contents}'
        return self.formatted_entry

    def count_words(self):
        word_list = self.formatted_entry.split()
        return len(word_list)

class EntryTask():
    def __init__(self, taskname, status):
        self.task = {'task': taskname, 'status': status}

class EntryContact():
    def __init__(self, name, number):
        self.name = name
        self.number = number
    