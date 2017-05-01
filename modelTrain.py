from wikipedia import search, page
from gensim.parsing import PorterStemmer
from gensim.models import Word2Vec
import re



min_count = 1
size = 50
window = 4
 
class StemmingHelper(object):
    """
    Class to aid the stemming process - from word to stemmed form,
    and vice versa.
    The 'original' form of a stemmed word will be returned as the
    form in which its been used the most number of times in the text.
    """
 
    #This reverse lookup will remember the original forms of the stemmed
    #words
    

    
    # with open('machine.txt') as my_file:
    # 	sentences = my_file.readlines()
    	# print (sentences)
    # file1 = open('text/history.txt').read()
    # sentences1 = file1.split('\n')
    # # print (sentences1)
    
    # model1 = Word2Vec(sentences1, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # model1.save('model/historyModel')
    # print (list(model1.wv.vocab.keys()))
    def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
        stopWords = []

        fp = open(stopWordListFileName, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
        return stopWords

    stopWords = []
    featureVector1 = []
    featureVector2 = []
    featureVector3 = []
    featureVector4 = []
    featureVector5 = []
    featureVector6 = []
    featureVector7 = []
    # st = open('stop_words_list.txt', 'r')
    stopWords = getStopWordList('stop_words_list.txt')
    print("stopwords: ", len(stopWords))

    file1 = open('text/bollywood_text.txt').read()
    sentences1 = file1.split('\n')
    voc_vec1 = [s.split() for s in sentences1]
    # print (voc_vec1)
    # print ("\n\n")
    # print (voc_vec1.split())


    for w in voc_vec1:
        # print (w)
        word1 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word1.append(w)
        featureVector1.append(word1)

    # print (featureVector)
    model1 = Word2Vec(featureVector1, min_count=min_count, size=size, window=window, hs=1, negative=0)
    print (list(model1.wv.vocab.keys()))
    model1.save('model/bollywoodModel')
        
    
    file2 = open('text/travel_text.txt').read()
    sentences2 = file2.split('\n')
    voc_vec2 = [s.split() for s in sentences2]
    # print (voc_vec)

    for w in voc_vec2:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word2 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word2.append(w)
        featureVector2.append(word2)

    # print (featureVector)
    model2 = Word2Vec(featureVector2, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model2.save('model/travelModel')
        
    
    file3 = open('text/hollywood_text.txt').read()
    sentences3 = file3.split('\n')
    voc_vec3 = [s.split() for s in sentences3]
    # print (voc_vec)

    for w in voc_vec3:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word3 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word3.append(w)
        featureVector3.append(word3)

    # print (featureVector)
    model3 = Word2Vec(featureVector3, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model3.save('model/hollywoodModel')
        
    
    file4 = open('text/music_text.txt').read()
    sentences4 = file4.split('\n')
    voc_vec4 = [s.split() for s in sentences4]
    # print (voc_vec)

    for w in voc_vec4:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word4 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word4.append(w)
        featureVector4.append(word4)

    # print (featureVector)
    model4 = Word2Vec(featureVector4, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model4.save('model/musicModel')
        
    
    file5 = open('text/politics_text.txt').read()
    sentences5 = file5.split('\n')
    voc_vec5 = [s.split() for s in sentences5]
    # print (voc_vec)

    for w in voc_vec5:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word5 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word5.append(w)
        featureVector5.append(word5)

    # print (featureVector)
    model5 = Word2Vec(featureVector5, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model5.save('model/politicsModel')
        
    
    file6 = open('text/science_text.txt').read()
    sentences6 = file6.split('\n')
    voc_vec6 = [s.split() for s in sentences6]
    # print (voc_vec)

    for w in voc_vec6:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word6 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word6.append(w)
        featureVector6.append(word6)

    # print (featureVector)
    model6 = Word2Vec(featureVector6, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model6.save('model/scienceModel')
        
    
    file7 = open('text/sport_text.txt').read()
    sentences7 = file7.split('\n')
    voc_vec7 = [s.split() for s in sentences7]
    # print (voc_vec)

    for w in voc_vec7:
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        word7 = []
        for w in w:
            # print (w)
        # w = w.strip('\'"?,.')
        # val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            if(w in stopWords):
                continue
            else:
                word7.append(w)
        featureVector7.append(word7)

    # print (featureVector)
    model7 = Word2Vec(featureVector7, min_count=min_count, size=size, window=window, hs=1, negative=0)
    # print (list(model2.wv.vocab.keys()))
    model7.save('model/sportModel')



        
    


    # print (model)
    # vocab = list(model.wv.vocab.keys())
    # print (vocab)
    # 'learn' in model.wv.vocab
    # print (model['learn'])
    # model.save('mymodel')
    # print (model.most_similar("svm"))
    # print (abs(model.score(["minimization statistics classification deep software decreases stanfor"d.split()])))
	