import pickle

#Pickel Loading Trained Model
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

#Input
testSentence = "idk how to feel about these bandwagon stans like i'm glad that J is adored by the GP again but im gonna need some of these hoes to fall back"
classification = loaded_model.classify(testSentence)

#Output
print "\n"
print " Sarcasm Sentiment Detection ".center(50,'-')
print "\n"
print "Sentence: "+testSentence
if (classification[0][0]=='1'):
    print "\nResult : Sarcastic"
else: print "\nResult : Not Sarcastic"
print "\n"