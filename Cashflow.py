# This software is a GUI connected to a database for expense management
import sqlite3
import wx
from datetime import datetime

# Now let's implement the basic GUI in wxpython
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size = (600, 480))

        panel = MyPanel(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent = None, title = "Cashflow")
        self.frame.Show()
        
        return True

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        wrapper = wx.BoxSizer(wx.VERTICAL)
        insert_sizer = wx.StaticBoxSizer(wx.StaticBox(self, label = "Insertion"), wx.VERTICAL)
        self.name = wx.StaticText(self, label = "Name")
        self.name_entry = wx.TextCtrl(self, size = (120,20))

        # It's the time for a radio button that tracks whether the cash is flowing in (revenue) or out (expense)
        self.flow_type = wx.StaticText(self, label = "Flow Type")
        radio_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.flow_in_rb = wx.RadioButton(self, label = "In", style = wx.RB_GROUP)
        self.flow_out_rb = wx.RadioButton(self, label = "Out") 

        self.type_text = wx.StaticText(self, label = "Transaction Type")
        self.combo = wx.ComboBox(self, choices = type_list)

        self.description_text = wx.StaticText(self, label = "Transaction Description")
        self.description_entry = wx.TextCtrl(self, size = (120,40))

        self.amount_text = wx.StaticText(self, label = "Expense Amount")
        self.amount_entry = wx.TextCtrl(self, size = (40, 20))

        self.confirm_btn = wx.Button(self, label = "Confirm and Insert")
        self.confirm_btn.Bind(wx.EVT_BUTTON, self.onInsertClick)

        self.date_text = wx.StaticText(self, label = "Date (Y-M-D)")
        self.date_entry = wx.TextCtrl(self, size = (80, 20))

        wrapper.Add(insert_sizer, flag = wx.ALL | wx.CENTER, border = 10)
        insert_sizer.Add(self.name, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.name_entry, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.flow_type, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(radio_sizer, flag = wx.ALL | wx.CENTER, border = 2)
        radio_sizer.Add(self.flow_in_rb, flag = wx.ALL | wx.CENTER, border = 2)
        radio_sizer.Add(self.flow_out_rb, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.type_text, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.combo, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.description_text, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.description_entry, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.amount_text, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.amount_entry, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.date_text, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.date_entry, flag = wx.ALL | wx.CENTER, border = 2)
        insert_sizer.Add(self.confirm_btn, flag = wx.ALL | wx.CENTER, border = 2)

        self.SetSizer(wrapper)
    
    def onCombo(self):
        return self.combo.GetValue()

    def checkFlow(self):
        if (self.flow_in_rb.GetValue()):
            return 0
        else:
            return 1

    def checkName(self):
        return self.name_entry.GetValue()

    def checkDescription(self):
        return self.description_entry.GetValue()

    def checkAmount(self):
        return self.amount_entry.GetValue()
    
    def checkDate(self):
        return self.date_entry.GetValue()

    def onInsertClick(self, evt):
        # Check input values and store them into values list 
        inout = MyPanel.checkFlow(self)
        transaction_type = MyPanel.onCombo(self)
        name = MyPanel.checkName(self)
        description = MyPanel.checkDescription(self)
        amount = MyPanel.checkAmount(self)
        date = MyPanel.checkDate(self)
        if date == "":
            date = datetime.today().strftime('%Y-%m-%d')
        values = [name, inout, transaction_type, description, amount, date]

        # Insert values in the database
        c.execute("INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?)".format(table_name), values)

# Generic functions definition
def checkIfTableExists(c, table_name):
    c.execute("SELECT count(name) FROM sqlite_master WHERE TYPE = 'table' AND name = '{}'".format(table_name))
    check_result = list(c.fetchone())
    if check_result[0] == 1:
        return True
    else:
        return False

# Still have to add a date field (also in the GUI)
def createTable(c, table_name):
    c.execute("""CREATE TABLE {} ( 
        name text,
        inout NULL,
        type text,
        description text,
        amount real,
        date text
    )""".format(table_name))

# Let's connect to the database, or create one if it doesn't exist (same with the cashflow table)
conn = sqlite3.connect("CashflowDB")
c = conn.cursor()
table_name = "cashflow"
if (not checkIfTableExists(c, table_name)):
    createTable(c, table_name)

# Now let's define the expense variables, ordered from most to least valuable (definitely arbitrary ranking)
type_list = ["groceries", "education", "investments", "rent", "utilities", "mortgage", "gifts", "subscriptions" , "entertainment", "eat and drink"]

# Let's start the GUI mainloop
app = MyApp()
app.MainLoop()

conn.commit()
conn.close()