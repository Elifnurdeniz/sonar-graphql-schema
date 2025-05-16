```graphql
"""
The input object that defines the fields for the createIdentityProviderActiveDirectory mutation.
"""
input CreateIdentityProviderActiveDirectoryMutationInput {
  """The display name."""
  display_name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The ActiveDirectory icon URL."""
  icon_url: URL
  """Whether to disable the cache or not."""
  disable_cache: Boolean!
  """Whether to use client SSL certificate authentication or not."""
  cert_auth: Boolean!
  """Whether to use Windows Integrated Auth (Kerberos) or not."""
  kerberos: Boolean!
  """The list of domains that can be authenticated."""
  domain_aliases: [String]
  """The range of IPs with which to use Windows Integrated Auth (Kerberos)."""
  ips: [String]
}

"""
The input object that defines the fields for the createIdentityProviderGoogle mutation.
"""
input CreateIdentityProviderGoogleMutationInput {
  """The display name."""
  display_name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The client ID for this identity provider."""
  client_id: String!
  """The client secret for this identity provider."""
  client_secret: String!
}

"""
The input object that defines the fields for the createIdentityProviderMicrosoft mutation.
"""
input CreateIdentityProviderMicrosoftMutationInput {
  """The display name."""
  display_name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The client ID for this identity provider."""
  client_id: String!
  """The client secret for this identity provider."""
  client_secret: String!
}

"""
The input object that defines the fields for the createIdentityProviderSaml mutation.
"""
input CreateIdentityProviderSamlMutationInput {
  """The display name."""
  display_name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The SAML sign in URL."""
  sign_in_endpoint: URL!
  """The SAML sign out URL."""
  sign_out_endpoint: URL
  """
  The attribute in the SAML token that will be mapped to the user_id property.
  """
  user_id_attribute: URL
  """The X.509 signing certificate contents."""
  certificate: Text!
  """
  Whether to include more verbose logging during the authentication process or not.
  """
  debug: Boolean!
  """Whether to sign the SAML request or not."""
  sign_saml_request: Boolean!
  """The sign request algorithm."""
  signature_algorithm: SamlSignatureAlgorithm!
  """The sign request algorithm digest."""
  digest_algorithm: SamlDigestAlgorithm!
  """The SAML protocol binding."""
  protocol_binding: SamlProtocolBinding!
  """Authentication domains."""
  auth_domains: String!
}
```
