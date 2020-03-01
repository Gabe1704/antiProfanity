import nltk
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.stem.porter import PorterStemmer
import pandas as pd
import numpy as np


################################
abuseIndex = 0.00
tokensInput = input("Enter your phrase : ")

tokens = word_tokenize(tokensInput)
tokens = [w for w in tokens if not w in stop_words]

porter = PorterStemmer()
stems = []

for t in tokens:
    stems.append(porter.stem(t))

##########

df = pd.read_csv('experiment.csv')
df = df.drop_duplicates(subset = 'word')
print(df.head(15))

##########
print(tokens)
print(stems)
###########

for part in tokens:
    df_a = df[df["word"] == part]
    df_aIndex = df_a.index
    abuseIndex = abuseIndex + float(df.iloc[df_aIndex]["counter"])
print ("counter is", abuseIndex)
