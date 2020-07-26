
import math
#from time import sleep,clock
import threading
import random
import sys
from collections import namedtuple
from math import sqrt
from collections import namedtuple
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.button import Button
from kivy.clock import Clock   

''' 

GRAPH is in form of ADJENCY MATRIX
	

	Implimentation is of Christofides Algorithm


	1- Create minimum Spanning Tree 'T' of graph 'G'

	2- O is set of odd vertices, |O| is even

	3- Find a minimum weight 'perfect matching' 'M' in the 'induced subgraph'
			given by the vertices from 'O'

	4- Combine 'M' and 'T' to form a connected multigraph 'H'

	5- Form an Eulerian Circuit in 'H'

	6- Make the circuit found in previous step into Hamiltonian circuit by shortcutting

'''


Edge = namedtuple('Edge',['u','v','weight'])
pixel = namedtuple("pixel",['x','y','d'])
d=12
Subst = []
InputGraph = []
allPosGraph=[]
graphicsLine = []
graphicsTriangle = []
graphicsTriangleInd = 0
graphicsLineInd = 0

class edge:

	def __init__(self,anEdge):
		self.anEdge = anEdge

	def __gt__(self,other):
		return self.anEdge.weight>other.anEdge.weight

	def __lt__(self,other):
		return self.anEdge.weight<other.anEdge.weight

	def __eq__(self,other):
		return self.anEdge.weight==other.anEdge.weight


class graph():

	def __init__(self,A,**kwargs):
		super().__init__(**kwargs)
		self.Adj = A
		self.edges = []

	def initEdges(self):
		for i in range(len(self.Adj)):
			for j in range(len(self.Adj[i])):
				self.edges.append(edge(Edge(i,j,self.Adj[i][j])))
				ai=InputGraph[i].p.x + InputGraph[i].p.d/2
				bi=InputGraph[i].p.y + InputGraph[i].p.d/2
				ci=InputGraph[j].p.x + InputGraph[j].p.d/2
				di=InputGraph[j].p.y + InputGraph[j].p.d/2
				#Line(points=[ai,bi,ci,di],width=1)
				graphicsLine.append([(0,0,0),[ai+allPosGraph[0][0],bi-allPosGraph[0][1],ci+allPosGraph[0][0],di-allPosGraph[0][1]],1])
				graphicsLine.append([(0,0,0),[ai+allPosGraph[1][0],bi-allPosGraph[1][1],ci+allPosGraph[1][0],di-allPosGraph[1][1]],1])
				graphicsLine.append([(0,0,0),[ai+allPosGraph[2][0],bi-allPosGraph[2][1],ci+allPosGraph[2][0],di-allPosGraph[2][1]],1])
				graphicsLine.append([(0,0,0),[ai+allPosGraph[3][0],bi-allPosGraph[3][1],ci+allPosGraph[3][0],di-allPosGraph[3][1]],1])
				#self.canvas.Refresh()

		self.edges = sorted(self.edges)



class union:

	def __init__(self,n):
		self.parent = [0 for i in range(n)]
		self.rank = [0 for i in range(n)]

	def makeSet(self,v):
		self.parent[v]=v
		self.rank[v]=0

	def findSet(self,v): # Recursive algorithm to find Parent in disjoint set structure
		if(v== self.parent[v]):
			return v
		return self.findSet(self.parent[v]);

	def unionSets(self,a,b):
		a= self.findSet(a)
		b= self.findSet(b)

		if(a!=b):
			if(self.rank[a]<self.rank[b]):
				a,b = b,a

			self.parent[b]=a

			if(self.rank[a]==self.rank[b]):
				self.rank[a]+=1




class spantheTree(Widget):   #Krushal's algorithm with union by rank.
	
	def __init__(self,gra,**kwargs):
		super().__init__(**kwargs)
		self.graph = gra
		self.n = len(self.graph.Adj)
		self.set = union(self.n)
		self.cost = 0
		self.result = []

		for i in range(self.n):
			self.set.makeSet(i)



	def solve(self):

		
		for every in self.graph.edges:
			
			if(self.set.findSet(every.anEdge.u)!=self.set.findSet(every.anEdge.v)):
				self.cost+=every.anEdge.weight

				self.result.append(every.anEdge)
				ai=InputGraph[every.anEdge.u].p.x + d/2
				bi=InputGraph[every.anEdge.u].p.y + d/2
				ci=InputGraph[every.anEdge.v].p.x + d/2
				di=InputGraph[every.anEdge.v].p.y + d/2

				#Line(points=[ai,bi,ci,di],width=2)
				graphicsLine.append([(.20,.72,.11),[ai,bi,ci,di],2])


				self.set.unionSets(every.anEdge.u,every.anEdge.v)


		with self.canvas:
			Button(text="%d" % self.cost)


		return self.result


class subgraphInduced:

	def __init__(self,Tree):
		self.tree = Tree
		self.MST=[]
		self.edgesInduced = []
		deg = {}
		self.matching = []
		for every in Tree:
			if every.u not in deg.keys():
				deg[every.u]=0

			if every.v not in deg.keys():
				deg[every.v]=0

			deg[every.u]+=1
			deg[every.v]+=1

		for every in deg:
			if(deg[every]%2!=0):
				self.matching.append(every)


	def toDraw(self):

		for each in self.matching:
			for every in self.matching:
				if(each!=every):
					self.edgesInduced.append((each,every))
					ai=InputGraph[every].p.x + d/2
					bi=InputGraph[every].p.y + d/2
					ci=InputGraph[each].p.x + d/2
					di=InputGraph[each].p.y + d/2
					graphicsLine.append([(.84,.70,0),[ai+allPosGraph[3][0],bi-allPosGraph[3][1],ci+allPosGraph[3][0],di-allPosGraph[3][1]],2])


	def Matching(self):

		random.shuffle(self.matching)

		while self.matching:
			v = self.matching.pop()
			length = float("inf")

			u =1
			closest =0

			for u in self.matching:
				global Subst
				if v!=u and Subst[v][u]<length:
					length = Subst[v][u]
					closest =u

			self.MST.append((v,closest))

			ai=InputGraph[v].p.x + d/2
			bi=InputGraph[v].p.y + d/2
			ci=InputGraph[closest].p.x + d/2
			di=InputGraph[closest].p.y + d/2
			graphicsLine.append([(.5,.36,1),[ai+allPosGraph[0][0],bi-allPosGraph[0][1],ci+allPosGraph[0][0],di-allPosGraph[0][1]],2])

			self.matching.remove(closest)



	def union(self):
		for each in self.MST:
			self.tree.append(Edge(each[0],each[1],Subst[each[0]][each[1]]))

		return self.tree


class EulerianCycle:

	def __init__(self,H):
		self.H = H
		self.deg = {}
		self.vertices = []
		for every in self.H:

			if every.u not in self.deg.keys():
				self.vertices.append(every.u)
				self.deg[every.u]=0

			if every.v not in self.deg.keys():
				self.vertices.append(every.v)
				self.deg[every.v]=0

			self.deg[every.u]+=1
			self.deg[every.v]+=1

		self.n = len(self.vertices)
		self.g = [[0 for i in range(self.n)] for j in range(self.n)]

		for every in self.H:
			self.g[every.u][every.v]=1
			self.g[every.v][every.u]=1

		#print(self.g)

		self.result = []


	def getCycles(self):
		

		first = 0

		while(self.deg[first]==0):
			first+=1

		v1=-1
		v2=-1
		bad=False

		for i in range(self.n):

			if self.deg[i]%2!=0:

				if v1!=-1:
					v1=i
				elif v2!=-1:
					v2=i
				else:
					bad=True

		if v1!=-1:
			self.g[v1][v2]+=1
			self.g[v2][v1]+=1

		stack = []
		stack.append(first)

		while(len(stack)>0):

			v = stack[len(stack)-1]
			i=0

			for i in range(self.n+1):
				if(i==self.n):
					break
				if(self.g[v][i]>0):
					break
			
			if(i==self.n):
				self.result.append(v)
				stack.pop()
			else:
				self.g[v][i]-=1
				self.g[i][v]-=1
				stack.append(i)

		if v1!=-1:
			for i in range(len(self.result)):
				if(  ( (self.result[i]==v1) and (self.result[i+1]==v2) ) or ( (self.result[i]==v2 and self.result[i+1]==v1) )  ):
					result2 = []

					for j in range(i+1,lem(self.result)):
						result2.append(self.result[j])
					for j in range(1,i+1):
						result2.append(self.result[j])
					self.result=result2[:]
					break



		for i in range(self.n):
			for j in range(self.n):
				if(self.g[i][j]>0):
					bad = True

		if(bad):
			assert(False)
		else:
			return self.result









	


#Adjacent = graph([[0,10,11,5],[10,0,15,7],[11,15,0,7],[5,7,7,0]])
#Adjacent.initEdges()
#Spanning = spantheTree(Adjacent)
#print(Spanning.solve())



"""
Adjacent = graph
			([[1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525],
            [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862],
            [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420],
            [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728],
            [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236],
            [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368],
            [3874, 1318], [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622],
            [953, 268], [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052],
            [2588, 302], [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673],
            [872, 1559], [2863, 558], [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048],
            [1178, 100], [2599, 901], [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286],
            [161, 906], [1429, 134], [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43],
            [3756, 882], [776, 392], [1724, 1642], [198, 1810], [3950, 1558]]
            )

"""
