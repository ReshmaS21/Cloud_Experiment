words = ['Berkshire', 'Hackney', 'Hampshire', 'Yorkshire']
vowels = list('aeiou')
output = []

for word in words:
    new_list = list(word.lower())
    
    for vowel in vowels:
        while True:
            try:
                new_list.remove(vowel)
            except:
                break
    
    output.append(''.join(new_list).capitalize())
    
print(output)