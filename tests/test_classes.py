from lib.skills_classes import *

def test_say_hello():
    assert say_hello('kay') == 'hello kay'



def test_format():
    subject = DiaryEntry('Title', 'Contents')
    assert subject.format() == {'Title': 'Contents'}

def test_count_words():
    subject = DiaryEntry('Day 1', 'Today was a good day in the quiet town of Berkshire')
    subject.format()
    assert subject.count_words() == 13

def test_reading_time():
    subject = DiaryEntry('Day 2', 'Today was a terrible day as I went into a noisy city and got overwhelmed')
    subject.format()
    assert subject.reading_time(100), 2 == 0.17


def test_reading_chunk():
    subject = DiaryEntry('Day1','This is an example text')
    subject.format()
    assert subject.reading_chunk(5, 1) == "Day1: This is an example"


def test_grammar_stats_check():
    subject = GrammarStats()
    assert subject.check('Hello.') == True
    assert subject.check('Hello!') == True
    assert subject.check('Hello?') == True
    assert subject.check('Hello') == False
    assert subject.check('hello.') == False
    assert subject.check('hello') == False

def test_grammar_stats_percentage_good():
    subject = GrammarStats()
    subject.check('Hello.')
    subject.check('Hello.')
    subject.check('Hello.')
    subject.check('Hello.')
    subject.check('Hello')
    subject.check('Hello')
    subject.check('Hello')
    subject.check('Hello')
    assert subject.percentage_good() == 50

def test_todo_list():
    subject = ToDoList()
    subject.add_task('Meeting1')
    subject.add_task('Meeting2')
    subject.add_task('Meeting3')
    subject.add_task('Meeting4')
    subject.add_task('Meeting5')
    subject.add_task('Meeting6')
    assert subject.see_list() ==  "This is your list of to do items: ['Meeting1', 'Meeting2', 'Meeting3', 'Meeting4', 'Meeting5', 'Meeting6']"
    subject.remove_completed_task('Meeting5')
    assert subject.see_list() == "This is your list of to do items: ['Meeting1', 'Meeting2', 'Meeting3', 'Meeting4', 'Meeting6']"