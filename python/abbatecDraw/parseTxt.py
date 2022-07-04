import sys
import os

path = sys.argv[1]

try:
    f = open(path, 'r', encoding="utf-8")
except:
    f = open('L:\\PRG\nodejs\\ABBA\\現場log\\20220621\\log\\RFIDAtag_20220621.log', 'r', encoding="utf-8")

a = os.path.splitext(path)
destination = open(a[0]+'after'+a[1], 'w')

for line in f.readlines():
    if line.find("RFID - EPC") > 0:
        destination.write(line)
f.close()
destination.close()

#f = open('D:\\SynologyDrive\\AidiaLink\\客戶資料\\啟翔\\現場測試\\0610\\20220610_testlog\\confirmcount2\\RFIDAtag入櫃ru.txt', 'r', encoding="utf-8")
#for line in f.readlines():
    #get first time
    #print(line.split(16:24))
#f.close()