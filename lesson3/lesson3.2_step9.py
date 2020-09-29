"""s = 'My Name is Iovan'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')"""

full_string = "13"
substring = "9"

assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)
