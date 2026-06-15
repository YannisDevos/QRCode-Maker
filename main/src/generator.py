from qrcode.main import QRCode
import os


def createQrCode(url,boxSize,borderSize,bc,fc, filename, extension):
    path = "qrcodes/" + filename + extension
    qr = QRCode(box_size= boxSize, border= borderSize)
    qr.add_data(url)
    img = qr.make_image(fill_color=fc, back_color=bc)
    
    try:
        img.save(path)
    except FileNotFoundError as fnfe:
        os.makedirs("qrcodes", exist_ok=True)
        img.save(path)
    
    return qr


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
    img.show()