```graphql
"""
The input object that defines the fields for the createSonarImport mutation.
"""
input CreateSonarImportMutationInput {
  """The unique identifier of an import at Sonar."""
  sonar_batch_identifier: String!
  """The JSON metadata for an import at Sonar."""
  sonar_batch_metadata: String!
}
```
