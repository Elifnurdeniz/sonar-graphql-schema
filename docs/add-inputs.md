```graphql
"""
The input object that defines the fields for the addInstanceServiceFunds mutation.
"""
input AddInstanceServiceFundsMutationInput {
  """The instance service fund type."""
  instance_service_fund_type: InstanceServiceFundType!
  """The amount, in the smallest currency value (e.g. cents, pence, pesos.)"""
  amount: Int!
}

"""
The input object that defines the fields for the addPackageToAccount mutation.
"""
input AddPackageToAccountMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a `Package`."""
  package_id: Int64Bit!
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """The date to prorate the transaction as of."""
  proration_date: Date
  """
  Items specific to a voice service. Includes the quantity, price override, and related configuration parameter of each.
  """
  account_voice_service_details: [AccountVoiceServiceDetailMutationInput]
}

"""
The input object that defines the fields for the addServiceToAccount mutation.
"""
input AddServiceToAccountMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a Service."""
  service_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
  """The reason that the price of a service has been overridden."""
  price_override_reason: String
  """
  Overriding the service name will alter the service name printed on an invoice.
  """
  name_override: String
  """
  The next date this service will bill. If this is null, it will bill on the next account billing date.
  """
  next_bill_date: Date
  """
  Service metadata allows you to store individualized information about a
  service, as it relates to a specific account. For example, on a domain renewal
  service, you could store the domain name as metadata.
  """
  service_metadata: [AccountServiceMetadataMutationInput]
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """The date to prorate the transaction as of."""
  proration_date: Date
  """
  Items specific to a voice service. Includes the quantity, price override, and related configuration parameter of each.
  """
  account_voice_service_details: [AccountVoiceServiceDetailMutationInput]
}
```
