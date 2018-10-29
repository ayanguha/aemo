from ..database import db
from ..database.models import *
from sqlalchemy.orm.exc import NoResultFound
from flask_restplus import fields
import uuid,random
from flask_restplus import reqparse
from datetime import datetime

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


def getRandomBigInt():
  return random.randint(1,2000000000) #uuid.uuid4().hex, 

############################################################################################

def getAllBatchProcessArtefact():
  qryRes = BatchProcessArtefact.query.order_by(BatchProcessArtefact.BatchProcessArtefactID.desc()).all()
  
  return [i.serialize for i in qryRes],200