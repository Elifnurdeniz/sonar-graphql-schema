```graphql
"""The details on the individual file to be associated."""
input AssociateFileMutationInput {
  """The ID of a `File`."""
  file_id: Int64Bit!
  """A description of the file."""
  description: String
  """
  An image file may be set to the primary image. This will be used as the
  displayed image for the object that this file is associated to throughout Sonar.
  """
  primary_image: Boolean
}
```
