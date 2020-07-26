from dynamicSalesman import Subst,InputGraph,graphicsLine,graphicsLineInd
import math


class TSP:


	def __init__(self):
		self.n = len(InputGraph)
		self.C = [[-1 for i in range(self.n)] for j in range(pow(2,self.n))]
		self.VISITED_ALL = pow(2,self.n)-1


	def naive(self,mask,pos):
		if(mask==self.VISITED_ALL):
			return Subst[pos][0]

		if(self.C[mask][pos]!=-1):
			return self.C[mask][pos]

		ans = 2147483647

		for city in range(1,self.n):

			if(mask&(1<<city)==0):
				mask= (mask|(1<<city))
				newAns = Subst[pos][city]+self.naive(mask,pos)
				ans = min(ans,newAns)

		self.C[mask][pos]=ans
		return self.C[mask][pos]


	def callNaive(self):

		#print("Naive=",self.naive(0,0))
		pass



