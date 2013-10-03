
'''
Created on 2 Oct 2013

@author: Brian
'''
import json

class Data_Import:
    #read in datset
    def readin(self, file_in):
        self.file = file_in
        self.holder = open(self.file, 'r',encoding='utf-8')#encoding='iso-8859-1'??
        self.array_holder = []
        self.data_dictionary = {}
        return self.holder
    
    # function to print out result
    def writeout(self, filename):
        self.file
        check="xxx"
        for row in self.holder:
            ident = self.identifier(row)
            start = len(ident) + 1
            snippet = row[start:-1]
            snippet = self.parse_snippet(snippet)
            #if new student
            if check not in row:
                self.array_holder =[]
                check = ident
                
                self.array_holder.append(snippet) 
            else:    
                self.array_holder.append(snippet)   
                #store the multidimensional array as a value in a dictionary
            self.data_dictionary[ident] = self.array_holder
        #output to json file for testing 
        print(self.data_dictionary)
        out = open(filename, 'w')
        json.dump(self.data_dictionary, out)
        print("data imported to Dictionary")         
        return self.data_dictionary
    #the student identifier at the start of the row 
    def identifier(self, row):
        loc = row.find(',')
        return row[:loc]
    
    def parse_snippet(self, snippet):
        snippet = snippet.split(',')
        print (snippet)
        #convert string into arrayand add to 2 d array
        snippet = list(map(int,snippet))
        print(snippet)
        return snippet
               
if __name__ == "__main__":
    tester1 = Data_Import()
    file_in = "jamestestcase1.csv"
    tester1.readin(file_in)
    file_out ="data.json"
    data = tester1.writeout(file_out)
    for student, scores in data.items():
        print (student, scores)
    
