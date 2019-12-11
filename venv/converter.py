from struct import *
import binascii
f = open('workin_.txt', mode="br")
#print(str(f.read()))
traceType = f.readline()
#print(str(traceType.decode('utf8')))
traceTag = f.readline()
#print(str(traceTag.decode('utf8')))
traceComment = f.readline()
#print(str(traceComment.decode('utf8')))
test = f.read(1)
if test[0] == 0x1a:
    print("File Passed yeet")
else:
    print("File is corrupted!")
    exit(1)
f.read(1)
nlTag = unpack('<10s', f.read(10))[0]
nlLastRunFlag = unpack('<i', f.read(4))[0]
nhLastRunTimingIdx = unpack('<B', f.read(1))[0]
nhLastRunTrigPos = unpack('<B', f.read(1))[0]
nhTraceWidth = unpack('<B', f.read(1))[0]
#print(nhTraceWidth)
nhDelay = f.read(4)
nhFirstTrig = f.read(4)
nhFirstValTrcLine = unpack('<i', f.read(4))[0]
#print(nhFirstValTrcLine)
nhLastValTrcLine = unpack('<i', f.read(4))[0]
#print(nhLastValTrcLine)
nhTrigFound = f.read(2)
nhTrcCompleted = f.read(2)
nhTrigLineTxt = f.read(10)
lineNo, nhTrigLineTxt = unpack('<i6s', nhTrigLineTxt)
#print(str(nhTrigLineTxt.decode('utf8')) + " " + str(lineNo))
nhTime = f.read(8)
nhCalcADCVal = f.read(8)
x = f.read(1)
#print(x)
while x[0] != 200:
    x = f.read(1)

W = int(unpack('>i', f.read(4))[0]/16)
#print(W)
traceList = []

for i in range(0, W):
    trace = {}
    trace["Address"] = unpack('>i', f.read(4))[0]
    trace["Data"] = unpack('>i', f.read(4))[0]
    trace["TagL"] = unpack('>B', f.read(1))[0]
    trace["TagU"] = unpack('>B', f.read(1))[0]
    trace["Am"] = unpack('>B', f.read(1))[0]
    trace["Irq"] = unpack('>B', f.read(1))[0]
    trace["Str"] = unpack('>B', f.read(1))[0]
    trace["Bg"] = unpack('>B', f.read(1))[0]
    trace["St2"] = unpack('>B', f.read(1))[0]
    trace["St3"] = unpack('>B', f.read(1))[0]
    #print(trace)
    traceList.append(trace)

print(traceList)

