import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt') # one time execution
nltk.download('stopwords')# one time execution
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
stop_words = stopwords.words('english')
import re
import sys
from operator import itemgetter

class ConversionTool(object):

    def formatSentences(self, content):

        #split message into sentences
        sentences = sent_tokenize(content)

        # remove some punctuations and special characters
        #clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z0-9',.€$£)(]", " ")

        return clean_sentences

class AbusiveLexicon(object):

    theLexDict = {
        "hi":0
    }

    def __init__(self, lexicon):
        self.lexicon = lexicon

    def lexiconDict(lexicon):
        secfile = open('experiment.txt')

        for aline in secfile:
            values = aline.split()
            lexicon.theLexDict[values[0]] = values[1]
            #print("word is ", values[0], " and has a score of ", values[1])

        secfile.close()


def main():

    abusecount = 0.0
    g = input("Enter your phrase : ")

    ct = ConversionTool()

    file = open('SampleFile.txt')

    lines = file.readlines()
    numOfLines = len(lines)

    # checking if file is empty
    if numOfLines <= 0:
        sys.exit("message contains no title/content!")
    else:
        print("hello world")

    al = AbusiveLexicon("lexicon")
    al.lexiconDict()
    for x,y in al.theLexDict.items():
        print(x,y)

    for words in g:
        values = words.split()
        if "horrible" in al.theLexDict.keys():
            print("value = success")

    print(abusecount)


if __name__ == '__main__':
    main()
