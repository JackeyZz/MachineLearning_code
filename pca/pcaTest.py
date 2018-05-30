from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def loadDataSet(fileName,delim='\t'):
	fr=open(fileName)
	stringArr=[line.strip().split(delim) for line in fr.readlines()]
	datArr=[list(map(float,line)) for line in stringArr]
	return mat(datArr)

def pca(dataMat,topNfeat=9999999):
	meanVals=mean(dataMat,axis=0)  ##axis的值表示哪一维度压缩为1.=0时表示输出一行，每一列的平均值
	meanRemoved=dataMat-meanVals   ##减去平均值
	covMat=cov(meanRemoved,rowvar=0)  ##协方差
	eigVals,eigVects=linalg.eig(mat(covMat))  ##特征值和特征向量
	eigValInd=argsort(eigVals)    ##特征值排序从小到大
	eigValInd=eigValInd[:-(topNfeat+1):-1]   
	redEigVects=eigVects[:,eigValInd]   ##前topNfeat个特征及特征向量
	lowDDataMat=meanRemoved*redEigVects  
	reconMat=(lowDDataMat*redEigVects.T)+meanVals
	return lowDDataMat,reconMat

if __name__=="__main__":
	dataMat=loadDataSet("testSet.txt")
	print(dataMat)
	lowDMat,reconMat=pca(dataMat,1)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(dataMat[:,0].flatten().A[0],dataMat[:,1].flatten().A[0],marker='^',s=90)
	ax.scatter(reconMat[:,0].flatten().A[0],reconMat[:,1].flatten().A[0],marker='o',s=50,c='red')
	plt.show()
	