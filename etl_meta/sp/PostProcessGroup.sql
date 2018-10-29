USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostProcessGroup]    Script Date: 15/10/2018 12:56:06 PM ******/
DROP PROCEDURE [metadata].[PostProcessGroup]
GO

/****** Object:  StoredProcedure [metadata].[PostProcessGroup]    Script Date: 15/10/2018 12:56:06 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






CREATE Procedure [metadata].[PostProcessGroup] 
(
	@ProcessGroupID NVARCHAR(200)
	,@Name NVARCHAR(200)
	,@Description NVARCHAR(200)
	
	,@LoadPlanID NVARCHAR(200)
	,@ProcessID NVARCHAR(200)
	,@SourceArtefactFileSourceID NVARCHAR(200)
	,@SourceArtefactTableSourceID NVARCHAR(200)
	,@TargetArtefactFileSourceID NVARCHAR(200)
	,@TargetArtefactTableSourceID NVARCHAR(200)
	,@OrderofExecution Integer
)
As BEGIN

		BEGIN TRY
		

			
			INSERT INTO [ProcessGroup]
             Select  @ProcessGroupID
		            ,@Name [Name]
		            ,upper(@Description) [Description]
					,@LoadPlanID
					,@ProcessID
					,CASE WHEN @SourceArtefactFileSourceID = '' then NULL else @SourceArtefactFileSourceID end
					,CASE WHEN  @SourceArtefactTableSourceID = '' then NULL else @SourceArtefactTableSourceID end
					,CASE WHEN  @TargetArtefactFileSourceID = '' then NULL else @TargetArtefactFileSourceID end
					,CASE WHEN  @TargetArtefactTableSourceID = '' then NULL else @TargetArtefactTableSourceID end
					, @OrderofExecution
		            ,CURRENT_USER [CreatedBy]
		            ,GETDATE() [CreateDate]
		            ,'9999-12-31 23:59:59.997' [ExpiryDate]
		            
		END TRY

		BEGIN CATCH
		insert into metadata.ag select ERROR_MESSAGE()
			SELECT  
				ERROR_NUMBER() AS ErrorNumber,
				ERROR_SEVERITY() AS ErrorSeverity,
				ERROR_STATE() AS ErrorState,
				ERROR_PROCEDURE() AS ErrorProcedure,
				ERROR_MESSAGE() AS ErrorMessage
		   
		END CATCH

		

END;
GO

