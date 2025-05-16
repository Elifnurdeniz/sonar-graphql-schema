```graphql
"""
The input object that defines the fields for the updateOrderGroup mutation.
"""
input UpdateOrderGroupMutationInput {
  """The name of an order group."""
  name: String
  """
  Disabled order groups cannot be assigned users or used to create purchase orders.
  """
  enabled: Boolean
  """
  The threshold at which requesters require approval of their purchase orders.
  """
  automatic_approval_threshold: Int
  """
  A list of user IDs that should have authority to approve purchase orders in this order group.
  """
  approver_ids: [Int64Bit]!
  """
  A list of user IDs that should have permission to create product requests in this group.
  """
  requester_ids: [Int64Bit]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
