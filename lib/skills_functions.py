def snippet(string_input):
    new_list = string_input.split()
    answer_string = ' '.join(new_list[:5])
    return answer_string + '...'
print(snippet('Good morning! You are all wonderful people!'))

def counter(string_input):
    new_list = string_input.split()
    return len(new_list)

def reading_speed(string_input):
    new_list = string_input.split()
    answer = float(len(new_list) / 200)
    return (f'{answer} minutes')

def grammar_check(string_input):
    spag = '.?!'
    if string_input[0].isupper() and string_input[-1] in spag:
        return 'Well Done!'
    elif string_input[0].islower() and string_input[-1] in spag:
        return 'You need to start with a capital letter!'
    elif string_input[0].isupper() and string_input[-1] not in spag:
        return 'You need to end the string with punctuation!'
    else:
        return 'You need to start with a capital letter and end with punctuation!'