USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostLoadPlan]    Script Date: 15/10/2018 12:55:34 PM ******/
DROP PROCEDURE [metadata].[PostLoadPlan]
GO

/****** Object:  StoredProcedure [metadata].[PostLoadPlan]    Script Date: 15/10/2018 12:55:34 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE Procedure [metadata].[PostLoadPlan] 
(
	@LoadPlanID NVARCHAR(200)
	,@Name NVARCHAR(200)
	,@Category NVARCHAR(200)
	 ,@Type NVARCHAR(200)
	,@Description NVARCHAR(200)	
)
As BEGIN

		BEGIN TRY
		/* Populate metadata.[Artefact] Table */

			
			INSERT INTO metadata.LoadPlan
             Select  @LoadPlanID
		            ,@Name
		            ,@Category [Category]
		            ,@Type [Type]
		            ,@Description
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

