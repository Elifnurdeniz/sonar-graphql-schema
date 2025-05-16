```graphql
"""
The input object that defines the fields for the updateMapOverlay mutation.
"""
input UpdateMapOverlayMutationInput {
  """A descriptive name."""
  name: String!
  """Map Overlay Language (KML) file contents."""
  contents: Base64Clob
  """Network site id."""
  network_site_id: Int64Bit
  """file type"""
  file_type: MapOverlayFileType
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `network_site_id` to null."""
  unset_network_site_id: Boolean
}
```
