
from sklearn import datasets, svm
import pickle


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
		
	
if __name__ == "__main__":
	
	tester2 = Bayesian()
	#tester2.test_data()
	#tester2.test_Svm()
	tester2.test_persistence()
	
	