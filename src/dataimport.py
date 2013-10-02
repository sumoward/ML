
'''
Created on 2 Oct 2013

@author: Brian
'''

class Data_Import:
    #read in datset
    def readin(self, file_in):
        self.file = file_in
        #print (self.file)
        self.holder = open(self.file, 'r',encoding='utf-8')#encoding='iso-8859-1'??
        #print(self.holder)
        self.data_structure = []
        self.alternate_data_structure = {}
        print(self.data_structure)
        return self.holder
    
    # function to print out result
    def writeout(self, filename):
        self.file
        for row in self.holder:
            #print(row)
            if row[:2] =='id':
                print('data is : ' + row[5:-1])
                self.data_structure.append(row[5:-1])
                #lets see if a dictionary is a better data structure
                self.alternate_data_structure[row[:4]] = row[5:-1]
                
        print(self.data_structure) 
        print(self.alternate_data_structure)
        
        
if __name__ == "__main__":
    tester1 = Data_Import()
    file_in = "jamestestcase1.csv"
    tester1.readin(file_in)
    file_out ="output.txt"
    tester1.writeout(file_out)
