# -*- coding: gbk -*-
import time
import wx
import DBFun
# import FrameFun


class AboutDialog(wx.AboutDialogInfo):
    def __init__(self):
        wx.AboutDialogInfo.__init__(self)
        description = "PyMemo是一个基于重复学习原理的记忆软件，简单易用，免费并开源。\n" \
            "PyMeomo以AGPL3协议发布。\n\n" \
            "这是我的一项毕业设计，课题为：基于Python的单词记忆软件开发\n" \
            "GUI库：wxpython 2.7.9\n\n" \
            "开发工具：pyCharm Community Edition 4.0.4\n" \
            "这些图标是来自于不同的来源\n其中大部分来自：http://findicons.com/\n\n" \
            "特别感谢：张治国老师的指导\n\n" \
            "向所有提出过建议，报告Bug的人们致谢！\n\n" \
            "联系：iliuyang@foxmail.com"
        self.SetIcon(wx.Icon('images/64/PyMemo_logo_white.png', wx.BITMAP_TYPE_PNG))
        self.SetName("PyMemo")
        self.SetVersion('1.0')
        self.SetDescription(description)
        self.SetCopyright('(c)2015 刘洋')
        wx.AboutBox(self)


class SettingDialog(wx.Dialog):
    def __init__(self, LIBRARIES, flag):
        wx.Dialog.__init__(self, None, -1, '词库设置', size=(200, 400),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        # global lib_index
        lib_items = ['请选择词库']
        for index, element in enumerate(LIBRARIES):
            lib_items.append(LIBRARIES[element].decode('utf-8'))

        v_box = wx.BoxSizer(wx.VERTICAL)
        panel_combo = wx.Panel(self, -1)
        h_box_combo = wx.BoxSizer(wx.HORIZONTAL)
        lib_text = wx.StaticText(panel_combo, -1, "你想让这些设置应用在哪个词库上？")

        lib_combo_box = wx.ComboBox(panel_combo, choices=lib_items, style=wx.CB_READONLY)
        if flag == -1:
            lib_combo_box.SetSelection(0)
        else:
            lib_index = lib_items.index(LIBRARIES[flag].decode('utf-8'))
            lib_combo_box.SetSelection(lib_index)

        h_box_combo.Add(lib_text, 0, wx.TOP | wx.RIGHT, 10)
        h_box_combo.Add(lib_combo_box, 0, wx.TOP | wx.LEFT, 5)
        panel_combo.SetSizer(h_box_combo)

        v_box.Add(panel_combo, 0, wx.TOP | wx.LEFT | wx.RIGHT, 10)

        line_1 = wx.StaticLine(self, -1, size=(-1, -1), style=wx.LI_HORIZONTAL)
        v_box.Add(line_1, 0, wx.EXPAND | wx.ALL, 10)

        grid_sizer = wx.GridSizer(2, 2, 5, 5)
        # (0, 0)
        panel_left_top = wx.Panel(self)
        preview_setting = wx.StaticBox(panel_left_top, -1, label='学习卡片界面')
        sbs1 = wx.StaticBoxSizer(preview_setting, orient=wx.VERTICAL)

        show_interval = wx.CheckBox(panel_left_top,
                            label='在回答按钮上显示下一次复习时间',
                            style=wx.CHK_3STATE)
        show_rest = wx.CheckBox(panel_left_top,
                            label='在复习的时候显示剩余卡片数',
                            style=wx.CHK_3STATE)
        show_duration = wx.CheckBox(panel_left_top,
                            label='在复习的时候显示所用时间',
                            style=wx.CHK_3STATE)
        show_interval.SetValue(True)
        show_rest.SetValue(True)
        show_duration.SetValue(True)

        sbs1.Add(show_interval, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)
        sbs1.Add(show_rest, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)
        sbs1.Add(show_duration, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)

        panel_left_top.SetSizer(sbs1)

        grid_sizer.Add(panel_left_top, 3, wx.EXPAND | wx.ALL, border=10)

        # (0, 1)
        panel_right_top = wx.Panel(self)
        study_setting = wx.StaticBox(panel_right_top, -1, label='自定义学习卡片')
        sbs2 = wx.StaticBoxSizer(study_setting, orient=wx.VERTICAL)
        grid1 = wx.FlexGridSizer(0, 2, 0, 0)

        # group of controls:
        self.group_ctrl = []
        text1 = wx.StaticText(panel_right_top, label="每日学习卡片上限（张）")
        text2 = wx.StaticText(panel_right_top, label="每日复习卡片上限（张）")
        text3 = wx.StaticText(panel_right_top, label="超时显示卡片反面（秒）")

        study_limit = wx.SpinCtrl(panel_right_top, -1)
        study_limit.SetRange(1, 200)
        study_limit.SetValue(50)

        review_limit = wx.SpinCtrl(panel_right_top, -1)
        review_limit.SetRange(1, 200)
        review_limit.SetValue(50)

        deadline_limit = wx.SpinCtrl(panel_right_top, -1)
        deadline_limit.SetRange(1, 60)
        deadline_limit.SetValue(30)

        self.group_ctrl.append((text1, study_limit))
        self.group_ctrl.append((text2, review_limit))
        self.group_ctrl.append((text3, deadline_limit))

        for text, spin_ctrl in self.group_ctrl:
            grid1.Add(text, 0, wx.ALIGN_CENTRE | wx.LEFT | wx.RIGHT | wx.TOP, 5)
            grid1.Add(spin_ctrl, 0, wx.ALIGN_CENTRE | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        sbs2.Add(grid1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        panel_right_top.SetSizer(sbs2)
        grid_sizer.Add(panel_right_top, 1, wx.EXPAND | wx.ALL, border=10)

        # (1, 0)
        panel_left_bottom = wx.Panel(self)
        order_setting = wx.StaticBox(panel_left_bottom, -1, label='学习卡片的顺序')
        sbs3 = wx.StaticBoxSizer(order_setting, orient=wx.VERTICAL)

        old_after_new = wx.RadioButton(panel_left_bottom, -1, "新卡片学习完之后再复习旧卡片")
        new_after_old = wx.RadioButton(panel_left_bottom, -1, "旧卡片复习完之后再学习新卡片")
        new_or_old = wx.RadioButton(panel_left_bottom, -1, "新旧卡片交替出现")

        new_or_old.SetValue(True)

        sbs3.Add(old_after_new, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)
        sbs3.Add(new_after_old, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)
        sbs3.Add(new_or_old, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM, border=10)

        panel_left_bottom.SetSizer(sbs3)

        grid_sizer.Add(panel_left_bottom, 1, wx.EXPAND | wx.ALL, border=10)

        # (1, 1)
        panel_right_bottom = wx.Panel(self)
        font_setting = wx.StaticBox(panel_right_bottom, -1, label='字体设置')
        sbs4 = wx.StaticBoxSizer(font_setting, orient=wx.VERTICAL)
        # h_box_1 = wx.BoxSizer(wx.HORIZONTAL)
        h_box_2 = wx.BoxSizer(wx.HORIZONTAL)

        # font_family_list = ['font-family-one',
        #                    'font-family-two',
        #                    'font-family-three',
        #                    'font-family-flour']
        # font_family_text = wx.StaticText(panel_right_bottom, -1, "字体：",)
        # font_family = wx.Choice(panel_right_bottom, -1, choices=font_family_list)
        #
        # h_box_1.Add(font_family_text, 1, wx.LEFT | wx.TOP, border=10)
        # h_box_1.Add(font_family, 3, wx.TOP, border=10)

        font_size_text = wx.StaticText(panel_right_bottom, -1, "字号：")
        font_size = wx.SpinCtrl(panel_right_bottom, -1)
        font_size.SetRange(1, 30)
        font_size.SetValue(12)

        h_box_2.Add(font_size_text, 1, wx.LEFT | wx.TOP, border=10)
        h_box_2.Add(font_size, 3, wx.TOP, border=10)

        # sbs4.Add(h_box_1, wx.LEFT, border=5)
        sbs4.Add(h_box_2, wx.LEFT, border=5)

        panel_right_bottom.SetSizer(sbs4)
        grid_sizer.Add(panel_right_bottom, 1, wx.EXPAND | wx.ALL, border=10)
        v_box.Add(grid_sizer, 1)

        # (2, 1)
        h_box = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(self, -1, label='确定')
        apply_button = wx.Button(self, -1, label="应用")
        close_button = wx.Button(self, -1, label='关闭')
        h_box.Add(ok_button, 1, wx.RIGHT, border=5)
        h_box.Add(apply_button, 1, wx.RIGHT, border=5)
        h_box.Add(close_button, 1, wx.RIGHT, border=10)

        v_box.Add(h_box, 0, wx.ALIGN_RIGHT | wx.BOTTOM, border=10)

        self.Bind(wx.EVT_BUTTON, self.on_close, close_button)

        self.SetSizer(v_box)
        self.Fit()
        self.Centre()
        self.Show(True)

    def on_close(self, e):
        self.Destroy()
        e.Skip()


class CardInfoDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '单词卡片详细信息', size=(300, 400),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        info_dir = {1: ['添加时间', '2015-3-24'],
                   2: ['首次学习', '2015-3-24'],
                   3: ['最近复习', '2015-3-24'],
                   4: ['到期时间', '2015-3-24'],
                   5: ['间隔', '9天'],
                   6: ['复习次数', '2'],
                   7: ['错误次数', '2'],
                   8: ['所属词库', 'CET-4高频词汇'],
                   9: ['卡片ID', '15456468465'],
                   10: ['词库ID', '564645635218']}

        v_box = wx.BoxSizer(wx.VERTICAL)
        head_title = wx.StaticText(panel, label="单词卡片的详细信息")
        add_time = wx.StaticText(panel, label=info_dir[1][0] + " " * 6 + info_dir[1][1])
        first_study_time = wx.StaticText(panel, label=info_dir[2][0] + " " * 6 + info_dir[2][1])
        review_time = wx.StaticText(panel, label=info_dir[3][0] + " " * 6 + info_dir[3][1])
        dead_line = wx.StaticText(panel, label=info_dir[4][0] + " " * 6 + info_dir[4][1])
        interval_day = wx.StaticText(panel, label=info_dir[5][0] + " " * 6 + info_dir[5][1])
        review_num = wx.StaticText(panel, label=info_dir[6][0] + " " * 6 + info_dir[6][1])
        error_num = wx.StaticText(panel, label=info_dir[7][0] + " " * 6 + info_dir[7][1])
        belong_lib = wx.StaticText(panel, label=info_dir[8][0] + " " * 6 + info_dir[8][1])
        record_id = wx.StaticText(panel, label=info_dir[9][0] + " " * 6 + info_dir[9][1])
        lib_id = wx.StaticText(panel, label=info_dir[10][0] + " " * 6 + info_dir[10][1])

        v_box.Add(head_title, 1, wx.CENTER | wx.TOP, border=10)
        v_box.Add(add_time, 1, wx.ALL, border=10)
        v_box.Add(first_study_time, 1, wx.ALL, border=10)
        v_box.Add(review_time, 1, wx.ALL, border=10)
        v_box.Add(dead_line, 1, wx.ALL, border=10)
        v_box.Add(interval_day, 1, wx.ALL, border=10)
        v_box.Add(review_num, 1, wx.ALL, border=10)
        v_box.Add(error_num, 1, wx.ALL, border=10)
        v_box.Add(belong_lib, 1, wx.ALL, border=10)
        v_box.Add(record_id, 1, wx.ALL, border=10)
        v_box.Add(lib_id, 1, wx.ALL, border=10)

        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)


class AddNewLib(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '新建词库', size=(-1, 270),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        v_box = wx.BoxSizer(wx.VERTICAL)
        name_text = wx.StaticText(panel, -1, "词库名称：")
        lib_name = wx.TextCtrl(panel, -1, "", style=wx.TE_CAPITALIZE)

        desc_text = wx.StaticText(panel, -1, "词库描述：")
        lib_desc = wx.TextCtrl(panel, -1, "", size=(-1, 80), style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL)

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(panel, -1, label='确定')
        cancel_button = wx.Button(panel, wx.ID_CANCEL, label='取消')
        self.Bind(wx.EVT_BUTTON, lambda evt, name=lib_name, desc=lib_desc: self.on_submit(evt, name, desc), ok_button)
        h_box.Add(ok_button, 1, wx.RIGHT, border=5)
        h_box.Add(cancel_button, 1)

        v_box.Add(name_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        v_box.Add(lib_name, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(desc_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(lib_desc, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(h_box, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)

    def on_submit(self, evt, name, desc):
        lib_name = name.GetValue().encode('utf-8')
        lib_desc = desc.GetValue().encode('utf-8')

        next_lib_id = int(DBFun.max_lib('libId')) + 1
        lib_id = str(next_lib_id).zfill(3)
        create_time = time.strftime('%Y/%m/%d %H:%I:%M:%S', time.localtime(time.time()))

        insert_lib_sql = "INSERT INTO library(libId, name, libDesc, createTime) VALUES ('" + lib_id + "', '" + lib_name + "', '" +\
                         lib_desc + "', '" + create_time + "')"
        conn = DBFun.connect_db('db_pymemo.db')
        if DBFun.update(conn, insert_lib_sql):
            conn.commit()

        conn.close()
        self.Close()


class RenameLib(wx.Dialog):
    def __init__(self, old_name, old_desc, lib_id):
        wx.Dialog.__init__(self, None, -1, '修改' + old_name + '名称和描述', size=(-1, 270),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        v_box = wx.BoxSizer(wx.VERTICAL)

        name_text = wx.StaticText(panel, -1, "词库名称：")
        lib_name = wx.TextCtrl(panel, -1, old_name, style=wx.TE_CAPITALIZE)

        desc_text = wx.StaticText(panel, -1, "词库描述：")
        lib_desc = wx.TextCtrl(panel, -1, old_desc, size=(-1, 80), style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL)

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(panel, -1, label='确定')
        cancel_button = wx.Button(panel, wx.ID_CANCEL, label='取消')
        self.Bind(wx.EVT_BUTTON, lambda evt, name=lib_name, desc=lib_desc, i=lib_id: self.on_submit(evt, name, desc, i), ok_button)
        h_box.Add(ok_button, 1, wx.RIGHT, border=5)
        h_box.Add(cancel_button, 1)

        v_box.Add(name_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        v_box.Add(lib_name, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(desc_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(lib_desc, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(h_box, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)

    def on_submit(self, evt, name, desc, i):
        lib_name = name.GetValue().encode('utf-8')
        lib_desc = desc.GetValue().encode('utf-8')
        update_lib_sql = "UPDATE library SET " \
                         "name = '" + lib_name + "', libDesc = '" + lib_desc + "' WHERE libId = '" + i + "'"
        conn = DBFun.connect_db('db_pymemo.db')
        conn.text_factory = str
        if DBFun.update(conn, update_lib_sql):
            print 'update succeed !'
            conn.commit()
        else:
            print 'update fault !'
        conn.close()
        self.Close()


class LibInfo(wx.Dialog):
    def __init__(self, lib_info):
        wx.Dialog.__init__(self, None, -1, lib_info[1].decode('utf-8') + '词库的信息', size=(-1, 300),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)

        v_box = wx.BoxSizer(wx.VERTICAL)

        panel = wx.Panel(self, -1, style=wx.BORDER)
        panel.SetBackgroundColour('white')
        v_box_panel = wx.BoxSizer(wx.VERTICAL)
        lib_id = wx.StaticText(panel, -1, '词库ID：' + lib_info[0])
        name_text = wx.StaticText(panel, -1, '词库名称：' + lib_info[1].decode('utf-8'))
        desc_text = wx.StaticText(panel, -1, '词库描述：' + lib_info[2].decode('utf-8'))
        create_time = wx.StaticText(panel, -1, '创建时间：' + str(lib_info[3]))
        max_reviews = wx.StaticText(panel, -1, '每日复习：' + str(lib_info[4]))
        max_new = wx.StaticText(panel, -1, '每日学习：' + str(lib_info[5]))
        easy_interval = wx.StaticText(panel, -1, '简单间隔：' + str(lib_info[6]) + '（天）' )
        max_interval = wx.StaticText(panel, -1, '最大间隔：' + str(lib_info[7]) + '（天）')
        max_time = wx.StaticText(panel, -1, '最长回答：' + str(lib_info[8]) + '（秒）')
        is_show_timer = wx.StaticText(panel, -1, '显示计时器：' + lib_info[9])


        v_box_panel.Add(lib_id, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        v_box_panel.Add(name_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(desc_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(create_time, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(max_reviews, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(max_new, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(easy_interval, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(max_interval, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(max_time, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box_panel.Add(is_show_timer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        panel.SetSizer(v_box_panel)

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(self, wx.ID_OK, label='确定')
        h_box.Add(ok_button, 1, wx.RIGHT, border=5)

        v_box.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        v_box.Add(h_box, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        self.SetSizer(v_box)
        self.Centre()
        self.Show(True)


class DeleteLib(wx.Dialog):
    def __init__(self, old_name, lib_id):
        wx.Dialog.__init__(self, None, -1, '删除' + old_name + '词库', size=(-1, 180),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('white')
        v_box = wx.BoxSizer(wx.VERTICAL)
        info_text = wx.StaticText(panel, -1, old_name + '词库将被删除，词库中的记录会被转移至孤儿院。\n你确定要这样做么？')

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(panel, -1, label='确定')
        cancel_button = wx.Button(panel, wx.ID_CANCEL, label='取消')
        h_box.Add(ok_button, 1, wx.RIGHT, border=5)
        h_box.Add(cancel_button, 1)

        v_box.Add(info_text, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP , 20)
        v_box.Add(h_box, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)


class Export(wx.DirDialog):
    def __init__(self, parent):
        wx.DirDialog.__init__(self, parent, "请选择一个文件来保存导出的词库：",
                          style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        self.CentreOnParent()
        self.Show(True)


class Import(wx.FileDialog):
    def __init__(self, parent):
        wx.FileDialog.__init__(self, parent, "选择导入的词库文件",
                               wildcard="BMP and GIF files (*.bmp*.gif)|*.bmp*.gif|PNG files (*.png)|*.png",
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_CHANGE_DIR
                               )
        self.Centre()
        self.Show(True)


class AddNewRecord(wx.Dialog):
    def __init__(self, LIBRARIES, flag):
        wx.Dialog.__init__(self, None, -1, '增加一条记录', size=(-1, 350),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        global lib_id
        v_box = wx.BoxSizer(wx.VERTICAL)
        h_box_info = wx.BoxSizer(wx.HORIZONTAL)

        lib_items = ['请选择词库']
        for index, element in enumerate(LIBRARIES):
            lib_items.append(LIBRARIES[element].decode('utf-8'))

        lib_combo_box = wx.ComboBox(panel, choices=lib_items, style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, lambda evt, ob=lib_combo_box: self.test(evt, ob, lib_id), lib_combo_box)
        global lib_id
        if flag == -1:
            lib_index = 0
            self.set_lib_id(-1)
        else:
            lib_index = lib_items.index(LIBRARIES[flag].decode('utf-8'))
            self.set_lib_id(str(flag).zfill(3))
        lib_combo_box.SetSelection(lib_index)

        # preview = wx.BitmapButton(panel, -1, wx.Bitmap('images/32/preview.png'), size=(32, 32), style=wx.NO_BORDER)
        h_box_info.Add(lib_combo_box, 1, wx.TOP, 10)
        # h_box_info.Add(preview, 0, wx.ALIGN_RIGHT | wx.TOP, 6)

        name_text = wx.StaticText(panel, -1, "问题（正面）：")
        record_ques = wx.TextCtrl(panel, -1, "", size=(-1, 80), style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL)

        desc_text = wx.StaticText(panel, -1, "答案（反面）：")
        record_ans = wx.TextCtrl(panel, -1, "", size=(-1, 80), style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL)

        h_box_btn = wx.BoxSizer(wx.HORIZONTAL)
        ok_button = wx.Button(panel, -1, label='确定')
        close_button = wx.Button(panel, wx.ID_CANCEL, label='取消')

        self.Bind(wx.EVT_BUTTON, lambda evt, ques=record_ques, ans=record_ans: self.on_submit(evt, ques, ans), ok_button)
        h_box_btn.Add(ok_button, 1, wx.RIGHT, border=5)
        h_box_btn.Add(close_button, 1)

        v_box.Add(h_box_info, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(name_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        v_box.Add(record_ques, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(desc_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(record_ans, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(h_box_btn, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)

    @staticmethod
    def set_lib_id(value):
        lib_id = value

    @staticmethod
    def get_lib_id():
        return lib_id

    def on_submit(self, evt, ques, ans):
        if self.get_lib_id() == -1:
            msg_dlg = wx.MessageDialog(self, '请选择词库！',
                           '提示',
                           wx.OK | wx.ICON_WARNING)
            msg_dlg.ShowModal()
            msg_dlg.Destroy()
        else:
            record_ques = ques.GetValue().encode('utf-8')
            record_ans = ans.GetValue().encode('utf-8')
            next_record_id = int(DBFun.max_record('recordId')) + 1
            record_id = str(next_record_id).zfill(5) + lib_id
            print record_id
            create_time = time.strftime('%Y/%m/%d %H:%I:%M:%S', time.localtime(time.time()))

            # insert_lib_sql = "INSERT INTO record(libId, name, libDesc, createTime) VALUES ('" + lib_id + "', '" + lib_name + "', '" +\
            #                  lib_desc + "', '" + create_time + "')"

    def test(self, evt, ob, lib_id):
        lib_name = ob.GetValue()
        print lib_name
        select_sql = "SELECT libId FROM library WHERE name = '" + lib_name + "'"
        conn = DBFun.connect_db('db_pymemo.db')
        cursor = DBFun.select(conn, select_sql)
        if cursor == None:
            print '请选择词库'
        else:
            for rows in cursor:
                self.set_lib_id(rows[0])
                print rows[0]
        DBFun.close_db(conn)
        print self.get_lib_id()

class MemoQues(wx.Dialog):
    """
    这里有些问题，应该只刷新 panel_word 和 panel_btn
    而不是销毁当前的对话框，重新绘制一个新的！！
    """
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '学习', size=(-1, 470),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)

        panel = wx.Panel(self, -1)
        font_ques = wx.Font(14, wx.FONTFAMILY_DEFAULT,
                            wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD,
                            faceName="Consolas",
                            underline=False)
        font_api = wx.Font(13, wx.FONTFAMILY_DEFAULT,
                           wx.FONTSTYLE_ITALIC,
                           wx.FONTWEIGHT_NORMAL,
                           faceName="Consolas",
                           underline=False)
        # font_ans = wx.Font(12, wx.FONTFAMILY_DEFAULT,
        #                    wx.FONTSTYLE_NORMAL,
        #                    wx.FONTWEIGHT_NORMAL,
        #                    faceName="Consolas",
        #                    underline=False)

        # ------

        v_box = wx.BoxSizer(wx.VERTICAL)

        h_box_title = wx.BoxSizer(wx.HORIZONTAL)
        lib_name = wx.StaticText(panel, -1, "当前学习的词库名称")
        backward = wx.BitmapButton(panel, -1, wx.Bitmap('images/32/backward.png'), style=wx.NO_BORDER)
        more = wx.BitmapButton(panel, -1, wx.Bitmap('images/other-size/more26.png'), style=wx.NO_BORDER)

        h_box_title.Add(lib_name, 1, wx.TOP | wx.RIGHT, 10)
        h_box_title.Add(backward, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, 5)
        h_box_title.Add(more, 0, wx.ALIGN_RIGHT | wx.LEFT | wx.TOP, 5)

        # ------

        line_1 = wx.StaticLine(panel, -1, size=(-1, -1), style=wx.LI_HORIZONTAL)

        # ------

        h_box_info = wx.BoxSizer(wx.HORIZONTAL)
        rest_list = [68, 8, 65]
        rest_text = "剩余卡片："

        for label in rest_list:
            rest_text += str(label) + " " * 2

        rest_label = wx.StaticText(panel, -1, rest_text)
        duration_label = wx.StaticText(panel, -1, "01:09")

        h_box_info.Add(rest_label, 1, wx.RIGHT, 10)
        h_box_info.Add(duration_label, 0, wx.ALIGN_RIGHT)

        # ------

        ques = "general"
        ipa = "['d?en?r?l]".encode('utf-8')
        # ans = "[n.] 将军\n[adj.]全体的，总的，普遍的"
        panel_word = wx.Panel(panel, -1, size=(-1, 300), style=wx.BORDER_THEME)
        panel_word.SetBackgroundColour('white')
        v_box_pw = wx.BoxSizer(wx.VERTICAL)
        ques_text = wx.StaticText(panel_word, -1, ques)
        ipa_text = wx.StaticText(panel_word, -1, ipa)
        # ans_text = wx.StaticText(panel_word, -1, ans)
        ques_text.SetFont(font_ques)
        ipa_text.SetFont(font_api)
        # ans_text.SetFont(font_ans)
        line_2 = wx.StaticLine(panel_word, -1, size=(-1, -1), style=wx.LI_HORIZONTAL)

        v_box_pw.Add(ques_text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 20)
        v_box_pw.Add(ipa_text, 0, wx.ALIGN_CENTER_HORIZONTAL)
        v_box_pw.Add(line_2, 0, wx.EXPAND | wx.ALL, 10)
        # v_box_pw.Add(ans_text, 1, wx.ALIGN_CENTER_HORIZONTAL)
        panel_word.SetSizer(v_box_pw)

        # ---------

        panel_btn = wx.Panel(panel, -1)
        h_box_btn = wx.BoxSizer(wx.HORIZONTAL)
        show_ans = wx.Button(panel_btn, -1, "显示答案")
        self.Bind(wx.EVT_BUTTON, self.on_show_ans, show_ans)
        h_box_btn.Add(show_ans, 1, wx.EXPAND)
        panel_btn.SetSizer(h_box_btn)

        v_box.Add(h_box_title, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(line_1, 0, wx.EXPAND)
        v_box.Add(h_box_info, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(panel_word, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(panel_btn, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)

    def on_show_ans(self, evt):
        self.Destroy()
        dlg = MemoAns()
        dlg.ShowModal()
        dlg.Destroy()
        evt.Skip()


class MemoAns(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, '学习', size=(-1, 470),
                           style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        panel = wx.Panel(self, -1)
        font_ques = wx.Font(14, wx.FONTFAMILY_DEFAULT,
                            wx.FONTSTYLE_NORMAL,
                            wx.FONTWEIGHT_BOLD,
                            faceName="Consolas",
                            underline=False)
        font_api = wx.Font(13, wx.FONTFAMILY_DEFAULT,
                           wx.FONTSTYLE_ITALIC,
                           wx.FONTWEIGHT_NORMAL,
                           faceName="Consolas",
                           underline=False)
        font_ans = wx.Font(12, wx.FONTFAMILY_DEFAULT,
                           wx.FONTSTYLE_NORMAL,
                           wx.FONTWEIGHT_NORMAL,
                           faceName="Consolas",
                           underline=False)

        # ------

        v_box = wx.BoxSizer(wx.VERTICAL)

        h_box_title = wx.BoxSizer(wx.HORIZONTAL)
        lib_name = wx.StaticText(panel, -1, "当前学习的词库名称")
        backward = wx.BitmapButton(panel, -1, wx.Bitmap('images/32/backward.png'), style=wx.NO_BORDER)
        more = wx.BitmapButton(panel, -1, wx.Bitmap('images/other-size/more26.png'), style=wx.NO_BORDER)

        h_box_title.Add(lib_name, 1, wx.TOP | wx.RIGHT, 10)
        h_box_title.Add(backward, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, 5)
        h_box_title.Add(more, 0, wx.ALIGN_RIGHT | wx.LEFT | wx.TOP, 5)

        # ------

        line_1 = wx.StaticLine(panel, -1, size=(-1, -1), style=wx.LI_HORIZONTAL)

        # ------

        h_box_info = wx.BoxSizer(wx.HORIZONTAL)
        rest_list = [68, 8, 65]
        rest_text = "剩余卡片："
        for label in rest_list:
            rest_text += str(label) + " " * 2

        rest_label = wx.StaticText(panel, -1, rest_text)
        duration_label = wx.StaticText(panel, -1, "01:09")

        h_box_info.Add(rest_label, 1, wx.RIGHT, 10)
        h_box_info.Add(duration_label, 0, wx.ALIGN_RIGHT)

        # ------

        ques = "general"
        ipa = "['d?en?r?l]".encode('utf-8')
        ans = "[n.] 将军\n[adj.]全体的，总的，普遍的"
        panel_word = wx.Panel(panel, -1, size=(-1, 300), style=wx.BORDER_THEME)
        panel_word.SetBackgroundColour('white')
        v_box_pw = wx.BoxSizer(wx.VERTICAL)
        ques_text = wx.StaticText(panel_word, -1, ques)
        ipa_text = wx.StaticText(panel_word, -1, ipa)
        ans_text = wx.StaticText(panel_word, -1, ans)
        ques_text.SetFont(font_ques)
        ipa_text.SetFont(font_api)
        ans_text.SetFont(font_ans)
        line_2 = wx.StaticLine(panel_word, -1, size=(-1, -1), style=wx.LI_HORIZONTAL)

        v_box_pw.Add(ques_text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 20)
        v_box_pw.Add(ipa_text, 0, wx.ALIGN_CENTER_HORIZONTAL)
        v_box_pw.Add(line_2, 0, wx.EXPAND | wx.ALL, 10)
        v_box_pw.Add(ans_text, 1, wx.ALIGN_CENTER_HORIZONTAL)
        panel_word.SetSizer(v_box_pw)

        # ---------

        panel_btn = wx.Panel(panel, -1)
        h_box_btn = wx.BoxSizer(wx.HORIZONTAL)
        again = wx.Button(panel_btn, -1, "重来")
        hard = wx.Button(panel_btn, -1, "困难")
        good = wx.Button(panel_btn, -1, "一般")
        easy = wx.Button(panel_btn, -1, "简单")

        self.Bind(wx.EVT_BUTTON, self.on_again, again)
        self.Bind(wx.EVT_BUTTON, self.on_hard, hard)
        self.Bind(wx.EVT_BUTTON, self.on_good, good)
        self.Bind(wx.EVT_BUTTON, self.on_easy, easy)

        h_box_btn.Add(again, 1, wx.EXPAND | wx.RIGHT, 5)
        h_box_btn.Add(hard, 1, wx.EXPAND | wx.RIGHT, 5)
        h_box_btn.Add(good, 1, wx.EXPAND | wx.RIGHT, 5)
        h_box_btn.Add(easy, 1, wx.EXPAND)
        panel_btn.SetSizer(h_box_btn)

        v_box.Add(h_box_title, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(line_1, 0, wx.EXPAND)
        v_box.Add(h_box_info, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 10)
        v_box.Add(panel_word, 0, wx.EXPAND | wx.ALL, 10)
        v_box.Add(panel_btn, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(v_box)
        self.Centre()
        self.Show(True)

    def on_again(self, evt):
        pass

    def on_hard(self, evt):
        pass

    def on_good(self, evt):
        pass

    def on_easy(self, evt):
        pass