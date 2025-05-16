```graphql
"""types.vertex"""
type Vertex {
  """A decimal latitude."""
  latitude: Latitude!
  """A decimal longitude."""
  longitude: Latitude!
}

"""The connection wrapper around the `Vertex` type."""
type VertexConnection {
  """A list of the entities provided by this connection."""
  entities: [Vertex]!
}
```
