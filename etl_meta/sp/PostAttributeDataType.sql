USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostAttributeDataType]    Script Date: 15/10/2018 12:54:11 PM ******/
DROP PROCEDURE [metadata].[PostAttributeDataType]
GO

/****** Object:  StoredProcedure [metadata].[PostAttributeDataType]    Script Date: 15/10/2018 12:54:11 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO




CREATE Procedure [metadata].[PostAttributeDataType] 
(
	@AttributeDataTypeID NVARCHAR(200)
	,@DataTypeSQLServer NVARCHAR(200)
	,@DataTypeSybase NVARCHAR(200)
	,@DataTypeOracle NVARCHAR(200)
	,@DataTypePolybase NVARCHAR(200)
	,@DataTypeAzureSQLDW NVARCHAR(200)
	,@DataTypeHive NVARCHAR(200)
)

As BEGIN

DECLARE @openkeyquery NVARCHAR(MAX)

		BEGIN TRY
			
			INSERT INTO AttributeDataType
			SELECT @AttributeDataTypeID,
			       @DataTypeSQLServer,
				   @DataTypeSybase,
				   @DataTypeOracle,
				   @DataTypePolybase,
				   @DataTypeAzureSQLDW,
				   @DataTypeHive,
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

