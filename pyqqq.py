import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
   def __init__(self):
      super().__init__()
      #Add a title
      self.setWindowTitle("windowew")

      #Set Layout
      self.setLayout(qtw.QVBoxLayout())

      #Create a label

      my_label = qtw.QLabel("Hello World! Whats your name")
      self.layout().addWidget(my_label)

      #change font size of label
      my_label.setFont(qtg.QFont('Helvetica', 18))

      # create an entry box
      my_entry = qtw.QLineEdit()
      my_entry.setObjectName("name_field")
      my_entry.setText("")
      self.layout().addWidget(my_entry)

      #Create a button
      my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
      self.layout().addWidget(my_button)

      #show the app
      self.show()

      def press_it():
         my_label.setText(f'Hello {my_entry.text()}')
         my_entry.setText("")




app = qtw.QApplication([])
mw = MainWindow()



app.exec_()