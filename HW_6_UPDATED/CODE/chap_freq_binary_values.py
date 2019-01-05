'''
Created on May 25, 2018

@author: urvipatel
'''

import os
import collections

stopwords = open('stopwords.txt', 'r').read().split()
path = './literature/'
#path = './abr/'
NUM_TOP_WORDS = 500

    
def get_top_words():    
    word_counts = {}
    word_list = []
    files = os.listdir(path)
    for f in files:
        if '.DS_Store' in f:
            continue
        fileObj = open(path + f)
        contents = fileObj.read()
        tr = str.maketrans(';.,?!-\'"', '        ')
        contents = contents.translate(tr)
        paragraphs = str(contents).split('\n\n')
        for p in paragraphs:
            p = p.split()
            if len(p) > 10:
                for word in p:
                    if len(word) < 5 or word in stopwords or word[0].isupper():
                        continue
                    word_list.append(word)
                    if word not in word_counts:
                        word_counts[word] = 1
                    else:
                        word_counts[word] += 1
        fileObj.close()
    freq_of_top_words = collections.Counter(word_list).most_common(NUM_TOP_WORDS)
    top_words = dict(freq_of_top_words)
    return top_words


def get_chapters_by_author(fObj):
    with open(fObj.name, 'r') as f:
        a = f.name.split('/')[-1]
        author = a[:a.find('.')]
        tr = str.maketrans(';.,?!-\'"', '        ')
        chapters = {}
        chapter = ''
        line = ''
        for line in f:
            while not (line.startswith('CHAPTER') or line.startswith('<CHAPTER') or line.startswith('Stave') or line.find('Chapter') != -1 or line.find('CHAPTER') != -1):
                line = next(f)
            break
           
        while line:
            try:
                if line.startswith('CHAPTER') or line.startswith('<CHAPTER') or line.startswith('Stave') or line.find('Chapter') != -1 or line.find('CHAPTER') != -1:
                    line = next(f)
                    while not (line.startswith('CHAPTER') or line.startswith('<CHAPTER') or line.startswith('Stave') or line.find('Chapter') != -1 or line.find('CHAPTER') != -1):
                        if line  != '\n':
                            line = line.translate(tr)
                            chapter += line
                        line = next(f)
                    if author not in chapters:
                        chapters[author] = [chapter]
                    else:
                        chapters[author].append(chapter)
                    chapter = ''
            except StopIteration:
                chapters[author].append(chapter)
                f.close()
                return chapters           
def make_arff():
    print("\n******* Creating arff file for CHAPTER FREQ - BINARY ************")
    f = open('./chapter_freq_binary.arff', 'w')
    f.write('@relation bookauthor\n\n')
    top_words = get_top_words()
    for word in top_words:   #keywords:
        f.write('@attribute {}'.format(word) + ' real\n')
    f.write('@attribute bookauthor {austen,dickens,twain,wells}\n')
    f.write('\n@data\n')
    files = os.listdir(path)
    for fs in files:
        if '.DS_Store' in fs:
            continue
        fileObj = open(path + fs)
        a = fileObj.name.split('/')[-1]
        author = a[:a.find('.')]
        chap_by_auth = get_chapters_by_author(fileObj)
        for auth, chap in chap_by_auth.items():
            for c in chap:
                line = ''
                c_split = c.split()
                for cw in top_words:
                    if cw in c_split:
                        line += '1,'
                    else:
                        line += '0,'
                line += author
                f.write(line + '\n')
    f.close()
    fileObj.close()

make_arff()
print('Done')





