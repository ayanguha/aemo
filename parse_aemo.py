import os,sys
import json

def getRecordGroups(fullFile):
    recordGroupStart = '200'
    inRg = False
    recordGroup = []
    for line in fullFile.split("\n"):
        line = line.strip('\r\n')
        if line.split(',')[0] == recordGroupStart and not inRg :
            rg = []
            rg.append(line)
            inRg = True
        elif line.split(',')[0] == recordGroupStart and inRg:
            # Close the previous group, yield it
            # Start the new group
            recordGroup.append(rg)
            rg = []
            inRg = False
            rg.append(line)
        elif line.split(',')[0] in ['300','400','500']:
            rg.append(line)
        else:
            pass
    recordGroup.append(rg)
    return recordGroup
  
def parse200(r):
    #Parse 200 Record. Simple csv
    RecordIndicator,NMI,NMIConfiguration,RegisterID,NMISuffix,MDMDataStreamIdentifier, MeterSerialNumber,UOM,IntervalLength,NextScheduledReadDate = r.split(',')
    MeterInfo = {}
    MeterInfo['RecordIndicator'] = RecordIndicator
    MeterInfo['NMI'] = NMI
    MeterInfo['NMIConfiguration'] = NMIConfiguration
    MeterInfo['RegisterID'] = RegisterID
    MeterInfo['NMISuffix'] = NMISuffix
    MeterInfo['MDMDataStreamIdentifier'] = MDMDataStreamIdentifier
    MeterInfo['MeterSerialNumber'] =  MeterSerialNumber
    MeterInfo['UOM'] = UOM
    MeterInfo['IntervalLength'] = int(IntervalLength)
    MeterInfo['NextScheduledReadDate'] = NextScheduledReadDate
    return MeterInfo

def makeIntervalInfo(readings,qm=None,rc=None,rd=None):
    intervalInfo = {}
    for k,v in enumerate(readings):
        intervalDetails = {}
        intervalDetails['Reading'] = v
        intervalDetails['QualityMethod'] = qm
        intervalDetails['ReasonCode'] = rc
        intervalDetails['ReasonDescription'] = rd
        intervalInfo[k+1] = intervalDetails
    return intervalInfo

def updateIntervalInfo(reading,qmdetails=None,b2bdetails=None):
    if qmdetails:
        for k in qmdetails: # Format: [(Interval,QMM,ReasonCode,ReasonDescription)]. Tuple Example: (1,A,None,None), (30,E52,None,None), (40,S53,9,None)
            reading[k[0]]['QualityMethod'] = k[1]
            reading[k[0]]['ReasonCode'] = k[2]
            reading[k[0]]['ReasonCode'] = k[3]
    return reading

def parse400(lst_400):
    # lst_400 format: ['400,1,31,A,,', '400,32,48,E52,,']
    qmdetails = []
    for l in lst_400:
        q = l.split(',')
        
        for k in xrange(int(q[1]),int(q[2])+1):
            qm = (k,q[3],q[4],q[5])
            qmdetails.append(qm)
    return qmdetails

def parse300(r,IntervalLength):
    # Parse 300 Record. Mostly simple csv, except readings
    # Readings: Depending on IntervalLength, 24 hours is divided into lengths. Ex: if IntervalLength=30, there will be 48 readings. If IntervalLength=15, there will be 96 readings
    dataRange=(24*60)/IntervalLength
    RecordIndicator = r.split(',')[0]
    IntervalDate = r.split(',')[1]
    Readings = r.split(',')[2:dataRange+2]
    QualityMethod,ReasonCode,ReasonDescription,UpdateDateTime,MSATSLoadDateTime = r.split(',')[dataRange+2:]
    ReadingInfo = {}
    ReadingInfo['RecordIndicator'] = RecordIndicator
    ReadingInfo['IntervalDate'] = IntervalDate
    ReadingInfo["QualityMethodFlag"] = QualityMethod[0]
    ReadingInfo["ReasonCode"] = ReasonCode
    qm = QualityMethod
    rc = ReasonCode
    rd = ReasonDescription
    ReadingInfo['Readings'] = makeIntervalInfo(Readings,qm,rc,rd)
    ReadingInfo['UpdateDateTime'] = UpdateDateTime
    ReadingInfo['MSATSLoadDateTime'] = MSATSLoadDateTime
    return ReadingInfo


def filterRG(r,recordIndicator):
    return filter(lambda l: l.split(',')[0] == recordIndicator, r)

def myprint(l):
    print "-------------------------------------------"
    print
    print
    print l
    print
    print
    print "-------------------------------------------"
    
def parseRecordGroup(recordGroup):
    ReadingRecord = {}
    ReadingInfoGroup = []
    MeterInfo = parse200(recordGroup[0])
    for frg in filterRG(recordGroup,'300'):
        ReadingInfo = parse300(frg,MeterInfo['IntervalLength'])
        
        if ReadingInfo["QualityMethodFlag"] == "V" or (ReadingInfo["QualityMethodFlag"] == "A" and (ReadingInfo["ReasonCode"] == "79" or ReadingInfo["ReasonCode"] == "89")):
            rec_400 = filterRG(recordGroup,'400')
            ReadingInfo['Readings'] = updateIntervalInfo(ReadingInfo['Readings'],qmdetails=parse400(rec_400))
        ReadingInfoGroup.append(ReadingInfo)
    ReadingRecord['MeterInfo'] = MeterInfo
    ReadingRecord['ReadingInfo'] = ReadingInfoGroup
    
    ReadingRecord_Json = json.dumps(ReadingRecord, sort_keys=True,indent=4, separators=(',', ': '))
    return  ReadingRecord_Json



def dateTODReadings(p):
    recordGroup = json.loads(p)
    IntervalDate = recordGroup['ReadingInfo']['IntervalDate']
    Readings = recordGroup['ReadingInfo']['Readings']
    for r in Readings:
        yield ((r[0],IntervalDate),float(r[1]))


if __name__ == "__main__":
    meter_csv_file = sys.argv[1]
    meter_json_file = sys.argv[2]
    # meter_file = "C:\\Users\\ayguha\\Google Drive\\Work\\Projects\EA\\METER_FILES\\METER_FILES\\sample3.csv"
    fp=open(meter_csv_file,'r')
    fo = open(meter_json_file,'w')
    for k in getRecordGroups(fp.read()):
        fo.write(parseRecordGroup(k))
    
        

