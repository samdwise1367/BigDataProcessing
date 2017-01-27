import pandas as pd
import numpy as np

class DataProcessing:

	def process(self,ls):
		df1 = pd.read_csv('##csv file here',encoding="ISO-8859-1")
		df = df1.replace(np.nan, ' ', regex=True)
		
		uniqueList = self.list_duplicates(ls) #get unique list elements
		
		lengthValue = len(uniqueList)
		
		if lengthValue == 1:
			dfSub = df.loc[(df['Subject type']== uniqueList[0]) & (df['Object type']== uniqueList[0])]
			return dfSub
		elif lengthValue == 2:
			dfSub = df.loc[((df['Subject type']== uniqueList[0]) & (df['Object type']== uniqueList[1])) | ((df['Subject type']== uniqueList[1]) & (df['Object type']== uniqueList[0]))]
			return dfSub
		elif lengthValue == 3:
			dfSub = df.loc[((df['Subject type']== uniqueList[0]) & (df['Object type']== uniqueList[1])) | ((df['Subject type']== uniqueList[1]) & (df['Object type']== 
				uniqueList[0])) | ((df['Subject type']== uniqueList[0])& (df['Object type']== uniqueList[2])) | ((df['Subject type']== uniqueList[2])& (df['Object type']== uniqueList[0]))|
				((df['Subject type']== uniqueList[1])& (df['Object type']== uniqueList[2])) | ((df['Subject type']== uniqueList[2])& (df['Object type']== uniqueList[1]))]
			return dfSub
		return None
	def list_duplicates(self,seq):
		myset = set(seq)
		return list( myset )
		
getData = DataProcessing()
getData.process("drug/chemical compound")
