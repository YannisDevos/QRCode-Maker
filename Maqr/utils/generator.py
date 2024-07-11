from qrcode.main import QRCode


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

def showQR(boxSize,borderSize,bc,fc):
    qr = QRCode(box_size= boxSize, border= borderSize)
    img = qr.make_image(fill_color=fc, back_color=bc)
    img.show()