from sklearn import svm
import numpy as np
import os
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.grid_search import GridSearchCV
import pickle
import matplotlib
import matplotlib.pyplot as plt

def getData():
	path1="C:\\Users\\acer\\Desktop\\PRtest\\PR_dataset\\PR_dataset\\train\\neg"
	path2="C:\\Users\\acer\\Desktop\\PRtest\\PR_dataset\\PR_dataset\\train\\pos"
	pathTest1="C:\\Users\\acer\\Desktop\\PRtest\\PR_dataset\\PR_dataset\\test\\pos"
	pathTest2="C:\\Users\\acer\\Desktop\\PRtest\\PR_dataset\\PR_dataset\\test\\neg"
	train_sample=[]
	train_label=[]
	test_sample=[]
	test_label=[]
	#save1="C:\\Users\\acer\\Desktop\\PRtest\\train_data.txt"
	#save2="C:\\Users\\acer\\Desktop\\PRtest\\test_negdata.txt"
	#save3="C:\\Users\\acer\\Desktop\\PRtest\\test_posdata.txt"
	#savelabel="C:\\Users\\acer\\Desktop\\PRtest\\label_data.txt"
	
	for temp in os.listdir(path1):
		List=[]
		#print(path+"\\"+temp+"\n")
		newpath=path1+"\\"+temp
		for line in open(newpath):
			List.append(line.strip())
		train_sample.append(np.array(List,dtype=float))
		train_label.append(-1)
	
	for temp in os.listdir(path2):
		List=[]
		#print(path+"\\"+temp+"\n")
		newpath=path2+"\\"+temp
		for line in open(newpath):
			List.append(line.strip())
		train_sample.append(np.array(List,dtype=float))
		train_label.append(1)
	
	for temp in os.listdir(pathTest1):
		List=[]
		#print(path+"\\"+temp+"\n")
		newpath=pathTest1+"\\"+temp
		for line in open(newpath):
			List.append(line.strip())
		test_sample.append(np.array(List,dtype=float))
		test_label.append(1)
	
	for temp in os.listdir(pathTest2):
		List=[]
		#print(path+"\\"+temp+"\n")
		newpath=pathTest2+"\\"+temp
		for line in open(newpath):
			List.append(line.strip())
		test_sample.append(np.array(List,dtype=float))
		test_label.append(-1)
	
	#np.savetxt("train_data.txt",np.array(train_sample))
	#np.savetxt("label_data.txt",np.array(train_label))
	#np.savetxt("test_posdata.txt",np.array(test_sample))
	#np.savetxt("test_negdata.txt",np.array(test_sample1))
	return np.array(train_sample),np.array(train_label),np.array(test_sample),np.array(test_label)
	#return np.array(train_negsample),np.array(train_possample),np.array(train_neglabel),np.array(train_poslabel)
	
#通过调不同的gama值来画出训练值和测试纸的曲线
def plot_val_curve(features, labels, model):
    p_range = np.logspace(-5, 5, 5)
    train_scores, test_scores = validation_curve(
        model, features, labels, param_name='gamma', param_range=p_range,
        cv=6, scoring='accuracy', n_jobs=1
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.title('Validation Curve')
    plt.xlabel('$\gamma$')
    plt.ylabel('Score')
    plt.semilogx(p_range, train_scores_mean, label='Training score', color='#E29539')
    plt.semilogx(p_range, test_scores_mean, label='Cross-validation score', color='#94BA65')
    plt.legend(loc='best')
    plt.show()
	
def plot_val_curve_C(features, labels, model):
    C_range = np.logspace(-2, 10, 5)
    train_scores, test_scores = validation_curve(
        model, features, labels, param_name='C', param_range=C_range,
        cv=6, scoring='accuracy', n_jobs=1
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.title('Validation Curve')
    plt.xlabel('$\gamma$')
    plt.ylabel('Score')
    plt.semilogx(C_range, train_scores_mean, label='Training score', color='#E29539')
    plt.semilogx(C_range, test_scores_mean, label='Cross-validation score', color='#94BA65')
    plt.legend(loc='best')
    plt.show()	
	
def visual_gridsearch(model, X, y):
    C_range = np.logspace(-2, 10, 5)
    gamma_range = np.logspace(-5, 5, 5)
    param_grid = dict(gamma=gamma_range, C=C_range)
    grid = GridSearchCV(model, param_grid=param_grid)
    grid.fit(X, y)
    scores = [x[1] for x in grid.grid_scores_]
    scores = np.array(scores).reshape(len(C_range), len(gamma_range))
    plt.figure(figsize=(8, 6))
    plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
    plt.imshow(scores, interpolation='nearest', cmap=ddlheatmap)
    plt.xlabel('gamma')
    plt.ylabel('C')
    plt.colorbar()
    plt.xticks(np.arange(len(gamma_range)), gamma_range, rotation=45)
    plt.yticks(np.arange(len(C_range)), C_range)
    plt.title(
        "The best parameters are {} with a score of {:0.2f}.".format(
        grid.best_params_, grid.best_score_)
    )
    plt.show()
	
	
#预测错误曲线
def error_compare_three(model,X,y):
	predicted = cross_val_predict(model, X, y, cv=6)
	fig=plt.figure()
	ax=fig.add_subplot(111)
	ax.scatter(y, predicted, c='#F2BE2C')
	ax.set_title('Prediction Error for SVR')
	ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4, c='#2B94E9')
	ax.set_ylabel('Predicted')
	plt.xlabel('Measured')
	plt.show()

if __name__=='__main__':
	
	'''
	train_sample,train_label,test_sample,test_label=getData()
	print(train_sample.shape,test_sample.shape)
	print(train_label,test_label)
	f_data=open('dataSet.pkl','wb')
	pickle.dump(train_sample,f_data,True)
	pickle.dump(train_label,f_data,True)
	pickle.dump(test_sample,f_data,True)
	pickle.dump(test_label,f_data,True)
	f_data.close()
	'''
	
	f_data=open('dataSet_norm.pkl','rb')
	train_sample=pickle.load(f_data)
	train_label=pickle.load(f_data)
	test_sample=pickle.load(f_data)
	test_label=pickle.load(f_data)
	f_data.close()
	print('训练集特征')
	print(train_sample.shape)
	print(train_sample)
	print('训练集标签')
	print(train_label)
	print('测试集特征')
	print(test_sample.shape)
	print(test_sample)
	print('测试集标签')
	print(test_label)
	
	#pca=PCA(n_components=2)
	#train_sample_pca=pca.fit_transform(train_sample)
	#test_sample_pca=pca.fit_transform(test_sample)
	
	#print(train_sample_pca)
	#fig=plt.figure()
	#ax1=fig.add_subplot(211)
	#ax1.set_title('train_sample data_view')
	#ax1.scatter(train_sample_pca[:10054,0],train_sample_pca[:10054,1],marker='^')
	#ax1.scatter(train_sample_pca[10055:,0],train_sample_pca[10055:,1],marker='o',c='red')
	#ax2=fig.add_subplot(212)
	#ax2.set_title('test_sample data_view')
	#ax2.scatter(test_sample_pca[2043:,0],test_sample_pca[2043:,1],marker='^')
	#ax2.scatter(test_sample_pca[:2042,0],test_sample_pca[:2042,1],marker='o',c='red')
	#plt.show()
	
	#train_sample_norm=preprocessing.scale(train_sample)
	#test_sample_norm=preprocessing.scale(test_sample)
	#scaler=preprocessing.StandardScaler().fit(train_sample)
	#train_sample_norm=scaler.transform(train_sample)
	#test_sample_norm=scaler.transform(test_sample)
	
	#f_data=open('dataSet_norm.pkl','wb')
	#pickle.dump(train_sample_norm,f_data,True)
	#pickle.dump(train_label,f_data,True)
	#pickle.dump(test_sample_norm,f_data,True)
	#pickle.dump(test_label,f_data,True)
	#f_data.close()
	
	
	#count=0
	#sum=0
	#svr=svm.SVC(kernel='rbf',C=2)
	print("******训练集******")
	print(train_sample,train_label)
	print("\n")
	print("*******开始训练********")
	print("\n")
	#score=cross_val_score(svr,train_sample,train_label,cv=4)
	#pre_Test=svr.fit(train_sample,train_label).predict(test_sample)
	#joblib.dump(svr,"train_model.pkl")
	print("*********训练成功*************")
	
	#svr=joblib.load("train_model.pkl")
	
	#error_compare_three(svr,test_sample,test_label)
	#plot_val_curve(test_sample,test_label,svr)
	#plot_val_curve_C(test_sample,test_label,svr)
	visual_gridsearch(svm.SVC(),train_sample,train_label)
	
	#score=cross_val_score(svr,train_sample,train_label,cv=8)
	
	#pre_Test=svr.predict(test_sample)
	#print('查准率：')
	#print(precision_score(test_label,pre_Test))
	#print('召回率：')
	#print(recall_score(test_label,pre_Test))
	#np.set_printoptions(threshold=np.inf)
	#print(pre_Test)
	#accuracy=accuracy_score(test_label,pre_Test)
	#for data in pre_Test:
		#sum += 1
		#if data==1:
			#count += 1
	#print(count)
	#print(sum)
	#print(score)
	#print('训练集的8折交叉验证：')
	#print(score)
	#print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
	
