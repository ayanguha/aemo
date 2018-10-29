from ..database import db
from ..database.models import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import fields
import uuid,random
from flask_restplus import reqparse
from datetime import datetime

CERT = "talend_meta_cert_02"
KEY = "talend_meta_symm_key_02"
def safeCommit():
    try:
        db.session.commit()
    except:
        print "Rolling Back"
        db.session.rollback()
        raise

def safeFlush():
    try:
        db.session.flush()
    except:
        print "Rolling Back"
        db.session.rollback()
        raise

def modelExists(db,model):
    try:
        r = db.session.query(model).one()
        return True
    except:
        return False

def createAllModels(db):
    db.create_all()

def getRandomBigInt():
  return random.randint(1,100000000) #uuid.uuid4().hex, 

def addArtefactFileSource(Request):
  #if not modelExists(db=db, model=ArtefactFileSource):
  #  createAllModels(db)
  #o = ArtefactFileSource(request)
  
  
  
  
  params = {'ArtefactFileSourceID': getRandomBigInt(),
            'Type' : Request.json.get('Type'),
            'Location': Request.json.get('Location'), 
            'ContainerName': Request.json.get('ContainerName'),
            'AccountName': Request.json.get('AccountName'), 
            'Server': Request.json.get('Server'), 
            'Port':  Request.json.get('Port'), 
            'Username': Request.json.get('Username'), 
            'IsInternal': Request.json.get('IsInternal'),
            'SourceAlias':  Request.json.get('SourceAlias'), 
            'AccountKey': Request.json.get('AccountKey'), 
            'Password': Request.json.get('Password'),
            'key': KEY, 'cert': CERT
            }
  db.session.execute('exec metadata.PostArtefactFileSource :ArtefactFileSourceID,:Type, :Location, :ContainerName, :AccountName, :Server, :Port, :Username, :IsInternal, :SourceAlias, :AccountKey, :Password, :key, :cert', params)
  #db.session.add(o)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllArtefactFileSource():
  if not modelExists(db=db, model=ArtefactFileSource):
    createAllModels(db)
  qryRes = ArtefactFileSource.query.all()
  return [i.serialize for i in qryRes],200


def getSingleArtefactFileSource(ArtefactFileSourceID):
  qryRes = ArtefactFileSource.query.filter_by(ArtefactFileSourceID=ArtefactFileSourceID).all()
  
  return qryRes[0].serialize,200

def updateSingleArtefactFileSource(ArtefactFileSourceID,request):
  
  qryRes = ArtefactFileSource.query.filter_by(ArtefactFileSourceID=ArtefactFileSourceID).all()
  afs = qryRes[0]
  afs.Type = request.json['Type']
  afs.Location = request.json['Location']
  afs.AccountName = request.json['AccountName']
  afs.ContainerName = request.json['ContainerName']
  afs.Server = request.json['Server']
  afs.Port = request.json['Port']
  afs.Username = request.json['Username']
  afs.SourceAlias = request.json['SourceAlias']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactFileSource(ArtefactFileSourceID):
    qryRes = ArtefactFileSource.query.filter_by(ArtefactFileSourceID=ArtefactFileSourceID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

############################################################################################

def addArtefactTableSource(Request):
  
  params = {'ArtefactTableSourceID': getRandomBigInt(),
            'Type': Request.json.get('Type'), 
            'Server': Request.json.get('Server'), 
            'Port': Request.json.get('Port'), 
            'Database': Request.json.get('Database'), 
            'ServiceName': Request.json.get('ServiceName'), 
            'SID': Request.json.get('SID'), 
            'Schema': Request.json.get('Schema'), 
            'Username': Request.json.get('Username'), 
            'ExternalDataSource': Request.json.get('ExternalDataSource'), 
            'ExternalFileFormat': Request.json.get('ExternalFileFormat'), 
            'Location': Request.json.get('Location'), 
            'ContainerName': Request.json.get('ContainerName'), 
            'AccountName': Request.json.get('AccountName'), 
            'IsInternal': Request.json.get('IsInternal'), 
            'AccountKey': Request.json.get('AccountKey'), 
            'Password': Request.json.get('Password'), 
            'SourceAlias': Request.json.get('SourceAlias'), 
            'GROUP': Request.json.get('GROUP'),
            'key': KEY, 
            'cert': CERT
            }
  db.session.execute('exec metadata.PostArtefactTableSource :ArtefactTableSourceID,:Type,:Server,:Port,:Database,:ServiceName,:SID,:Schema,:Username,:ExternalDataSource,:ExternalFileFormat,:Location,:AccountName,:ContainerName,:IsInternal,:SourceAlias,:AccountKey,:Password,:GROUP,:key,:cert', params)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllArtefactTableSource():
  qryRes = ArtefactTableSource.query.all()
  return [i.serialize for i in qryRes],200


def getSingleArtefactTableSource(ArtefactTableSourceID):
  qryRes = ArtefactTableSource.query.filter_by(ArtefactTableSourceID=ArtefactTableSourceID).all()
  return qryRes[0].serialize ,200

def updateSingleArtefactTableSource(ArtefactTableSourceID,request):
  qryRes = ArtefactTableSource.query.filter_by(ArtefactTableSourceID=ArtefactTableSourceID).all()
  afs = qryRes[0]
  afs.Type = request.json['Type']
  afs.Server = request.json['Server']
  afs.Port = request.json['Port']
  afs.Database = request.json['Database']
  afs.ServiceName = request.json['ServiceName']
  afs.Schema = request.json['Schema']
  afs.Username = request.json['Username']
  afs.ExternalDataSource = request.json['ExternalDataSource']
  afs.ExternalFileFormat = request.json['ExternalFileFormat']
  afs.Location = request.json['Location']
  afs.AccountName = request.json['AccountName']
  afs.ContainerName = request.json['ContainerName']
  afs.IsInternal = request.json['IsInternal']
  afs.SourceAlias = request.json['SourceAlias']
  afs.GROUP = request.json['GROUP']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactTableSource(ArtefactTableSourceID):
    qryRes = ArtefactTableSource.query.filter_by(ArtefactTableSourceID=ArtefactTableSourceID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204


############################################################################################

def addAttributeDataType(Request):
  adtid = getRandomBigInt()
  params = {'AttributeDataTypeID':adtid,
            'DataTypeSQLServer':Request.json.get('DataTypeSQLServer'), 
            'DataTypeSybase':Request.json.get('DataTypeSybase'), 
            'DataTypeOracle':Request.json.get('DataTypeOracle'), 
            'DataTypePolybase':Request.json.get('DataTypePolybase'), 
            'DataTypeAzureSQLDW':Request.json.get('DataTypeAzureSQLDW'),  
            'DataTypeHive':Request.json.get('DataTypeHive')}
  db.session.execute('exec metadata.PostAttributeDataType :AttributeDataTypeID,:DataTypeSQLServer,:DataTypeSybase,:DataTypeOracle,:DataTypePolybase,:DataTypeAzureSQLDW,:DataTypeHive', params)   
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllAttributeDataType():
  qryRes = AttributeDataType.query.all()
  return [i.serialize for i in qryRes],200


def getSingleAttributeDataType(AttributeDataTypeID):
  qryRes = AttributeDataType.query.filter_by(AttributeDataTypeID=AttributeDataTypeID).all()
  return qryRes[0].serialize ,200

def updateSingleAttributeDataType(AttributeDataTypeID,request):
  qryRes = AttributeDataType.query.filter_by(AttributeDataTypeID=AttributeDataTypeID).all()
  afs = qryRes[0]
  afs.DataTypeSQLServer = request.json['DataTypeSQLServer']
  afs.DataTypeSybase = request.json['DataTypeSybase']
  afs.DataTypeOracle = request.json['DataTypeOracle']
  afs.DataTypePolybase = request.json['DataTypePolybase']
  afs.DataTypeAzureSQLDW = request.json['DataTypeAzureSQLDW']
  afs.DataTypeHive = request.json['DataTypeHive']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleAttributeDataType(AttributeDataTypeID):
    qryRes = AttributeDataType.query.filter_by(AttributeDataTypeID=AttributeDataTypeID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204


############################################################################################

def addArtefactFileType(Request):
  aftid = getRandomBigInt()
  params = {'ArtefactFileTypeID':aftid,
            'Type':Request.json.get('Type'), 
            'Format':Request.json.get('Format'), 
            'Encoding':Request.json.get('Encoding'), 
            'FieldSeparator':Request.json.get('FieldSeparator'), 
            'RowSeparator':Request.json.get('RowSeparator'),  
            'TextQualifier':Request.json.get('TextQualifier')
            }
  db.session.execute('exec metadata.PostArtefactFileType :ArtefactFileTypeID,:Type,:Format,:Encoding,:FieldSeparator,:RowSeparator,:TextQualifier', params)   
  
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllArtefactFileType():
  qryRes = ArtefactFileType.query.all()
  return [i.serialize for i in qryRes],200


def getSingleArtefactFileType(ArtefactFileTypeID):
  qryRes = ArtefactFileType.query.filter_by(ArtefactFileTypeID=ArtefactFileTypeID).all()
  return qryRes[0].serialize ,200

def updateSingleArtefactFileType(ArtefactFileTypeID,request):
  qryRes = ArtefactFileType.query.filter_by(ArtefactFileTypeID=ArtefactFileTypeID).all()
  afs = qryRes[0]
  afs.Type = request.json['Type']
  afs.Format = request.json['Format']
  afs.Encoding = request.json['Encoding']
  afs.FieldSeparator = request.json['FieldSeparator']
  afs.RowSeparator = request.json['RowSeparator']
  afs.TextQualifier = request.json['TextQualifier']
  

  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactFileType(ArtefactFileTypeID):
    qryRes = ArtefactFileType.query.filter_by(ArtefactFileTypeID=ArtefactFileTypeID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

############################################################################################

def addProcess(Request):
  processid = getRandomBigInt()
  params = {'ProcessID':processid,
            'Name':Request.json.get('Name'), 
            'Description':Request.json.get('Description'), 
            'Type':Request.json.get('Type'), 
            'RollbackType':Request.json.get('RollbackType')}
  db.session.execute('exec metadata.PostProcess :ProcessID,:Name,:Description,:Type,:RollbackType', params)   
  
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllProcesss():
  qryRes = Process.query.all()
  return [i.serialize for i in qryRes],200


def getSingleProcess(ProcessID):
  qryRes = Process.query.filter_by(ProcessID=ProcessID).all()
  return qryRes[0].serialize ,200

def updateSingleProcess(ProcessID,request):
  qryRes = Process.query.filter_by(ProcessID=ProcessID).all()
  afs = qryRes[0]
  afs.Type = request.json['Type']
  afs.Name = request.json['Name']
  afs.Description = request.json['Description']
  afs.RollbackType = request.json['RollbackType']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleProcess(ProcessID):
    qryRes = Process.query.filter_by(ProcessID=ProcessID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204


############################################################################################

def addLoadPlan(Request):  
  params = {'LoadPlanID': getRandomBigInt(),
            'Name': Request.json.get('Name'), 
            'Category': Request.json.get('Category'), 
            'Description': Request.json.get('Description'),
            'Type': Request.json.get('Type')
            }
  db.session.execute('exec metadata.PostLoadPlan :LoadPlanID,:Name,:Category,:Type,:Description', params)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllLoadPlans():
  qryRes = LoadPlan.query.all()
  return [i.serialize for i in qryRes],200


def getSingleLoadPlan(LoadPlanID):
  
  qryRes = LoadPlan.query.filter_by(LoadPlanID=LoadPlanID).all()
  return qryRes[0].serialize ,200



def updateSingleLoadPlan(LoadPlanID,request):
  qryRes = LoadPlan.query.filter_by(LoadPlanID=LoadPlanID).all()
  afs = qryRes[0]
  afs.Name = request.json['Name']
  afs.Category = request.json['Category']
  afs.Type = request.json['Type']
  afs.Description = request.json['Description']
  
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleLoadPlan(LoadPlanID):
    qryRes = LoadPlan.query.filter_by(LoadPlanID=LoadPlanID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

############################################################################################

def addProcessGroup(Request):  
  params = {'ProcessGroupID': getRandomBigInt(),
            'Name': Request.json.get('Name'), 
            'Description': Request.json.get('Description'),
            'LoadPlanID': Request.json.get('LoadPlanID'),
            'ProcessID': Request.json.get('ProcessID'),
            'SourceArtefactFileSourceID': Request.json.get('SourceArtefactFileSourceID'),
            'SourceArtefactTableSourceID': Request.json.get('SourceArtefactTableSourceID'),
            'TargetArtefactFileSourceID': Request.json.get('TargetArtefactFileSourceID'),
            'TargetArtefactTableSourceID': Request.json.get('TargetArtefactTableSourceID'),
            'OrderOfExecution': Request.json.get('OrderOfExecution')
            }
  
  db.session.execute('exec metadata.PostProcessGroup :ProcessGroupID,:Name,:Description,:LoadPlanID,:ProcessID,:SourceArtefactFileSourceID,:SourceArtefactTableSourceID,:TargetArtefactFileSourceID,:TargetArtefactTableSourceID,:OrderOfExecution', params)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllProcessGroups():
  qryRes = ProcessGroup.query.order_by(ProcessGroup.OrderOfExecution).all()
  return [i.serialize for i in qryRes],200


def getSingleProcessGroup(ProcessGroupID):
  
  qryRes = ProcessGroup.query.filter_by(ProcessGroupID=ProcessGroupID).all()
  return qryRes[0].serialize ,200



def updateSingleProcessGroup(ProcessGroupID,request):
  qryRes = ProcessGroup.query.filter_by(ProcessGroupID=ProcessGroupID).all()
  afs = qryRes[0]
  afs.Name = request.json['Name']
  afs.Description = request.json['Description']
  afs.OrderOfExecution = request.json['OrderOfExecution']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleProcessGroup(ProcessGroupID):
    qryRes = ProcessGroup.query.filter_by(ProcessGroupID=ProcessGroupID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

############################################################################################

def addProcessWrapper(Request):  
  params = {'ProcessWrapperID': getRandomBigInt(),
            'Name': Request.json.get('Name')
            }
  
  db.session.execute('exec metadata.PostProcessWrapper :ProcessWrapperID,:Name', params)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllProcessWrappers():
  qryRes = ProcessWrapper.query.order_by(ProcessWrapper.Order).all()
  return [i.serialize for i in qryRes],200

def getProcessWrapperOrchMaster():
  qryRes = ProcessWrapper.query.order_by(ProcessWrapper.Order).all()
  return [i.serialize for i in qryRes if not i.ParentProcessWrapperID ],200

def getSingleProcessWrapper(ProcessWrapperID):
  
  qryRes = ProcessWrapper.query.filter_by(ProcessWrapperID=ProcessWrapperID).all()
  return qryRes[0].serialize ,200



def updateSingleProcessWrapper(ProcessWrapperID,request):
  qryRes = ProcessWrapper.query.filter_by(ProcessWrapperID=ProcessWrapperID).all()
  afs = qryRes[0]
  afs.Name = request.json['Name']
  
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleProcessWrapper(ProcessWrapperID):
    qryRes = ProcessWrapper.query.filter_by(ProcessWrapperID=ProcessWrapperID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204


############################################################################################



def getAllProcessArtefacts():
  qryRes = ProcessArtefact.query.all()
  return [i.serialize for i in qryRes],200


def getSingleProcessArtefact(ProcessArtefactID):
  
  qryRes = ProcessArtefact.query.filter_by(ProcessArtefactID=ProcessArtefactID).all()
  return qryRes[0].serialize ,200



def updateSingleProcessArtefact(ProcessArtefactID,request):
  qryRes = ProcessArtefact.query.filter_by(ProcessArtefactID=ProcessArtefactID).all()
  afs = qryRes[0]
  afs.MaxRunAttempts = request.json['MaxRunAttempts']
  
  afs.MaxRunAttempts = request.json['MaxRunAttempts']
  afs.RerunWaitingTime = request.json['RerunWaitingTime']
  afs.InMinThreshold = request.json['InMinThreshold']
  afs.InMaxThreshold = request.json['InMaxThreshold']
  afs.OutMinThreshold = request.json['OutMinThreshold']
  afs.OutMaxThreshold = request.json['OutMaxThreshold']
  afs.DurationMinThreshold = request.json['DurationMinThreshold']
  afs.DurationMaxThreshold = request.json['DurationMaxThreshold']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

