```graphql
"""
The input object that defines the fields for the mergeSubnets mutation.
"""
input MergeSubnetsMutationInput {
  """The first subnet."""
  subnet_1_id: Int64Bit!
  """The second subnet."""
  subnet_2_id: Int64Bit!
}

"""
The input object that defines the fields for the mergeTickets mutation.
"""
input MergeTicketsMutationInput {
  """The ticket IDs to merge into the parent ticket."""
  merged_ticket_ids: [Int64Bit!]!
}
```
