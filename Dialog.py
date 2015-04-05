# -*- coding: gbk -*-
import wx
import Fun

class AboutDialog(wx.AboutDialogInfo):
    def __init__(self):
        description = "PyMemo是一个基于重复学习原理的记忆软件，简单易用，免费并开源。\n" \
	                  "PyMeomo以AGPL3协议发布。\n\n" \
	                  "这是我的一项毕业设计，课题为：基于Python的单词记忆软件开发\n" \
	                  "GUI库：wxpython 2.7.9\n\n" \
	                  "开发工具：pyCharm Community Edition 4.0.4\n" \
	                  "这些图标是来自于不同的来源\n其中大部分来自：http://findicons.com/\n\n" \
	                  "特别感谢：张治国老师的指导\n\n" \
	                  "向所有提出过建议，报告Bug的人们致谢！\n\n" \
	                  "联系：iliuyang@foxmail.com"
        info = wx.AboutDialogInfo()
        info.SetIcon(wx.Icon('images/64/PyMemo_logo_white.png', wx.BITMAP_TYPE_PNG))
        info.SetName("PyMemo")
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(c)2015 刘洋')
        wx.AboutBox(info)

class SettingDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '单词卡片详细信息',size=(200, 400),
                           style=wx.CAPTION
                                 |wx.SYSTEM_MENU
                                 |wx.CLOSE_BOX)
        vbox =wx.BoxSizer(wx.VERTICAL)

        gridSizer = wx.GridSizer(2, 2, 5, 5)

        # (0, 0)
        panel1 = wx.Panel(self)
        CardSetting = wx.StaticBox(panel1, -1, label='卡片')
        sbs1 = wx.StaticBoxSizer(CardSetting, orient=wx.VERTICAL)

        showNextTime = wx.CheckBox(panel1,
                            label='在回答按钮上显示下一次复习时间',
                            style=wx.CHK_3STATE)
        showLeftCard = wx.CheckBox(panel1,
                            label='在复习的时候显示剩余卡片数',
                            style=wx.CHK_3STATE)
        showTime = wx.CheckBox(panel1,
                            label='在复习的时候显示时间',
                            style=wx.CHK_3STATE)
        showNextTime.SetValue(True)
        showLeftCard.SetValue(True)
        showTime.SetValue(True)

        sbs1.Add(showNextTime, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)
        sbs1.Add(showLeftCard, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)
        sbs1.Add(showTime, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)

        panel1.SetSizer(sbs1)

        gridSizer.Add(panel1, 3, wx.EXPAND|wx.ALL, border=10)

        # (0, 1)
        panel2 = wx.Panel(self)
        StudySetting = wx.StaticBox(panel2, -1, label='学习卡片设置')
        sbs2 = wx.StaticBoxSizer(StudySetting, orient=wx.VERTICAL)
        grid1 = wx.FlexGridSizer(0, 2, 0, 0)

        # group of controls:
        self.group_ctrls = []
        text1 = wx.StaticText(panel2, label="每日学习卡片上限（张）")
        text2 = wx.StaticText(panel2, label="每日复习卡片上限（张）")
        text3 = wx.StaticText(panel2, label="超时显示卡片反面（秒）")

        studyLimit = wx.SpinCtrl(panel2, -1)
        studyLimit.SetRange(1, 200)
        studyLimit.SetValue(80)

        reviewLimit = wx.SpinCtrl(panel2, -1)
        reviewLimit.SetRange(1, 200)
        reviewLimit.SetValue(80)

        showTimeLimit = wx.SpinCtrl(panel2, -1)
        showTimeLimit.SetRange(1, 60)
        showTimeLimit.SetValue(10)

        self.group_ctrls.append((text1, studyLimit))
        self.group_ctrls.append((text2, reviewLimit))
        self.group_ctrls.append((text3, showTimeLimit))

        for text, spinctrl in self.group_ctrls:
            grid1.Add( text, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
            grid1.Add( spinctrl, 0, wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

        sbs2.Add(grid1, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        panel2.SetSizer(sbs2)
        gridSizer.Add(panel2, 1, wx.EXPAND|wx.ALL, border=10)

        # (1, 0)
        panel3 = wx.Panel(self)
        fontSetting = wx.StaticBox(panel3, -1, label='卡片顺序')
        sbs3 = wx.StaticBoxSizer(fontSetting, orient=wx.VERTICAL)

        oldAfterNew = wx.RadioButton(panel3, -1, "新卡片学习完之后再复习旧卡片")
        newAfterOld = wx.RadioButton(panel3, -1, "旧卡片复习完之后再学习新卡片")
        newOrOld = wx.RadioButton(panel3, -1, "新旧卡片交替出现")

        sbs3.Add(oldAfterNew, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)
        sbs3.Add(newAfterOld, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)
        sbs3.Add(newOrOld, 1, wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)

        panel3.SetSizer(sbs3)

        gridSizer.Add(panel3, 1, wx.EXPAND|wx.ALL, border=10)

        # (1, 1)
        panel4 = wx.Panel(self)
        fontSetting = wx.StaticBox(panel4, -1, label='字体设置')
        sbs4 = wx.StaticBoxSizer(fontSetting, orient=wx.VERTICAL)
        panel41 = wx.Panel(self)
        panel42 = wx.Panel(self)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        fontFamilyList = ['font-family-one',
                           'font-family-two',
                           'font-family-three',
                           'font-family-flour']
        fontFamilyText = wx.StaticText(panel4, -1, "字体：",)
        fontFamily = wx.Choice(panel4, -1, choices=fontFamilyList)

        hbox1.Add(fontFamilyText, 1, wx.LEFT|wx.TOP, border=10)
        hbox1.Add(fontFamily, 3, wx.TOP, border=10)

        fontSizeText = wx.StaticText(panel4, -1, "字号：")
        fontSize = wx.SpinCtrl(panel4, -1)
        fontSize.SetRange(1, 30)
        fontSize.SetValue(12)

        hbox2.Add(fontSizeText, 1, wx.LEFT|wx.TOP, border=10)
        hbox2.Add(fontSize, 3, wx.TOP, border=10)

        sbs4.Add(hbox1, wx.LEFT, border=5)
        sbs4.Add(hbox2, wx.LEFT, border=5)

        panel4.SetSizer(sbs4)
        gridSizer.Add(panel4, 1, wx.EXPAND|wx.ALL, border=10)


        # (2, 1)
        vbox.Add(gridSizer, 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, -1, label='确定')
        applyButton = wx.Button(self, -1, label="应用")
        closeButton = wx.Button(self, -1, label='关闭')
        hbox.Add(okButton, 1, wx.RIGHT, border=5)
        hbox.Add(applyButton, 1, wx.RIGHT, border=5)
        hbox.Add(closeButton, 1, wx.RIGHT, border=5)

        vbox.Add(hbox, 1, wx.ALIGN_RIGHT)

        self.Bind(wx.EVT_BUTTON, self.OnClose, closeButton)

        self.SetSizer(vbox)
        self.Fit()
        self.Centre()
        self.Show(True)

    def OnClose(self, e):
        self.Destroy()

class CardInfoDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '单词卡片详细信息',size=(300, 400),
                           style=wx.CAPTION
                                 |wx.SYSTEM_MENU
                                 |wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        infoDir = {1:['添加时间','2015-3-24'],
                   2:['首次学习','2015-3-24'],
                   3:['最近复习','2015-3-24'],
                   4:['到期时间','2015-3-24'],
                   5:['间隔','9天'],
                   6:['复习次数','2'],
                   7:['错误次数','2'],
                   8:['所属词库','CET-4高频词汇'],
                   9:['卡片ID','15456468465'],
                   10:['词库ID','564645635218'],}

        vbox = wx.BoxSizer(wx.VERTICAL)
        headTitle = wx.StaticText(panel, label="单词卡片的详细信息")
        addTime = wx.StaticText(panel, label=infoDir[1][0]+"      "+infoDir[1][1])
        firstStudyTime = wx.StaticText(panel, label=infoDir[2][0]+"      "+infoDir[2][1])
        reviewTime = wx.StaticText(panel, label=infoDir[3][0]+"      "+infoDir[3][1])
        deadLine = wx.StaticText(panel, label=infoDir[4][0]+"      "+infoDir[4][1])
        delayDay = wx.StaticText(panel, label=infoDir[5][0]+"      "+infoDir[5][1])
        reviewNum = wx.StaticText(panel, label=infoDir[6][0]+"      "+infoDir[6][1])
        errorNum = wx.StaticText(panel, label=infoDir[7][0]+"      "+infoDir[7][1])
        belongLib = wx.StaticText(panel, label=infoDir[8][0]+"      "+infoDir[8][1])
        cardId = wx.StaticText(panel, label=infoDir[9][0]+"      "+infoDir[9][1])
        libId = wx.StaticText(panel, label=infoDir[10][0]+"      "+infoDir[10][1])


        vbox.Add(headTitle, 1, wx.CENTER|wx.TOP, border=10)
        vbox.Add(addTime, 1, wx.ALL, border=10)
        vbox.Add(firstStudyTime, 1, wx.ALL, border=10)
        vbox.Add(reviewTime, 1, wx.ALL, border=10)
        vbox.Add(deadLine, 1, wx.ALL, border=10)
        vbox.Add(delayDay, 1, wx.ALL, border=10)
        vbox.Add(reviewNum, 1, wx.ALL, border=10)
        vbox.Add(errorNum, 1, wx.ALL, border=10)
        vbox.Add(belongLib, 1, wx.ALL, border=10)
        vbox.Add(cardId, 1, wx.ALL, border=10)
        vbox.Add(libId, 1, wx.ALL, border=10)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

class AddNewLib(wx.Dialog):
    def __init__(self, parent, id, title, size, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, id, title, pos, size, style)

        self.PostCreate(pre)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "新建词库的名称：")
        hbox.Add(label, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(80,-1))
        hbox.Add(text, 1, wx.ALIGN_CENTER|wx.ALL, 5)

        vbox.Add(hbox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)

        vbox.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()

        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_OK, "确定")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL, "取消")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        vbox.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(vbox)
        vbox.Fit(self)
        self.Centre()
        self.Show(True)

class Export(wx.DirDialog):
    def __init__(self, parent):
        wx.DirDialog.__init__(self, parent, "请选择一个文件来保存导出的词库：",
                          style=wx.DD_DEFAULT_STYLE
                                |wx.DD_NEW_DIR_BUTTON)
        self.Centre()
        self.Show(True)

class Import(wx.FileDialog):
    def __init__(self, parent):
        wx.FileDialog.__init__(self, parent, "选择导入的词库文件",
                               wildcard="BMP and GIF files (*.bmp*.gif)|*.bmp*.gif|PNG files (*.png)|*.png",
                               style=wx.FD_OPEN
                                     |wx.FD_FILE_MUST_EXIST
                                     |wx.FD_CHANGE_DIR
                               )
        self.Centre()
        self.Show(True)

class AddNewCard(wx.Dialog):
    def __init__(self, parent, id, title, size, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, id, title, pos, size, style)

        self.PostCreate(pre)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        Lib_Items = ['词频分级词汇一',
                     '词频分级词汇二',
                     '词频分级词汇三',
                     '词频分级词汇四',
                     'CET-4高频词汇']

        label = wx.StaticText(self, -1, "所属词库：")
        hbox1.Add(label, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        LibComboBox = wx.ComboBox(self,
		                          choices=Lib_Items,
		                          style=wx.CB_READONLY)
        hbox1.Add(LibComboBox, 1, wx.ALIGN_CENTER|wx.ALL, 5)

        vbox.Add(hbox1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        textBold = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/bold16.png'))
        textItalic = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/italic16.png'))
        textUnderline = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/underline16.png'))
        textColor = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/color16.png'))
        textAlighLeft = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/align_left16.png'))
        textAlighCenter = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/align_center16.png'))
        textAlighRight = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/align_right16.png'))
        textList = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/text_list16.png'))
        insertRecord = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/record16.png'))
        insertPicture = wx.BitmapButton(self, -1, wx.Bitmap('images/rich-text/picture16.png'))


        hbox2.Add(textBold, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textItalic, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textUnderline, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textList, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textColor, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textAlighLeft, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textAlighCenter, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(textAlighRight, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(insertPicture, 0, wx.ALIGN_CENTER_VERTICAL)
        hbox2.Add(insertRecord, 1, wx.ALIGN_CENTER_VERTICAL)

        vbox.Add(hbox2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line1 = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        vbox.Add(line1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5)


        vbox1 = wx.BoxSizer(wx.VERTICAL)
        titleText1 = wx.StaticText(self, -1, label="编辑卡片的正面：")
        editCard1 = wx.TextCtrl(self, -1, size=(-1, 100), style=wx.TE_MULTILINE)
        vbox1.Add(titleText1, 0, wx.EXPAND|wx.ALL, 10)
        vbox1.Add(editCard1, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)

        vbox.Add(vbox1, 1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        line2 = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        vbox.Add(line2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT|wx.TOP, 5)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        titleText2 = wx.StaticText(self, -1, label="编辑卡片的反面：")
        editCard2 = wx.TextCtrl(self, -1, size=(-1, 100), style=wx.TE_MULTILINE)
        vbox1.Add(titleText2, 0, wx.EXPAND|wx.ALL, 10)
        vbox1.Add(editCard2, 1, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)

        vbox.Add(vbox2, 1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()

        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_OK, "确定")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL, "取消")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        vbox.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(vbox)
        vbox.Fit(self)
        self.Centre()
        self.Show(True)

# class StartMemo(wx.Dialog):
#    def __init__(self):
#         wx.Dialog.__init__(self, None, -1, '单词卡片详细信息',size=(500, 600),
#                            style=wx.CAPTION
#                                  |wx.SYSTEM_MENU
#                                  |wx.CLOSE_BOX)
#
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         hbox1 = wx.BoxSizer(wx.HORIZONTAL)
#
#         titleText = wx.StaticText(self, -1, "当前记忆词库的名称")
#         backwardBtn = wx.BitmapButton(self, -1, wx.Bitmap("images/32/backward.png"), style=wx.NO_BORDER)
#         moreBtn = wx.BitmapButton(self, -1, wx.Bitmap("images/other-size/more26.png"), style=wx.NO_BORDER)
#
#         hbox1.Add(titleText, 1, wx.ALIGN_CENTRE_VERTICAL)
#         hbox1.Add(backwardBtn, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5)
#         hbox1.Add(moreBtn, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT)
#
#         vbox.Add(hbox1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 8)
#
#         line1 = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
#         vbox.Add(line1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 8)
#
#         gBox1 = wx.GridSizer(1, 2, 3, 3)
#
#         remainingText = [68, 8, 65]
#         text = "剩余的卡片数量："
#
#         for label in remainingText:
#             text += str(label)+"  "
#
#         textLabel = wx.StaticText(self, -1, text)
#         gBox1.Add(textLabel, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_LEFT)
#
#         timeLabel = wx.StaticText(self, -1, "01:09")
#         gBox1.Add(timeLabel, 1, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT)
#
#         vbox.Add(gBox1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
#
#         panel = wx.Panel(self, -1, size=(-1, 300))
#         panel.SetBackgroundColour("white")
#         gBox2 = wx.GridSizer(3, 1, 5, 5)
#
#         frontPageText1 = wx.StaticText(panel, -1, "Lying")
#         frontPageText2 = wx.StaticText(panel, -1, "['la???]")
#         frontPageText3 = wx.StaticText(panel, -1, "")
#         font1 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
#         font2 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False)
#         font3 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
#         frontPageText1.SetFont(font1)
#         frontPageText2.SetFont(font2)
#         frontPageText3.SetFont(font3)
#
#         gBox2.Add(frontPageText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
#         gBox2.Add(frontPageText2, 0, wx.ALIGN_CENTER_HORIZONTAL)
#         gBox2.Add(frontPageText3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
#
#         panel.SetSizer(gBox2)
#
#         vbox.Add(panel, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
#
#         showAnswerBtn = wx.Button(self, -1, "显示答案", size=(-1, 50), style=wx.BORDER_NONE)
#         vbox.Add(showAnswerBtn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, border=5)
#
#         self.SetSizer(vbox)
#         vbox.Fit(self)
#         self.Centre()
#         self.Show(True)

class StartMemo(wx.Dialog):
   def __init__(self):
        wx.Dialog.__init__(self, None, -1, '单词卡片详细信息',size=(500, 600),
                           style=wx.CAPTION
                                 |wx.SYSTEM_MENU
                                 |wx.CLOSE_BOX)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        titleText = wx.StaticText(self, -1, "当前记忆词库的名称")
        backwardBtn = wx.BitmapButton(self, -1, wx.Bitmap("images/32/backward.png"), style=wx.NO_BORDER)
        moreBtn = wx.BitmapButton(self, -1, wx.Bitmap("images/other-size/more26.png"), style=wx.NO_BORDER)

        hbox1.Add(titleText, 1, wx.ALIGN_CENTRE_VERTICAL)
        hbox1.Add(backwardBtn, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5)
        hbox1.Add(moreBtn, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT)

        vbox.Add(hbox1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 8)

        line1 = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        vbox.Add(line1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 8)

        gBox1 = wx.GridSizer(1, 2, 3, 3)

        remainingText = [68, 8, 65]
        text = "剩余的卡片数量："

        for label in remainingText:
            text += str(label)+"  "

        textLabel = wx.StaticText(self, -1, text)
        gBox1.Add(textLabel, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_LEFT)

        timeLabel = wx.StaticText(self, -1, "01:09")
        gBox1.Add(timeLabel, 1, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_RIGHT)

        vbox.Add(gBox1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        panel = wx.Panel(self, -1, size=(400, 300))
        panel.SetBackgroundColour("white")
        gBox2 = wx.GridSizer(3, 1, 5, 5)

        frontPageText1 = wx.StaticText(panel, -1, "Lying")
        frontPageText2 = wx.StaticText(panel, -1, "['la???]")
        frontPageText3 = wx.StaticText(panel, -1, "lie的现在分词")
        font1 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        font2 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False)
        font3 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        frontPageText1.SetFont(font1)
        frontPageText2.SetFont(font2)
        frontPageText3.SetFont(font3)

        gBox2.Add(frontPageText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL)
        gBox2.Add(frontPageText2, 0, wx.ALIGN_CENTER_HORIZONTAL)
        gBox2.Add(frontPageText3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)

        panel.SetSizer(gBox2)

        vbox.Add(panel, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)


        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        restartBtn = wx.Button(self, -1, "<1分钟\n重来", size=(-1, 50))
        normalBtn = wx.Button(self, -1, "<10分钟\n一般", size=(-1, 50))
        simpleBtn = wx.Button(self, -1, "3天\n简单", size=(-1, 50))

        hbox2.Add(restartBtn, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5)
        hbox2.Add(normalBtn, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 2.5)
        hbox2.Add(simpleBtn, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5)

        vbox.Add(hbox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, border=5)

        self.SetSizer(vbox)
        vbox.Fit(self)
        self.Centre()
        self.Show(True)