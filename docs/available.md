```graphql
"""types.available_explore"""
type AvailableExplore {
  """A descriptive name."""
  name: Text!
  """The category."""
  category: Text!
  """The endpoint."""
  endpoint: Text!
}

"""The connection wrapper around the `AvailableExploresConnection` type."""
type AvailableExploresConnection {
  """A list of the entities provided by this connection."""
  entities: [AvailableExplore]!
}

"""An available report."""
type AvailableReport {
  """A descriptive name."""
  name: Text!
  """The category."""
  category: Text!
  """The endpoint."""
  endpoint: Text!
  """The URL to a thumbnail image."""
  thumbnail_url: URL!
  """Whether or not this is a custom report."""
  is_custom: Boolean!
  """Whether or not this is a personal report."""
  is_user: Boolean!
}

"""The connection wrapper around the `AvailableReportsConnection` type."""
type AvailableReportsConnection {
  """A list of the entities provided by this connection."""
  entities: [AvailableReport]!
}
```
