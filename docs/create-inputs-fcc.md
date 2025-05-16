```graphql
"""
The input object that defines the fields for the createFccForm477Report mutation.
"""
input CreateFccForm477ReportMutationInput {
  """
  A list of IDs of data `Service`s used to generate data for FCC Form 477.
  """
  data_service_ids: [Int]
  """A list of IDs of voice `Service`s for use with FCC Form 477."""
  voice_service_ids: [Int]
  """The format of the reporting for FCC Form 477."""
  format: FccForm477Format!
  """
  A single file to associate with this object. Any existing file will be overwritten.
  """
  file: AssociateFileMutationInput
}
```
