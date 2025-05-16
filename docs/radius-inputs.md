```graphql
"""RADIUS server credentials."""
input RadiusServerCredentialInput {
  """A RADIUS server credential."""
  credential: RadiusServerAuthCredential!
  """The value of the RADIUS server credential."""
  value: String!
}
```
