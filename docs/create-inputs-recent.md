```graphql
"""
The input object that defines the fields for the createRecentItem mutation.
"""
input CreateRecentItemMutationInput {
  """The entity that a recent item entry is for."""
  recentitemable_type: RecentitemableType!
  """The ID of the entity that this recent item entry is for."""
  recentitemable_id: Int64Bit!
}
```
