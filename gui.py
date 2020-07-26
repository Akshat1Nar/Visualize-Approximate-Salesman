import kivy
kivy.require('1.0.1')
import time
from math import *
from kivy.config import Config
Config.set('graphics','resizable',0)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.uix.button import Button
from collections import namedtuple
from dynamicSalesman import *
from exponentialSalesman import TSP
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
Window.size = (800,600)
colours = [(0,1.,0,1.),(1.,0,0,1.),(1.,1.,0,1.),(0,0,1.,1.)]
colorIndex=0
Clock.max_iteration=20

class Draw:

	def getTriangles(self,x,y):
		y1 = y-d/2
		x1 = x-(d/sqrt(3))
		y2 = y-d/2
		x2 = x+(d/sqrt(3))
		y3 = y+d/2
		x3 = x
		graphicsTriangle.append([(x1+allPosGraph[0][0],y1-allPosGraph[0][1],x2+allPosGraph[0][0],y2-allPosGraph[0][1],x3+allPosGraph[0][0],y3-allPosGraph[0][1]),(x-d/1.8,y-d/1.8)])
		graphicsTriangle.append([(x1+allPosGraph[1][0],y1-allPosGraph[1][1],x2+allPosGraph[1][0],y2-allPosGraph[1][1],x3+allPosGraph[1][0],y3-allPosGraph[1][1]),(x-d/1.8,y-d/1.8)])
		graphicsTriangle.append([(x1+allPosGraph[2][0],y1-allPosGraph[2][1],x2+allPosGraph[2][0],y2-allPosGraph[2][1],x3+allPosGraph[2][0],y3-allPosGraph[2][1]),(x-d/1.8,y-d/1.8)])
		graphicsTriangle.append([(x1+allPosGraph[3][0],y1-allPosGraph[3][1],x2+allPosGraph[3][0],y2-allPosGraph[3][1],x3+allPosGraph[3][0],y3-allPosGraph[3][1]),(x-d/1.8,y-d/1.8)])

	def drawEdges(self,Union):

		for each in Union:
			ai=InputGraph[each.u].p.x + d/2
			bi=InputGraph[each.u].p.y + d/2
			ci=InputGraph[each.v].p.x + d/2
			di=InputGraph[each.v].p.y + d/2
	
			graphicsLine.append([(0.69,0.63,0.80),[ai+allPosGraph[0][0],bi-allPosGraph[0][1],ci+allPosGraph[0][0],di-allPosGraph[0][1]],2])

	def DrawEuler(self,Path):

		for i in range(len(Path)-1):

			ai=InputGraph[Path[i]].p.x + d/2
			bi=InputGraph[Path[i]].p.y + d/2
			ci=InputGraph[Path[i+1]].p.x + d/2
			di=InputGraph[Path[i+1]].p.y + d/2
	
			graphicsLine.append([(1,0,0),[ai+allPosGraph[1][0],bi-allPosGraph[1][1],ci+allPosGraph[1][0],di-allPosGraph[1][1]],2])	
			#self.getTriangles(ci,di)

class Point:

	def __init__(self,p):
		self.p=p

	def __sub__(self,other):
		return sqrt((self.p.x-other.p.x)**2 + (self.p.y-other.p.y)**2)

	def __eq__(self,other):
		return (self.p.x==other.p.x and self.y==other.p.y)

class getGraph(Widget):

	def on_touch_down(self, touch):
		#print(Window.size)
		if(touch.pos[0]<Window.size[0]/2 and touch.pos[1]>Window.size[1]/2):
			with self.canvas:
				Color(0, 0, 0,1)
				d = 15.
				Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
				InputGraph.append(Point(pixel(touch.x,touch.y,d)))

			


class makeGraph(Widget):

	def __init__(self,**kwargs):
		super(makeGraph,self).__init__(**kwargs)
		self.curPos=[]
		

	def getPos(self,temp):
		self.curPos.append(self.pos[0])
		self.curPos.append(self.pos[1])
		allPosGraph.append(self.curPos)

	def draw(self):



		#print(self.curPos)

		self.color=(0,1,0,1)
		
		for each in InputGraph:
			global colorIndex
			with self.canvas:
				Color(rgba=(colours[colorIndex]))
				colorIndex = (colorIndex+1)%4
				d=12
				Ellipse(pos=(each.p.x+self.curPos[0],each.p.y-self.curPos[1]),size=(d,d))

		colorIndex=0

	def makeEdges(self):
		
		for i in range(len(InputGraph)): 
			temp = []
			for i in range(len(InputGraph)):
				temp.append(0)
			Subst.append(temp)
		
		for i,each in enumerate(InputGraph):
			for j,every in enumerate(InputGraph):

				if(i==j):
					Subst[i][j]=0
					continue

				Subst[i][j] = each-every


class customLabel(Label):

	def __init__(self,text,**kwargs):
		super().__init__(**kwargs)
		self.text=text
		self.color=(0,0,0,1)



class ChristofidesApp(App):

	def nextFrame(self,*args):

		#print("call")

		if(self.flag==True and self.once==False):
			
			print(len(self.Grapha.curPos))
			self.once=True
			self.next()

		global graphicsLineInd,graphicsLine,graphicsTriangleInd,graphicsTriangle

		if(graphicsLineInd>len(graphicsLine)-1):
			if(graphicsTriangleInd>len(graphicsTriangle)-1):
				return
			else:
				with self.layout.canvas:
					Color(rgb=(0,0,1))
					Ellipse(segments=3,pos=graphicsTriangle[graphicsTriangleInd][1],size=(d*1.5,d*1.5))
					graphicsTriangleInd+=1
				return


		if(graphicsLine[graphicsLineInd][0]==(.20,.72,.11)):
			self.speed=0.7
		with self.layout.canvas:
			Color(rgb=graphicsLine[graphicsLineInd][0])
			Line(points=graphicsLine[graphicsLineInd][1],width=graphicsLine[graphicsLineInd][2])

		graphicsLineInd+=1





	def build(self):

		self.once=False
		self.flag=False

		self.layout = GridLayout(cols=2)
		Window.clearcolor = (1, 1, 1, 1)
		self.speed=0.03

		self.partition()
		self.painter = getGraph()
		self.doneButton = Button(text="DONE")
		self.doneButton.bind(on_release=self.done)
		self.text=customLabel("Select Points on Left Block")

		self.layout.add_widget(self.painter)
		self.layout.add_widget(self.text)
		self.layout.add_widget(self.doneButton)


		Clock.schedule_interval(self.nextFrame,self.speed)

		return self.layout


	def partition(self):

		with self.layout.canvas:
			Color(rgba=(0,0,0,1))
			Line(points=[0,Window.size[1]/2,Window.size[0],Window.size[1]/2],width=2)
			Line(points=[Window.size[0]/2,0,Window.size[0]/2,Window.size[1]],width=2)


	def done(self,obj):
		self.flag=True
		self.painter.canvas.clear()
		self.layout.remove_widget(self.doneButton)
		self.layout.remove_widget(self.painter)
		self.layout.remove_widget(self.text)

		self.Grapha=makeGraph()
		self.Graphb=makeGraph()
		self.Graphc=makeGraph()
		self.Graphd=makeGraph()
		
		self.layout.add_widget(Button(text="Minimum Spanning Tree",size_hint = (1,0.04)))
		self.layout.add_widget(Button(text="Induced Subgraph",size_hint = (1,0.04)))
		
		self.layout.add_widget(self.Grapha)
		self.layout.add_widget(self.Graphb)

		self.layout.add_widget(Button(text="Perfect Matching",size_hint = (1,0.04)))
		self.layout.add_widget(Button(text="Hamiltonian Circuit",size_hint = (1,0.04)))

		self.layout.add_widget(self.Graphc)
		self.layout.add_widget(self.Graphd)

		self.t1=Clock.schedule_once(self.Grapha.getPos)
		self.t2=Clock.schedule_once(self.Graphb.getPos)
		self.t3=Clock.schedule_once(self.Graphc.getPos)
		self.t4=Clock.schedule_once(self.Graphd.getPos)
		Clock.tick()
		
		
	def next(self):

		self.Grapha.draw()
		self.Graphb.draw()
		self.Graphc.draw()
		self.Graphd.draw()
		self.Grapha.makeEdges()
		

		Adjacent = graph(Subst)
		Adjacent.initEdges()


		Spanning = spantheTree(Adjacent)
		Matching = Spanning.solve()
		self.Grapha.draw()

		
		MST = subgraphInduced(Matching)
		MST.toDraw()
		MST.Matching()
		Union = MST.union()
		Cycle = EulerianCycle(Union).getCycles()

		DrawEvery = Draw()
		DrawEvery.drawEdges(Union)
		DrawEvery.DrawEuler(Cycle)

		
		

ChristofidesApp().run()

