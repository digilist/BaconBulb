class Highscore(object):
	"""docstring fos Highscore"""
	def __init__(self):
		self._filename = "highscore.txt"

	def addScore(self,name,score):
		f = open(self._filename,'a')
		f.write(name+':'+str(score)+ "\n")
		f.close()

	def getScore(self):
		f = open(self._filename,'r')
		scorelist =[]
		for line in f:
			scorelist.append({line.split(':')[0] : int(line.split(':')[1])})
		f.close()
		return scorelist



