"""
GUI Tutorial from sebsauvage.net/python/gui/


"""

try:
    import wx
except ImportError:
    raise ImportError, "The wxPython module is required to run this program"

class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
