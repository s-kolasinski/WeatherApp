import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox
from PySide6.QtGui import QIcon
from api_client import get_weather
import json
import os

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(400, 300)
        self.city_input = QLineEdit()
        self.check_button = QPushButton("Check weather")
        self.temp_label = QLabel()
        self.history_dropdown = QComboBox()
        history = self.load_history()
        self.history_dropdown.addItems(history)
        self.city_input.setPlaceholderText("Enter a city name")
        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.history_dropdown)
        layout.addWidget(self.check_button)
        layout.addWidget(self.temp_label)
        self.setLayout(layout)
        self.check_button.clicked.connect(self.fetch_weather)
        self.history_dropdown.currentTextChanged.connect(self.city_input.setText)

    def fetch_weather(self):
        city = self.city_input.text()
        data = get_weather(city)
        if(data["Success"] == True):
            self.temp_label.setText(f"Temperature: {data['Temperature']}")
            self.save_to_history(city)
        else:
            self.error = QMessageBox()
            self.error.setWindowTitle("ERROR")
            self.error.setText(data['Error'])
            self.error.setWindowIcon(QIcon("error-icon.png"))
            self.error.exec()
    def load_history(self):
        if(os.path.exists("history.json")):
            with open("history.json", "r") as file:
                return json.load(file)
        else:
            return []

    def save_to_history(self, city):
        history = self.load_history()
        if(city not in history):
            history.append(city)
            with open("history.json", "w") as file:
                json.dump(history, file)
            self.history_dropdown.addItem(city)

app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec()