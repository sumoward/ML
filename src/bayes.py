
from sklearn import datasets, svm
import pickle
import json
import numpy as np


class Bayesian():
	#instaniate the class with the test data from sklearn
	def __init__(self, data ={}):
		self.data = data
		self.iris = datasets.load_iris()
		self.digits = datasets.load_digits()

	def parse_data(self):
		pass
	
	#explore sklearn
	def test_data(self):
		print('*'*79)
		#load the iris and digits datasets
		
		#metadata
		print(self.digits['DESCR'])
		#
		print(self.digits.data)
		print(self.digits.target)
		print('*'*79)
		#check dataset size
		print(len(self.digits.images))
		#The data is always a 2D array, n_samples, n_features,
		#although the original data may have had a different shape
		#lest print the last digit
		print(self.digits.images[1796])
		
	def test_Svm(self):
		print('*'*79)
		clf = svm.SVC(gamma=0.001, C=100.)
		print(clf)
		#As a training set, let us use all the images of our dataset apart from the last one:
		fit = clf.fit(self.digits.data[:-1], self.digits.target[:-1])
		print(fit)
		#Now you can predict new values,
		#in particular, we can ask to the classifier what is the digit of our last image in the digits dataset,
		# which we have not used to train the classifier:
		predict = clf.predict(self.digits.data[-1])
		print(predict)
		
	def test_persistence(self):
		print('*'*79)
		clf = svm.SVC()
		X, y = self.iris.data, self.iris.target
		fit = clf.fit(X, y)
		#print(fit)
		#use pickle for persistence
		s = pickle.dumps(clf)
		clf2 = pickle.loads(s)
		proof = clf2.predict(X[0])
		print(proof)
	
	def import_json(self,filename):
		with open('data.json', 'r') as fp:
			data = json.load(fp)
		return data
	#convert student data to a numpy arrays
	def convert_np_array(self, student_data):
		for student, scores in student_data.items():
			#print(type(student_data[student]))
			student_data[student] = np.array(scores)
			#print(type(student_data[student]))
		return 	student_data
	
	def play_numpy(self, student_data):
		print ("student 1:\n", student_data['id_1'])
		#ndarray.ndim -the number of axes (dimensions) of the array.
		print ("ndim ", student_data['id_1'].ndim)
		#ndarray.shape the dimensions of the array.
		print ("shape ", student_data['id_1'].shape)
		#ndarray.size the total number of elements of the array.
		print ("size", student_data['id_1'].size)
		#ndarray.dtype an object describing the type of the elements in the array
		print ("dtype ", student_data['id_1'].dtype)
		#ndarray.itemsize the size in bytes of each element of the array.
		print ("itemsize ", student_data['id_1'].itemsize)
		#ndarray.data the buffer containing the actual elements of the array.
		
	
if __name__ == "__main__":
	
	tester2 = Bayesian()
	#tester2.test_data()
	#tester2.test_Svm()
	#tester2.test_persistence()
	filename = "data.json"
	student_data = tester2 .import_json(filename)
	#print("the data imported from json is :\n", student_data)
	student_data = tester2.convert_np_array(student_data)
	tester2.play_numpy(student_data)
	
	