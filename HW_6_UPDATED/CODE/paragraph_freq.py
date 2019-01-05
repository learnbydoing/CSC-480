'''
Created on May 26, 2018

@author: urvipatel
'''

import os
import collections


stopwords = open('stopwords.txt', 'r').read().split()
path = './literature/'
#path = './abr/'
word_counts = {} 
word_list = []
NUM_TOP_WORDS = 500

    
def get_top_words():
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

def get_paragraphs_for_all_authors ():
    paragraphs_per_author = {}
    files = os.listdir(path)
    for f in files:
        if '.DS_Store' in f:
            continue
        file = open(path + f)
        contents = file.read()
        tr = str.maketrans('.,?!-\'"', '       ')
        contents = contents.translate(tr)
        paragraphs = contents.split('\n\n')
        for p in paragraphs:
            #===================================================================
            # if random.random() < .8 :
            #     continue
            #===================================================================
            if len(p.split()) > 10:
                if not f in paragraphs_per_author:
                    paragraphs_per_author[f] = [p]
                else:
                    paragraphs_per_author[f].append(p)
        file.close()
    return paragraphs_per_author
                      
def make_arff():
    print("\n******* Creating arff file for PARAGRAPH FREQ - COUNT ************")
    f = open('./paragraph_freq_count.arff', 'w')
    f.write('@relation bookauthor\n\n')
    top_words = get_top_words()
    for word in top_words:   #keywords:
        f.write('@attribute {}'.format(word) + ' real\n')
    f.write('@attribute bookauthor {austen,dickens,twain,wells}\n')
    f.write('\n@data\n')
    
    pba = get_paragraphs_for_all_authors()
    auth  = pba.keys()
    for a in auth:
        author = a[:a.find('.')]
        pghs = pba[a]
        for p in pghs:
            line = ''
            p = p.split()
            for cw in top_words:
                count = collections.Counter(p)[cw]
                line = line + str(count) + ','
            line += author
            f.write(line + '\n')        
    f.close()

make_arff()
print('Done')