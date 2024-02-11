from lib.skills_class_systems import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_remove_all_vowels():
    remover = VowelRemover("aeiou")
    assert remover.remove_vowels() == ""

def test_letter_counter():
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]

def test_diary_add():
    subject = DiaryEntry('Day1', 'Hello')
    subject.format()
    diary = Diary()
    diary.add(subject)
    assert diary.entry_list == [subject]

def test_diary_all():
    subject = DiaryEntry('Day1', 'Hello')
    subject.format()
    subject2 = DiaryEntry('Day2', 'Goodbye')
    subject2.format()
    subject3 = DiaryEntry('Day3', 'Yes')
    subject3.format()
    subject4 = DiaryEntry('Day4', 'No')
    subject4.format()
    diary = Diary()
    diary.add(subject)
    diary.add(subject2)
    diary.add(subject3)
    diary.add(subject4)
    assert diary.all() == [subject, subject2, subject3, subject4]

def test_diary_count():
    subject = DiaryEntry('Day1', 'Hello')
    subject.format()
    subject2 = DiaryEntry('Day2', 'Goodbye')
    subject2.format()
    subject3 = DiaryEntry('Day3', 'Yes')
    subject3.format()
    subject4 = DiaryEntry('Day4', 'No')
    subject4.format()
    diary = Diary()
    diary.add(subject)
    diary.add(subject2)
    diary.add(subject3)
    diary.add(subject4)
    assert diary.count_words() == 8

def test_reading_time():
    subject = DiaryEntry('Day1', 'Hello')
    subject.format()
    subject2 = DiaryEntry('Day2', 'Goodbye')
    subject2.format()
    subject3 = DiaryEntry('Day3', 'Yes')
    subject3.format()
    subject4 = DiaryEntry('Day4', 'No')
    subject4.format()
    diary = Diary()
    diary.add(subject)
    diary.add(subject2)
    diary.add(subject3)
    diary.add(subject4)
    assert diary.reading_time(8) == 1

def test_diary_best_entry():
    subject = DiaryEntry('Day1', 'Hello you beautiful people')
    subject.format()
    subject2 = DiaryEntry('Day2', 'Goodbye everybody')
    subject2.format()
    subject3 = DiaryEntry('Day3', 'Yes I would like an apple please')
    subject3.format()
    subject4 = DiaryEntry('Day4', "No, I dont want to do that, you are a very rude person and I'm insulted")
    subject4.format()
    diary = Diary()
    diary.add(subject)
    diary.add(subject2)
    diary.add(subject3)
    diary.add(subject4)
    assert diary.find_best_entry_for_reading_time(3,3) == subject3

def test_entry_format():
    subject = DiaryEntry('Title', 'Contents')
    assert subject.format() == "Title: Contents"

def test_entry_count_words():
    subject = DiaryEntry('Day 1', 'Today was a good day in the quiet town of Berkshire')
    subject.format()
    assert subject.count_words() == 13

def test_entry_reading_time():
    subject = DiaryEntry('Day 2', 'Today was a terrible day as I went into a noisy city and got overwhelmed')
    subject.format()
    assert subject.reading_time(100), 2 == 0.17

def test_entry_reading_chunk():
    subject = DiaryEntry('Day1','This is an example text')
    subject.format()
    assert subject.reading_chunk(5, 1) == "Day1: This is an example"

def test_return_entry():
    subject = EntryExperience('Day 1', 'Hello there')
    subject.format()
    diary = SecondDiary()
    diary.add(subject)
    assert diary.show_entry('Day 1') == 'Day 1: Hello there'

def test_return_reading_block():
    subject = EntryExperience('Day1', 'Hello you beautiful people')
    subject.format()
    subject2 = EntryTask('Task' , 'Completed')
    subject3 = EntryExperience('Day3', 'Yes I would like an apple please')
    subject3.format()
    subject4 = EntryExperience('Day4', "No, I dont want to do that, you are a very rude person and I'm insulted")
    subject4.format()
    diary = SecondDiary()
    diary.add(subject)
    diary.add(subject2)
    diary.add(subject3)
    diary.add(subject4)
    assert diary.best_entry_for_time(3,3) == subject3

def test_return_todo():
    subject = EntryTask('Meeting', 'To Do')
    subject2 = EntryTask('Task', 'Completed')
    subject3 = EntryTask('Interview', 'To Do')
    subject4 = EntryExperience('Day4', "No, I dont want to do that, you are a very rude person and I'm insulted")
    subject4.format()
    subject5 = EntryContact('Ann', '07965438754')

    diary = SecondDiary()
    diary.entry_list.extend([subject, subject2, subject3, subject4, subject5])

    assert diary.show_todo_list() == ['Meeting', 'Interview']

def test_return_phone():
    subject = EntryContact('Phil', '07760645645')
    subject2 = EntryContact('George' , '07891234567')
    subject3 = EntryContact('Ann', '07965438754')
    subject4 = EntryTask('Interview', 'To Do')
    subject5 = EntryExperience('Day4', "No, I dont want to do that, you are a very rude person and I'm insulted")
    subject5.format()

    diary = SecondDiary()
    diary.entry_list.extend([subject, subject2, subject3, subject4, subject5])

    assert diary.show_contact('Phil') == '07760645645'
    assert diary.show_number('07760645645') == 'Phil'

