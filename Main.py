# -*- coding: gbk -*-
import wx
import Frame
def main():
	app = wx.App()
	Frame.PyMemo(None, -1, 'PyMemo', (1000, 620))
	app.MainLoop()
if __name__ == '__main__':
	main()