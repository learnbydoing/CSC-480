'''
Created on May 25, 2018

@author: urvipatel
'''
romanNumerals = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

def dickens():
    import re
    with open('./literature/dickens.txt', 'r') as f:
    #with open(fObj.name, 'r') as f:
        a = f.name.split('/')[-1]
        author = a[:a.find('.')]
        tr = str.maketrans(';.,?!-\'"', '        ')
        i = 0
        chapters = {}
        chapter = ''
        line = ''
        for line in f:
            line = line.replace(' ', '')
            while not re.match(romanNumerals, line):
                line = next(f)
                line = line.strip()
            break
           
        while line:
            try:
                if re.match(romanNumerals, line):
                    line = next(f)
                    while not re.match(romanNumerals, line):
                        if line  != '\n':
                            line = line.translate(tr)
                            chapter += line
                        if 'the Lord Mayor' in line:
                            print('here')
                        line = next(f)
                    if author not in chapters:
                        chapters[author] = [chapter]
                    else:
                        chapters[author].append(chapter)
                    chapter = ''
                    i = i + 1
                    print(len(chapters[author]))
            except StopIteration:
                chapters[author].append(chapter)
                f.close()
                return chapters