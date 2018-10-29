USE [EDMETL_AGUHA]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFile]    Script Date: 15/10/2018 12:52:50 PM ******/
DROP PROCEDURE [metadata].[PostArtefactFile]
GO

/****** Object:  StoredProcedure [metadata].[PostArtefactFile]    Script Date: 15/10/2018 12:52:50 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO









CREATE Procedure [metadata].[PostArtefactFile] 
(
	@ArtefactID NVARCHAR(200)
	,@Name NVARCHAR(200)
	,@ArtefactFileTypeID NVARCHAR(200)	
	,@NamePattern NVARCHAR(200)	
	,@TargetSchema NVARCHAR(200)
	,@TargetTableName NVARCHAR(200)
	,@IsCompressed Integer
	,@MasterProcessWrapperID NVARCHAR(200)
	,@LoadPlanID NVARCHAR(200)
)
As BEGIN



		BEGIN TRY
	INSERT INTO metadata.Artefact
        Select  @ArtefactID	[ArtefactID]
		,upper(RTRIM(LTRIM(@Name))) [Name]
		,'Business' [Category]
		,'SOURCEISFILE' [Type]
		,upper(@Name) [Description]
		,upper(@Name) [BusinessDescription]
		,CURRENT_USER [CreatedBy]
		,GETDATE() [CreateDate]
		,'9999-12-31 23:59:59.997' [ExpiryDate]
		,@Name

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

		
	
	BEGIN TRY
			
			INSERT INTO metadata.ArtefactFile
			
			SELECT @ArtefactID + r * 100,		       
			       @ArtefactID,
				   @ArtefactFileTypeID,
				   fileid,
				   0,
				   0,
				   1000000,
				   90,
				   CURRENT_USER,
				   GETDATE(),
				   '9999-12-31 23:59:59.997',
				   @NamePattern ,
				   NULL, 
				   @IsCompressed 
			FROM (SELECT fileid, row_number() over (order by fileid) r
			     FROM (
                SELECT distinct [SourceArtefactFileSourceID] fileid 
                  FROM [metadata].ProcessGroup pg 
                 WHERE LoadPlanID = @LoadPlanID AND [SourceArtefactFileSourceID] is not null
               UNION
			     SELECT distinct [TargetArtefactFileSourceID] 
                   FROM [metadata].ProcessGroup pg 
                  WHERE LoadPlanID = @LoadPlanID AND [TargetArtefactFileSourceID] is not null
				  ) X
				  ) Y
				  
		INSERT INTO metadata.ArtefactTable
			  Select	@ArtefactID + r * 100
		               ,@ArtefactID
		               ,fileid
		               ,CASE WHEN ty = 'Polybase' THEN upper(RTRIM(LTRIM(@TargetSchema))) + '_HIST'
					         WHEN ty = 'SQLDW' THEN upper(RTRIM(LTRIM(@TargetSchema))) + '_HIST'
							 WHEN ty = 'Hive' THEN upper(RTRIM(LTRIM(@TargetSchema))) + '_HIST'
							ELSE upper(RTRIM(LTRIM(@TargetSchema)))
						END	[Schema]
		               ,CASE WHEN ty = 'Polybase' THEN upper(RTRIM(LTRIM(@TargetTableName))) + '_External'
					         WHEN ty = 'SQLDW' THEN upper(RTRIM(LTRIM(@TargetTableName))) 
							 WHEN ty = 'Hive' THEN upper(RTRIM(LTRIM(@TargetTableName)))
							ELSE upper(RTRIM(LTRIM(@TargetTableName)))  
						  END	[Name]
		               ,'Table'
		               ,'' [FilterExpression]
		               ,CURRENT_USER [CreatedBy]
		               ,GETDATE() [CreateDate]
		               ,'9999-12-31 23:59:59.997' [ExpiryDate]
		               ,''	
			    FROM (select fileid, ats.Type ty, row_number() over (order by fileid) r
                       from 
                     (
				   SELECT distinct [SourceArtefactTableSourceID] fileid 
                     FROM [metadata].ProcessGroup pg 
                    WHERE LoadPlanID = @LoadPlanID AND [SourceArtefactTableSourceID] is not null
                    UNION
			       SELECT distinct [TargetArtefactTableSourceID] 
                     FROM [metadata].ProcessGroup pg 
                    WHERE LoadPlanID = @LoadPlanID AND [TargetArtefactTableSourceID] is not null
				      ) X	
				inner join [metadata].ArtefactTableSource ats on ats.[ArtefactTableSourceID] = X.fileid
				)Y
	
	INSERT INTO metadata.ProcessArtefact
	SELECT  @ArtefactID + OrderofExecution * 100
		,pg.ProcessID
		,sf.ArtefactFileID
		,st.ArtefactTableID [SourceArtefactTableID]
		,tf.ArtefactFileID [TargetArtefactFileID]
		,tt.ArtefactTableID [TargetArtefactTableID]
		,2 [MaxRunAttempts]
		,60 [RerunWaitingTime]
		,1000 [InMinThreshold]
		,100000 [InMaxThreshold]
		,1000 [OutMinThreshold]
		,100000 [OutMaxThreshold]
		,0 [DurationMinThreshold]
		,100 [DurationMaxThreshold]
		,CURRENT_USER [CreatedBy]
		,GETDATE() [CreateDate]
		,'9999-12-31 23:59:59.997' [ExpiryDate]
	FROM  (select ProcessGroupID, ProcessID, OrderofExecution, rank() over (order by ProcessGroupID) r 
             FROM  [metadata].ProcessGroup 
	   where LoadPlanID = @LoadPlanID) pg 
inner join (select pg.ProcessGroupID,sf.ArtefactFileID ,sf.ArtefactFileSourceID
        From [metadata].ProcessGroup pg 
       left outer  join metadata.ArtefactFile sf on pg.SourceArtefactFileSourceID = sf.ArtefactFileSourceID
       WHERE LoadPlanID = @LoadPlanID 
        and (ArtefactID = @ArtefactID or ArtefactID is null)) sf on pg.ProcessGroupID = sf.ProcessGroupID
inner join (select pg.ProcessGroupID,st.ArtefactTableID,st.ArtefactTableSourceID
        From [metadata].ProcessGroup pg 
       left outer  join metadata.ArtefactTable st on pg.SourceArtefactTableSourceID = st.ArtefactTableSourceID
       WHERE LoadPlanID = @LoadPlanID
        and (ArtefactID = @ArtefactID or ArtefactID is null)) st on pg.ProcessGroupID = st.ProcessGroupID
inner join (select pg.ProcessGroupID,tf.ArtefactFileID,tf.ArtefactFileSourceID
        From [metadata].ProcessGroup pg 
       left outer  join metadata.ArtefactFile tf on pg.TargetArtefactFileSourceID = tf.ArtefactFileSourceID
       WHERE LoadPlanID = @LoadPlanID
        and (ArtefactID = @ArtefactID or ArtefactID is null)) tf on pg.ProcessGroupID = tf.ProcessGroupID
inner join (select pg.ProcessGroupID,tt.ArtefactTableID ,tt.ArtefactTableSourceID
        From [metadata].ProcessGroup pg 
       left outer  join metadata.ArtefactTable tt on pg.TargetArtefactTableSourceID = tt.ArtefactTableSourceID
       WHERE LoadPlanID = @LoadPlanID
        and (ArtefactID = @ArtefactID or ArtefactID is null)) tt on pg.ProcessGroupID=tt.ProcessGroupID


		INSERT INTO metadata.ProcessWrapper
		SELECT @ArtefactID + 100
			,@MasterProcessWrapperID [ParentProcessWrapperID]
			,NULL [ProcessArtefactID]
			,pw.Name + '-' + @Name + '-' + @TargetSchema + '.' + @TargetTableName [Name]
			,'ORCHESTRATOR' [Type]
			,1 [Order]
			,'STOP' [ActionOnError]
			,GETDATE()  [EffectiveFrom]
			,'9999-12-31 23:59:59.997' [EffectiveTo]
			,CURRENT_USER [CreatedBy]
		,GETDATE() [CreateDate]
		,'9999-12-31 23:59:59.997' [ExpiryDate]
		, @LoadPlanID
		FROM metadata.ProcessWrapper pw where ProcessWrapperID = @MasterProcessWrapperID

		INSERT INTO metadata.ProcessWrapper
		SELECT @ArtefactID + (pw.OrderofExecution + r) * 5 * 100 [ProcessWrapperID]
			,@ArtefactID + 100 [ParentProcessWrapperID]
			,@ArtefactID + OrderofExecution * 100 [ProcessArtefactID]
			,pw.mastername + '-' + @Name + '-' + @TargetSchema + '.' + @TargetTableName + '-' + processname [Name]
			,'WORKER' [Type]
			,OrderofExecution [Order]
			,'STOP' [ActionOnError]
			,GETDATE()  [EffectiveFrom]
			,'9999-12-31 23:59:59.997' [EffectiveTo]
			,CURRENT_USER [CreatedBy]
			,GETDATE() [CreateDate]
		    ,'9999-12-31 23:59:59.997' [ExpiryDate]
			, @LoadPlanID
		FROM (SELECT oml.Name mastername,pg.OrderOfExecution,p.Name processname,
		           row_number() over (order by ProcessGroupID) r
                FROM [metadata].ProcessGroup pg 
          inner join metadata.Process p on pg.ProcessID = p.ProcessID
          cross join  metadata.ProcessWrapper oml
               WHERE pg.LoadPlanID = @LoadPlanID
                 AND ProcessWrapperID = @MasterProcessWrapperID) pw


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

