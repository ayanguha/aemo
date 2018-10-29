USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFileType]    Script Date: 15/10/2018 12:55:16 PM ******/
DROP PROCEDURE [metadata].[PostArtefactFileType]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFileType]    Script Date: 15/10/2018 12:55:16 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





CREATE Procedure [metadata].[PostArtefactFileType] 
(
	@ArtefactFileTypeID NVARCHAR(200)
	,@Type NVARCHAR(200)
	,@Format NVARCHAR(200)
	,@Encoding NVARCHAR(200)
	,@FieldSeparator NVARCHAR(200)
	,@RowSeparator NVARCHAR(200)
	,@TextQualifier NVARCHAR(200)
)

As BEGIN

DECLARE @openkeyquery NVARCHAR(MAX)

		BEGIN TRY
			
			INSERT INTO ArtefactFileType([ArtefactFileTypeID], [Type], [Format], [Encoding], [FieldSeparator], [RowSeparator], [TextQualifier], [File_Type_Alias], [CreateBy], [CreateDate], [ExpiryDate])
			SELECT @ArtefactFileTypeID,
			       @Type,
			       @Format,
				   @Encoding,
		           @FieldSeparator,
				   @RowSeparator,
				   @TextQualifier,
				   @Type + '-' + @Format + '-' + @Encoding + '-' + @FieldSeparator + '-' + @RowSeparator + '-' + @TextQualifier [File_Type_Alias], 
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

