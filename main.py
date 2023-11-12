from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QComboBox
from PyQt6.QtCore import QSize, Qt

import sys

calculate_str = "Oblicz"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalorymetr")
        
        self.MainLayout = MainWindowLayout()

        self.setCentralWidget(self.MainLayout)

class MainWindowLayout(QWidget):
    def __init__(self):
        super().__init__()

        # Buttons
        calculate_btn = QPushButton(calculate_str)

        # Input fields and labels
        m1_label = QLabel("m1", self)
        m1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.m1_input = QLineEdit(self)
        c1_label = QLabel("c1", self)
        self.c1_input = QLineEdit(self)
        delta_T1_label = QLabel("delta_T1", self)
        self.delta_T1_input = QLineEdit(self)

        m2_label = QLabel("m2", self)
        self.m2_input = QLineEdit(self)
        c2_label = QLabel("c2", self)
        self.c2_input = QLineEdit(self)
        delta_T2_label = QLabel("delta_T2", self)
        self.delta_T2_input = QLineEdit(self)

        # Drop-down list
        self.chosen_variable_combobox = QComboBox(self)
        self.chosen_variable_combobox.currentTextChanged.connect(self.choose_variable)
        list_of_variables = ["m1", "c1", "delta T1", "m2", "c2", "delta T2"]
        for variable in list_of_variables:
            self.chosen_variable_combobox.addItem(variable)
        chosen_variable_label = QLabel("Wybierz szukaną niewiadomą")
        
        main_layout = QVBoxLayout(self)
        layout = QHBoxLayout(self)

        choose_variable_layout = QHBoxLayout(self)
        choose_variable_layout.addWidget(chosen_variable_label)
        choose_variable_layout.addWidget(self.chosen_variable_combobox)
        main_layout.addLayout(choose_variable_layout)


        m1_layout = QVBoxLayout(self)
        m1_layout.addWidget(m1_label)
        m1_layout.addWidget(self.m1_input)
        layout.addLayout(m1_layout)

        c1_layout = QVBoxLayout(self)
        c1_layout.addWidget(c1_label)
        c1_layout.addWidget(self.c1_input)
        layout.addLayout(c1_layout)

        delta_T1_layout = QVBoxLayout(self)
        delta_T1_layout.addWidget(delta_T1_label)
        delta_T1_layout.addWidget(self.delta_T1_input)
        layout.addLayout(delta_T1_layout)

        layout.addWidget(QLabel("=", self))

        m2_layout = QVBoxLayout(self)
        m2_layout.addWidget(m2_label)
        m2_layout.addWidget(self.m2_input)
        layout.addLayout(m2_layout)

        c2_layout = QVBoxLayout(self)
        c2_layout.addWidget(c2_label)
        c2_layout.addWidget(self.c2_input)
        layout.addLayout(c2_layout)

        delta_T2_layout = QVBoxLayout(self)
        delta_T2_layout.addWidget(delta_T2_label)
        delta_T2_layout.addWidget(self.delta_T2_input)
        layout.addLayout(delta_T2_layout)

        
        main_layout.addLayout(layout)

        self.setLayout(main_layout)

    def choose_variable(self):
        chosen_variable = self.chosen_variable_combobox.currentText()

        if chosen_variable == "m1":
            self.m1_input.setEnabled(False)
            self.c1_input.setEnabled(True)
            if self.m2_input.text() != "" and self.c2_input.text() != "" and self.delta_T2_input.text() != "" and self.c1_input.text() != "" and self.delta_T1_input.text() != "":
                m1_value = str((float(self.m2_input.text()) * float(self.c2_input.text()) * float(self.delta_T2_input.text())) / (float(self.c1_input.text()) * float(self.delta_T1_input.text())))
                self.m1_input.setText(m1_value)
        elif chosen_variable == "c1":
            self.c1_input.setEnabled(False)
            self.m1_input.setEnabled(True)

            


def input_field_with_label(label, parent):
    input_field = QLineEdit(parent)
    label_field = QLabel(label, parent)

    input_layout = QHBoxLayout(parent)
    input_layout.addWidget(label_field)
    input_layout.addWidget(input_field)








# Create an instance of QApplication. Pass in sys.argv to allow comman line arguments.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window
window = MainWindow()
# Show the window
window.show()

# Start the event loop
app.exec()

# App won't reach here until we exit and the event loop has stopped.