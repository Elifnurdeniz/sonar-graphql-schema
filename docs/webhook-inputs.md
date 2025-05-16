```graphql
"""A model and event that will fire webhooks to its associated endpoint."""
input WebhookEndpointModelEventInput {
  """The model."""
  model: String!
  """The event(s) for the model attached to a webhook endpoint."""
  event: WebhookEndpointModelEvent!
}
```
