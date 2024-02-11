## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

Take a block of text, find the numbers of words inside, divide it by the reading speed.

## 2. Design the Function Signature

def draft
    take a string and turn it into a list using .split()
    divide the length of that list by the words per minute

def reading_speed(string):
    new_list = string.split()
    speed = len(new_list) / 200
    return speed

## 3. Create Examples as Tests

Input a text with a known number of words e.g 400
assert that the result of that function is 400 / 200 = 2

assert reading_speed(*First paragraph of moby dick*) = 0.99

## 4. Implement the Behaviour
See test_functions.py
