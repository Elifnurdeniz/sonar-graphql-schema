```graphql
"""types.polygon"""
type Polygon {
  """The connection wrapper around the `Vertex` type."""
  vertexes: VertexConnection!
}

"""The connection wrapper around the `Vertex` type."""
type PolygonConnection {
  """A list of the entities provided by this connection."""
  entities: [Polygon]!
}
```
