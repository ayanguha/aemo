ALTER TABLE [metadata].[ArtefactAttribute] DROP CONSTRAINT [ArtefactAttribute_Artefact_FK]
GO

ALTER TABLE [metadata].[ArtefactAttribute]  WITH CHECK ADD  CONSTRAINT [ArtefactAttribute_Artefact_FK] FOREIGN KEY([ArtefactID])
REFERENCES [metadata].[Artefact] ([ArtefactID]) ON DELETE CASCADE
GO


ALTER TABLE [metadata].[ArtefactAttribute] CHECK CONSTRAINT [ArtefactAttribute_Artefact_FK]
GO


ALTER TABLE [metadata].[ArtefactAttribute] DROP CONSTRAINT [ArtefactAttribute_AttributeDataType_FK]
GO

ALTER TABLE [metadata].[ArtefactAttribute]  WITH CHECK ADD  CONSTRAINT [ArtefactAttribute_AttributeDataType_FK] FOREIGN KEY([AttributeDataTypeID])
REFERENCES [metadata].[AttributeDataType] ([AttributeDataTypeID])
ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactAttribute] CHECK CONSTRAINT [ArtefactAttribute_AttributeDataType_FK]
GO


ALTER TABLE [metadata].[ArtefactFile] DROP CONSTRAINT [ArtefactFile_Artefact_FK]
GO

ALTER TABLE [metadata].[ArtefactFile]  WITH CHECK ADD  CONSTRAINT [ArtefactFile_Artefact_FK] FOREIGN KEY([ArtefactID])
REFERENCES [metadata].[Artefact] ([ArtefactID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactFile] CHECK CONSTRAINT [ArtefactFile_Artefact_FK]
GO


ALTER TABLE [metadata].[ArtefactFile] DROP CONSTRAINT [ArtefactFile_ArtefactFileSource_FK]
GO

ALTER TABLE [metadata].[ArtefactFile]  WITH CHECK ADD  CONSTRAINT [ArtefactFile_ArtefactFileSource_FK] FOREIGN KEY([ArtefactFileSourceID])
REFERENCES [metadata].[ArtefactFileSource] ([ArtefactFileSourceID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactFile] CHECK CONSTRAINT [ArtefactFile_ArtefactFileSource_FK]
GO


ALTER TABLE [metadata].[ArtefactFile] DROP CONSTRAINT [ArtefactFile_ArtefactFileType_FK]
GO

ALTER TABLE [metadata].[ArtefactFile]  WITH CHECK ADD  CONSTRAINT [ArtefactFile_ArtefactFileType_FK] FOREIGN KEY([ArtefactFileTypeID])
REFERENCES [metadata].[ArtefactFileType] ([ArtefactFileTypeID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactFile] CHECK CONSTRAINT [ArtefactFile_ArtefactFileType_FK]
GO

ALTER TABLE [metadata].[ArtefactTable] DROP CONSTRAINT [ArtefactTable_Artefact_FK]
GO

ALTER TABLE [metadata].[ArtefactTable]  WITH CHECK ADD  CONSTRAINT [ArtefactTable_Artefact_FK] FOREIGN KEY([ArtefactID])
REFERENCES [metadata].[Artefact] ([ArtefactID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactTable] CHECK CONSTRAINT [ArtefactTable_Artefact_FK]
GO

ALTER TABLE [metadata].[ArtefactTable] DROP CONSTRAINT [ArtefactTable_ArtefactTableSource_FK]
GO

ALTER TABLE [metadata].[ArtefactTable]  WITH CHECK ADD  CONSTRAINT [ArtefactTable_ArtefactTableSource_FK] FOREIGN KEY([ArtefactTableSourceID])
REFERENCES [metadata].[ArtefactTableSource] ([ArtefactTableSourceID])  ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ArtefactTable] CHECK CONSTRAINT [ArtefactTable_ArtefactTableSource_FK]
GO

ALTER TABLE [metadata].[ProcessArtefact] DROP CONSTRAINT [ProcessArtefact_Process_FK]
GO

ALTER TABLE [metadata].[ProcessArtefact]  WITH CHECK ADD  CONSTRAINT [ProcessArtefact_Process_FK] FOREIGN KEY([ProcessID])
REFERENCES [metadata].[Process] ([ProcessID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ProcessArtefact] CHECK CONSTRAINT [ProcessArtefact_Process_FK]
GO

ALTER TABLE [metadata].[ProcessGroup] DROP CONSTRAINT [ProcessGroup_LoadPlan_FK]
GO

ALTER TABLE [metadata].[ProcessGroup]  WITH CHECK ADD  CONSTRAINT [ProcessGroup_LoadPlan_FK] FOREIGN KEY([LoadPlanID])
REFERENCES [metadata].[LoadPlan] ([LoadPlanID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ProcessGroup] CHECK CONSTRAINT [ProcessGroup_LoadPlan_FK]
GO


ALTER TABLE [metadata].[ProcessGroup] DROP CONSTRAINT [ProcessGroup_Process_FK]
GO

ALTER TABLE [metadata].[ProcessGroup]  WITH CHECK ADD  CONSTRAINT [ProcessGroup_Process_FK] FOREIGN KEY([ProcessID])
REFERENCES [metadata].[Process] ([ProcessID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ProcessGroup] CHECK CONSTRAINT [ProcessGroup_Process_FK]
GO


ALTER TABLE [metadata].[ProcessWrapper] DROP CONSTRAINT [ProcessWrapper_ProcessArtefact_FK]
GO

ALTER TABLE [metadata].[ProcessWrapper]  WITH CHECK ADD  CONSTRAINT [ProcessWrapper_ProcessArtefact_FK] FOREIGN KEY([ProcessArtefactID])
REFERENCES [metadata].[ProcessArtefact] ([ProcessArtefactID]) ON DELETE CASCADE
GO

ALTER TABLE [metadata].[ProcessWrapper] CHECK CONSTRAINT [ProcessWrapper_ProcessArtefact_FK]
GO

