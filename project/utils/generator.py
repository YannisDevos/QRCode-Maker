from qrcode.main import QRCode
import tempfile
import subprocess
import os
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from utils.Saver import saveDatas

SAVEFILE = "project/utils/csv/save.csv"

def createQrCode(datas):
    qr = QRCode(box_size=datas.boxSize, border=datas.borderSize)
    qr.add_data(datas.url)
    img = qr.make_image(fill_color=datas.fillColor, back_color=datas.bgColor)

    filepath = asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])

    if filepath:
        img.save(filepath)
        print(f"Saved to : {filepath}")
        saveDatas(SAVEFILE, datas)
    else:
        print("Not saved")
        
    return

def showQR(datas):
    qr = QRCode(box_size=datas.boxSize, border=datas.borderSize)
    qr.add_data(datas.url)
    img = qr.make_image(fill_color=datas.fillColor, back_color=datas.bgColor)
    
    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        temp_path = temp_file.name
        img.save(temp_path)  # temp image saved

    if os.name == "nt":  # Windows
        subprocess.Popen(["start", "", temp_path], shell=True)
    elif os.name == "posix":  # Mac & Linux
        subprocess.Popen(["xdg-open", temp_path])