from qrcode.main import QRCode
import tempfile
import subprocess
import os
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def createQrCode(url, boxSize, borderSize, bc, fc):
    qr = QRCode(box_size=boxSize, border=borderSize)
    qr.add_data(url)
    img = qr.make_image(fill_color=fc, back_color=bc)


    filepath = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])

    if filepath:
        img.save(filepath)
        print(f"Saved to : {filepath}")
    else:
        print("Not saved")
        
    return

def showQR(url,boxSize,borderSize,bc,fc):
    qr = QRCode(box_size= boxSize, border= borderSize)
    qr.add_data(url)
    img = qr.make_image(fill_color=fc, back_color=bc)
    
    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        temp_path = temp_file.name
        img.save(temp_path)  # temp image saved

    if os.name == "nt":  # Windows
        subprocess.Popen(["start", "", temp_path], shell=True)
    elif os.name == "posix":  # Mac & Linux
        subprocess.Popen(["xdg-open", temp_path])