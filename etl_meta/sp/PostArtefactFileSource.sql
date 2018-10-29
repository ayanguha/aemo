USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFileSource]    Script Date: 15/10/2018 12:53:13 PM ******/
DROP PROCEDURE [metadata].[PostArtefactFileSource]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFileSource]    Script Date: 15/10/2018 12:53:13 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE Procedure [metadata].[PostArtefactFileSource] 
(
	@ArtefactFileSourceID NVARCHAR(200)
	,@Type NVARCHAR(200)
	,@Location NVARCHAR(200)
	,@AccountName NVARCHAR(200)
	,@ContainerName NVARCHAR(200)
	,@Server NVARCHAR(200)
	,@Port NVARCHAR(200)
	,@Username NVARCHAR(200)
	,@IsInternal NVARCHAR(200)
	,@SourceAlias NVARCHAR(20)
	,@AccountKey NVARCHAR(200)
	,@Password NVARCHAR(200)
	,@key NVARCHAR(50)
	,@certificate NVARCHAR(200)
)

As BEGIN

DECLARE @openkeyquery NVARCHAR(MAX)

		BEGIN TRY
			SET @openkeyquery=REPLACE(REPLACE('OPEN SYMMETRIC KEY @key DECRYPTION BY CERTIFICATE @certificate','@key',@key),'@certificate',@certificate)
			EXECUTE sp_executesql @openkeyquery

			INSERT INTO ArtefactFileSource
			SELECT @ArtefactFileSourceID,
			       @Type,
				   @Location,
				   @AccountName,
				   @ContainerName,
				   @Server,
				   @Port,
				   @Username,
				   @IsInternal,
				   CURRENT_USER,
				   GETDATE(),
				   '9999-12-31 23:59:59.997' ,
				   @SourceAlias,
				   EncryptByKey(Key_GUID(@key), @AccountKey),
				   EncryptByKey(Key_GUID(@key), @Password) 
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

