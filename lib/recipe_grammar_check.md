## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

Take a string, check for capital letter, check for punctuation, return appropriate result.

## 2. Design the Function Signature

def draft
    string of punction chracters
    if statement for capital letter and punc present
    say good job
    else if for just capital letter
    say you need a capital letter
    else if for just punc
    say you need punctuation
    else
    You need both a capital letter and punctation

def grammar_check(string):
    punc string = '!.?'
    if string[0].isupper() and string[-1] in punc string.
    reutrn "Well done!"
    etc
    etc


## 3. Create Examples as Tests

assert that a simple string like hello follows the rules.

assert grammer_check('Hello!') == 'Well done!'

## 4. Implement the Behaviour
See test_functions.py
