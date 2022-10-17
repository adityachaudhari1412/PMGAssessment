import sys
import pandas as pd
import unittest
from csvCombiner import CSVCombiner
from io import StringIO
import warnings
class Unit_TestMethod(unittest.TestCase):

    resultPath = "./test_output.csv"
    csvCombinerPath = "./csvCombiner.py"
    accessoriesPath = "./fixtures/accessories.csv"
    clothingPath = "./fixtures/clothing.csv"
    householdPath="./fixtures/household_cleaners.csv"
    emptyFilePath = "./empty.csv"
    testResultFile = None
    csvCombinerClassObj = CSVCombiner()

    @classmethod      
    def setUp(self):
        self.result = StringIO()
        sys.stdout = self.result
        self.testResultFile = open(self.resultPath, 'w+', encoding="utf-8")
        if not sys.warnoptions:
            warnings.simplefilter("ignore")
            
    def testNumOfColumns(self):
   
        accessoriesDataFrame = pd.read_csv(self.accessoriesPath, lineterminator='\n')
        clothingDataFrame = pd.read_csv(self.clothingPath, lineterminator='\n')
        householdDataFrame = pd.read_csv(self.householdPath, lineterminator='\n')
        self.assertEqual(len(accessoriesDataFrame.columns), len(clothingDataFrame.columns))
        self.assertEqual(len(clothingDataFrame.columns), len(householdDataFrame.columns))
        self.assertEqual(len(householdDataFrame.columns), len(accessoriesDataFrame.columns))
        
    
    
    def testWithWrongPath(self):
       
        argv = [self.csvCombinerPath, "no_file.csv"]
        self.assertRaises(FileNotFoundError, lambda: self.csvCombinerClassObj.csvCombiner(argv))

 
    def testWithoutFile(self):
        argv = [self.csvCombinerPath]
        self.assertRaises(ValueError, lambda: self.csvCombinerClassObj.csvCombiner(argv))


    def testWithEmptyFile(self):
        argv = [self.csvCombinerPath, self.emptyFilePath]
        self.assertRaises(ValueError, lambda: self.csvCombinerClassObj.csvCombiner(argv))

