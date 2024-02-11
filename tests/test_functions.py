from lib.skills_functions import *

def test_snippet():
    assert snippet('Good morning! You are all wonderful people!') == 'Good morning! You are all...'

def test_counter():
    assert counter('Hello') == 1
    assert counter('Hello People') == 2
    assert counter('Hello you People') == 3
    assert counter('Hello you silly People') == 4
    assert counter('H E L L O') == 5
    assert counter('H E L L O W O R L D') == 10

def test_reading_speed():
    assert reading_speed('Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time tozz get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.') == '0.99 minutes'

def test_grammar_check():
    assert grammar_check('Hello.') == 'Well Done!'
    assert grammar_check('Hello') == 'You need to end the string with punctuation!'
    assert grammar_check('hello.') == 'You need to start with a capital letter!'
    assert grammar_check('hello') == 'You need to start with a capital letter and end with punctuation!'