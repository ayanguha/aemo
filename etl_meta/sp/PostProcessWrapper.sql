USE [@DBNAME]
GO

/****** Object:  StoredProcedure [metadata].[PostProcessWrapper]    Script Date: 17/10/2018 1:55:46 PM ******/
DROP PROCEDURE [metadata].[PostProcessWrapper]
GO

/****** Object:  StoredProcedure [metadata].[PostProcessWrapper]    Script Date: 17/10/2018 1:55:46 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO







CREATE Procedure [metadata].[PostProcessWrapper] 
(
	@ProcessWrapperID NVARCHAR(200)
	,@Name NVARCHAR(200)
	
)
As BEGIN

		BEGIN TRY
		
			
			INSERT INTO metadata.ProcessWrapper
             Select  @ProcessWrapperID
		            ,NULL 
		            ,NULL
		            ,@Name 
		            ,'ORCHESTRATOR'
		            ,1
					,'STOP'
					,GETDATE() [EffectiveFrom]
		            ,'9999-12-31 23:59:59.997' [EffectiveTo]
		            ,CURRENT_USER [CreatedBy]
		            ,GETDATE() [CreateDate]
		            ,'9999-12-31 23:59:59.997' [ExpiryDate]
		END TRY

		BEGIN CATCH
			SELECT  
				ERROR_NUMBER() AS ErrorNumber,
				ERROR_SEVERITY() AS ErrorSeverity,
				ERROR_STATE() AS ErrorState,
				ERROR_PROCEDURE() AS ErrorProcedure,
				ERROR_MESSAGE() AS ErrorMessage
		   insert into metadata.ag select ERROR_MESSAGE()
		END CATCH

		

END;
GO


