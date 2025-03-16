from qrcode.main import QRCode
import tempfile
import subprocess
import os

def createQrCode(url,boxSize,borderSize,bc,fc, filename, extension):
    qr = QRCode(box_size= boxSize, border= borderSize)
    qr.add_data(url)
    img = qr.make_image(fill_color=fc, back_color=bc)
    img.save(filename + extension)


def getColor(txt):
    i = 0   
    while(txt[i] != '#'):
        i = i + 1
    
    nvtxt = ""
    for j in range(7):
        nvtxt = nvtxt + txt[i+j]
        
    return nvtxt

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