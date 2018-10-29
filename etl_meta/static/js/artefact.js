function readFile(src,tgt) {
  
  var fileToRead = document.getElementById(src);
  
  var fReader = new FileReader();
  fReader.readAsText(fileToRead.files[0]);
  fReader.onload = ( function (e) {
    
    var content = document.getElementById(tgt);
    content.value = e.target.result;
  })
   
}
    

function addArtefactTable() {
     

    var data = {
                "Name": $('#TArtefactName').val(),
                "Schema": $('#TArtefactSchema').val(),
                "Category": $('#TArtefactCategory').val(),
                
                "Description": $('#TArtefactDescription').val(),
                "BusinessDescription": $('#TArtefactBusinessDescription').val(),
                "FilterExpression": $('#TArtefactFilterExpression').val(),
                "Group": $('#TArtefactGroup').val(),                
                "ArtefactFileTypeId": $('#TArtefactFileTypeDropDown').val(),               
                "SourceTechnology": $("#TSourceTechnology").val(),
                "ProcessWrapperID": $("#TArtefactOMLDropDown").val(),
                "LoadPlanID": $("#TArtefactLPDropDown").val(),
                "ColumnList": $('#TArtefactColumnList').val(),
                "ColumnListContent": $('#TArtefactColumnListFileContent').val()
              };



    var formData = JSON.stringify(data);
    $.blockUI();
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ArtefactTableURL,
          success: function(result) {alert('Artefact Added'); redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }

function addArtefactAttribute() {

      var data = {
                "ColumnList": $('#ArtefactColumnList').val()
              };

    var formData = JSON.stringify(data);
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ArtefactAttributeURL,
          success: function(result) {alert('Artefact Attributes Added');},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });

}

function addArtefactFile() {
    
    var data = {
               "ArtefactFileTypeID": $('#FArtefactFileTypeDropDown').val(),
               "Name": $('#FArtefactName').val(),
                "NamePattern": $('#FArtefactNamePattern').val(),
                "IsCompressed": $('#FArtefactIsCompressed').val(),
                "TargetSchema": $('#FArtefactTargetSchema').val(),
                "TargetTableName": $('#FArtefactTargetTableName').val(),
                 "SourceTechnology": $("#FSourceTechnology").val(),
                 "ProcessWrapperID": $('#FArtefactOMLDropDown').val(),
                 "LoadPlanID": $('#FArtefactLPDropDown').val(),
                 "ColumnList": $('#FArtefactColumnList').val(),
                 "ColumnListContent": $('#FArtefactColumnListFileContent').val()

              };



    var formData = JSON.stringify(data);
    $.blockUI();
    $.ajax({
          type: "POST",cache: false,data: formData,contentType: 'application/json',
          url: ArtefactFileURL,
          success: function(result) {alert('Artefact File Added');redirectHome();},
          error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
          });
    }


function setAndOpenArtefactTableModal(ArtefactTableID) {
         $('#UpdateArtefactTableHiddenid').val(ArtefactTableID);
         var url = SingleArtefactTableURL.replace("PLACEHOLDER", ArtefactTableID);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdateArtefactTableSchema").val(result.Schema);
              $('#UpdateArtefactTableName').val(result.Name); 
              $('#UpdateArtefactTableFilterExpression').val(result.FilterExpression);  
              $('#UpdateArtefactTableGroup').val(result.Group); 

               $('#UpdateArtefactTableModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

         
      

function updateArtefactTable() {
        var ArtefactTableID = $('#UpdateArtefactTableHiddenid').val();
        var url = SingleArtefactTableURL.replace("PLACEHOLDER", ArtefactTableID);
        var data = {"Schema": $("#UpdateArtefactTableSchema").val(),
                    "Name": $('#UpdateArtefactTableName').val(),                    
                    "FilterExpression": $('#UpdateArtefactTableFilterExpression').val(),
                    "Group": $('#UpdateArtefactTableGroup').val(),
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Table Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }


function setAndOpenArtefactFileModal(ArtefactFileID) {
         $('#UpdateArtefactFileHiddenid').val(ArtefactFileID);
         var url = SingleArtefactFileURL.replace("PLACEHOLDER", ArtefactFileID);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdateArtefactFileHeaderRowsToSkip").val(result.HeaderRowsToSkip);
              $('#UpdateArtefactFileFooterRowsToSkip').val(result.FooterRowsToSkip); 
              $('#UpdateArtefactFileSplitThreshold').val(result.SplitThreshold);  
              $('#UpdateArtefactFileRetentionPeriod').val(result.RetentionPeriod); 

              $('#UpdateArtefactFileNamePattern').val(result.NamePattern); 
              $('#UpdateArtefactFileName').val(result.Name); 
              $('#UpdateArtefactFileIsCompressed').val(result.IsCompressed); 

               $('#UpdateArtefactFileModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function updateArtefactFile() {
        var ArtefactFileID = $('#UpdateArtefactFileHiddenid').val();
        var url = SingleArtefactFileURL.replace("PLACEHOLDER", ArtefactFileID);
        var data = {"HeaderRowsToSkip": $("#UpdateArtefactFileHeaderRowsToSkip").val(),
                    "FooterRowsToSkip": $('#UpdateArtefactFileFooterRowsToSkip').val(),                    
                    "SplitThreshold": $('#UpdateArtefactFileSplitThreshold').val(),
                    "RetentionPeriod": $('#UpdateArtefactFileRetentionPeriod').val(),

                    "NamePattern": $('#UpdateArtefactFileNamePattern').val(),
                    "Name": $('#UpdateArtefactFileName').val(),
                    "IsCompressed": $('#UpdateArtefactFileIsCompressed').val(),
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact File Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenArtefactModal(ArtefactID) {
         $('#UpdateArtefactHiddenid').val(ArtefactID);
         var url = SingleArtefactURL.replace("PLACEHOLDER", ArtefactID);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
                
              $("#UpdateArtefactCategory").val(result.Category);
              $('#UpdateArtefactDescription').val(result.Description); 
              $('#UpdateArtefactBusinessDescription').val(result.BusinessDescription);  

               $('#UpdateArtefactModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

         
      

function updateArtefact() {
        var ArtefactID = $('#UpdateArtefactHiddenid').val();
        var url = SingleArtefactURL.replace("PLACEHOLDER", ArtefactID);
        var data = {"Category": $("#UpdateArtefactCategory").val(),
                    "Description": $('#UpdateArtefactDescription').val(),                    
                    "BusinessDescription": $('#UpdateArtefactBusinessDescription').val() 
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function setAndOpenArtefactAttributeModal(ArtefactAttributeID) {
         $('#UpdateArtefactAttributeHiddenid').val(ArtefactAttributeID);
         var url = SingleArtefactAttributeURL.replace("PLACEHOLDER", ArtefactAttributeID);
         $.ajax({
              type: "GET",cache: false,dataType: 'json',contentType: 'application/json',
              url: url,
              success: function(result) {
              
              $("#UpdateArtefactAttributeIsIdentifier").val(result.IsIdentifier);
              $('#UpdateArtefactAttributeIsNullable').val(result.IsNullable); 
              $('#UpdateArtefactAttributeTechnicalName').val(result.TechnicalName);  
              $('#UpdateArtefactAttributeBusinessName').val(result.BusinessName); 
              
              $('#UpdateArtefactAttributePrecision').val(result.Precision); 
              $('#UpdateArtefactAttributeScale').val(result.Scale); 
              $('#UpdateArtefactAttributeMaxLength').val(result.MaxLength); 
              $('#UpdateArtefactAttributeDataTypeID').val(result.AttributeDataTypeID)

               $('#UpdateArtefactAttributeModal').modal('show');
              },
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

         
      

function updateArtefactAttribute() {
        var ArtefactAttributeID = $('#UpdateArtefactAttributeHiddenid').val();
        var url = SingleArtefactAttributeURL.replace("PLACEHOLDER", ArtefactAttributeID);
        var data = {"IsIdentifier": $("#UpdateArtefactAttributeIsIdentifier").val(),
                    "IsNullable": $('#UpdateArtefactAttributeIsNullable').val(),                    
                    "TechnicalName": $('#UpdateArtefactAttributeTechnicalName').val(),
                    "BusinessName": $('#UpdateArtefactAttributeBusinessName').val(),
                    "AttributeDataTypeID": $('#UpdateArtefactAttributeDataTypeID').val(),
                    "Precision": $('#UpdateArtefactAttributePrecision').val(),
                    "Scale": $('#UpdateArtefactAttributeScale').val(),
                    "MaxLength": $('#UpdateArtefactAttributeMaxLength').val()
                  };

        var formData = JSON.stringify(data);
        
        $.ajax({
              type: "PUT",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Table Updated');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteArteAttribute(ArtefactAttributeID) {

        var data = {};
        var url = SingleArtefactAttributeURL.replace("PLACEHOLDER", ArtefactAttributeID);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Attributes Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

 function deleteArtefact(ArtefactID) {

        var data = {};
        var url = SingleArtefactURL.replace("PLACEHOLDER", ArtefactID);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function deleteArtefactFile(ArtefactFileID) {

        var data = {};
        var url = SingleArtefactFileURL.replace("PLACEHOLDER", ArtefactFileID);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact File Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }

function deleteArtefactTable(ArtefactTableID) {

        var data = {};
        var url = SingleArtefactTableURL.replace("PLACEHOLDER", ArtefactTableID);
        var formData = JSON.stringify(data);
        $.ajax({
              type: "DELETE",cache: false,data: formData,contentType: 'application/json',
              url: url,
              success: function(result) {alert('Artefact Table Deleted');redirectHome();},
              error: function(xhr, status, error) {alert(status);alert(xhr.responseText);redirectHome();}
              });
        }