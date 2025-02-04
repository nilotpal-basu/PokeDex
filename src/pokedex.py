import sys , os
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QImage , QFont
from PyQt6.QtCore import Qt
from predict import pred_poke
from att_fetcher import get_pokemon_info



class PokedexApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pokédex")
        self.setGeometry(100, 100, 600, 400)

        # Set background image
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(QPixmap(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),"pkdex.jpg")))
        self.bg_label.setScaledContents(True)
        self.bg_label.resize(600, 400)

        # Pokémon Display Screen
        self.pokemon_label = QLabel(self)
        self.pokemon_label.setGeometry(45, 109, 212, 135)
        self.pokemon_label.setStyleSheet("border: 2px solid black; background-color: white;")
        self.pokemon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Prediction Label
        self.prediction_label = QLabel("", self)
        self.prediction_label.setGeometry(360, 116, 199, 93)
        self.prediction_label.setFont(QFont('Times')) 
        self.prediction_label.setStyleSheet("background-color: #19f223; color: black; font-size: 14px;")
        self.prediction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        # Button to Open File Dialog
        self.button = QPushButton("Choose Poke", self)
        self.button.setGeometry(65, 325, 120, 50)
        self.button.setStyleSheet("background-color: yellow; color: black;")
        self.button.clicked.connect(self.open_image)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        try:
            if file_path:
                pokemon_name = pred_poke(file_path)
                self.pokemon_label.setPixmap(QPixmap(file_path).scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio))
            attribute = get_pokemon_info(pokemon_name)
            self.prediction_label.setText(f"{pokemon_name.upper()} \n\nHeight : {attribute['Height']}   Weight : {attribute['Weight']} \n\nType : {attribute['Types']}")
        except Exception as e:
            self.prediction_label.setText("Error: Invalid Image")


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokedexApp()
    window.show()
    sys.exit(app.exec())
