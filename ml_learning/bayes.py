from numpy import *
def loadDataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],\
                 ['maybe','not','take','him','to','dog','park','stupid'],\
                 ['my','dalmation','is','so','cute','I','love','him'],\
                 ['stop','posting','stupid','worthless','garbage'],\
                 ['mr','licks','ate','my','steak','how','to','stop','him'],\
                 ['quit','buying','worthless','dog','food','stupid']]
    listClass=[0,1,0,1,0,1]#1代表存在侮辱性的文字,0代表不存在
    return postingList,listClass
#将所有文档所有词都存在一个列表里，用set（）函数去除重复出现的单词
def createNonRepeatedList(dataSet):
    vocSet=set([])
    for doc in dataSet:
        vocSet=vocSet|set(doc)#两个集合和在一起
    return list(vocSet)
def setOfWords2Vec(vocList,inputSet):
    returnVec=[0]*len(vocList)
    for word in inputSet:
        if word in vocList:
            returnVec[vocList.index(word)]=1
        else:
            print('the word:%s is not in the vocabulary' % word)
    return returnVec
def trainNBo(trainMatrix,trainCategory):#trainCategory是句子的标签（侮辱性、非侮辱行）trainMatrix是一个list
    numTrainDocs=len(trainMatrix)#在这个文档里有多少句话
    numWords=len(trainMatrix[0])#单词表的长度
    pAb=sum(trainCategory)/float(numTrainDocs)#侮辱性句儿的比例
    # p0Num=zeros(numWords)
    # p1Num=zeros(numWords)
    # p0Denom=0.0
    # p1Denom=0.0
    p0Num=ones(numWords)
    p1Num=ones(numWords)
    p0Denom=2.0
    p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:#numTrainDocs的长度和trainCategory的长度相同都是句子的个数
            p1Num +=trainMatrix[i]#就是侮辱性句子单词出现的个数
            p1Denom +=sum(trainMatrix[i])#句子里单词的数量
        else:
            p0Num +=trainMatrix[i]
            p0Denom +=sum(trainMatrix[i])
    p1Vect=log(p1Num/p1Denom)
    p0Vect=log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAb
def classifyNB(vec2Classify,p0Vec,p1Vec,pAb):
    p1=sum(vec2Classify*p1Vec)+log(pAb)
    p0=sum(vec2Classify*p0Vec)+log(1-pAb)
    if p1>p0:
        return 1
    else:
        return 0
def testingNB():
    listOPosts,listClasses=loadDataSet()
    myVocabList=createNonRepeatedList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb=trainNBo(array(trainMat),array(listClasses))
    testEntry=['love','my','dalmation']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as：',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry=['stupid','garbage']
    thisDoc=array(setOfWords2Vec(myVocabList,testEntry))
    print (testEntry,'classified as：',classifyNB(thisDoc,p0V,p1V,pAb))
def bagOfWords2VecMN(vocabList,inputSet):#文档词袋模型
    returnVec=[0]*len(vocabList)
    for i in inputSet:
        if i in vocabList:
            returnVec[vocabList.index(i)]+=1
    return returnVec
def textParse(bigString):
    import re
    listOfTokens=re.split(r'\W*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]
def spamTest():
    docList=[];classList=[];fullTest=[]
    for i in range(1,26):
        wordList=textParse(open('email/spam/%d.txt'% i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(1)
        wordList=textParse(open('email/ham/%d.txt'% i).read())
        docList.append(wordList)
        fullTest.extend(wordList)
        classList.append(0)
    vocabList=createNonRepeatedList(docList)
    trainingSet=list(range(50))
    testSet=[]
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]
    trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pAb=trainNBo(array(trainMat),array(trainClasses))
    errorCount=0
    for docIndex in testSet:
        wordVector=bagOfWords2VecMN(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pAb)!=classList[docIndex]:
            errorCount+=1
            print ("classification error", docList[docIndex])
    print('the error rate is:',float(errorCount)/len(testSet))





