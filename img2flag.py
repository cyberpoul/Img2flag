# Script OCR - Made by opscur
import cv2
import pytesseract
from PIL import Image
import argparse

# Créer un analyseur d'arguments en ligne de commande
parser = argparse.ArgumentParser(description='Effectuer OCR sur une image.')
parser.add_argument('-f', '--file', type=str, help='Chemin de l\'image à traiter')

# Analyser les arguments de la ligne de commande
args = parser.parse_args()

# Vérifier si l'argument -f est spécifié
if args.file is None:
    print("Veuillez spécifier le chemin de l'image avec l'argument -f image_path.")
else:
    image_path = args.file

    # Charger l'image avec OpenCV
    image = cv2.imread(image_path)

    if image is None:
        print("L'image n'a pas pu être chargée correctement.")
    else:
        # Convertir l'image en niveaux de gris (pour une meilleure OCR)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Utiliser Tesseract pour effectuer l'OCR
        ascii_characters = pytesseract.image_to_string(Image.fromarray(gray_image))

        # Filtrer les caractères ASCII
        ascii_characters = "".join(filter(lambda x: x.isascii(), ascii_characters))

        # Remplacer les sauts de ligne par un espace
        ascii_characters = ascii_characters.replace('\n', ' ')

        # Supprimer tous les espaces
        ascii_characters = ''.join(ascii_characters.split())

        # Afficher les caractères ASCII extraits
        print("Caractères ASCII extraits :")
        print(ascii_characters)
