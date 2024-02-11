from lib.mocking_bites import *
from unittest.mock import Mock
import pytest
import time

def test_music_library_search():
    track1 = Track('Motorhead', 'Ace of spades')
    track2 = Track('Oneheart', 'Snowfall')
    track3 = Track('Motorhead', 'We are the road crew')
    subject = MusicLibrary()
    subject.track_list.extend([track1, track2, track3])
    assert subject.search('Motor') ==[track1, track3]

def test_music_library_search_unit_testing():
    track1 = Mock()
    track1.matches.return_value = True
    subject = MusicLibrary()
    subject.add(track1)
    assert subject.search('Yes') ==[track1]

def test_adds_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.tasks == [task_1, task_2]

def test_marks_tasks_as_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    task_2.mark_complete()
    assert task_list.all_complete() == True

def test_constructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

def test_can_be_marked_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.is_complete() == True

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def task_list_add():
    task_list = TaskList()
    task1 = Mock()
    task2 = Mock()
    task3 = Mock()
    task_list.add(task1)
    task_list.add(task2)
    task_list.add(task3)
    assert task_list.all() == [task1, task2, task3]

def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_taskformatter_init():
    task = Mock()
    task.title = 'Meeting'
    task.complete = False
    formatter = TaskFormatter(task)
    assert formatter.formatter_title == 'Meeting'
    assert formatter.formatter_complete == False

def test_taskformatter_format():
    task = Mock()
    task.title = 'Meeting'
    task.complete = False
    formatter = TaskFormatter(task)
    assert formatter.format() == "[ ] Meeting"
    task2 = Mock()
    task2.title = 'Meeting'
    task2.complete = True
    formatter = TaskFormatter(task2)
    assert formatter.format() == "[X] Meeting"

def test_set_up_blank_mock():
    fake_object = Mock()
    assert fake_object is not None

def test_set_up_mock_with_methods():
    fake_object = Mock()
    fake_object.speak.return_value = "Meow, Jess"
    fake_object.count_ears.return_value = 2
    fake_object.count_legs.return_value = 4

    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4

def test_assert_that_mock_was_called():
    fake_object = Mock()
    fake_object.speak("Steve")
    fake_object.speak.assert_called_with("Steve")

def test_creates_mock_for_specific_case():
    fake_diary = Mock()
    fake_diary.count_entries.return_value = 2

    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add(Mock())
    assert fake_diary.count_entries() == 2

def test_secret_diary_init():
    example = Diary('Hello')
    secret = SecretDiary(example)
    assert secret.secret_diary == example
    assert secret.secret_diary.contents == 'Hello'

def test_secret_diary_read_lock():
    example = Diary('Hello')
    secret = SecretDiary(example)
    secret.lock()
    with pytest.raises(Exception) as e:
        secret.read()
    assert str(e.value) == "Go away!"

def test_secret_diary_read_unlock():
    example = Diary('Hello')
    secret = SecretDiary(example)
    secret.lock()
    secret.unlock()
    assert secret.read() == 'Hello'

def test_diary_read():
    example = Diary('Hello')
    assert example.read() == 'Hello'

def test_secret_diary_mock_init():
    example = Mock()
    secret = SecretDiary(example)
    example.contents = 'Hello'
    assert secret.secret_diary == example
    assert secret.secret_diary.contents == 'Hello'

def test_secret_diary_read_mock_lock():
    example = Mock()
    secret = SecretDiary(example)
    secret.lock()
    with pytest.raises(Exception) as e:
        secret.read()
    assert str(e.value) == "Go away!"

def test_secret_diary_read_mock_unlock():
    example = Mock()
    secret = SecretDiary(example)
    example.read.return_value = 'Hello'
    secret.lock()
    secret.unlock()
    assert secret.read() == 'Hello'

def test_calls_api_to_provide_suggested_activity():
    requester_mock = Mock(name="requester") # This name is just for readability
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock` 
    # when we call `get()` on it.
    requester_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {
        "activity": "Write a short story",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "",
        "key": "6301585",
        "accessibility": 0.1
    }

    activity_suggester = ActivitySuggester(requester_mock)
    result = activity_suggester.suggest()
    assert result == "Why not: Write a short story"

def test_time_error_mock():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')
    time_mock = Mock()

    time_mock.time.return_value = 1707476789
    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"unixtime": 1707476789}

    timeobject = TimeError(requester_mock)
    assert timeobject.error(time_mock) == 0

def test_cat_facts():
    
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime."}
    test_class = CatFacts(requester_mock)
    assert test_class.provide() == "Cat fact: A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime."