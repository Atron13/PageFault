import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore,QtGui
#import fcfsalgorithm


#from firsttemplete import Ui_MainWindow

arrivaltime=[]
turnaroundtime=[]
brusttime=[]
waitingtime=[]
completiontime=[]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi("pagefault.ui", self)
        #self.getbrusttime()
        self.pushButton.clicked.connect(self.getcalculation)
        #self.pushButton2.clicked.connect(self.getghantchart)
        
    
   
    #def getghantchart(self):

        
    def getarrival(self):
        print("arrival")
        return arrivaltime

    def getwaiting(self):
        print("waiting")
        return waitingtime

    def getcompletion(self):
        print("completion")
        return completiontime

    def getbrust(self):
        print("brust")
        return brusttime

    def getturnaround(self):
        print("turnaround")
        return turnaroundtime

    def getcompletion(self):
        process=[1,2,3,4,5,6]
        n=6
        findavgtime(process,n,brusttime)
        findTurnAroundTime(process, n,brusttime,waitingtime,turnaroundtime)
        findWaitingTime(process,n,bt, wt)



    def getcalculation(self):
        b1=self.p1b1id.value()
        b2=self.p2b2id.value()
        b3=self.p3b3id.value()
        b4=self.p4b4id.value()
        b5=self.p5b5id.value()
        b6=self.p6b6id.value()
        global brusttime
        brusttime=[b1,b2,b3,b4,b5,b6]
        c11=b1
        c22=b1+b2
        c33=b1+b2+b3
        c44=b1+b2+b3+b4
        c55=b1+b2+b3+b4+b5
        c66=b1+b2+b3+b4+b5+b6
        global completiontime
        completiontime=[c11,c22,c33,c44,c55,c66]
        self.p1c1id.setText(str(c11))
        self.p2c2id.setText(str(c22))
        self.p3c3id.setText(str(c33))
        self.p4c4id.setText(str(c44))
        self.p5c5id.setText(str(c55))
        self.p6c6id.setText(str(c66))
        self.p1c1id.setAlignment(QtCore.Qt.AlignCenter)
        self.p2c2id.setAlignment(QtCore.Qt.AlignCenter)
        self.p3c3id.setAlignment(QtCore.Qt.AlignCenter)
        self.p4c4id.setAlignment(QtCore.Qt.AlignCenter)
        self.p5c5id.setAlignment(QtCore.Qt.AlignCenter)
        self.p6c6id.setAlignment(QtCore.Qt.AlignCenter)
        

        a1=self.p1a1id.value()
        a2=self.p2a2id.value()
        a3=self.p3a3id.value()
        a4=self.p4a4id.value()
        a5=self.p5a5id.value()
        a6=self.p6a6id.value()
        global arrivaltime
        arrivaltime=[a1,a2,a3,a4,a5,a6]
        global turnaroundtime
        t1=abs(c11-a1)
        t2=abs(c22-a2)
        t3=abs(c33-a3)
        t4=abs(c44-a4)
        t5=abs(c55-a5)
        t6=abs(c66-a6)
        turnaroundtime=[t1,t2,t3,t4,t5,t6]
        #a1=self.p1c1id.text()
        self.p1t1id.setText(str(turnaroundtime[0]))
        self.p2t2id.setText(str(turnaroundtime[1]))
        self.p3t3id.setText(str(turnaroundtime[2]))
        self.p4t4id.setText(str(turnaroundtime[3]))
        self.p5t5id.setText(str(turnaroundtime[4]))
        self.p6t6id.setText(str(turnaroundtime[5]))
        self.p1t1id.setAlignment(QtCore.Qt.AlignCenter)
        self.p2t2id.setAlignment(QtCore.Qt.AlignCenter)
        self.p3t3id.setAlignment(QtCore.Qt.AlignCenter)
        self.p4t4id.setAlignment(QtCore.Qt.AlignCenter)
        self.p5t5id.setAlignment(QtCore.Qt.AlignCenter)
        self.p6t6id.setAlignment(QtCore.Qt.AlignCenter)
        self.getarrival()
        self.getwaiting()
        self.getturnaround()
        self.getbrust()
        self.getcompletion()


        w1=t1-b1
        w2=t2-b2
        w3=t3-b3
        w4=t4-b4
        w5=t5-b5
        w6=t6-b6
        global waitingtime
        #waitingtime.append(abs(w1))
        #waitingtime.append(abs(w2))
        #waitingtime.append(abs(w3))
        #waitingtime.append(abs(w4))
        #waitingtime.append(abs(w5))
        #waitingtime.append(abs(w6))
        waitingtime=[abs(w1),abs(w2),abs(w3),abs(w4),abs(w5),abs(w6)]
        print("waiting time")
        print(waitingtime)
        self.p1w1id.setText(str(waitingtime[0]))
        self.p2w2id.setText(str(waitingtime[1]))
        self.p3w3id.setText(str(waitingtime[2]))
        self.p4w4id.setText(str(waitingtime[3]))
        self.p5w5id.setText(str(waitingtime[4]))
        self.p6w6id.setText(str(waitingtime[5]))
        self.p1w1id.setAlignment(QtCore.Qt.AlignCenter)
        self.p2w2id.setAlignment(QtCore.Qt.AlignCenter)
        self.p3w3id.setAlignment(QtCore.Qt.AlignCenter)
        self.p4w4id.setAlignment(QtCore.Qt.AlignCenter)
        self.p5w5id.setAlignment(QtCore.Qt.AlignCenter)
        self.p6w6id.setAlignment(QtCore.Qt.AlignCenter)

    #def fetch_data1(self):
    	#self.tex_name.setText("PushButton_1 is pressed")

    #def fetch_data2(self):
    	#self.tex_name.setText("PushButton_2 is pressed")

    #def fetch_data3(self):
    	#self.tex_name.setText("PushButton_3 is pressed")

#print ("Hello, world!")
#c1=2c2=2c3=2c4=2c5=2c6=2

#tempcompletion=[c1,c1+c2,c1+c2+c3,c1+c2+c3+c4,c1+c2+c3+c4+c5,c1+c2+c3+c4+c5+c6]
#completiontime=list(tempcompletion)
#print(completiontime[0])
#hello=[]
#hello.append(2)
#hello.append("list")
#print(hello)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()