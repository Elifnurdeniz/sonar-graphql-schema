```graphql
"""A standardized vehicle."""
type GetGpsTrackingProviderVehiclesConnection {
  """A list of the entities provided by this connection."""
  entities: [StandardizedVehicle]
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
}
```
