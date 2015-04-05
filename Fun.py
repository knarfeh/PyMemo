# -*- coding: gbk -*-
import wx
import sys

packages = [('Apple', '苹果', '2015-3-22', 'lib-one', '5', '9'),
            ('New York', '纽约', '2015-3-23', 'lib-one', '3', '7'),
            ('London', '伦敦', '2015-3-24', 'lib-two', '0', '8'),
            ('NoteBook', '笔记本', '2015-3-25', 'lib-two', '2', '9'),
            ('Library', '图书馆', '2015-3-26', 'lib-one', '0', '4'),
            ('Professional', '专业的', '2015-3-28', 'lib-two', '0', '2')]

listHeadName = ['正面', '反面', '到期时间', '所属词库', '复习', '间隔天数']

def createListCtrl(self, parent):
	hbox = wx.BoxSizer(wx.HORIZONTAL)

	self.list = wx.ListCtrl(parent, -1, style=wx.LC_REPORT
	                                          |wx.LC_SINGLE_SEL
	                                          |wx.LC_VRULES
	                                          |wx.LC_HRULES)
	for i in range(len(listHeadName)):
		self.list.InsertColumn(i, listHeadName[i], width=wx.LIST_AUTOSIZE)

	for i in packages:
		index = self.list.InsertStringItem(sys.maxint, i[0])
		for j in range(len(listHeadName)-1):
			self.list.SetStringItem(index, j+1, i[j+1])

	hbox.Add(self.list, 1, wx.EXPAND)
	parent.SetSizer(hbox)
	self.Centre()
	self.Show(True)

def createInfoPanel(self, parent):
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	fromLib = wx.StaticText(parent, -1, label="词库名称")
	moreInfoBtn = wx.BitmapButton(parent, -1, wx.Bitmap('images/other-size/info16.png'), style=wx.NO_BORDER)
	hbox.Add(fromLib, 9, wx.CENTER|wx.TOP, border=5)
	hbox.Add(moreInfoBtn, 1, wx.CENTER|wx.ALIGN_RIGHT|wx.RIGHT, border=10)

	parent.SetSizer(hbox)
	self.Bind(wx.EVT_BUTTON, self.OnCardInfo, moreInfoBtn)
	self.Centre()
	self.Show(True)

def createRichText(self, parent):
	hbox = wx.BoxSizer(wx.HORIZONTAL)

	textBold = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/bold16.png'))
	textItalic = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/italic16.png'))
	textUnderline = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/underline16.png'))
	textColor = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/color16.png'))
	textAlighLeft = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/align_left16.png'))
	textAlighCenter = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/align_center16.png'))
	textAlighRight = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/align_right16.png'))
	textList = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/text_list16.png'))
	insertRecord = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/record16.png'))
	insertPicture = wx.BitmapButton(parent, -1, wx.Bitmap('images/rich-text/picture16.png'))


	hbox.Add(textBold, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textItalic, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textUnderline, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textList, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textColor, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textAlighLeft, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textAlighCenter, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(textAlighRight, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(insertPicture, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)
	hbox.Add(insertRecord, 0, wx.TOP|wx.ALIGN_RIGHT, border=10)

	parent.SetSizer(hbox)
	self.Centre()
	self.Show(True)

def createEditCard(self, parent, title):
	vbox = wx.BoxSizer(wx.VERTICAL)
	titleText = wx.StaticText(parent, -1, label=title)
	editCard = wx.TextCtrl(parent, -1, style=wx.TE_MULTILINE)
	vbox.Add(titleText, 1, wx.EXPAND)
	vbox.Add(editCard, 10, wx.EXPAND)
	parent.SetSizer(vbox)
	self.Centre()
	self.Show(True)

def createOperationCol(self, parent):
    gridSizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
    cancelBW = wx.Button(parent, -1, label="取消修改")
    submitBW = wx.Button(parent, -1, label="确认修改")
    gridSizer.Add(cancelBW, 0, 0)
    gridSizer.Add(submitBW, 0, wx.LEFT, 10)
    parent.SetSizer(gridSizer)
    self.Centre()
    self.Show(True)

