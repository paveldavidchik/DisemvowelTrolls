
def disemvowel(string):
    return ''.join([l for l in string if l.lower() not in 'aeiou'])


string = input('Enter any string: ')
print(disemvowel(string))
