```graphql
"""
The input object that defines the fields for the createWebhookEndpointEvent mutation.
"""
input CreateWebhookEndpointEventMutationInput {
  """The ID of a webhook endpoint."""
  webhook_endpoint_id: Int64Bit!
  """The model."""
  model: String!
  """The event(s) for the model attached to a webhook endpoint."""
  event: WebhookEndpointModelEvent!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createWebhookEndpoint mutation.
"""
input CreateWebhookEndpointMutationInput {
  """A descriptive name."""
  name: String!
  """The endpoint."""
  endpoint: HttpsUrl!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The model and event associated with a webhook endpoint."""
  model_events: [WebhookEndpointModelEventInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
