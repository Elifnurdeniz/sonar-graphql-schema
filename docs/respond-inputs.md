```graphql
"""
The input object that defines the fields for the respondToInstanceManagementRequest mutation.
"""
input RespondToInstanceManagementRequestMutationInput {
  """The date until which the authorization is valid."""
  authorization_valid_until: Date
  """The ID of a Role."""
  role_id: Int64Bit
}
```
