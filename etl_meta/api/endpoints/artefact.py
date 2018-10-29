from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.artefact import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('api/artefact', description='Artefact Data')

#########################################################
ArtefactRecord = api.model('ArtefactRecord', {    
    'Name': fields.String,
    'Category': fields.String,
    'Type': fields.String,
    'Description': fields.String,
    'BusinessDescription': fields.String,
    'Target_File_Type_Alias': fields.String
})



@ns.route('/artefact')
class Artefact(Resource):
    @api.expect(ArtefactRecord)
    def post(self):      
        response,code = addArtefact(request)
        return response, code
    def get(self):
        response,code = getAllArtefacts()
        return response, code

@ns.route('/artefact/<string:ArtefactID>')
class SingleArtefact(Resource):
    @api.expect(ArtefactRecord)
    def put(self,ArtefactID):
        response,code = updateSingleArtefact(ArtefactID,request)
        return response, code
    def get(self,ArtefactID):
        response,code = getSingleArtefact(ArtefactID)
        return response, code
    def delete(self,ArtefactID):
        response,code = deleteSingleArtefact(ArtefactID)
        return response, code


#########################################################

@ns.route('/ArtefactFile')
class ArtefactFile(Resource):
    def post(self):      
        response,code = addArtefactFile(request)
        return response, code
    def get(self):
        response,code = getAllArtefactFiles()
        return response, code

@ns.route('/ArtefactFile/<string:ArtefactFileID>')
class SingleArtefactFile(Resource):
    def put(self,ArtefactFileID):
        response,code = updateSingleArtefactFile(ArtefactFileID,request)
        return response, code
    def get(self,ArtefactFileID):
        response,code = getSingleArtefactFile(ArtefactFileID)
        return response, code
    def delete(self,ArtefactFileID):
        response,code = deleteSingleArtefactFile(ArtefactFileID)
        return response, code

@ns.route('/artefact/<string:ArtefactID>/ArtefactFile/')
class ArtefactFileByArtefact(Resource):
    
    def get(self,ArtefactID):
        response,code = geteArtefactFileByArtefact(ArtefactID)
        return response, code
   

#########################################################
ArtefactTableRecord = api.model('ArtefactTableRecord', {    
    'ArtefactID': fields.Integer,
    'ArtefactTableSourceID': fields.Integer,
    'Schema': fields.String,
    'Name': fields.String,
    'Type': fields.String,
    'FilterExpression': fields.String,
    'Group': fields.String
})

@ns.route('/ArtefactTable')
class ArtefactTable(Resource):
    @api.expect(ArtefactTableRecord)
    def post(self):      
        response,code = addArtefactTable(request)
        return response, code
    def get(self):
        response,code = getAllArtefactTables()
        return response, code

@ns.route('/ArtefactTable/<string:ArtefactTableID>')
class SingleArtefactTable(Resource):
    @api.expect(ArtefactTableRecord)
    def put(self,ArtefactTableID):
        response,code = updateSingleArtefactTable(ArtefactTableID,request)
        return response, code
    def get(self,ArtefactTableID):
        response,code = getSingleArtefactTable(ArtefactTableID)
        return response, code
    def delete(self,ArtefactTableID):
        response,code = deleteSingleArtefactTable(ArtefactTableID)
        return response, code

@ns.route('/artefact/<string:ArtefactID>/ArtefactTable/')
class ArtefactTableByArtefact(Resource):
    
    def get(self,ArtefactID):
        response,code = geteArtefactTableByArtefact(ArtefactID)
        return response, code
#########################################################


@ns.route('/ArtefactAttribute')
class ArtefactAttribute(Resource):
    def post(self):
        response,code = addArtefactAttribute(request)
        return response, code
    def get(self):
        response,code = getAllArtefactAttributes()
        return response, code

@ns.route('/ArtefactAttribute/<string:ArtefactAttributeID>')
class SingleArtefactAttribute(Resource):
    def put(self,ArtefactAttributeID):
        response,code = updateSingleArtefactAttribute(ArtefactAttributeID,request)
        return response, code
    def get(self,ArtefactAttributeID):
        response,code = getSingleArtefactAttribute(ArtefactAttributeID)
        return response, code
    def delete(self,ArtefactAttributeID):
        response,code = deleteSingleArtefactAttribute(ArtefactAttributeID)
        return response, code