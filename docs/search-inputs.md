```graphql
"""
Allows you to search for objects with specific combinations of values. All
fields submitted within this `Search` object are treated as an `AND`. Each outer
`Search` object is treated as an `OR` in relation to each other.
"""
input Search {
  """
  Search where a string field partially matches a value, or where a string field does not partially match a value.
  """
  string_fields: [SearchStringField]
  """Search against an integer field using a range operator."""
  integer_fields: [SearchIntegerField]
  """Search against a float using a range operator."""
  float_fields: [SearchFloatField]
  """Search against an ISO8601 date/timestamp using a range operator."""
  datetime_fields: [SearchDatetimeField]
  """Search against a date using a range operator."""
  date_fields: [SearchDateField]
  """
  Search for IP addresses that fit into a subnet, or IP addresses that do not fit into a subnet.
  """
  ip_address_fields: [SearchIpAddressField]
  """Search for a specific boolean (`true` or `false`.)"""
  boolean_fields: [SearchBooleanField]
  """
  A minimum of 3 vertices to make up a polygon. This will search for all objects
  where their geopoint field fall within the polygon. Can only be used if the
  object has a `geopoint` field on it.
  """
  geopoint_fields: [SearchGeopointVertex]
  """Return only items where the fields listed here have a `null` value."""
  unset_fields: [String]
  """
  Return only items where the fields listed here are not equal to `null` or `[]`.
  """
  exists: [String]
  """
  Reverse relation filters allow you to filter the result of a relation, and use
  that filter to affect the returned root elements.
  """
  reverse_relation_filters: [ReverseRelationFilter]
}

"""types.search_boolean_field"""
input SearchBooleanField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: Boolean!
  """
  An operator that defines how to apply the search value to the boolean attribute.
  """
  operator: BooleanOperator
}

"""Used in the `Search` object. Allows you to search against date fields."""
input SearchDateField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: Date!
  """
  An operator that defines how to apply the search value to the attribute.
  """
  operator: RangeOperator!
}

"""
Used in the `Search` object. Allows you to search against datetime fields.
"""
input SearchDatetimeField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: Datetime!
  """
  An operator that defines how to apply the search value to the attribute.
  """
  operator: RangeOperator!
}

"""
Used in the `Search` object. Allows you to search against float fields.
"""
input SearchFloatField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: Float!
  """
  An operator that defines how to apply the search value to the attribute.
  """
  operator: RangeOperator!
}

"""
Used in the `Search` object. Allows you to create a polygon to search within against geopoint fields.
"""
input SearchGeopointVertex {
  """A decimal latitude."""
  latitude: Latitude!
  """A decimal longitude."""
  longitude: Longitude!
}

"""
Used in the `Search` object. Allows you to search against integer fields.
"""
input SearchIntegerField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: Int64Bit!
  """
  An operator that defines how to apply the search value to the attribute.
  """
  operator: RangeOperator!
}

"""
Used in the `Search` object. Allows you to search against IP address fields.
"""
input SearchIpAddressField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: String!
  """
  `true` to match results that match the search value. `false` to exclude results that match the search value.
  """
  match: Boolean!
}

"""
Used in the `Search` object. Allows you to search against string fields.
"""
input SearchStringField {
  """The model attribute you wish to reference."""
  attribute: String!
  """The value to search for."""
  search_value: String!
  """
  `true` to match results that match the search value. `false` to exclude results that match the search value.
  """
  match: Boolean!
  """
  If `true`, return results that match the value in `search_value` in any part
  of their value. If `false`, the entire string must match the value in
  `search_value` to match.
  """
  partial_matching: Boolean = true
}
```
