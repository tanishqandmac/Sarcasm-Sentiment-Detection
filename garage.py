import pickle
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def datasetDictCreation(filename):
    SCount = 0.0
    NCount = 0.0
    f = open(filename)
    for sentence in f:
        sentenceToken = sentence.split('\t')
        try:
            sentenceDictionary.append({'text':sentenceToken[2].encode('utf8'),'category':sentenceToken[1]})
            if(sentenceToken[1]=="0"):
                SCount+=1.0
            else:
                NCount+=1.0
        except:
            continue
    return sentenceDictionary,SCount,NCount

#Variable Declaration
sentenceDictionary = []
SCount = 0.0
NCount = 0.0
filename = 'trainedDataset.tsv'

#Dataset to Dictionary Mapping
sentenceDictionary,SCount,NCount = datasetDictCreation(filename)

for a in sentenceDictionary:
    if(a['category']=="0"):
        print(a['text'])

'''
f = open("Files/neg.txt","w")
for a in sentenceDictionary:
    if(a['category']=="0"):
        f.write(a['text'])
f.close()

f = open("Files/pos.txt","w")
for a in sentenceDictionary:
    if(a['category']=="1"):
        f.write(a['text'])
f.close()
'''
