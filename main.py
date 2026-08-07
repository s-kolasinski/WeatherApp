import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.resize(400, 300)
        self.city_input = QLineEdit()
        self.check_button = QPushButton("Check weather")
        self.temp_label = QLabel()
        self.city_input.setPlaceholderText("Enter a city name")
        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.temp_label)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec()