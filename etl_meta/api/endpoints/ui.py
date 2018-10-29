from flask import request,render_template,make_response,jsonify,redirect,url_for
from flask_restplus import  Resource, reqparse
from ..handlers.standing import *
from ..handlers.artefact import *
from ..handlers.monitoring import *

class UIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template('index.html'), 200,headers)


class StandingUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs,code = getAllArtefactFileSource()
        ats,code = getAllArtefactTableSource()
        adt,code = getAllAttributeDataType()
        aft,code = getAllArtefactFileType()
        process,code = getAllProcesss()
        lp,code = getAllLoadPlans()
        pg,code = getAllProcessGroups()
        oml,code = getProcessWrapperOrchMaster()
        ol,code = getAllProcessWrappers()
        pal,code = getAllProcessArtefacts()
        return make_response(
                render_template('standing.html',
                             AFSList=afs,
                             ATSList=ats,
                             ADTList=adt,
                             AFTList=aft,
                             ProcessList=process,
                             LPList=lp,
                             PGList=pg,
                             OrchestratorMasterList=oml,
                             OrchestratorList=ol,
                             ProcessArtefactList=pal), 200,headers)

############################################################################################

class AFSUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs,code = getAllArtefactFileSource()
        
        return make_response(
                render_template('AFS.html',
                             AFSList=afs), 200,headers)
############################################################################################

class ATSUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        ats,code = getAllArtefactTableSource()
        
        return make_response(
                render_template('ATS.html',
                              ATSList=ats), 200,headers)
############################################################################################

class ADTUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        adt,code = getAllAttributeDataType()
        
        return make_response(
                render_template('ADT.html',
                              ADTList=adt), 200,headers)
############################################################################################

class AFTUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        aft,code = getAllArtefactFileType()
        
        return make_response(
                render_template('AFT.html',
                              AFTList=aft), 200,headers)
############################################################################################


class ProcessUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        process,code = getAllProcesss()
        
        return make_response(
                render_template('Process.html',
                              ProcessList=process), 200,headers)
############################################################################################


class LoadPlanUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        afs,code = getAllArtefactFileSource()
        ats,code = getAllArtefactTableSource()
        process,code = getAllProcesss()
        lp,code = getAllLoadPlans()
        pg,code = getAllProcessGroups()
        return make_response(
                render_template('LoadPlan.html',
                               AFSList=afs,
                               ATSList=ats,
                               ProcessList=process,
                               LPList=lp,
                               PGList=pg), 200,headers)

class ProcessWrapperUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        lp,code = getAllLoadPlans()
        oml,code = getProcessWrapperOrchMaster()
        ol,code = getAllProcessWrappers()
        pal,code = getAllProcessArtefacts()
        return make_response(
                render_template('ProcessWrapper.html',
                               LPList=lp,
                               OrchestratorMasterList=oml,
                               OrchestratorList=ol,
                               ProcessArtefactList=pal
                               ), 200,headers)

############################################################################################

class ArtefactListUIHandler(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        adt,code = getAllAttributeDataType()
        aft,code = getAllArtefactFileType()
        oml,code = getProcessWrapperOrchMaster()
        lp,code = getAllLoadPlans()
        artefact,code = getAllArtefact()
        
        return make_response(
                render_template('ingestion.html',
                                ADTList=adt,
                                AFTList=aft,
                                LoadPlanList=lp,
                                OrchestratorMasterList=oml,
                                ArtefactList=artefact,
                                ), 
                   200,headers)


ArtrfactResourceParser = reqparse.RequestParser()
ArtrfactResourceParser.add_argument('ArtefactID', type=int)

############################################################################################

class ArtefactUIHandler(Resource):
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        args = ArtrfactResourceParser.parse_args()
        
        ArtefactID = args['ArtefactID']
        afs,code = getAllArtefactFileSource()
        ats,code = getAllArtefactTableSource()
        adt,code = getAllAttributeDataType()
        aft,code = getAllArtefactFileType()
        artefact,code = getSingleArtefact(ArtefactID)
        
        artefactfile,code = geteArtefactFileByArtefact(ArtefactID)
        artefacttable,code = geteArtefactTableByArtefact(ArtefactID)
        
        artefactAttributes,code = getArtefactAttributeByArtefact(ArtefactID)


        
        return make_response(
                render_template('artefact.html',
                                AFSList=afs,
                                ATSList=ats,
                                ADTList=adt,
                                AFTList=aft,
                                ArtefactList=artefact,
                                ArtefactFileList=artefactfile,
                                ArtefactTableList=artefacttable,
                                
                                ArtefactAttributes=artefactAttributes), 
                   200,headers)


############################################################################################

class MonitoringUIHandler(Resource):
    
    def get(self):
        headers = {'Content-Type': 'text/html'}
        

        BatchProcessArtefactList,code = getAllBatchProcessArtefact()
        

        return make_response(
                render_template('monitoring.html',
                                BatchProcessArtefactList=BatchProcessArtefactList,), 
                   200,headers)
