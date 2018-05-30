from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation
from keras.optimizers import SGD
from keras.datasets import mnist

import numpy as np

if __name__=="__main__":
	np.random.seed(1)

	model = Sequential()
	##
	model.add(Dense(4000,kernel_initializer='glorot_uniform',input_shape=(2330,)))
	model.add(Activation('tanh'))
	model.add(Dropout(0.5))

	model.add(Dense(4000,kernel_initializer='glorot_uniform',))
	model.add(Activation('tanh'))
	model.add(Dropout(0.5))

	#输出结果是10个类别，所以维度是10
	model.add(Dense(1,kernel_initializer='glorot_uniform',))
	#最后一层用softmax
	model.add(Activation('softmax'))

	model.summary()
	#设定训练参数
	sgd = SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)

	#使用交叉熵损失函数
	model.compile(loss='sparse_categorical_crossentropy',
				  optimizer=sgd,metrics=['accuracy'])

	#准备数据
	#(X_train,y_train),(X_test,y_test) = mnist.load_data()
	#转换数据维度
	#X_train = X_train.reshape(X_train.shape[0],X_train.shape[1]*X_train.shape[2])
	#X_test = X_test.reshape(X_test.shape[0],X_test.shape[1]*X_test.shape[2])

	print("加载数据")
	train_sample=np.loadtxt("train_data.txt")
	label=np.loadtxt("label_data.txt")
	test_negsample=np.loadtxt("test_negdata.txt")
	print(train_sample,label)
	
	#转换数据标签
	#Y_train = (np.arange(10)==y_train[:,None]).astype(int)
	#Y_test = (np.arange(10)==y_test[:,None]).astype(int)
	'''
	print Y_train.shape
	print Y_test.shape
	print Y_train[0]
	print X_train[0].shape
	'''
	model.fit(train_sample,label,batch_size=128,epochs=6)
	print('test set')
	#loss,accu = model.evaluate(X_test,Y_test,batch_size=100,verbose=1)
	#print(loss,accu) 