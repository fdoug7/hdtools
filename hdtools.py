# File: hdtools.py
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import importlib
import dns.resolver as dr   
from datetime import datetime 

check = 'spfva.gofax.com.au'
spf = "v=spf1"




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.DKIMCheck)
        self.ui.pushButton.clicked.connect(self.SPFCheck)

    def log(self, logText):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.logBrowser.append(f'{current_time}: {logText}')

    def DKIMCheck(self, key):
        domain = self.ui.lineEdit.text()
        key1 = 'gfdk1._domainkey.' + domain
        key2 = 'gfdk2._domainkey.' + domain
        try:
            record1 = dr.resolve(key1, 'CNAME').rrset
        except(dr.NoAnswer, dr.NXDOMAIN) as err:
            self.ui.DKIMLabelResult_1.setText(f'Unexpected {err=}, {type(err)=}')
            self.log(f'Unexpected {err=}, {type(err)=}')

        try:
            record2 = dr.resolve(key2, 'CNAME').rrset
        except(dr.NoAnswer, dr.NXDOMAIN) as err:
            self.ui.DKIMLabelResult_2.setText(f'Unexpected {err=}, {type(err)=}')
            self.log(f'Unexpected {err=}, {type(err)=}')


        # //? Cannot access record error is being thrown. Need to correct if statment
        if record1 & record2:
            records = []
            records.append(str(record1).split())
            records.append(str(record2).split())
            if 'CNAME' in records:
                if 'dk1.gofax.com.au.' in records:
                    self.ui.DKIMLabelResult_1.setText(f'{key1} is configured for {domain}')
                    self.log(f'{key1} is configured for {domain}')
                else:
                    self.ui.DKIMLabelResult_1.setText(f'{key1} is NOT configured correctly for {domain}')
                    self.log(f'{key1} is NOT configured correctly for {domain}')
                
                if 'dk2.gofax.com.au.' in records:
                    self.ui.DKIMLabelResult_2.setText(f'{key2} is configured for {domain}')
                    self.log(f'{key2} is configured for {domain}')
                else:
                    self.ui.DKIMLabelResult_2.setText(f'{key2} is NOT configured correctly for {domain}')
                    self.log(f'{key2} is NOT configured correctly for {domain}')
            else:
                self.ui.DKIMLabelResult_1.setText(f'No CNAME records found for {key1}')
                self.ui.DKIMLabelResult_2.setText(f'No CNAME records found for {key2}')
                self.log(f'No CNAME records found for {key1}')
                self.log(f'No CNAME records found for {key2}')
            


    def SPFCheck(self,domain):        
        response = ""
        txt = []
        i = 0
        try:
            domain = self.ui.lineEdit.text()
            self.ui.domainLabelResult.setText(domain)
            answer = dr.resolve(domain, 'TXT').rrset

            for x in answer:
                t = x.to_text()
                i = t.find('"')
                n = t[i+1:-1]
                if spf in n:
                    if 'include:' in n:
                        for x in n.split():
                            if 'include' in x:
                                txt.append(x.split("include:",1)[1])   
                                # txt.append(x.replace('include:', '')) 


            if check in txt:
                self.ui.spfLabelResult.setText(f'{check} record is in {domain}')
                self.log(f'{check} record is in {domain}')
                return
            
            else:
                while i < 1:
                    for x in txt:
                        z = dr.resolve(x, 'TXT').rrset
                        t = z.to_text()
                        i = t.find('"')
                        n = t[i+1:-1]
                        
                        if spf in n:
                            if 'include:' in n:
                                for x in n.split():
                                    if 'include' in x:
                                        txt.append(x.split("include:",1)[1])  

                    i += 1

            if check in txt:
                self.ui.spfLabelResult.setText(f'{check} record is in {domain}')
                self.log(f'{check} record is in {domain}')
            else: 
                self.ui.spfLabelResult.setText(f'{check} record is NOT in {domain}')
                self.log(f'{check} record is NOT in {domain}')


        except (dr.NoAnswer, dr.NXDOMAIN) as err:
            self.ui.domainLabelResult.setText(f'Unexpected {err=}, {type(err)=}')
            self.log(f'Unexpected {err=}, {type(err)=}')

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    sp = app.primaryScreen().availableGeometry()
    window = MainWindow()
    x = sp.right() - window.width() 
    y = sp.bottom() - window.height()
    window.move(x, y)
    window.show()

    sys.exit(app.exec())



# Function to import python scripts into UI as tabs
# def moduleCheck():
#     path = "D:\\code\\HD_Tool\\hdtools\\modules\\"
#     custommodules = []
#     sys.path.insert(1, path)
#     python = False, ()
#     ui = False,()
#     for i in os.listdir(path):
#         if os.path.isdir(path + i):
#             print(path + i)
#             print(os.listdir(path + i))
#             for x in os.listdir(path + i):
#                 if x.endswith('.py'):
#                     python = True, (x)
#                 if x.endswith('.ui'):
#                     ui = True, (x)

#             if ui[0] & python[0] == True:
#                 print (f'Module contains required files \n{python}\n{ui}')
#                 custommodules.append(python[1].split('.')[0])
#                 for module in custommodules:
#                     imodule_obj = __import__(i + '.' + module)
#                     globals()[module] = imodule_obj                                     
#                     recordsChecker
#             else:
#                 print(f'Module does not contain required files. \nPython file: {python} \nUI file: {ui}')


                
#         else:
#             pass