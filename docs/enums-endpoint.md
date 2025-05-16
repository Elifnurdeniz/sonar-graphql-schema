```graphql
"""
The status of a send attempt for a dispatched webhook of a model and event.
"""
enum WebhookEndpointEventDispatchAttemptStatus {
  """The dispatched webhook is pending to be sent."""
  PENDING
  """The dispatched webhook had been sent and was successful."""
  SUCCESS
  """The dispatched webhook had been sent and failed."""
  FAIL
}

"""A model and event that a webhook is attached to."""
enum WebhookEndpointModelEvent {
  """The created event for the model."""
  CREATED
  """The updated event for the model."""
  UPDATED
  """The deleted event for the model."""
  DELETED
  """The pivot attach event for the model."""
  ATTACHED
  """The pivot detach event for the model."""
  DETACHED
}
```
