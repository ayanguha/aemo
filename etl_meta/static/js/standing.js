function redirectHome(collapseId){
  
  window.location =  location.href;
}

function addAFS() {
    
    var name = $('#AFSSourceAlias').val();
    if (!name) {
      alert("Name is Required");
      $('#AFSSourceAlias').addClass('warning');
      
    }
    else {
    var isChecked = $('#AFSIsInternal').is(':checked')? 1: 0;
    
    var data = {
                "Type": $('#AFStype').val(),
                "Location": $('#AFSLocation').val(),
                "AccountName": $('#AFSAccountName').val(),
                "AccountName": $('#AFSAccountName').val(),
                "ContainerName": $('#AFSContainerName').val(),
                "Server": $('#AFSServer').val(),
                "Port": $('#AFSPort').val(),
                "Username": $('#AFSUsername').val(),
                "IsInternal": isChecked,
                "AccountKey": $('#AFSAccountKey').val(),
                "Password": $('#AFSPassword').val(),
                "SourceAlias": $('#AFSSourceAlias').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: AFSURL,
          success: function(result) {alert('AFS Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

  }

function addATS() {
    var name = $('#ATSSourceAlias').val();
    if (!name) {
      alert("Name is Required");
      $('#ATSSourceAlias').addClass('warning');
      
    }
    else {
    var isChecked = $('#ATSIsInternal').is(':checked')? 1: 0;
    var data = {
                "Type": $('#ATStype').val(),
                "Server": $('#ATSServer').val(),
                "Port": $('#ATSPort').val(),
                "Database": $('#ATSDatabase').val(),
                "ServiceName": $('#ATSServiceName').val(),
                "SID": $('#ATSSID').val(),
                "Schema": $('#ATSSchema').val(),
                "Username": $('#ATSUsername').val(),
                "ExternalDataSource": $('#ATSExternalDataSource').val(),
                "ExternalFileFormat": $('#ATSExternalFileFormat').val(),
                "Location": $('#ATSLocation').val(),
                "AccountName": $('#ATSAccountName').val(),
                "AccountName": $('#ATSAccountName').val(),
                "ContainerName": $('#ATSContainerName').val(),
                "IsInternal": isChecked,
                "AccountKey": $('#ATSAccountKey').val(),
                "Password": $('#ATSPassword').val(),
                "SourceAlias": $('#ATSSourceAlias').val(),
                "GROUP": $('#ATSGROUP').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ATSURL,
          success: function(result) {alert('ATS Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }
  }

function addADT() {
    
    var data = {
                "DataTypeSQLServer": $('#ADTDataTypeSQLServer').val(),
                "DataTypeSybase": $('#ADTDataTypeSybase').val(),
                "DataTypeOracle": $('#ADTDataTypeOracle').val(),
                "DataTypePolybase": $('#ADTDataTypePolybase').val(),
                "DataTypeAzureSQLDW": $('#ADTDataTypeAzureSQLDW').val(),
                "DataTypeHive": $('#ADTDataTypeHive').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ADTURL,
          success: function(result) {alert('ADT Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }


function addAFT() {
    
    var data = {
                "Type": $('#AFTType').val(),
                "Format": $('#AFTFormat').val(),
                "Encoding": $('#AFTEncoding').val(),
                "FieldSeparator": $('#AFTFieldSeparator').val(),
                "RowSeparator": $('#AFTRowSeparator').val(),
                "TextQualifier": $('#AFTTextQualifier').val(),
                "File_Type_Alias": $('#AFTFile_Type_Alias').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: AFTURL,
          success: function(result) {alert('AFT Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

function addProcess() {
    
    var data = {
                "Name": $('#ProcessName').val(),
                "Description": $('#ProcessDescription').val(),
                "Type": $('#ProcessType').val(),
                "RollbackType": $('#ProcessRollbackType').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ProcessURL,
          success: function(result) {alert('Process Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

function addLP() {
    
    var data = {
                "Name": $('#LPName').val(),
                "Type": $('#LPType').val(),
                "Category": $('#LPCategory').val(),
                "Description": $('#LPDescription').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: LoadPlanURL,
          success: function(result) {alert('Load Plan Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

function addPG(lpid) {
    
    var data = {
                "Name": $('#PGName_'+lpid).val(),
                "Description": $('#PGDescription_'+lpid).val(),
                "LoadPlanID": lpid,
                "ProcessID": $('#PGProcessDropDown_'+lpid).val(),
                "SourceArtefactFileSourceID": $('#PGSourceArtefactFileSourceID_'+lpid).val(),
                "SourceArtefactTableSourceID": $('#PGSourceArtefactTableSourceID_'+lpid).val(),
                "TargetArtefactFileSourceID": $('#PGTargetArtefactFileSourceID_'+lpid).val(),
                "TargetArtefactTableSourceID": $('#PGTargetArtefactTableSourceID_'+lpid).val(),
                "OrderOfExecution": $('#PGOrderOfExecution_'+lpid).val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ProcessGroupURL,
          success: function(result) {alert('Process Group Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

function addProcessWrapper() {
    
    var data = {
                "Name": $('#PWName').val()
              };



    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ProcessWrapperURL,
          success: function(result) {alert('new Orchestrator Master Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }


function setAndOpenAFSModal(afsid) {
         $('#UpdAFSHiddenid').val(afsid);
         //var url = "{{ url_for('api.api/standing_single_artefact_file_source', ArtefactFileSourceID='PLACEHOLDER') }}".replace("PLACEHOLDER", afsid);
         var url = SingleAFSURL.replace("PLACEHOLDER", afsid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdAFSType").val(result.Type);
              $('#UpdAFSLocation').val(result.Location);  

              $('#UpdAFSAccountName').val(result.AccountName);  
              $('#UpdAFSContainerName').val(result.ContainerName);  
              $('#UpdAFSServer').val(result.Server);  
              $('#UpdAFSPort').val(result.Port);  
              $('#UpdAFSUsername').val(result.Username);  
              $('#UpdAFSIsInternal').val(result.IsInternal);  
              $('#UpdAFSSourceAlias').val(result.SourceAlias);  
              $('#UpdAFSAccountKey').val(result.AccountKey);  
              $('#UpdAFSPassword').val(result.Password);  

               $('#UpdateAFSModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

         
      

function updateAFS() {
        var afsid = $('#UpdAFSHiddenid').val();
        var url = SingleAFSURL.replace("PLACEHOLDER", afsid);
        var data = {"Type": $("#UpdAFSType").val(),
                    "Location": $('#UpdAFSLocation').val(),
                    "AccountName": $('#UpdAFSAccountName').val(),
                    "ContainerName": $('#UpdAFSContainerName').val(),
                    "Server": $('#UpdAFSServer').val(),
                    "Port": $('#UpdAFSPort').val(),
                    "Username": $('#UpdAFSUsername').val(),
                    "SourceAlias": $('#UpdAFSSourceAlias').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('AFS Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenATSModal(atsid) {
         $('#UpdATSHiddenid').val(atsid);
         var url = SingleATSURL.replace("PLACEHOLDER", atsid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdATSType").val(result.Type);
              $("#UpdATSServer").val(result.Server);
              $("#UpdATSPort").val(result.Port);
              $("#UpdATSDatabase").val(result.Database);
              $("#UpdATSServiceName").val(result.ServiceName);
              $("#UpdATSSID").val(result.SID);
              $("#UpdATSSchema").val(result.Schema);
              $("#UpdATSDUsername").val(result.Username);
              $("#UpdATSExternalDataSource").val(result.ExternalDataSource);
              $("#UpdATSExternalFileFormat").val(result.ExternalFileFormat);
              $("#UpdATSLocation").val(result.Location);
              $("#UpdATSAccountName").val(result.AccountName);
              $("#UpdATSContainerName").val(result.ContainerName);
              $("#UpdATSIsInternal").val(result.IsInternal);
              $("#UpdATSAccountKey").val(result.AccountKey);
              $("#UpdATSPassword").val(result.Password);
              $("#UpdATSSourceAlias").val(result.SourceAlias);
              $("#UpdATSGROUP").val(result.GROUP);
               $('#UpdateATSModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }
       
function updateATS() {
        var atsid = $('#UpdATSHiddenid').val();
        var url = SingleATSURL.replace("PLACEHOLDER", atsid);
        var data = {"Type": $("#UpdATSType").val(),
                    "Server": $("#UpdATSServer").val(),
                    "Port": $("#UpdATSPort").val(),
                    "Database": $("#UpdATSDatabase").val(),
                    "ServiceName": $("#UpdATSServiceName").val(),
                    "SID": $("#UpdATSSID").val(),
                    "Schema": $("#UpdATSSchema").val(),
                    "Username": $("#UpdATSDUsername").val(),
                    "ExternalDataSource": $("#UpdATSExternalDataSource").val(),
                    "ExternalFileFormat": $("#UpdATSExternalFileFormat").val(),
                    "Location": $("#UpdATSLocation").val(),
                    "AccountName": $("#UpdATSAccountName").val(),
                    "ContainerName": $("#UpdATSContainerName").val(),
                    "IsInternal": $("#UpdATSIsInternal").val(),
                    "SourceAlias": $("#UpdATSSourceAlias").val(),
                    "GROUP": $("#UpdATSGROUP").val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('ATS Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenADTModal(adtid) {
         $('#UpdADTHiddenid').val(adtid);
         var url = SingleADTURL.replace("PLACEHOLDER", adtid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdADTDataTypeSQLServer").val(result.DataTypeSQLServer);
              $('#UpdADTDataTypeSybase').val(result.DataTypeSybase);  
              $('#UpdADTDataTypeOracle').val(result.DataTypeOracle);  
              $('#UpdADTDataTypePolybase').val(result.DataTypePolybase);  
              $('#UpdADTDataTypeAzureSQLDW').val(result.DataTypeAzureSQLDW);  
              $('#UpdADTDataTypeHive').val(result.DataTypeHive); 
               $('#UpdateADTModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }
       
function updateADT() {
        var adtid = $('#UpdADTHiddenid').val();
        var url = SingleADTURL.replace("PLACEHOLDER", adtid);
        var data = {"DataTypeSQLServer": $("#UpdADTDataTypeSQLServer").val(),
                    "DataTypeSybase": $('#UpdADTDataTypeSybase').val(),
                    "DataTypeOracle": $('#UpdADTDataTypeOracle').val(),
                    "DataTypePolybase": $('#UpdADTDataTypePolybase').val(),
                    "DataTypeAzureSQLDW": $('#UpdADTDataTypeAzureSQLDW').val(),
                    "DataTypeHive": $('#UpdADTDataTypeHive').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('ADT Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenAFTModal(aftid) {
         $('#UpdAFTHiddenid').val(aftid);
         var url = SingleAFTURL.replace("PLACEHOLDER", aftid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdAFTType").val(result.Type);
              $('#UpdAFTFormat').val(result.Format);  
              $('#UpdAFTEncoding').val(result.Encoding);  
              $('#UpdAFTFieldSeparator').val(result.FieldSeparator);  
              $('#UpdAFTRowSeparator').val(result.RowSeparator);  
              $('#UpdAFTTextQualifier').val(result.TextQualifier);  
              
               $('#UpdateAFTModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }



function updateAFT() {
        var aftid = $('#UpdAFTHiddenid').val();
        var url = SingleAFTURL.replace("PLACEHOLDER", aftid);
        var data = {"Type": $("#UpdAFTType").val(),
                    "Format": $('#UpdAFTFormat').val(),
                    "Encoding": $('#UpdAFTEncoding').val(),
                    "FieldSeparator": $('#UpdAFTFieldSeparator').val(),
                    "RowSeparator": $('#UpdAFTRowSeparator').val(),
                    "TextQualifier": $('#UpdAFTTextQualifier').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('AFT Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenProcessModal(processid) {
         $('#UpdProcessHiddenid').val(processid);
         var url = SingleProcessURL.replace("PLACEHOLDER", processid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdProcessType").val(result.Type);
              $('#UpdProcessName').val(result.Name);  
              $('#UpdProcessDescription').val(result.Description);  
              $('#UpdProcessRollbackType').val(result.RollbackType);  
               $('#UpdateProcessModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }
       
function updateProcess() {
        var processid = $('#UpdProcessHiddenid').val();
        var url = SingleProcessURL.replace("PLACEHOLDER", processid);
        var data = {"Type": $("#UpdProcessType").val(),
                    "Name": $('#UpdProcessName').val(),
                    "Description": $('#UpdProcessDescription').val(),
                    "RollbackType": $('#UpdProcessRollbackType').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenLPModal(afsid) {
         $('#UpdLPHiddenid').val(afsid);
         var url = SingleLoadPlanURL.replace("PLACEHOLDER", afsid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              
              $('#UpdLPName').val(result.Name);  
              $('#UpdLPCategory').val(result.Category); 
              $("#UpdLPType").val(result.Type); 
              $('#UpdLPDescription').val(result.Description); 

               $('#UpdateLPModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function updateLP() {
        var lpid = $('#UpdLPHiddenid').val();
        var url = SingleLoadPlanURL.replace("PLACEHOLDER", lpid);
        var data = {"Type": $("#UpdLPType").val(),
                    "Name": $('#UpdLPName').val(),
                    "Description": $('#UpdLPDescription').val(),
                    "Category": $('#UpdLPCategory').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Load Plan Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenPGModal(afsid) {
         $('#UpdPGHiddenid').val(afsid);
         var url = SingleProcessGroupURL.replace("PLACEHOLDER", afsid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              
              $('#UpdPGName').val(result.Name);  
              $('#UpdPGDescription').val(result.Description); 
              $('#UpdPGOrderOfExecution').val(result.OrderOfExecution)
               $('#UpdatePGModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function updatePG() {
        var pgid = $('#UpdPGHiddenid').val();
        var url = SingleProcessGroupURL.replace("PLACEHOLDER", pgid);
        var data = {"Name": $('#UpdPGName').val(),
                    "Description": $('#UpdPGDescription').val(),
                    'OrderOfExecution': $('#UpdPGOrderOfExecution').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process Group Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenProcessWrapperModal(afsid) {
         $('#UpdPWHiddenid').val(afsid);
         var url = SingleProcessWrapperURL.replace("PLACEHOLDER", afsid);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              
              $('#UpdPWName').val(result.Name);  
              
               $('#UpdatePWModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function updateProcessWrapper() {
        var pwid = $('#UpdPWHiddenid').val();
        var url = SingleProcessWrapperURL.replace("PLACEHOLDER", pwid);
        var data = {"Name": $('#UpdPWName').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process Group Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }
/////////////////////////////
  function deleteAFS(afsid) {

        var data = {};
        var url = SingleAFSURL.replace("PLACEHOLDER", afsid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('AFS Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

  function deleteATS(atsid) {

        var data = {};
        var url = SingleATSURL.replace("PLACEHOLDER", atsid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('ATS Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteADT(adtid) {

        var data = {};
        var url = SingleADTURL.replace("PLACEHOLDER", adtid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('ADT Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteAFT(aftid) {

        var data = {};
        var url = SingleAFTURL.replace("PLACEHOLDER", aftid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('AFT Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteProcess(processid) {

        var data = {};
        var url = SingleProcessURL.replace("PLACEHOLDER", processid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteLP(lpid) {

        var data = {};
        var url = SingleLoadPlanURL.replace("PLACEHOLDER", lpid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Load Plan Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

   function deletePG(pgid) {

        var data = {};
        var url = SingleProcessGroupURL.replace("PLACEHOLDER", pgid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process GroupDeleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

   function deleteProcessWarapper(pwid) {

        var data = {};
        var url = SingleProcessWrapperURL.replace("PLACEHOLDER", pwid);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Process Wrapper Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }