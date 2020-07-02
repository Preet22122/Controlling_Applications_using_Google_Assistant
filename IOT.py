import os
import threading
import csv
import time
# Import library and create instance of REST client.
from Adafruit_IO import Client,Feed,Data
aio = Client('Preetgill', 'be6ca9015da34ef6b66088f23791e6e7')
a=0
while True:
    x = []
    try:
        data = aio.receive_next('preet')
        print('Data value: {0}'.format(data.value))
        if (format(data.value) != ''):
            x.append(format(data.value))
            wr = open("C:\\Users\\hp\\Desktop\\datatemp.csv", "a", newline='')
            obj = csv.writer(wr)
            obj.writerow(x)
            test = aio.feeds('preet')
            aio.send_data(test.key, )
        else:
            print("no data")
    except:
        print("no data")
    ###################################################################
    def notepad():
        os.system(r"C:\Windows\notepad.exe")
    def Fileexplorer():
        os.system(r"C:\Windows\explorer.exe")

    def chrome():
        os.system(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    def netbeans():
         os.system(r"C:\Program Files\NetBeans 8.2\bin\netbeans64.exe")

    def pycharm():
          os.system(r"C:\Program Files\JetBrains\PyCharm 2019.3.1\bin\pycharm64.exe")

    def androidstudio():
          os.system(r"C:\Program Files\Android\Android Studio\bin\studio64.exe")
    if __name__ == "__main__":
        # creating thread
        t1 = threading.Thread(target=notepad)
        t2 = threading.Thread(target=Fileexplorer)
        t3 = threading.Thread(target=chrome)
        t4 = threading.Thread(target=netbeans)
        t5 = threading.Thread(target=pycharm)
        t6 = threading.Thread(target=androidstudio())

    try:
        # Get next unread value from feed 'Test'.
        data = aio.receive_next('preet2')

        # Print the value.
        print('Data value: {0}'.format(data.value))
#######################Notepad#######################################3
        if format(data.value)=="1":
            t1.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value)=="2":
            os.system("TASKKILL /PID notepad.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
##############################################################################

##################File Explorar##############################################
        if format(data.value) == "3":
            t2.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value) == "4":
            os.system("TASKKILL /PID explorer.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
##############################################################################
#####################Chrome###################################################
        if format(data.value) == "5":
            t3.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value) == "6":
            os.system("TASKKILL /PID chrome.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
##############################################################################
#####################Netbeans###################################################
        if format(data.value) == "7":
            t4.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value) == "8":
            os.system("TASKKILL /PID netbeans64.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
##############################################################################
#####################PyCharm###################################################
        if format(data.value) == "9":
            t5.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value) == "10":
            os.system("TASKKILL /PID pycharm64.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
##############################################################################
#####################Android Studio###################################################
        if format(data.value) == "11":
            t6.start()
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
        elif format(data.value) == "12":
            os.system("TASKKILL /PID studio64.exe /T")
            test = aio.feeds('preet2')
            aio.send_data(test.key, 0)
###############################################################################
    except:
        print("no data")
################################################################################

#################################################################################
