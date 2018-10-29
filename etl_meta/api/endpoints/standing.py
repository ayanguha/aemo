from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import Resource
from ..database.models import *
from ..handlers.standing import *
from flask_restplus import abort
import traceback

from flask_restplus import Api

api = Api(version='1.0', title='ETL MEta',doc='/doc/',description='ETL Meta API')


ns = api.namespace('api/standing', description='Standing Data')

ArtefactFileSourceRecord = api.model('ArtefactFileSourceRecord', {
    'Type': fields.String,
    'Location': fields.String,
    'ContainerName': fields.String,
    'FeedAttributeType': fields.String,
    'AccountName': fields.String,
    'Server': fields.String,
    'Port': fields.String,
    'Username': fields.String,
    'IsInternal': fields.Integer,
    'AccountKey': fields.String,
    'Password': fields.String,
    'CreateBy': fields.String
})

ArtefactTableSourceRecord = api.model('ArtefactTableSourceRecord', {
    'Type': fields.String,
    'Server': fields.String,
    'Port': fields.String,
    'Database': fields.String,
    'ServiceName': fields.String,
    'SID': fields.String,
    'Schema': fields.String,
    'Username': fields.String,
    'ExternalDataSource': fields.String,
    'ExternalFileFormat': fields.String,
    'Location': fields.String,
    'ContainerName': fields.String,
    'FeedAttributeType': fields.String,
    'AccountName': fields.String, 
    'IsInternal': fields.Integer,
    'AccountKey': fields.String,
    'Password': fields.String,
    'SourceAlias': fields.String,
    'GROUP': fields.String,
    'CreateBy': fields.String
})

AttributeDataTypeRecord = api.model('AttributeDataTypeRecord', {
    'DataTypeSQLServer': fields.String,
    'DataTypeSybase': fields.String,
    'DataTypeOracle': fields.String,
    'DataTypePolybase': fields.String,
    'DataTypeAzureSQLDW': fields.String,
    'DataTypeHive': fields.String,
    'CreateBy': fields.String
})

ArtefactFileTypeRecord = api.model('ArtefactFileTypeRecord', {
    'Type': fields.String,
    'Format': fields.String,
    'Encoding': fields.String,
    'FieldSeparator': fields.String,
    'RowSeparator': fields.String,
    'TextQualifier': fields.String,
    'File_Type_Alias': fields.String,
    'CreateBy': fields.String
})

ProcessRecord = api.model('ProcessRecord', {
    'Name': fields.String,
    'Description': fields.String,
    'Type': fields.String,
    'RollbackType': fields.String,
    'CreateBy': fields.String
})



######################################################

@ns.route('/ArtefactFileSource')
class ArtefactFileSource(Resource):
    @api.expect(ArtefactFileSourceRecord)
    def post(self):      
        
        response,code = addArtefactFileSource(request)
        return response, code
    def get(self):
        response,code = getAllArtefactFileSource()
        return response, code

@ns.route('/ArtefactFileSource/<ArtefactFileSourceID>')
class SingleArtefactFileSource(Resource):
    @api.expect(ArtefactFileSourceRecord)
    def put(self,ArtefactFileSourceID):
        response,code = updateSingleArtefactFileSource(ArtefactFileSourceID,request)
        return response, code
    def get(self,ArtefactFileSourceID):
        response,code = getSingleArtefactFileSource(ArtefactFileSourceID)
        return response
    def delete(self,ArtefactFileSourceID):
        response,code = deleteSingleArtefactFileSource(ArtefactFileSourceID)
        return response, code

##############################################################################################

@ns.route('/ArtefactTableSource')
class ArtefactTableSource(Resource):
    @api.expect(ArtefactFileSourceRecord)
    def post(self):      
        response,code = addArtefactTableSource(request)
        return response, code
    def get(self):
        response,code = getAllArtefactTableSource()
        return response, code

@ns.route('/ArtefactTableSource/<string:ArtefactTableSourceID>')
class SingleArtefactTableSource(Resource):
    @api.expect(ArtefactFileSourceRecord)
    def put(self,ArtefactTableSourceID):
        response,code = updateSingleArtefactTableSource(ArtefactTableSourceID,request)
        return response, code
    def get(self,ArtefactTableSourceID):
        response,code = getSingleArtefactTableSource(ArtefactTableSourceID)
        return response, code
    def delete(self,ArtefactTableSourceID):
        response,code = deleteSingleArtefactTableSource(ArtefactTableSourceID)
        return response, code

##############################################################################################

@ns.route('/AttributeDataType')
class AttributeDataType(Resource):
    @api.expect(AttributeDataTypeRecord)
    def post(self):      
        response,code = addAttributeDataType(request)
        return response, code
    def get(self):
        response,code = getAllAttributeDataType()
        return response, code

@ns.route('/AttributeDataType/<string:AttributeDataTypeID>')
class SingleAttributeDataType(Resource):
    @api.expect(AttributeDataTypeRecord)
    def put(self,AttributeDataTypeID):
        response,code = updateSingleAttributeDataType(AttributeDataTypeID,request)
        return response, code
    def get(self,AttributeDataTypeID):
        response,code = getSingleAttributeDataType(AttributeDataTypeID)
        return response, code
    def delete(self,AttributeDataTypeID):
        response,code = deleteSingleAttributeDataType(AttributeDataTypeID)
        return response, code

##############################################################################################

@ns.route('/ArtefactFileType')
class ArtefactFileType(Resource):
    @api.expect(ArtefactFileTypeRecord)
    def post(self):      
        response,code = addArtefactFileType(request)
        return response, code
    def get(self):
        response,code = getAllArtefactFileType()
        return response, code

@ns.route('/ArtefactFileType/<string:ArtefactFileTypeID>')
class SingleArtefactFileType(Resource):
    @api.expect(ArtefactFileTypeRecord)
    def put(self,ArtefactFileTypeID):
        response,code = updateSingleArtefactFileType(ArtefactFileTypeID,request)
        return response, code
    def get(self,ArtefactFileTypeID):
        response,code = getSingleArtefactFileType(ArtefactFileTypeID)
        return response, code
    def delete(self,ArtefactFileTypeID):
        response,code = deleteSingleArtefactFileType(ArtefactFileTypeID)
        return response, code


##############################################################################################

@ns.route('/Process')
class Process(Resource):
    @api.expect(ProcessRecord)
    def post(self):      
        response,code = addProcess(request)
        return response, code
    def get(self):
        response,code = getAllProcesss()
        return response, code

@ns.route('/Process/<string:ProcessID>')
class SingleProcess(Resource):
    @api.expect(ProcessRecord)
    def put(self,ProcessID):
        response,code = updateSingleProcess(ProcessID,request)
        return response, code
    def get(self,ProcessID):
        response,code = getSingleProcess(ProcessID)
        return response, code
    def delete(self,ProcessID):
        response,code = deleteSingleProcess(ProcessID)
        return response, code

##############################################################################################

LoadPlanRecord = api.model('LoadPlanRecord', {    
    'Name': fields.String,
    'Category': fields.String,
    'Type': fields.String,
    'Description': fields.String,
    'BusinessDescription': fields.String
})

@ns.route('/LoadPlan')
class LoadPlan(Resource):
    @api.expect(LoadPlanRecord)
    def post(self):      
        response,code = addLoadPlan(request)
        return response, code
    def get(self):
        response,code = getAllLoadPlans()
        return response, code

@ns.route('/LoadPlan/<string:LoadPlanID>')
class SingleLoadPlan(Resource):
    @api.expect(LoadPlanRecord)
    def put(self,LoadPlanID):
        response,code = updateSingleLoadPlan(LoadPlanID,request)
        return response, code
    def get(self,LoadPlanID):
        response,code = getSingleLoadPlan(LoadPlanID)
        return response, code
    def delete(self,LoadPlanID):
        response,code = deleteSingleLoadPlan(LoadPlanID)
        return response, code



##############################################################################################

ProcessGroupRecord = api.model('ProcessGroupRecord', {    
    'Name': fields.String,
    'Description': fields.String,
    'LoadPlanID': fields.String,
    'ProcessID': fields.String,
    'SourceArtefactFileSourceID': fields.String,
    'SourceArtefactTableSourceID': fields.String,
    'TargetArtefactFileSourceID': fields.String,
    'TargetArtefactTableSourceID': fields.String,
    'OrderOfExecution':fields.Integer
})

@ns.route('/ProcessGroup')
class ProcessGroup(Resource):
    @api.expect(ProcessGroupRecord)
    def post(self):      
        response,code = addProcessGroup(request)
        return response, code
    def get(self):
        response,code = getAllProcessGroups()
        return response, code

@ns.route('/ProcessGroup/<string:ProcessGroupID>')
class SingleProcessGroup(Resource):
    @api.expect(ProcessGroupRecord)
    def put(self,ProcessGroupID):
        response,code = updateSingleProcessGroup(ProcessGroupID,request)
        return response, code
    def get(self,ProcessGroupID):
        response,code = getSingleProcessGroup(ProcessGroupID)
        return response, code
    def delete(self,ProcessGroupID):
        response,code = deleteSingleProcessGroup(ProcessGroupID)
        return response, code

##############################################################################################

ProcessWrapperRecord = api.model('ProcessWrapperRecord', {    
    'Name': fields.String,
    'Description': fields.String,
    'LoadPlanID': fields.String,
    'ProcessID': fields.String,
    'SourceArtefactFileSourceID': fields.String,
    'SourceArtefactTableSourceID': fields.String,
    'TargetArtefactFileSourceID': fields.String,
    'TargetArtefactTableSourceID': fields.String,
    'OrderOfExecution':fields.Integer
})

@ns.route('/ProcessWrapper')
class ProcessWrapper(Resource):
    @api.expect(ProcessWrapperRecord)
    def post(self):      
        response,code = addProcessWrapper(request)
        return response, code
    def get(self):
        response,code = getAllProcessWrappers()
        return response, code

@ns.route('/ProcessWrapper/<string:ProcessWrapperID>')
class SingleProcessWrapper(Resource):
    @api.expect(ProcessWrapperRecord)
    def put(self,ProcessWrapperID):
        response,code = updateSingleProcessWrapper(ProcessWrapperID,request)
        return response, code
    def get(self,ProcessWrapperID):
        response,code = getSingleProcessWrapper(ProcessWrapperID)
        return response, code
    def delete(self,ProcessWrapperID):
        response,code = deleteSingleProcessWrapper(ProcessWrapperID)
        return response, code


##############################################################################################


@ns.route('/ProcessArtefact')
class ProcessArtefact(Resource):
    
    def get(self):
        response,code = getAllProcessArtefacts()
        return response, code

@ns.route('/ProcessArtefact/<string:ProcessArtefactID>')
class SingleProcessArtefact(Resource):
    def put(self,ProcessArtefactID):
        response,code = updateSingleProcessArtefact(ProcessArtefactID,request)
        return response, code
    def get(self,ProcessArtefactID):
        response,code = getSingleProcessArtefact(ProcessArtefactID)
        return response, code
    