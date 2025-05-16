```graphql
"""
The input object that defines the fields for the verifyOneTimePasswordForAuthenticationFactor mutation.
"""
input VerifyOneTimePasswordForAuthenticationFactorMutationInput {
  """The type of authentication factor this is."""
  type: AuthenticationFactorType!
  """A one-time password (OTP)."""
  one_time_password: String!
}
```
