from lib.add_five import *
import pytest

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

def test_greet():
    assert greet('Harold') == 'Hello, Harold!'

def test_checkcodeword():
    assert check_codeword('horse') == "Correct! Come in."
    assert check_codeword('hope') == "Close, but nope."
    assert check_codeword('zebra') == "WRONG!"

def test_report_length():
    assert report_length("hello") == f"This string was 5 characters long."
    assert report_length("") == f"This string was 0 characters long."
    assert report_length("hello world") == f"This string was 11 characters long."

def test_counter():
    subject = Counter()
    assert subject.report() == "Counted to 0 so far."
    subject.add(4)
    assert subject.report() == "Counted to 4 so far."
    subject.add(3)
    assert subject.report() == "Counted to 7 so far."
    subject.add(8)
    assert subject.report() == "Counted to 15 so far."

def test_string_builder():
    subject = StringBuilder()
    assert subject.output() == ""
    subject.add("Hello ")
    assert subject.output() == "Hello "
    assert subject.size() == 6
    subject.add("World")
    assert subject.output() == "Hello World"
    assert subject.size() == 11
    subject.add("people")
    assert subject.output() == "Hello Worldpeople"
    assert subject.size() == 17

def test_gratitudes():
    subject = Gratitudes()
    subject.add('Herpes')
    assert subject.format() == "Be grateful for: Herpes"
    subject.add('HPV')
    assert subject.format() == "Be grateful for: Herpes, HPV"

def test_present():
    subject = Present()
    subject.contents = 'Waaa'
    with pytest.raises(Exception) as e:
        subject.wrap('Ploop')
    assert str(e.value) == "A contents has already been wrapped."
    subject.contents = None
    with pytest.raises(Exception) as e:
        subject.unwrap()
    assert str(e.value) == "No contents have been wrapped." 
    
def test_password_checker():
    subject = PasswordChecker()
    with pytest.raises(Exception) as e:
        subject.check('1234')
    assert str(e.value) == "Invalid password, must be 8+ characters."
