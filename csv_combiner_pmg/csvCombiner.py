#Aditya Ramdas Chaudhari
#PMG Graduate LEadership Program 2023 
#chaudhariaditya1412@gmail.com
#469-345-9279

import sys
import pandas as pd
import os
from pathlib import Path

class CSVCombiner:
    """
        Validating the given arguments(is, extensions)
    """
    def Arguments(self, argv):
        
       # Csv myFile to process are listed after the name of the python file in the specified arguments.
#It should be provided with at least two arguments and at least one csv file to process.
        myFile = argv[1:]        
        
        if (len(argv)) < 2:
            raise ValueError("Argument was empty, please try again with file")

        for i in myFile:
            #validating the path 
            get_i = Path(i)
           
            if not get_i.exists():
                raise FileNotFoundError("No file found in the path")

            iWithoutExtension, iExtension = os.path.splitext(i)
            #file extension validation- to check if they are csv myFile
            if iExtension != ".csv":
                raise Exception("The file"+ str(iWithoutExtension)+ " is not in csv format")
                
            #File should not be empty
            infile = pd.read_csv(get_i)                  
            if infile.empty :
                raise ValueError("CSV file empty")
            
    """
        combining  the rows of csv file 
        """                       
    def csvCombiner(self, argv: list):
        
        myFile = argv[1:]
        # validating the arguments
        self.Arguments(argv)
    
        
        #To prevent memory-related problems, utilize default
        #  size of 10*5, and alter as necessary.

        
        notConcatenated = []
        
        #list of data frames that will contain all input myFile merged 
        for i in myFile:
            List = []  #To add each value
            file = pd.read_csv(i,chunksize=10000)
            #reading the data from the file

            for j in file:
                # this will have list of chuck
                j['filename'] = i.split('/')[-1]
                #splitting and creating filename 
                List.append(j)

            notConcatenated.append(pd.concat(List))
            
        outputFile = pd.concat(notConcatenated, ignore_index = True)
        
        #writing to output file
        outputFile.to_csv(sys.stdout,index=False,line_terminator='\n')
                
def main():
    csv = CSVCombiner() 
    
    #combining the myFile
    csv.csvCombiner(sys.argv)
    
  #main method call   
if __name__ == '__main__':
    main() 
    
    