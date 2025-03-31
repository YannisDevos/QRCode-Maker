from utils.data import qrDatas

def readSavedDatas(filepath):
    f = open(filepath, "r")
    
    lines = f.readlines()

    datas = []

    for i in range(len(lines)):
        l = lines[i]
        
        if i != len(lines) - 1:
            l = l[0 : len(l) - 1]
            
        splittedDatas = l.split(",")
        
        datas.append(qrDatas(splittedDatas[0], splittedDatas[1], splittedDatas[2], splittedDatas[3], splittedDatas[4]))
        
    f.close()
    return datas