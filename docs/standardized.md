```graphql
"""A standardized vehicle."""
type StandardizedVehicle {
  """A GPS Tracking Provider vehicle unique identifier."""
  uid: String
  """The vehicle identification number."""
  vin: String
  """The manufacturer."""
  manufacturer: String
  """The model."""
  model: String
  """A year."""
  year: String
  """A descriptive name."""
  name: String
}
```
