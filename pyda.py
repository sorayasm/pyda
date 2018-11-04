import wx
import wolframalpha
import wikipedia

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hola, ingresa una pregunta:")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            # WolfranAlpha
            app_id = "393HTE-V99P7HT978"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (answer)
        except:
            # Wikipedia
            input = input.split(" ")
            input = " ".join(input[2:])
            wikipedia.set_lang("es")
            print wikipedia.summary(input, sentences=5).encode("utf8")

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
