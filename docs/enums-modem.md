```graphql
"""A cable modem provisioner authentication credential."""
enum CableModemProvisionerAuthenticationCredential {
  """Incognito username"""
  INCOGNITO_USERNAME
  """Incognito password"""
  INCOGNITO_PASSWORD
  """Incognito MPS port"""
  INCOGNITO_MPS_PORT
  """Incognito DHCP port"""
  INCOGNITO_DHCP_PORT
}

"""The type of cable modem provisioner."""
enum CableModemProvisionerType {
  """Incognito"""
  INCOGNITO
}
```
