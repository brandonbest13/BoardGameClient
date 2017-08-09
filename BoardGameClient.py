import sys
import sqlite3

## Change these::
from PyQt5.QtCore import *
from PyQt5.QtGui import * #QWidget, 
from PyQt5.Qt import *


class stackedExample(QWidget):

   def __init__(self):
      super(stackedExample, self).__init__()
      self.conn = sqlite3.connect("GT_GGI.db")
      self.stack0 = QWidget()
      self.stack1 = QWidget()
      self.stack2 = QWidget()
      self.stack3 = QWidget()

      self.Stack = QStackedWidget(self)
      self.Stack.addWidget(self.stack0)
      self.Stack.addWidget(self.stack1)
      self.Stack.addWidget(self.stack2)
      self.Stack.addWidget(self.stack3)

      self.loginUI()
      # self.listViewUI\)

      self.setWindowTitle("GT Gamer's Guild Inventory")
      self.setGeometry(300, 300, 300, 200)
      self.show()

   def loginUI(self):
      hbox = QHBoxLayout(self)
      hbox.addWidget(self.Stack)
      # self.stack0.setLayout(hbox)    problems.
      uLabel = Label("Username: ")
      pLabel = Label("Password: ")
      self.stack0.addWidgets(uLabel, pLabel)




   def stack1UI(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      #self.setTabText(0,"Contact Details")
      self.stack1.setLayout(layout)

   def stack2UI(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())

      self.stack2.setLayout(layout)

   def stack3UI(self):
      layout = QHBoxLayout()
      layout.addWidget(QLabel("subjects"))
      layout.addWidget(QCheckBox("Physics"))
      layout.addWidget(QCheckBox("Maths"))
      self.stack3.setLayout(layout)

   def display(self,i):
      self.Stack.setCurrentIndex(i)
      
    """ sqlite elements/methods
    """
    def genDB(self):
         sql = """ CREATE TABLE IF NOT EXISTS BoardGames (
            GameID int PRIMARY KEY,
            Title varchar(255) NOT NULL,
            Condition int,
            Rating int,
            Avail boolean,
            Img text);
            """
         cur = self.conn.cursor()
         cur.execute(sql)
   
   def selectColumn(self, str):
      cur = self.conn.cursor()
      sql = "SELECT {} FROM BoardGames".format(str)
      return cur.execute(sql).fetchall()
   
   
   

def main():
   app = QApplication([])
   ex = stackedExample()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
