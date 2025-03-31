class qrDatas():
    def __init__(self, url, boxSize, borderSize, bgColor, fillColor):
        self.url = url
        self.boxSize = boxSize
        self.borderSize = borderSize
        self.bgColor = bgColor
        self.fillColor = fillColor
        
    def __str__(self):
        return self.url + " " + self.boxSize + " " + self.borderSize + " " + self.bgColor  + " " + self.fillColor