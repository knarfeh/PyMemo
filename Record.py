# -*- coding: gbk -*-
class Record(object):
    '''
    记录类
	根据记录的类型（基本记录，和逆转记录）来进行卡片的生成
	如果是基本记录，那么只生成1张卡片
	如果是逆转记录，那么生成2张卡片，这两张卡片正反面恰好相反，但是是两张独立的卡片
	recordId 记录的ID
	ques 记录的正面内容
	ans 记录的反面内容
	type 记录的类型（基本型，逆转型）
	addTime 记录添加的时间
	reviewTime 最后的复习时间
	alertTime 记录最后的修改时间
	libId 所属词库的ID
	grade 记录的级别（这个级别从0～5，初始的默认值为0.即表示这个记录是新的，陌生的）
	trashFlag 是否被挂起（挂起的记录意味着在学习记忆库的时候不会出现，这种情况可能是这个单词很简单，或者暂时不想学习这个单词）
    '''
    def __init__(self, recordId, ques, ans, type, addTime, reviewTime, alertTime, libId, grade=0, isTrash=False):
        self.__recordId = recordId
        self.__question = ques
        self.__answer = ans
        self.__type = type
        self.__addTime = addTime
        self.__reviewTime = reviewTime
        self.__alertTime = alertTime
        self.__libId = libId
        self.__grade = grade
        self.__isTrash = isTrash

	# get/set 方法
	def __getId(self):
		return self.recordId
	def __getQues(self):
		return self.question
	def __setQues(self, content):
		self.question = content
	def __getAns(self):
		return self.answer
	def __setAns(self, content):
		self.answer = content
	def __getType(self):
		return self.type
	def __setType(self, typeFlag):
		self.type = typeFlag
	def __getAddTime(self):
		return self.addTime
	def __getReviewTime(self):
		return self.reviewTime
	def __setReviewTime(self, time):
		self.reviewTime = time
	def __getAlertTime(self):
		return self.alertTime
	def __setAlertTime(self, time):
		self.alertTime = time
	def __getLibId(self):
		return self.libId
	def __setLibId(self, id):
		self.libId = id
	def __getGrade(self):
		return self.grade
	def __setGrade(self, grade):
		self.grade = grade
	def __getIsTrash(self):
		return self.isTrash
	def __setIsTrash(self, flag):
		self.isTrash = flag
