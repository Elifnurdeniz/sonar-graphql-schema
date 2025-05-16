```graphql
"""types.credential_validation_response"""
type CredentialValidationResponse {
  """The status of the validation attempt."""
  status: Boolean!
  """
  Any message returned from the device upon attempted credential validation.
  """
  message: String
}
```
