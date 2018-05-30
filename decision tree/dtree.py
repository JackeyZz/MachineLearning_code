import numpy as np
import math

def calcShannonEnt(dataSet):
	'''
	计算标签香农熵
	'''
	numEntries=len(dataSet)
	labelCounts={}
	for featVec in dataSet: #遍历每个实例，统计标签的频数
		currentLabel=featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel]=0
		labelCounts[currentLabel]+=1
	shannonEnt=0.0
	for key in labelCounts:
		prob=float(labelCounts[key])/numEntries
		shannonEnt -=prob*math.log(prob,2)
	return shannonEnt

def splitDataSet(dataSet,axis,value):
	'''
	按照给定特征划分数据集
	:param dataSet:待划分的数据集
    :param axis:划分数据集的特征
    :param value: 需要返回的特征的值
    :return: 划分结果列表
	'''
	retDataSet=[]
	for featVec in dataSet:
		if featVec[axis]==value:
			reducedFeatVec=featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
	
def calcConditionalEntropy(dataSet,i,featList,uniqueVals):
	'''
	计算X_i给定的条件下，Y的条件熵
	:param dataSet:数据集
    :param i:维度i
    :param featList: 数据集特征列表
    :param uniqueVals: 数据集特征集合
    :return: 条件熵
	'''
	conditionEnt=0.0
	for value in uniqueVals:
		subDataSet=splitDataSet(dataSet,i,value)
		prob=len(subDataSet)/float(len(dataSet))
		conditionEnt += prob*calcShannonEnt(subDataSet)
	return conditionEnt
	
def calcInformationGain(dataSet,baseEntropy,i):
	'''
    计算信息增益
    :param dataSet:数据集
    :param baseEntropy:数据集的信息熵
    :param i: 特征维度i
    :return: 特征i对数据集的信息增益g(D|X_i)
    '''
	featList=[example[i] for example in dataSet]
	uniqueVals=set(featList)
	newEntropy=calcConditionalEntropy(dataSet,i,featList,uniqueVals)
	infoGain=baseEntropy-newEntropy
	return infoGain
	
def calcInformationGainRatio(dataSet,baseEntropy,i):
	'''
    计算信息增益比
    :param dataSet:数据集
    :param baseEntropy:数据集的信息熵
    :param i: 特征维度i
    :return: 特征i对数据集的信息增益比gR(D|X_i)
    '''
	return calcInformationGain(dataSet,baseEntropy,i)/baseEntropy

def chooseBestFeatureToSplitByID3(dataSet):
	'''
    选择最好的数据集划分方式
    :param dataSet:数据集
    :return: 划分结果
    '''
	numFeatures=len(dataSet[0])-1
	baseEntropy=calcShannonEnt(dataSet)
	bestInfoGain=0.0
	bestFeature=-1
	for i in range(numFeatures):
		infoGain=calcInformationGain(dataSet,baseEntropy,i)
		if(infoGain>bestInfoGain):
			bestInfoGain=infoGain
			bestFeature=i
	return bestFeature

def majorityCnt(classList):
	'''
    采用多数表决的方法决定叶结点的分类
    :param: 所有的类标签列表
    :return: 出现次数最多的类
    '''
	classCount={}
	for vote in classList:
		if vote not in classList.keys():
			classCount[vote]=0
		classCount[vote] += 1
	sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
	
def createTree(dataSet,labels):
	'''
    创建决策树
    :param: dataSet:训练数据集
    :return: labels:所有的类标签
    '''
	classList=[example[-1] for example in dataSet]
	if classList.count(classList[0])==len(classList):
		return classList[0]
	if len(dataSet[0])==1:
		return majorityCnt(classList)
	bestFeat=chooseBestFeatureToSplitByID3(dataSet)
	bestFeatLabel=labels[bestFeat]
	myTree={bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues=[example[bestFeat] for example in dataSet]
	uniqueVals=set(featValues)
	for value in uniqueVals:
		subLabels=labels[:]
		myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree
	
	
	
	
	
	
	
	
	