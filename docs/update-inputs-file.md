```graphql
"""The input object that defines the fields for the updateFile mutation."""
input UpdateFileMutationInput {
  """A human readable description."""
  description: String
  """
  An image file may be set to the primary image. This will be used as the
  displayed image for the object that this file is associated to throughout Sonar.
  """
  primary_image: Boolean
  """Setting this value to `true` will set `description` to null."""
  unset_description: Boolean
}
```
