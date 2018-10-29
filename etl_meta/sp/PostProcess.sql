USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostProcess]    Script Date: 15/10/2018 12:55:48 PM ******/
DROP PROCEDURE [metadata].[PostProcess]
GO

/****** Object:  StoredProcedure [metadata].[PostProcess]    Script Date: 15/10/2018 12:55:48 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO




CREATE Procedure [metadata].[PostProcess] 
(
	@ProcessID NVARCHAR(200)
	,@Name NVARCHAR(200)
	,@Description NVARCHAR(200)
	,@Type NVARCHAR(200)
	,@RollbackType NVARCHAR(200)
)
As BEGIN

DECLARE @openkeyquery NVARCHAR(MAX)

		BEGIN TRY
			
			INSERT INTO Process
			SELECT @ProcessID,		       
			       @Name,
				   @Description,
				   @Type,
				   @RollbackType,
				  CURRENT_USER,
				   GETDATE(),
				   '9999-12-31 23:59:59.997' 
		END TRY

		BEGIN CATCH
			SELECT  
				ERROR_NUMBER() AS ErrorNumber,
				ERROR_SEVERITY() AS ErrorSeverity,
				ERROR_STATE() AS ErrorState,
				ERROR_PROCEDURE() AS ErrorProcedure,
				ERROR_MESSAGE() AS ErrorMessage
		END CATCH
	

END;
GO

