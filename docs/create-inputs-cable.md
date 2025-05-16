```graphql
"""
The input object that defines the fields for the createCableModemProvisioner mutation.
"""
input CreateCableModemProvisionerMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean! = true
  """The type of cable modem provisioner."""
  type: CableModemProvisionerType!
  """The cable modem provisioner hostname or IP address."""
  hostname: String!
  """Credentials for a cable modem provisioner."""
  cable_modem_provisioner_credentials: [CableModemAuthenticationCredentialMutationInput]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
