'''
Created on May 22, 2018

@author: urvipatel
'''

#===============================================================================
# import os
# import collections
# import pprint
# 
# top_5 = {}
# 
#         
# def get_paragraph_list():
#     plist = []
#     path = './literature/abr/'
#     files = os.listdir(path)
#     files.remove('.DS_Store')
#     for f in files:
#         file = open(path + f)
#         contents = file.read()
#         tr = str.maketrans('.,?!-\'"', '       ')
#         contents = contents.translate(tr)
#         paragraphs = contents.split('\n\n')
#         for p in paragraphs:
#             if len(p.split()) > 10:
#                 plist.append(p)
#         file.close()
#     return plist
# 
# def tf(w, p):
#     words_in_paragraph = p.split()
#     count = collections.Counter(words_in_paragraph)[w]
#     ret = count / len(words_in_paragraph)
#     return ret
# 
# def num_paragraphs_containing_word(word, pl):
#     ret = sum(1 for p in pl if word in p.split())
#     return ret
# 
# def idf(w, pl):
#     ret = len(pl) /num_paragraphs_containing_word(w, pl)
#     return ret
# 
# def tfidf(w, p, pl):
#     tf_val = tf(w, p)
#     idf_val = idf(w, pl)
#     ret = tf_val * idf_val
#     return ret
#===============================================================================

#===============================================================================
# def make_arff():
#     f = open('./books.arff', 'w')
#     f.write('@relation bookauthor\n\n')
#     for word in top_5:
#         f.write('@attribute real')
#     f.write('@attribute bookauthor {austen_abr,dickens_abr,twain_abr,wells_abr}\n')
#     auths = [ ]
# 
#      for author in authors:
#          print(author[:author.find('.')])
#          auths.append(author[:author.find('.')])
#      print(auths)
# 
#     i=0
#     f.write('\n@data\n')
#     for file in authors:
#         author = authors[file]
#         for p in author.paras:
#             # take a sampling of only 20% of paragraphs, since
#             # otherwise it will take forever to train, or Java
#             # will run out of heap space
#             if random.random() < .8 :
#                 continue
#             line = ''
#             # create the vector for a paragraph
#             for word in keywords:
#                 if word in p:
#                     line += '1,'
#                 else:
#                     line += '0,'
#             line += auths[i]
#             f.write(line + '\n')
#         i += 1
#     f.close()
#===============================================================================

#===============================================================================
# scores = {}
# freq = {}
# paragraph_list = get_paragraph_list()
# for paragraph in paragraph_list:
#     for word in paragraph.split():
#         if len(word) < 5:
#             continue
#         stat = tfidf(word, paragraph, paragraph_list)
#         scores[word] = stat
#         if word not in freq:
#             freq[word] = 1
#         else:
#             freq[word] = freq[word] + 1
# a = [(k,v) for v,k in sorted([(v,k) for k,v in scores.items()], reverse=True)]
# pprint.pprint(a)
# for k, v in a:
#     if len(top_5) < 5:
#         top_5[k] = v
#     else:
#         break
# print(top_5)
# print('Done')
#===============================================================================
