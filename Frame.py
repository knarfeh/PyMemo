# -*- coding: gbk -*-
import wx
import Dialog
import FrameFun
import sys
import wx.lib.dialogs

class PyMemo(wx.Frame):
    '''
    PyMemo�ࣺ������������Ŀ��
    �������ڣ��˵��������������ָ���

    PyMemo.py��Dialog.pyһ�𹹳��������ͼ��
    '''
    def __init__(self, parent, id, title, size):
        wx.Frame.__init__(self, parent, id, title=title, size=size)
        self.icon = wx.Icon('images/32/PyMemo_logo_white.png', wx.BITMAP_TYPE_PNG)
        self.SetIcon(self.icon)

        self.createSplitterWindow()
        self.createMenuBar()
        self.createToolBar()
        self.Centre()
        self.Show(True)

    def createMenuBar(self):
        menubar = wx.MenuBar()

        # �˵�
        fileMenu = wx.Menu()
        # editMenu = wx.Menu()
        viewMenu = wx.Menu()
        toolMenu = wx.Menu()
        helpMenu = wx.Menu()

        # ���˵���ӵ��˵���
        menubar.Append(fileMenu, '�ļ�')
        menubar.Append(viewMenu, '�鿴')
        menubar.Append(toolMenu, '����')
        menubar.Append(helpMenu, '����')

        # ��˵������ѡ��
        # fileMenu
        newLibItem = fileMenu.Append(-1, '�½������', '�½�����⣬ָ������')
        newCardItem = fileMenu.Append(-1, '�½���Ƭ', '�½���Ƭ���������')
        inputItem = fileMenu.Append(-1, '����...', '�ӱ���PC��PyAnki��������')
        outputItem = fileMenu.Append(-1, '����...', '��PyAnki�򱾵�PC���������')
        fileMenu.AppendSeparator()
        setItem = fileMenu.Append(-1, 'ƫ������', '����PyAnki��ʹ֮���ӷ����Ϊ�����')
        fileMenu.AppendSeparator()
        quitItem = fileMenu.Append(wx.ID_EXIT, '�˳�', '�뿪��Ӧ�ó���')

        # viewMenu
        # cardItem = viewMenu.Append(-1, '��Ƭ')
        # LibItem = viewMenu.Append(-1, '�����')
        # tagItem = viewMenu.Append(-1, '��ǩ')
        # viewMenu.AppendSeparator()
        # self.showLeftSideBarItem = viewMenu.AppendCheckItem(-1, '��ʾ������')
        # self.showCardListItem = viewMenu.AppendCheckItem(-1, '��ʾ��Ƭ�б�')
        self.showCardEditItem = viewMenu.AppendCheckItem(-1, '��ʾ��Ƭ�༭����')

        # self.showLeftSideBarItem.Check(True)
        # self.showCardListItem.Check(True)
        self.showCardEditItem.Check(True)



        # toolMenu
        studyItem = toolMenu.Append(-1, 'ѧϰ�����')
        # checkItem = toolMenu.Append(-1, '���տ�Ƭ')
        # optimizeItem = toolMenu.Append(-1, '�Ż����ݿ�')
        # kindItem = toolMenu.Append(-1, '����Ƭ����')


        # helpMenu
        guideItem = helpMenu.Append(wx.ID_HELP, '�û��ֲ�')
        aboutItem = helpMenu.Append(wx.ID_ABOUT, '����PyAnki')

        self.Bind(wx.EVT_MENU, self.OnStartMemo, studyItem)
        self.Bind(wx.EVT_MENU, self.OnSetting, setItem)
        self.Bind(wx.EVT_MENU, self.CloseWindow, quitItem)
        self.Bind(wx.EVT_MENU, self.OpenAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnGuide, guideItem)
        self.Bind(wx.EVT_MENU, self.OnNewLib, newLibItem)
        self.Bind(wx.EVT_MENU, self.OnExport, outputItem)
        self.Bind(wx.EVT_MENU, self.OnImport, inputItem)
        self.Bind(wx.EVT_MENU, self.OnNewCard, newCardItem)


        self.SetMenuBar(menubar)

    def createToolBar(self):
        toolId = {'import':wx.NewId(),
              'new_lib':wx.NewId(),
              'new_card':wx.NewId(),
              'setting':wx.NewId(),
              'learn':wx.NewId()}
        toolBar = self.CreateToolBar( wx.TB_HORIZONTAL
                          |wx.TB_FLAT
                          |wx.TB_TEXT
                          |wx.TB_HORZ_LAYOUT)
        quit = toolBar.AddLabelTool(wx.ID_EXIT, '�˳�', wx.Bitmap('images/32/quit.png'))
        toolBar.AddSeparator()
        importLib = toolBar.AddLabelTool(toolId['import'], '����ʿ�', wx.Bitmap('images/32/import.png'))
        newLib = toolBar.AddLabelTool(toolId['new_lib'], '�½��ʿ�', wx.Bitmap('images/32/library_add.png'))
        newCard = toolBar.AddLabelTool(toolId['new_card'], '�½���Ƭ', wx.Bitmap('images/32/card_add.png'))
        setting = toolBar.AddLabelTool(toolId['setting'], '����', wx.Bitmap('images/32/setting.png'))
        toolBar.AddSeparator()
        wordsLearn = toolBar.AddLabelTool(toolId['learn'], '��ʼѧϰ', wx.Bitmap('images/32/words_learn.png'))

        self.Bind(wx.EVT_TOOL, self.CloseWindow, quit)
        self.Bind(wx.EVT_TOOL, self.OnSetting, setting)
        self.Bind(wx.EVT_TOOL, self.OnNewLib, newLib)
        self.Bind(wx.EVT_TOOL, self.OnImport, importLib)
        self.Bind(wx.EVT_TOOL, self.OnNewCard, newCard)
        self.Bind(wx.EVT_TOOL, self.OnStartMemo, wordsLearn)

        toolBar.Realize()
        return 0

    def createSplitterWindow(self):
        splitter = wx.SplitterWindow(self, -1, style=wx.SP_LIVE_UPDATE)
        splitter.SetMinimumPaneSize(250)

        # ������
        panelContain = wx.Panel(splitter, -1)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        leftPanel = LeftPanel(panelContain, -1)
        vbox1.Add(leftPanel, 1, wx.EXPAND)
        panelContain.SetSizer(vbox1)

        # �зָ���
        splitter1 = wx.SplitterWindow(splitter, -1, style=wx.SP_LIVE_UPDATE)
        splitter1.SetMinimumPaneSize(480)
        # �м����
        middlePanelContain = wx.Panel(splitter1, -1)
        vboxMiddle = wx.BoxSizer(wx.VERTICAL)
        middlePanel = MiddlePanel(middlePanelContain, -1)
        vboxMiddle.Add(middlePanel, 1, wx.EXPAND)
        middlePanelContain.SetSizer(vboxMiddle)

        # �Ҳ����
        rightPanelContain = wx.Panel(splitter1, -1)
        vboxRight = wx.BoxSizer(wx.VERTICAL)
        rightPanel = RightPanel(rightPanelContain, -1)
        vboxRight.Add(rightPanel, 1, wx.EXPAND)
        rightPanelContain.SetSizer(vboxRight)

        # ���÷ָ�������
        splitter.SplitVertically(panelContain, splitter1, 250)
        splitter1.SplitVertically(middlePanelContain, rightPanelContain,-300)

        # splitter1.Unsplit()
        # splitter.Unsplit()

        self.Centre()

    def CloseWindow(self, evt):
        self.Close()
        return 0

    def OpenAbout(self, evt):
        dlg = Dialog.AboutDialog()
        return 0

    def OnSetting(self, evt):
        settingDlg = Dialog.SettingDialog()
        settingDlg.ShowModal()
        settingDlg.Destroy()

    def OnGuide(self, evt):
        f = open("Dialog.py", "r")
        msg = f.read()
        f.close()
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg, "�û��ֲ�")
        dlg.ShowModal()

    def OnNewLib(self, evt):
        newLibDlg = Dialog.AddNewLib(None, -1, "�½��ʿ�", (400, 200))
        newLibDlg.ShowModal()
        newLibDlg.Destroy()

    def OnExport(self, evt):
        exportDlg = Dialog.Export(None)
        exportDlg.ShowModal()
        exportDlg.Destroy()

    def OnImport(self, evt):
        importDlg = Dialog.Import(None)
        importDlg.ShowModal()
        importDlg.Destroy()

    def OnNewCard(self, evt):
        newCardDlg = Dialog.AddNewCard(None, -1, "�½����ʿ�Ƭ", (500, 500))
        newCardDlg.ShowModal()
        newCardDlg.Destroy()

    def OnStartMemo(self, evt):
        startMemoDlg = Dialog.StartMemo()
        startMemoDlg.ShowModal()
        startMemoDlg.Destroy()

# Left Section
class LeftPanel(wx.Panel):
	'''
	���ɴ������ָ����Ĵʿ��б�
	'''
	def __init__(self, parent, id):
		libraryDic = {'0':['��Ƶ�ּ��ʻ�һ','100/0/100', ''],
			'1':['��Ƶ�ּ��ʻ��','0/0/17'],
			'2':['��Ƶ�ּ��ʻ���','100/0/100'],
			'3':['��Ƶ�ּ��ʻ���','74/0/100'],
			'4':['CET-4��Ƶ�ʻ�','0/0/100']}
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
		vbox = wx.BoxSizer(wx.VERTICAL)
		for i in range(len(libraryDic)):
			vbox.Add(wx.Button(self, -1, label=libraryDic[str(i)][0]+"    "+libraryDic[str(i)][1], size=(-1, 40)),
			 0,
			 wx.EXPAND|wx.ALL,
			 border=10)
		self.SetSizer(vbox)
		self.Show(True)

# Middle Section
class MiddlePanel(wx.Panel):
	'''
	���ɴ����м��ListCtrl
	'''
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
		Lib_Items=['��ѡ��ɸѡ����', '��ǰ�ʿ����е�', '����ѧϰ��', '�ѵ��ڵ�', '�Ѽ�ס��', '������ѧϰ��', 'ʼ�ռǲ�ס��', '������ӵ�']
		panelHeader = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		LibComboBox = wx.ComboBox(panelHeader,
		                          pos=(0, 5),
		                          choices=Lib_Items,
		                          style=wx.CB_READONLY)
		LibComboBox.SetSelection(0)
		LibComboBox.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		go = wx.BitmapButton(panelHeader, -1, wx.Bitmap('images/other-size/search26.png'), style=wx.NO_BORDER)
		search = wx.TextCtrl(panelHeader, -1)

		hbox.Add(LibComboBox, 5, wx.TOP, border=6)
		hbox.Add(search, 5, wx.TOP|wx.LEFT, border=6)
		hbox.Add(go, 1, wx.TOP, border=6)
		panelHeader.SetSizer(hbox)


		panelContent = wx.Panel(self, -1)
		self.createListCtrl(panelContent)
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(panelHeader, 1, wx.EXPAND)
		vbox.Add(panelContent, 11, wx.EXPAND)

		self.SetSizer(vbox)

		self.Centre()
		self.Show(True)

	def OnSelect(self, e):
		selectedLib = e.GetString()
		print selectedLib

	def createListCtrl(self, parent):
		packages = [('Apple', 'ƻ��', '2015-3-22', 'lib-one', '5', '9'),
			('New York', 'ŦԼ', '2015-3-23', 'lib-one', '3', '7'),
			('London', '�׶�', '2015-3-24', 'lib-two', '0', '8'),
			('NoteBook', '�ʼǱ�', '2015-3-25', 'lib-two', '2', '9'),
			('Library', 'ͼ���', '2015-3-26', 'lib-one', '0', '4'),
			('Professional', 'רҵ��', '2015-3-28', 'lib-two', '0', '2')]

		listHeadName = ['����', '����', '����ʱ��', '�����ʿ�', '��ϰ', '�������']
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

# Right Section
class RightPanel(wx.Panel):
	'''
	���ɴ����Ҳ�ĵ��ʿ�Ƭ�༭����

	�˷ָ����Ƿ���Ŀǰ����ȷ����������ϣ��ɾ��
	��Ϊ�Ҹо���Դʿ��е��ʿ�Ƭ�Ĳ�������Щ����
	'''
	def __init__(self, parent, id):
		wx.Panel.__init__(self, parent, id, style=wx.BORDER_NONE)
		vbox = wx.BoxSizer(wx.VERTICAL)

		# ��Ƭ��Ϣ���
		infoPanelContain = wx.Panel(self, -1)
		infoPanel = self.createInfoPanel(infoPanelContain)
		vbox.Add(infoPanelContain, 0, wx.EXPAND)

		# ���ı��������
		richTextContain = wx.Panel(self, -1)
		richText = self.createRichText(richTextContain)
		line = wx.StaticLine(richTextContain, -1, style=wx.LI_HORIZONTAL)
		vbox.Add(richTextContain, 0, wx.EXPAND)
		vbox.Add(line, 0, wx.EXPAND)

		# ��Ƭ�������
		positiveSideCardContain = wx.Panel(self, -1)
		positiveSide = self.createEditCard(positiveSideCardContain, '�༭��Ƭ�����棺')
		vbox.Add(positiveSideCardContain, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)

		# ��Ƭ�������
		negativeSideCardContain = wx.Panel(self, -1)
		negativeSide = self.createEditCard(negativeSideCardContain, '�༭��Ƭ�ķ��棺')
		vbox.Add(negativeSideCardContain, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, border=5)


		operationPanel = wx.Panel(self, -1)
		operationCol = self.createOperationCol(operationPanel)
		vbox.Add(operationPanel, 1, wx.EXPAND|wx.TOP, border=5)

		self.SetSizer(vbox)
		self.Centre()
		self.Show(True)

	def OnCardInfo(self, evt):
		cardInfoDlg = Dialog.CardInfoDialog()
		cardInfoDlg.ShowModal()
		cardInfoDlg.Destroy()

	def createInfoPanel(self, parent):
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		fromLib = wx.StaticText(parent, -1, label="�ʿ�����")
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
		cancelBW = wx.Button(parent, -1, label="ȡ���޸�")
		submitBW = wx.Button(parent, -1, label="ȷ���޸�")
		gridSizer.Add(cancelBW, 0, 0)
		gridSizer.Add(submitBW, 0, wx.LEFT, 10)
		parent.SetSizer(gridSizer)
		self.Centre()
		self.Show(True)

def main():
	app = wx.App()
	PyMemo(None, -1, 'PyMemo', (1000, 620))
	app.MainLoop()

if __name__ == '__main__':
	main()