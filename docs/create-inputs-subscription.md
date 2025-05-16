```graphql
"""
The input object that defines the fields for the createSubscription mutation.
"""
input CreateSubscriptionMutationInput {
  """The type of entity that is being subscribed to."""
  subscribable_type: SubscribableType!
  """The id of the entity that is being subscribed to."""
  subscribable_id: Int64Bit!
}
```
