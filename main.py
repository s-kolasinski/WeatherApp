import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from api_client import get_weather

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
        self.check_button.clicked.connect(self.fetch_weather)

    def fetch_weather(self):
        city = self.city_input.text()
        data = get_weather(city)
        if(data["Success"] == True):
            self.temp_label.setText(f"Temperature: {data['Temperature']}")
        else:
            self.temp_label.setText(f"{data['Error']}")

app = QApplication(sys.argv)
window = WeatherApp()
window.show()
app.exec()