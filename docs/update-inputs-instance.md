```graphql
"""
The input object that defines the fields for the updateInstanceServiceFundAutoPay mutation.
"""
input UpdateInstanceServiceFundAutoPayMutationInput {
  """The instance service fund type."""
  instance_service_fund_type: InstanceServiceFundType!
  """Whether the instance service is paid for automatically."""
  auto_pay: Boolean!
}
```
