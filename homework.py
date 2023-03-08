import re

full_names = "Abraham Lincoln, Andrew P Garfield, Connor Milliken, Jordan Alexander Williams, Madonna, programming is cool"

#I used the set up from the grouping function in lecture
#not confident at all in predetermining the string through the compile tool
name_pattern = re.compile('([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')

for name in full_names.split(','):
    match = name_pattern.search(name)
    
    if match:
        print(match.group(0))
    else:
        print("None")
        
#for some reason missing the Andrew P Garfield