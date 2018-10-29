USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactAttribute]    Script Date: 15/10/2018 12:52:31 PM ******/
DROP PROCEDURE [metadata].[PostArtefactAttribute]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactAttribute]    Script Date: 15/10/2018 12:52:31 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE Procedure [metadata].[PostArtefactAttribute] 
(
	@ArtefactAttributeID NVARCHAR(200)
	,@ArtefactID NVARCHAR(200)
	,@AttributeDataTypeID NVARCHAR(200)
	,@TechnicalName NVARCHAR(200)
	,@OrdinalPosition 	NVARCHAR(200)
)
As BEGIN

		BEGIN TRY
		INSERT INTO [metadata].[ArtefactAttribute]
       (	[ArtefactAttributeID]
	,[ArtefactID]
	,[AttributeDataTypeID]
	,[IsIdentifier]
	,[IsNullable]
	,[OrdinalPosition]
	,[TechnicalName]
	,[BusinessName]
	,[DataType]
	,[Precision]
	,[Scale]
	,[MaxLength]
	,[Pattern]
	,[UsedForETL]
	,[CreateBy]
	,[CreateDate]
	,[ExpiryDate]
	,[ColumnPrefix])
Select @ArtefactAttributeID
	   ,@ArtefactID
	   ,@AttributeDataTypeID
		, 0 [IsIdentifier]
		, 1 [IsNullable]
		, @OrdinalPosition	[OrdinalPosition]
			,@TechnicalName [TechnicalName]
			,@TechnicalName as [BusinessName]
			,'String' [DataType]	
			,NULL	[Precision]
			,NULL		[Scale]
			,1000 [MaxLength],
			'' [Pattern]				 
			,0 [UsedForETL]
			,CURRENT_USER [CreatedBy]
			,GETDATE() [CreateDate]
			,'9999-12-31 23:59:59.997' [ExpiryDate]

			,'' [ColumnPrefix]


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

