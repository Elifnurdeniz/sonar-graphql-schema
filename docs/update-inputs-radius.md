```graphql
"""
The input object that defines the fields for the updateRadiusAccount mutation.
"""
input UpdateRadiusAccountMutationInput {
  """A username, used for authentication."""
  username: String
  """A password."""
  password: String
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `password` to null."""
  unset_password: Boolean
}

"""
The input object that defines the fields for the updateRadiusGroup mutation.
"""
input UpdateRadiusGroupMutationInput {
  """A descriptive name."""
  name: String
  """The RADIUS group priority."""
  priority: Int
  """Whether or not this is a fall through group."""
  fall_through: Boolean
  """
  The types of account statuses for accounts that are part of this grouping.
  """
  account_status: AddressListAccountStatus
  """The delinquency state for accounts that are part of this grouping."""
  delinquency: AddressListDelinquency
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """IDs of `AccountStatus`es."""
  account_status_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """IDs of data `Service`s."""
  data_service_ids: [Int64Bit]
  """A list of IDs of `UsageBasedBillingPolicy` objects."""
  usage_based_billing_policy_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateRadiusGroupReplyAttribute mutation.
"""
input UpdateRadiusGroupReplyAttributeMutationInput {
  """A descriptive name."""
  name: String
  """A RADIUS reply operator."""
  operator: RadiusReplyOperator
  """A RADIUS reply."""
  reply: String
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateRadiusServer mutation.
"""
input UpdateRadiusServerMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean = true
  """An IPv4/IPv6 address."""
  ip_address: IP
  """The RADIUS server credentials."""
  radius_server_credentials: [RadiusServerCredentialInput]
  """
  Whether or not Sonar should track bandwidth usage data from this RADIUS server.
  """
  collect_bandwidth: Boolean
  """Send a change of authorization on account delinquency to this device."""
  send_change_auth_on_delinquency: Boolean
  """
  Send a change of authorization on account service change to this device.
  """
  send_change_auth_on_service_change: Boolean
  """
  Send a change of authorization on account status change to this device.
  """
  send_change_auth_on_status_change: Boolean
  """The secret used to send a change of authorization to this device."""
  coa_secret: String
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `coa_secret` to null."""
  unset_coa_secret: Boolean
}
```
