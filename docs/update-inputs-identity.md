```graphql
"""
The input object that defines the fields for the updateIdentityProviderActiveDirectory mutation.
"""
input UpdateIdentityProviderActiveDirectoryMutationInput {
  """The display name."""
  display_name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The ActiveDirectory icon URL."""
  icon_url: URL
  """Whether to disable the cache or not."""
  disable_cache: Boolean
  """Whether to use client SSL certificate authentication or not."""
  cert_auth: Boolean
  """Whether to use Windows Integrated Auth (Kerberos) or not."""
  kerberos: Boolean
  """The list of domains that can be authenticated."""
  domain_aliases: [String]
  """The range of IPs with which to use Windows Integrated Auth (Kerberos)."""
  ips: [String]
  """Setting this value to `true` will set `icon_url` to null."""
  unset_icon_url: Boolean
}

"""
The input object that defines the fields for the updateIdentityProviderGoogle mutation.
"""
input UpdateIdentityProviderGoogleMutationInput {
  """The display name."""
  display_name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The client ID for this identity provider."""
  client_id: String
  """The client secret for this identity provider."""
  client_secret: String
}

"""
The input object that defines the fields for the updateIdentityProviderMicrosoft mutation.
"""
input UpdateIdentityProviderMicrosoftMutationInput {
  """The display name."""
  display_name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The client ID for this identity provider."""
  client_id: String
  """The client secret for this identity provider."""
  client_secret: String
}

"""
The input object that defines the fields for the updateIdentityProviderSaml mutation.
"""
input UpdateIdentityProviderSamlMutationInput {
  """The display name."""
  display_name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The SAML sign in URL."""
  sign_in_endpoint: URL
  """The SAML sign out URL."""
  sign_out_endpoint: URL
  """
  The attribute in the SAML token that will be mapped to the user_id property.
  """
  user_id_attribute: URL
  """The X.509 signing certificate contents."""
  certificate: Text
  """
  Whether to include more verbose logging during the authentication process or not.
  """
  debug: Boolean
  """Whether to sign the SAML request or not."""
  sign_saml_request: Boolean
  """The sign request algorithm."""
  signature_algorithm: SamlSignatureAlgorithm
  """The sign request algorithm digest."""
  digest_algorithm: SamlDigestAlgorithm
  """The SAML protocol binding."""
  protocol_binding: SamlProtocolBinding
  """Authentication domains."""
  auth_domains: String
  """Setting this value to `true` will set `sign_out_endpoint` to null."""
  unset_sign_out_endpoint: Boolean
  """Setting this value to `true` will set `user_id_attribute` to null."""
  unset_user_id_attribute: Boolean
}
```
