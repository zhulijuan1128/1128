import wx
import time
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,
            title="Milo Chat",
            size=(520, 450),
            pos=(800, 300))
        panel = wx.Panel(frame, -1)
        labelall = wx.StaticText(panel, -1,
            'All Contents',
            pos=(210, 5))
        self.textall = wx.TextCtrl(panel, -1,
            size=(480, 200),
            pos=(10, 30),
            style=wx.TE_READONLY | wx.TE_MULTILINE)
        labelin = wx.StaticText(panel, -1, 'I Say',
            pos=(230, 230))
        self.textin = wx.TextCtrl(panel, -1,
            size=(480, 100),
            pos=(10, 260),
            style=wx.TE_MULTILINE)

        self.buttonSent = wx.Button(panel, -1, "Sent",
            size=(75, 25), pos=(175, 370))
        self.Bind(wx.EVT_BUTTON,
            self.OnButtonSent, self.buttonSent)
        self.buttonClear = wx.Button(panel, -1, "Clear",
            size=(75, 25), pos=(260, 370))
        self.Bind(wx.EVT_BUTTON,
            self.OnButtonClear, self.buttonClear)

        frame.Show()
        return True

    def OnButtonSent(self, event):
        userinput = self.textin.GetValue()
        self.textin.Clear()
        nowtime = time.ctime()
        inmsg = "You (%s) :\n%s \n" % (nowtime, userinput)
        self.textall.AppendText(inmsg)

    def OnButtonClear(self, event):
        self.textall.Clear()


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
