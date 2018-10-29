import uuid
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict 
db = SQLAlchemy()

import uuid
from flask import jsonify
from datetime import datetime

def __str2datetime__(s):
    try:
        return datetime.strptime(s,'%Y-%m-%dT%H:%M:%S.%fZ')
    except:
        return datetime.strptime(s + 'T00:00:00.000Z','%Y-%m-%dT%H:%M:%S.%fZ')

def __datetime2str__(d):
    if d is None:
      return d

    return datetime.strftime(d,'%Y-%m-%d %H:%M:%S').decode('utf-8', 'ignore')

def __stringifyArray__(arr):
    return ",".join(arr)
def __stringifyArrayStruct__(arr):
    return "|".join([",".join([i+'#'+str(k[i]) for i in k.keys()]) for k in arr])
def __DestringifyArray__(s):
    return s.split(',')
def __byteArrToString__(b):
  #return "".join([str(x) for x in b])
  return "**********"

def __bitTranslator__(b):
  
  if b:
    return 1
  else:
    return 0

def __DestringifyArrayStruct__(s):
    try:
        arr = [dict([i.split('#') for i in k.split(",")]) for k in s.split('|')]
    except:
        arr = []
    return arr

class ArtefactFileSource(db.Model):
    __tablename__ = 'ArtefactFileSource'
    __table_args__ = {"schema": "metadata"}
    ArtefactFileSourceID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Type = db.Column(db.String(200), nullable=False)
    Location = db.Column(db.String(200))
    AccountName =  db.Column(db.String(200))
    ContainerName =  db.Column(db.String(200))
    Server =  db.Column(db.String(200))
    Port = db.Column(db.String(200))
    Username =  db.Column(db.String(200))
    IsInternal =  db.Column(db.Integer)
    SourceAlias =  db.Column(db.String(20))
    AccountKey =  db.Column(db.String(200))
    Password =  db.Column(db.String(200))
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request):
        
        pass
        


    @property
    def serialize(self):
       return {'ArtefactFileSourceID': self.ArtefactFileSourceID,
                'DisplayName': self.SourceAlias,
                'Type': self.Type,
               'Location': self.Location,
               'ContainerName': self.ContainerName,
               'AccountName': self.AccountName,
               'Server': self.Server,
               'Port': self.Port,
               'Username': self.Username,
               'IsInternal': self.IsInternal,
               'AccountKey': __byteArrToString__(self.AccountKey),
               'Password': __byteArrToString__(self.Password),
               'SourceAlias': self.SourceAlias
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)s
              }

##########################################
class ArtefactTableSource(db.Model):
    __tablename__ = 'ArtefactTableSource'
    __table_args__ = {"schema": "metadata"}
    ArtefactTableSourceID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Type = db.Column(db.String(200), nullable=False)
    Server =  db.Column(db.String(200))
    Port = db.Column(db.String(200))
    Database =  db.Column(db.String(200))
    ServiceName =  db.Column(db.String(200))
    SID =  db.Column(db.String(200))
    Schema =  db.Column(db.String(200))
    Username =  db.Column(db.String(200))
    ExternalDataSource =  db.Column(db.String(200))
    ExternalFileFormat =  db.Column(db.String(200))
    Location = db.Column(db.String(200))
    ContainerName =  db.Column(db.String(200))
    AccountName =  db.Column(db.String(200))
    IsInternal =  db.Column(db.Integer)
    AccountKey =  db.Column(db.String(200))
    Password =  db.Column(db.String(200))
    SourceAlias =  db.Column(db.String(200))
    GROUP =  db.Column(db.String(200))
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request):
        pass
  

    @property
    def serialize(self):
       return {'ArtefactTableSourceID': self.ArtefactTableSourceID,
                'DisplayName': self.SourceAlias,
                'Type': self.Type,
               'Server': self.Server,
               'Port': self.Port,

               'Database': self.Database,
               'ServiceName': self.ServiceName,
               'SID': self.SID,
               'Schema': self.Schema,
               'Username': self.Username,
               'ExternalDataSource': self.ExternalDataSource,
               'ExternalFileFormat': self.ExternalFileFormat,
               
               'Location': self.Location,
               'ContainerName': self.ContainerName,
               'AccountName': self.AccountName,
               
               'IsInternal': self.IsInternal,
               'AccountKey': __byteArrToString__(self.AccountKey),
               'Password': __byteArrToString__(self.Password),
               'SourceAlias': self.SourceAlias,
               'GROUP': self.GROUP
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }


#########################################

class AttributeDataType(db.Model):
    __tablename__ = 'AttributeDataType'
    __table_args__ = {"schema": "metadata"}
    AttributeDataTypeID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    DataTypeSQLServer = db.Column(db.String(200), nullable=False)
    DataTypeSybase =  db.Column(db.String(200))
    DataTypeOracle = db.Column(db.String(200))
    DataTypePolybase = db.Column(db.String(200))
    DataTypeAzureSQLDW = db.Column(db.String(200))
    DataTypeHive = db.Column(db.String(200))
    
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,adtid):
        self.AttributeDataTypeID = adtid
        self.DataTypeSQLServer = Request.json.get('DataTypeSQLServer')
        self.DataTypeSybase = Request.json.get('DataTypeSybase')
        self.DataTypeOracle = Request.json.get('DataTypeOracle')        
        
        self.DataTypePolybase = Request.json.get('DataTypePolybase')
        self.DataTypeAzureSQLDW = Request.json.get('DataTypeAzureSQLDW')
        self.DataTypeHive = Request.json.get('DataTypeHive')

        


    @property
    def serialize(self):
       return {'AttributeDataTypeID': self.AttributeDataTypeID,
                'DataTypeSQLServer': self.DataTypeSQLServer,
               'DataTypeSybase': self.DataTypeSybase,
               'DataTypeOracle': self.DataTypeOracle,

               'DataTypePolybase': self.DataTypePolybase,
               'DataTypeAzureSQLDW': self.DataTypeAzureSQLDW,
               'DataTypeHive': self.DataTypeHive,
               'DisplayName': "-".join([self.DataTypeSQLServer or self.DataTypeSybase or self.DataTypeOracle ])

              }

#########################################################

class ArtefactFileType(db.Model):
    __tablename__ = 'ArtefactFileType'
    __table_args__ = {"schema": "metadata"}
    ArtefactFileTypeID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Type = db.Column(db.String(200), nullable=False)
    Format =  db.Column(db.String(200))
    Encoding = db.Column(db.String(200))
    
    FieldSeparator = db.Column(db.String(200))
    RowSeparator = db.Column(db.String(200))
    TextQualifier = db.Column(db.String(200))
    File_Type_Alias = db.Column(db.String(200))
    
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,aftid):
        self.ArtefactFileTypeID = aftid
        self.Type = Request.json.get('Type')
        self.Format = Request.json.get('Format')
        self.Encoding = Request.json.get('Encoding')      
        self.FieldSeparator = Request.json.get('FieldSeparator')
        self.RowSeparator = Request.json.get('RowSeparator')
        self.TextQualifier = Request.json.get('TextQualifier')
        self.File_Type_Alias = Request.json.get('File_Type_Alias')


    @property
    def serialize(self):
       return {'ArtefactFileTypeID': self.ArtefactFileTypeID,
                'Type': self.Type,
               'Format': self.Format,
               'Encoding': self.Encoding,
               'DisplayName': self.File_Type_Alias,
               'FieldSeparator': self.FieldSeparator,
               'RowSeparator': self.RowSeparator,
               'TextQualifier': self.TextQualifier
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################

class Process(db.Model):
    __tablename__ = 'Process'
    __table_args__ = {"schema": "metadata"}
    ProcessID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Description =  db.Column(db.String(200))
    Type = db.Column(db.String(200))    
    RollbackType = db.Column(db.String(200))
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        self.ProcessID = processid
        self.Name = Request.json.get('Name')
        self.Description = Request.json.get('Description')        
        self.Type = Request.json.get('Type')
        self.RollbackType = Request.json.get('RollbackType')

    @property
    def serialize(self):
       return {'ProcessID': self.ProcessID,
                'Name': self.Name,
                'DisplayName': self.Name,
               'Description': self.Description,
               'Type': self.Type,
               'RollbackType': self.RollbackType
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }
#########################################################

class LoadPlan(db.Model):
    __tablename__ = 'LoadPlan'
    __table_args__ = {"schema": "metadata"}
    LoadPlanID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Category = db.Column(db.String(200))    
    Type = db.Column(db.String(200))    
    Description =  db.Column(db.String(200))    
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'LoadPlanID': self.LoadPlanID,
                'Name': self.Name,
                'DisplayName': self.Name,
                'Category': self.Category,
                'Type': self.Type,
                'Description': self.Description,                
               'CreateBy': self.CreateBy,
               'CreateDate': __datetime2str__(self.CreateDate),
               'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################

class ProcessGroup(db.Model):
    __tablename__ = 'ProcessGroup'
    __table_args__ = {"schema": "metadata"}
    ProcessGroupID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Description =  db.Column(db.String(200))  
    LoadPlanID = db.Column(db.BigInteger)
    ProcessID = db.Column(db.BigInteger)
    SourceArtefactFileSourceID = db.Column(db.BigInteger)
    SourceArtefactTableSourceID = db.Column(db.BigInteger)
    TargetArtefactFileSourceID = db.Column(db.BigInteger)    
    TargetArtefactTableSourceID = db.Column(db.BigInteger)  
    OrderOfExecution = db.Column(db.Integer)
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ProcessGroupID': self.ProcessGroupID,
                'Name': self.Name,
                'DisplayName': self.Name,
                'Description': self.Description, 
                'LoadPlanID': self.LoadPlanID,    
                'ProcessID': self.ProcessID,
                'SourceArtefactFileSourceID': self.SourceArtefactFileSourceID,
                'SourceArtefactTableSourceID': self.SourceArtefactTableSourceID,
                'TargetArtefactFileSourceID': self.TargetArtefactFileSourceID,
                'TargetArtefactTableSourceID': self.TargetArtefactTableSourceID,
                'OrderOfExecution': self.OrderOfExecution
                 #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################

class ProcessWrapper(db.Model):
    __tablename__ = 'ProcessWrapper'
    __table_args__ = {"schema": "metadata"}
    ProcessWrapperID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    ParentProcessWrapperID =  db.Column(db.BigInteger)
    ProcessArtefactID =  db.Column(db.BigInteger)
    Name = db.Column(db.String(200), nullable=False)     
    Type = db.Column(db.String(200)) 
    Order = db.Column(db.String(200))      
    ActionOnError = db.Column(db.String(200))   
    EffectiveFrom = db.Column(db.String(200))  
    EffectiveTo = db.Column(db.String(200))  
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ProcessWrapperID': self.ProcessWrapperID,
                'ParentProcessWrapperID': self.ParentProcessWrapperID,
                'ProcessArtefactID': self.ProcessArtefactID,
                'DisplayName': self.Name,
                'Name': self.Name,
                'Type': self.Type,
                'Order': self.Order,
                'ActionOnError': self.ActionOnError,  
                'EffectiveFrom': __datetime2str__(self.EffectiveFrom),
                'EffectiveTo': __datetime2str__(self.EffectiveTo)
                 #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################

class ProcessArtefact(db.Model):
    __tablename__ = 'ProcessArtefact'
    __table_args__ = {"schema": "metadata"}
    ProcessArtefactID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    ProcessID = db.Column(db.BigInteger)
    SourceArtefactFileID = db.Column(db.BigInteger)
    SourceArtefactTableID = db.Column(db.BigInteger)
    TargetArtefactFileID = db.Column(db.BigInteger)    
    TargetArtefactTableID = db.Column(db.BigInteger)  
    MaxRunAttempts = db.Column(db.Integer)
    RerunWaitingTime = db.Column(db.Integer)
    InMinThreshold = db.Column(db.Integer)
    InMaxThreshold = db.Column(db.Integer)
    OutMinThreshold = db.Column(db.Integer)
    OutMaxThreshold = db.Column(db.Integer)
    DurationMinThreshold = db.Column(db.Integer)
    DurationMaxThreshold = db.Column(db.Integer)
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ProcessArtefactID': self.ProcessArtefactID,
                'DisplayName': self.ProcessArtefactID,
                'ProcessID': self.ProcessID,
                'SourceArtefactFileID': self.SourceArtefactFileID,
                'SourceArtefactTableID': self.SourceArtefactTableID,
                'TargetArtefactFileID': self.TargetArtefactFileID,
                'TargetArtefactTableID': self.TargetArtefactTableID,
                'MaxRunAttempts': self.MaxRunAttempts,
                'RerunWaitingTime': self.RerunWaitingTime,
                'InMinThreshold': self.InMinThreshold,
                'InMaxThreshold': self.InMaxThreshold,
                'OutMinThreshold': self.OutMinThreshold,
                'OutMaxThreshold': self.OutMaxThreshold,
                'DurationMinThreshold': self.DurationMinThreshold,  
                'DurationMaxThreshold': self.DurationMaxThreshold,
                 #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################


class Artefact(db.Model):
    __tablename__ = 'Artefact'
    __table_args__ = {"schema": "metadata"}
    ArtefactID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    Name = db.Column(db.String(200), nullable=False)
    Category = db.Column(db.String(200))    
    Type = db.Column(db.String(200))    
    Description =  db.Column(db.String(200))    
    BusinessDescription = db.Column(db.String(200))
    Target_File_Type_Alias = db.Column(db.String(200))
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ArtefactID': self.ArtefactID,
                'Name': self.Name,
                'DisplayName': self.Target_File_Type_Alias,
                'Category': self.Category,
                'Type': self.Type,
                'Description': self.Description,                
               'BusinessDescription': self.BusinessDescription,
               'Target_File_Type_Alias': self.Target_File_Type_Alias
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################

class ArtefactFile(db.Model):
    __tablename__ = 'ArtefactFile'
    __table_args__ = {"schema": "metadata"}
    ArtefactFileID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    ArtefactID = db.Column(db.BigInteger)
    ArtefactFileTypeID = db.Column(db.BigInteger)
    ArtefactFileSourceID = db.Column(db.BigInteger)
    HeaderRowsToSkip = db.Column(db.Integer)
    FooterRowsToSkip = db.Column(db.Integer)
    SplitThreshold = db.Column(db.BigInteger)
    RetentionPeriod = db.Column(db.Integer)
    NamePattern = db.Column(db.String(200))    
    LoadType = db.Column(db.String(200))    
    IsCompressed =  db.Column(db.Integer)
    
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ArtefactFileID': self.ArtefactFileID,
                'DisplayName': self.ArtefactFileID,
                'ArtefactID': self.ArtefactID,
                'ArtefactFileTypeID': self.ArtefactFileTypeID,
                'ArtefactFileSourceID': self.ArtefactFileSourceID,
                'HeaderRowsToSkip': self.HeaderRowsToSkip,
                'FooterRowsToSkip': self.FooterRowsToSkip,                
               'SplitThreshold': self.SplitThreshold,
               'RetentionPeriod': self.RetentionPeriod,
               'NamePattern': self.NamePattern,
               'LoadType': self.LoadType or 'File',
               'IsCompressed': self.IsCompressed
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }
 
 #########################################################

class ArtefactTable(db.Model):
    __tablename__ = 'ArtefactTable'
    __table_args__ = {"schema": "metadata"}
    ArtefactTableID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    ArtefactID =  db.Column(db.BigInteger)
    ArtefactTableSourceID = db.Column(db.BigInteger)
    Schema =  db.Column(db.String(200))
    Name = db.Column(db.String(200), nullable=False)
    Type = db.Column(db.String(200))    
    FilterExpression = db.Column(db.String(2000))
    Group = db.Column(db.String(200))
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)

    def __init__(self,Request,processid):
        pass

    @property
    def serialize(self):
       return {'ArtefactTableID': self.ArtefactTableID,
               'DisplayName': self.ArtefactTableID,
               'ArtefactID': self.ArtefactID, 
               'ArtefactTableSourceID': self.ArtefactTableSourceID,
               'Schema': self.Schema,
                'Name': self.Name,                
                'Type': self.Type,    
               'FilterExpression': self.FilterExpression,
               'Group': self.Group
                #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################
class ArtefactAttribute(db.Model):
    __tablename__ = 'ArtefactAttribute'
    __table_args__ = {"schema": "metadata"}
    ArtefactAttributeID =  db.Column(db.BigInteger, nullable=False, primary_key=True)
    ArtefactID =  db.Column(db.BigInteger)
    AttributeDataTypeID = db.Column(db.BigInteger)
    IsIdentifier =  db.Column(db.Integer)
    IsNullable =  db.Column(db.Integer)
    OrdinalPosition =  db.Column(db.Integer)
    TechnicalName =  db.Column(db.String(200))
    BusinessName =  db.Column(db.String(200))
    DataType =  db.Column(db.String(200))
    Precision =  db.Column(db.Integer)
    Scale =  db.Column(db.Integer)
    MaxLength =  db.Column(db.Integer)
    Pattern =  db.Column(db.String(200))
    UsedForETL =  db.Column(db.Integer)
    CreateBy =  db.Column(db.String(200))
    CreateDate =  db.Column(db.DateTime)
    ExpiryDate =  db.Column(db.DateTime)
    ColumnPrefix =  db.Column(db.String(10))

    def __init__(self,Request,adtid):
        pass

        


    @property
    def serialize(self):
       return {'ArtefactAttributeID': self.ArtefactAttributeID,
                'ArtefactID': self.ArtefactID,
               'AttributeDataTypeID': self.AttributeDataTypeID,
               'IsIdentifier': __bitTranslator__(self.IsIdentifier),
               'IsNullable': __bitTranslator__(self.IsNullable),
               'OrdinalPosition': self.OrdinalPosition,
               'TechnicalName': self.TechnicalName,
               'BusinessName': self.BusinessName,
               'DataType': self.DataType,
               'Precision': self.Precision,
               'Scale': self.Scale,
               'MaxLength': self.MaxLength,
               'Pattern': self.Pattern,
               'UsedForETL': self.Pattern,
               'ColumnPrefix': self.Pattern
               #'CreateBy': self.CreateBy,
               #'CreateDate': __datetime2str__(self.CreateDate),
               #'ExpiryDate': __datetime2str__(self.ExpiryDate)
              }

#########################################################
class BatchProcessArtefact(db.Model):
    __tablename__ = 'vw_BatchProcessArtefact'
    __table_args__ = {"schema": "metadata"}
    BatchProcessArtefactID = db.Column(db.String(200),primary_key=True)
    Source_ArtefactID =  db.Column(db.String(200))
    Source_ArtefactName =  db.Column(db.String(200))
    BatchID =  db.Column(db.String(200))
    
    RowsIn =  db.Column(db.String(200))
    RowsOut =  db.Column(db.String(200))
    Name =  db.Column(db.String(200))
    ActionOnError =  db.Column(db.String(200))
    Status =  db.Column(db.String(200))
    StartDT =  db.Column(db.String(200))
    EndDT =  db.Column(db.String(200))
    

    def __init__(self,Request,adtid):
        pass

        
    

    @property
    def serialize(self):

       o = OrderedDict()
       o['BatchProcessArtefactID'] = self.BatchProcessArtefactID
       o['Source_ArtefactID'] = self.Source_ArtefactID
       o['Source_ArtefactName'] = self.Source_ArtefactName
       o['BatchID'] = self.BatchID
       o['RowsIn'] = self.RowsIn
       o['RowsOut'] = self.RowsOut
       o['Discrepency'] = (self.RowsIn or 0) - (self.RowsOut or 0)
       o['Name'] = self.Name
       o['ActionOnError'] = self.ActionOnError
       o['Status'] = self.Status.upper()
       o['StartDT'] = __datetime2str__(self.StartDT)
       o['EndDT'] = __datetime2str__(self.EndDT)
       
       return o
       

