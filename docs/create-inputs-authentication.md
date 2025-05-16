```graphql
"""
The input object that defines the fields for the createAuthenticationFactor mutation.
"""
input CreateAuthenticationFactorMutationInput {
  """The type of authentication factor this is."""
  type: AuthenticationFactorType!
  """The configuration data of the authentication factor."""
  data: Text
}
```
