from ..database import db
from ..database.models import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import fields
import uuid,random
from flask_restplus import reqparse
from datetime import datetime


KEY = "talend_meta_symm_key_02"
CERT = "talend_meta_cert_02"

def printDict(d):
  for k in d:
    print "%s  %s" %(k,d[k])

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
  return random.randint(1,100000000)  

def cleanup(arr):
    o = []
    for a in arr:
        cleaned = a.strip(" ").replace(" ","_").replace('"','')
        o.append(cleaned)
    return o


def getColumnList(ColumnListContent):
    d = {}
    lines = ColumnListContent.split("\n")
    for l in lines:
        if len(l) == 0:
            break
        t = cleanup(l.split(","))
        schema,table,column = (t[0],t[1],t[2])
        k = "-".join([schema, table])
        if not d.has_key(k):
            d[k] = {}
            d[k]['schema'] = schema
            d[k]['table'] = table
            d[k]['columns'] = []
        d[k]['columns'].append(column)
    
    return d

############################################################################################

def addArtefact(Request):  
  pass

def getAllArtefact():
  qryRes = Artefact.query.order_by(Artefact.CreateDate).all()
  return [i.serialize for i in qryRes],200


def getSingleArtefact(ArtefactID):
  
  qryRes = Artefact.query.filter_by(ArtefactID=ArtefactID).all()
  return qryRes[0].serialize ,200

def getArtefactByType(t=None):
  qryRes = Artefact.query.filter_by(Type=t).all()
  return [i.serialize for i in qryRes],200


def updateSingleArtefact(ArtefactID,request):
  qryRes = Artefact.query.filter_by(ArtefactID=ArtefactID).all()
  afs = qryRes[0]
  afs.Category = request.json['Category']
  afs.Description = request.json['Description']
  afs.BusinessDescription = request.json['BusinessDescription']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefact(ArtefactID):
    qryRes = Artefact.query.filter_by(ArtefactID=ArtefactID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204


############################################################################################

def addArtefactFile(Request):
  ColumnListContent = getColumnList(Request.json.get('ColumnListContent'))
  if not ColumnListContent:
      ArtefactID =  getRandomBigInt()
      params = {'ArtefactID': ArtefactID,
                'ArtefactFileTypeID': Request.json.get('ArtefactFileTypeID'), 
                'Name': Request.json.get('Name'), 
                'NamePattern': Request.json.get('NamePattern'),
                'TargetSchema': Request.json.get('TargetSchema'),
                'TargetTableName': Request.json.get('TargetTableName'),
                'IsCompressed': Request.json.get('IsCompressed'),
                "ProcessWrapperID": Request.json.get('ProcessWrapperID'),
                 "LoadPlanID": Request.json.get('LoadPlanID')            
                }

  
      db.session.execute('exec metadata.PostArtefactFile :ArtefactID,:Name,:ArtefactFileTypeID,:NamePattern,:TargetSchema,:TargetTableName,:IsCompressed,:ProcessWrapperID,:LoadPlanID', params)
      addArtefactAttribute(Request.json.get('ColumnList'), Request.json.get('SourceTechnology') ,ArtefactID)
  else:

      for k  in ColumnListContent:
          
          colList = ",".join(ColumnListContent[k]['columns'])
          
          ArtefactID =  getRandomBigInt()
          schema = ColumnListContent[k]['schema']
          table =  ColumnListContent[k]['table']
          params = {'ArtefactID': ArtefactID,
                    'ArtefactFileTypeID': Request.json.get('ArtefactFileTypeID'), 
                    'Name': ".".join([schema,table]), 
                    'NamePattern': '',
                    'TargetSchema': schema,
                    'TargetTableName': table,
                    'IsCompressed': 0,
                    "ProcessWrapperID": Request.json.get('ProcessWrapperID'),
                    "LoadPlanID": Request.json.get('LoadPlanID')            
                   }
          
          db.session.execute('exec metadata.PostArtefactFile :ArtefactID,:Name,:ArtefactFileTypeID,:NamePattern,:TargetSchema,:TargetTableName,:IsCompressed,:ProcessWrapperID,:LoadPlanID', params)
          addArtefactAttribute(colList, Request.json.get('SourceTechnology') ,ArtefactID)

  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllArtefactFile():
  qryRes = ArtefactFile.query.order_by(ArtefactFile.CreateDate).all()
  return [i.serialize for i in qryRes],200

def getSingleArtefactFile(ArtefactFileID):
  qryRes = ArtefactFile.query.filter_by(ArtefactFileID=ArtefactFileID).all()

  return qryRes[0].serialize ,200

def updateSingleArtefactFile(ArtefactFileID,request):
  qryRes = ArtefactFile.query.filter_by(ArtefactFileID=ArtefactFileID).all()
  afs = qryRes[0]
  afs.HeaderRowsToSkip = request.json['HeaderRowsToSkip']
  afs.FooterRowsToSkip = request.json['FooterRowsToSkip']
  afs.SplitThreshold = request.json['SplitThreshold']
  afs.RetentionPeriod = request.json['RetentionPeriod']
  afs.NamePattern = request.json['NamePattern']
  afs.Name = request.json['Name']
  afs.IsCompressed = request.json['IsCompressed']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactFile(ArtefactFileID):
    qryRes = ArtefactFile.query.filter_by(ArtefactFileID=ArtefactFileID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

def geteArtefactFileByArtefact(ArtefactID):
  qryRes = ArtefactFile.query.filter_by(ArtefactID=ArtefactID).all()
  return [i.serialize for i in qryRes],200

############################################################################################

def addArtefactTable(Request):
  
  ColumnListContent = getColumnList(Request.json.get('ColumnListContent'))
  if not ColumnListContent:
      ArtefactID =  getRandomBigInt()
      params = {'ArtefactID': ArtefactID,            
                'Name': Request.json.get('Name'), 
                'Schema': Request.json.get('Schema'), 
                'Category': Request.json.get('Category'), 
                'Description': Request.json.get('Description'), 
                'BusinessDescription': Request.json.get('BusinessDescription'),  
                'Group': Request.json.get('Group'),            
                'FilterExpression': Request.json.get('FilterExpression'), 
                'ArtefactFileTypeId': Request.json.get('ArtefactFileTypeId') ,
                'ProcessWrapperID': Request.json.get('ProcessWrapperID'),
                'LoadPlanID': Request.json.get('LoadPlanID') 
            }

      db.session.execute('exec metadata.PostArtefactTable :ArtefactID,:Name,:Schema,:Category,:Description,:BusinessDescription,:Group,:FilterExpression,:ArtefactFileTypeId,:ProcessWrapperID,:LoadPlanID', params)
      addArtefactAttribute(Request.json.get('ColumnList'), Request.json.get('SourceTechnology') ,ArtefactID)

  
  else:
      for k  in ColumnListContent:
          
          colList = ",".join(ColumnListContent[k]['columns'])
          ArtefactID =  getRandomBigInt()
          schema = ColumnListContent[k]['schema']
          table =  ColumnListContent[k]['table']
          params = {'ArtefactID': ArtefactID,            
                'Name': table, 
                'Schema': schema, 
                'Category': '', 
                'Description': '', 
                'BusinessDescription': '',  
                'Group': '',            
                'FilterExpression': '', 
                'ArtefactFileTypeId': Request.json.get('ArtefactFileTypeId'),
                'SourceTechnology': Request.json.get('SourceTechnology'),
                'ProcessWrapperID': Request.json.get('ProcessWrapperID'),
                'LoadPlanID': Request.json.get('LoadPlanID')
            }
          print "Trying to create Artefact"
          db.session.execute('exec metadata.PostArtefactTable :ArtefactID,:Name,:Schema,:Category,:Description,:BusinessDescription,:Group,:FilterExpression,:ArtefactFileTypeId,:ProcessWrapperID,:LoadPlanID', params)
          addArtefactAttribute(colList, Request.json.get('SourceTechnology') ,ArtefactID)
  
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def getAllArtefactTable():
  qryRes = ArtefactTable.query.order_by(ArtefactTable.CreateDate).all()
  return [i.serialize for i in qryRes],200

def getSingleArtefactTable(ArtefactTableID):
  qryRes = ArtefactTable.query.filter_by(ArtefactTableID=ArtefactTableID).all()
  return qryRes[0].serialize ,200

def updateSingleArtefactTable(ArtefactTableID,request):
  qryRes = ArtefactTable.query.filter_by(ArtefactTableID=ArtefactTableID).all()
  afs = qryRes[0]
  afs.Schema = request.json['Schema']
  afs.Name = request.json['Name']
  afs.FilterExpression = request.json['FilterExpression']
  afs.Group = request.json['Group']
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactTable(ArtefactTableID):
    qryRes = ArtefactTable.query.filter_by(ArtefactTableID=ArtefactTableID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204

def geteArtefactTableByArtefact(ArtefactID):
  qryRes = ArtefactTable.query.filter_by(ArtefactID=ArtefactID).all()
  return [i.serialize for i in qryRes],200

############################################################################################

def addArtefactAttribute(ColumnList,SourceTechnology,ArtefactID):
   
  for k,v in enumerate(ColumnList.split(",")):
      params = {'ArtefactAttributeID': getRandomBigInt(),            
            'ArtefactID': ArtefactID, 
            'SourceTechnology': SourceTechnology,
            'TechnicalName': v, 
            'OrdinalPosition': k+1
            }
      
      db.session.execute('exec metadata.PostArtefactAttribute :ArtefactAttributeID,:ArtefactID,:SourceTechnology,:TechnicalName,:OrdinalPosition', params)
      safeFlush()
      safeCommit()
  return {"Success": True}, 201

def getAllArtefactAttribute():
  qryRes = ArtefactAttribute.query.order_by(ArtefactAttribute.ArtefactID,ArtefactAttribute.OrdinalPosition).all()

  return [i.serialize for i in qryRes],200

def getSingleArtefactAttribute(ArtefactAttributeID):
  qryRes = ArtefactAttribute.query.filter_by(ArtefactAttributeID=ArtefactAttributeID).all()
  
  return qryRes[0].serialize ,200

def updateSingleArtefactAttribute(ArtefactAttributeID,request):
  qryRes = ArtefactAttribute.query.filter_by(ArtefactAttributeID=ArtefactAttributeID).all()
  afs = qryRes[0]
  afs.IsIdentifier = request.json['IsIdentifier']
  afs.IsNullable = request.json['IsNullable']
  afs.TechnicalName = request.json['TechnicalName']
  afs.BusinessName = request.json['BusinessName']
  afs.AttributeDataTypeID = request.json['AttributeDataTypeID']
  afs.Precision = request.json['Precision']
  afs.Scale = request.json['Scale']
  afs.MaxLength = request.json['MaxLength']
  
  db.session.add(afs)
  safeFlush()
  safeCommit()
  return {"Success": True}, 201

def deleteSingleArtefactAttribute(ArtefactAttributeID):
    qryRes = ArtefactAttribute.query.filter_by(ArtefactAttributeID=ArtefactAttributeID).all()
    db.session.delete(qryRes[0])
    safeFlush()
    safeCommit()
    return {"Success": True}, 204    

def getArtefactAttributeByArtefact(ArtefactID):
  qryRes = ArtefactAttribute.query.filter_by(ArtefactID=ArtefactID).order_by(ArtefactAttribute.ArtefactID,ArtefactAttribute.OrdinalPosition).all()
  return [i.serialize for i in qryRes],200