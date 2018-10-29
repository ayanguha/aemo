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