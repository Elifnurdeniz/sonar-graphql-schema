```graphql
"""
The input object that defines the fields for the updateAvalaraTaxDefinition mutation.
"""
input UpdateAvalaraTaxDefinitionMutationInput {
  """The service name as defined by Avalara."""
  service_name: String
  """The service type as defined by Avalara."""
  service_type: Int
  """Whether or not this entity is archived."""
  archived: Boolean
}
```
