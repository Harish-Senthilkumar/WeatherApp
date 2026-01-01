import sys 
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("City Weather App")
        self.setGeometry(100, 100, 300, 200)

        myBox = QVBoxLayout()
        myBox.addWidget(self.city_label)
        myBox.addWidget(self.city_input)
        myBox.addWidget(self.get_weather_button)
        myBox.addWidget(self.temperature_label)
        myBox.addWidget(self.emoji_label)
        myBox.addWidget(self.description_label)

        self.setLayout(myBox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())