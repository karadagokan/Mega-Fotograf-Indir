from PyQt5.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import random
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import sys



class Sahibinden:
    def __init__(self,advertisementID):
        self.desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.osUserName = os.path.join(os.getlogin())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless') 
        self.options.add_argument('window-size=1920x1080') 
        self.options.add_argument('disable-gpu') 
        self.browser=webdriver.Chrome('C:/Users/'+self.osUserName+'/Downloads/chromedriver.exe',chrome_options=self.options)
        self.advertisementID = str(advertisementID)
        self.folderPath = self.desktopPath + "\\" + self.advertisementID 


    def goAdvertisement(self):
        self.browser.get("https://www.-.com/")# Website
        time.sleep(1)
        advertisementSearch = self.browser.find_element_by_xpath("//*[@id='searchText']")
        advertisementSearch.send_keys(self.advertisementID)
        advertisementSearch.send_keys(Keys.ENTER)
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='mega-foto']").click()

        megaPhotoLink = self.browser.find_element_by_xpath("//*[@id='megaPhotoBox']/div/div[1]/div/div/div/img")

        nextPhoto = self.browser.find_element_by_class_name("current-mega-image")

        while True:

            randomPhotoName = str((random.uniform(1,10)*10000000000).__round__())

            srcPhoto = megaPhotoLink.get_attribute("src") 

            if not os.path.exists(self.folderPath):
                os.makedirs(self.folderPath)
                urllib.request.urlretrieve(srcPhoto, self.folderPath + "\\" +randomPhotoName+".jpg")  
            else:
                urllib.request.urlretrieve(srcPhoto, self.folderPath + "\\" +randomPhotoName +".jpg")

            time.sleep(1)

            self.browser.find_element_by_xpath("//*[@id='megaPhotoBox']/div/div[1]/div/div/a[2]").click()

            currentPhotoNumber = int(nextPhoto.text)

            if currentPhotoNumber == 1:
                break

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_send.clicked.connect(self.download)

    def download(self):
        advertisementID = self.ui.txt_advertisementID.text()
        sahibinden = Sahibinden(advertisementID)
        sahibinden.goAdvertisement()
        myApp.close()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()



