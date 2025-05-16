```graphql
"""
The input object that defines the fields for the createSystemBackupDestination mutation.
"""
input CreateSystemBackupDestinationMutationInput {
  """The service that a system backup will be exported to."""
  provider: SystemBackupDestinationProvider!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The base path to the directory that the file will be stored in."""
  base_path: String
  """
  The credentials used to authenticate against a system backup destination provider.
  """
  system_backup_destination_credentials: [SystemBackupDestinationCredentialInput]!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createSystemBackup mutation.
"""
input CreateSystemBackupMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
  """
  A single file to associate with this object. Any existing file will be overwritten.
  """
  file: AssociateFileMutationInput
}
```
