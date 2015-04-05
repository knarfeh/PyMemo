# -*- coding: gbk -*-
class Record(object):
	'''
	记录类
	根据记录的类型（基本记录，和逆转记录）来进行卡片的生成
	如果是基本记录，那么只生成1张卡片
	如果是逆转记录，那么生成2张卡片，这两张卡片正反面恰好相反，但是是两张独立的卡片
	'''
	def __init__(self, cardId, ques, ans, type, addTime, alertTime, libId, grade=0, ):
		self.cardId = cardId
		self.question = ques
		self.answer =ans
		self.type =type
		self.addTime =addTime
		self.alertTime = alertTime
		self.libId = libId
		self.grade = grade

	# get/set 方法
	def getId(self):
		return self.cardId
	def getQues(self):
		return self.question
	def setQues(self, content):
		self.question = content
	def getAns(self):
		return self.answer
	def setAns(self, content):
		self.answer = content
	def getType(self):
		return self.type
	def setType(self, typeFlag):
		self.type = typeFlag
	def getAddTime(self):
		return self.addTime
	def getAlertTime(self):
		return self.alertTime
	def setAlertTime(self, time):
		self.alertTime = time
	def getLibId(self):
		return self.libId
	def setLibId(self, id):
		self.libId = id
	def getGrade(self):
		return self.grade
	def setGrade(self, grade):
		self.grade = grade
