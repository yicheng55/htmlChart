from fileinput import filename
import sys, os
import numpy as np
import math
from matplotlib import pyplot as plt, figure

firstTime = 0
lastTime = 0
traceData = []
epcNumber = 0
epcArray = []

i = 0

try:
    path = sys.argv[1]
except:
    path = 'D:\\SynologyDrive\\AidiaLink\\客戶資料\\啟翔\\現場測試\\0610\\20220610_testlog\\confirmcount4\\RFIDAtag出櫃2after.log'

fileName = os.path.basename(path)
fileName = fileName.split('.')
pathName = os.path.dirname(path)

f = open(path, 'r', encoding="utf-8")

for line in f.readlines():
    #get first time
    rTime = line[12:24]
    tTime = rTime.split(":")
    rTime = int(tTime[0])*3600+int(tTime[1])*60+float(tTime[2])
    epc = line[46:70]
    if i == 0:
        #First item
        i += 1
        firstTime = rTime
        traceData.append((0, epc))
    else:
        traceData.append((rTime-firstTime, epc))

    lastTime = rTime
f.close()

#    if not traceData:
#        traceData[0] = epc
#    else:
#        if epc != traceData

#print(traceData)
du = math.ceil(lastTime-firstTime)
#print("du = ", du)

#print(len(traceData))

# find different epc tag in traceData
for i in range(0,len(traceData)):
    epc = traceData[i][1]
    try:
        epcArray.index(epc)
    except:
        epcArray.append(epc)

epcNumber = len(epcArray)

# trace array find different epc and times in every second

traceDataNp = np.zeros((epcNumber,du),np.uint16)
inc = 1
for i in range(0,len(traceData)):
    traceTime = int(traceData[i][0]//inc)
    epc = traceData[i][1]
    a = epcArray.index(epc)
    #print(str(a)+' '+str(epc)+' '+str(traceTime))
    traceDataNp[[a],[traceTime]] += 1


fig, axs = plt.subplots(2)


for i in range(epcNumber):
    if epcArray[i][0] == 'A':
        axs[0].plot(traceDataNp[i], label=str(epcArray[i][20::]))
        axs[0].set_title('A tag')
    else:
        axs[1].plot(traceDataNp[i], label=str(epcArray[i][20::]))
        axs[1].set_title('B tag')

handles, labels = axs[0].get_legend_handles_labels()
axs[0].legend(handles, labels)
handles, labels = axs[1].get_legend_handles_labels()
axs[1].legend(handles, labels)
plt.tight_layout()
#plt.savefig('./'+fileName[0]+'.jpg')
plt.savefig(pathName+'\\'+fileName[0]+'.jpg')
plt.show()
