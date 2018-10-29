USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactTableSource]    Script Date: 15/10/2018 12:53:48 PM ******/
DROP PROCEDURE [metadata].[PostArtefactTableSource]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactTableSource]    Script Date: 15/10/2018 12:53:48 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO




CREATE Procedure [metadata].[PostArtefactTableSource] 
(
	@ArtefactTableSourceID NVARCHAR(200)
	,@Type NVARCHAR(200)
	,@Server NVARCHAR(200)
	,@Port NVARCHAR(200)

	,@Database NVARCHAR(200)
	,@ServiceName NVARCHAR(200)
	,@SID NVARCHAR(200)
	,@Schema NVARCHAR(200)

	,@Username NVARCHAR(200)
	,@ExternalDataSource NVARCHAR(200)
	,@ExternalFileFormat NVARCHAR(200)

	,@Location NVARCHAR(200)
	,@AccountName NVARCHAR(200)
	,@ContainerName NVARCHAR(200)
	
	,@IsInternal NVARCHAR(200)
	,@SourceAlias NVARCHAR(20)
	,@AccountKey NVARCHAR(200)
	,@Password NVARCHAR(200)
	,@GROUP NVARCHAR(200)
	,@key NVARCHAR(50)
	,@certificate NVARCHAR(200)
)

As BEGIN

DECLARE @openkeyquery NVARCHAR(MAX)

		BEGIN TRY
			SET @openkeyquery=REPLACE(REPLACE('OPEN SYMMETRIC KEY @key DECRYPTION BY CERTIFICATE @certificate','@key',@key),'@certificate',@certificate)
			EXECUTE sp_executesql @openkeyquery

			INSERT INTO ArtefactTableSource([ArtefactTableSourceID], [Type], [Server], [Port], [Database], [ServiceName], [SID], [Schema], [Username], [ExternalDataSource], [ExternalFileFormat], [Location], [AccountName], [ContainerName], [IsInternal], [CreateBy], [CreateDate], [ExpiryDate], [SourceAlias], [AccountKey], [Password], [GROUP])
			SELECT @ArtefactTableSourceID,
			       @Type,
				   @Server,
				   @Port,
				   @Database,
				   @ServiceName,
				   @SID,
				   @Schema,
				   @Username,
				   @ExternalDataSource,
				   @ExternalFileFormat,				   
				   @Location,
				   @AccountName,
				   @ContainerName,		
				   @IsInternal,
				   CURRENT_USER,
				   GETDATE(),
				   '9999-12-31 23:59:59.997' ,
				   @SourceAlias,
				   EncryptByKey(Key_GUID(@key), @AccountKey),
				   EncryptByKey(Key_GUID(@key), @Password) ,
				   @GROUP
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

