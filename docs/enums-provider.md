```graphql
"""The type of auth provider."""
enum AuthProviderType {
  """Auth0."""
  AUTH0
}

"""The type of identity provider."""
enum IdentityProviderType {
  """Active Directory."""
  ACTIVE_DIRECTORY
  """Google."""
  GOOGLE
  """Microsoft."""
  MICROSOFT
  """SAML."""
  SAML
}

"""An authentication credential for an LTE provider."""
enum LteProviderAuthenticationCredential {
  """Telrad REST API username."""
  TELRAD_USERNAME
  """Telrad REST API password."""
  TELRAD_PASSWORD
  """Telrad REST API IP address."""
  TELRAD_IP_ADDRESS
  """Telrad REST API port."""
  TELRAD_PORT
  """Baicells REST API username."""
  BAICELLS_USERNAME
  """Baicells REST API password."""
  BAICELLS_PASSWORD
  """Baicells REST API cloud key."""
  BAICELLS_CLOUD_KEY
}

"""The type of LTE provider."""
enum LteProviderType {
  """Telrad."""
  TELRAD
  """Baicells."""
  BAICELLS
  """Telrad RESTCONF."""
  TELRAD_RESTCONF
}

"""An authentication credential for a tax provider."""
enum TaxProviderCredentialType {
  """Avalara username"""
  AVALARA_USERNAME
  """Avalara password"""
  AVALARA_PASSWORD
  """Avalara client ID"""
  AVALARA_CLIENT_ID
  """Avalara client profile ID"""
  AVALARA_CLIENT_PROFILE_ID
  """Avalara service type. Allowed values: 'LOCAL' or 'LONG_DISTANCE'."""
  AVALARA_SERVICE_TYPE
  """Avalara facilities based. Allowed values: '1' or '0'."""
  AVALARA_FACILITIES_BASED
  """Avalara franchise agreement. Allowed values: '1' or '0'."""
  AVALARA_FRANCHISE_AGREEMENT
  """Avalara regulated. Allowed values: '1' or '0'."""
  AVALARA_REGULATED
  """How long to delay 'requests' to the manual tax processor."""
  MANUALASYNC_DELAY
}

"""The type of tax provider."""
enum TaxProviderType {
  """Manual"""
  MANUAL
  """Avalara"""
  AVALARA
  """Manual (Configurable Delay)"""
  MANUALASYNC
}
```
