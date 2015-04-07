# -*- coding: gbk -*-
class Record(object):
    '''
    ��¼��
	���ݼ�¼�����ͣ�������¼������ת��¼�������п�Ƭ������
	����ǻ�����¼����ôֻ����1�ſ�Ƭ
	�������ת��¼����ô����2�ſ�Ƭ�������ſ�Ƭ������ǡ���෴�����������Ŷ����Ŀ�Ƭ
	recordId ��¼��ID
	ques ��¼����������
	ans ��¼�ķ�������
	type ��¼�����ͣ������ͣ���ת�ͣ�
	addTime ��¼��ӵ�ʱ��
	reviewTime ���ĸ�ϰʱ��
	alertTime ��¼�����޸�ʱ��
	libId �����ʿ��ID
	grade ��¼�ļ�����������0��5����ʼ��Ĭ��ֵΪ0.����ʾ�����¼���µģ�İ���ģ�
	trashFlag �Ƿ񱻹��𣨹���ļ�¼��ζ����ѧϰ������ʱ�򲻻���֣��������������������ʺܼ򵥣�������ʱ����ѧϰ������ʣ�
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

	# get/set ����
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
