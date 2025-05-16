```graphql
"""
The input object that defines the fields for the updateWebhookEndpoint mutation.
"""
input UpdateWebhookEndpointMutationInput {
  """A descriptive name."""
  name: String
  """The endpoint."""
  endpoint: HttpsUrl
  """Whether or not this is enabled."""
  enabled: Boolean
  """The model and event associated with a webhook endpoint."""
  model_events: [WebhookEndpointModelEventInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
