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
        self.ui.pushButton.clicked.connect(self.recordChecker)

    
    def recordChecker(self,domain):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        response = ""
        txt = []
        i = 0
        try:
            domain = self.ui.lineEdit.text()
            answer = dr.resolve(domain, 'TXT').rrset

            for x in answer:
                t = x.to_text()
                i = t.find('"')
                n = t[i+1:-1]
                if spf in n:
                    if 'include:' in n:
                        for x in n.split():
                            if 'include' in x:
                                txt.append(x.replace('include:', ''))   


            if check in txt:
                self.ui.textBrowser.append(f'{current_time}: {check} record is in {domain}')
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
                                        txt.append(x.replace('include:', ''))   
                                print(txt)
                                print('\n')
                    i += 1

            if check in txt:
                self.ui.textBrowser.append(f'{current_time}: {check} record is in {domain}')
            else: 
                self.ui.textBrowser.append(f'{current_time}: {check} record is not in {domain}')


        except (dr.NoAnswer, dr.NXDOMAIN) as err:
            self.ui.textBrowser.append(f'{current_time}: Unexpected {err=}, {type(err)=}')
        

        



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
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