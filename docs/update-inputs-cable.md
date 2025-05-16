```graphql
"""
The input object that defines the fields for the updateCableModemProvisioner mutation.
"""
input UpdateCableModemProvisionerMutationInput {
  """A descriptive name."""
  name: String
  """The cable modem provisioner hostname or IP address."""
  hostname: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Credentials for a cable modem provisioner."""
  cable_modem_provisioner_credentials: [CableModemAuthenticationCredentialMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
