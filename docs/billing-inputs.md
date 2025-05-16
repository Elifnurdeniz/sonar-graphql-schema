```graphql
"""Details for a billing service on a Linked billing default."""
input BillingServiceMutationInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """
  Overriding the service name will alter the service name printed on an invoice.
  """
  name_override: String
  """The price per unit of this item."""
  price: Int64Bit!
  """
  The amount of the service that will be invoiced to the anchor account.  Cannot exceed price provided.
  """
  anchor_subsidy: Int64Bit
}
```
