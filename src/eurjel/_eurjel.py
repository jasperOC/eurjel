import sys
import re

import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')
PUNCTUATION_REGEXP = re.compile(u'[\u201c\u201d,\.!?;:\'\"\(\)\{\}\[\]]+')

def stemmer(words, current):
    result = None
    if current.endswith('s') and current[:-1] in words:
        result = current[:-1]
    if current.endswith('ies') and '%sy' % current[:-3] in words:
        result = '%sy' % current[:-3]
    if not result is None:
        sys.stderr.write('Stemmed %s -> %s\n' % (current.encode('utf8'), 
                                                 result.encode('utf8')))
    return result



def get_word_count(words):
    fd = FreqDist()
    for word in words:
        word = PUNCTUATION_REGEXP.sub('', word.lower())
        if word in STOPWORDS or len(word) < 3 or word.isdigit():
            continue
        fd.inc(word)

    words = fd.sorted()
    for word in words:
        stemmed = stemmer(words, word)
        if stemmed:
            fd[stemmed] += fd[word]
            del fd[word]

    result = fd.sorted()
    for word in result[:100]:
        yield word, fd[word]

def word_frequency():
    if not len(sys.argv[1:]):
        print 'USAGE: word_frequency [TEXT_FILE] [...]'
        sys.exit()

    for file in sys.argv[1:]:
        data = open(file, 'r').read()
        words = data.decode('utf8').split()
        for word, count in get_word_count(words):
            print word.encode('utf8'), count

