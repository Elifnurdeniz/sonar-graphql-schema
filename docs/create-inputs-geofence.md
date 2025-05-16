```graphql
"""
The input object that defines the fields for the createGeofence mutation.
"""
input CreateGeofenceMutationInput {
  """A descriptive name."""
  name: String!
  """A collection of points that makes up a polygon."""
  vertexes: [[VertexMutationInput!]]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
