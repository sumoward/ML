from src.dataimport import Data_Import
from src.bayes import Bayesian


class ML:
    
    def calc(self):
        
        #call dataimport
        tester1 = Data_Import()
        file_in = "jamestestcase1.csv"
        tester1.readin(file_in)
        file_out = "output.txt"
        tester1.writeout(file_out)
        
        #call bayesian calculation
        tester2  = Bayesian()
        
        
if __name__ == "__main__":
    ML1 = ML()