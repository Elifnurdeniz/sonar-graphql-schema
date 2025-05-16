```graphql
"""
The input object that defines the fields for the updateDeploymentType mutation.
"""
input UpdateDeploymentTypeMutationInput {
  """A descriptive name."""
  name: String
  """The ID of a `NetworkMonitoringTemplate`."""
  network_monitoring_template_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `network_monitoring_template_id` to null.
  """
  unset_network_monitoring_template_id: Boolean
}
```
