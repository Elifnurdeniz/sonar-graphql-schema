```graphql
"""Allows the addition of custom field data to the parent entity."""
input CustomFieldDataMutationInput {
  """The ID of a CustomField that is associated with this type of entity."""
  custom_field_id: Int64Bit!
  """
  The value of the custom field. For custom fields of the TEXT type, this should
  be arbitrary text, or one of the allowed values. For custom fields of the DATE
  type, this should be a date in YYYY-MM-DD format. For custom fields of the
  BOOLEAN type, this should be 1 or 0.
  """
  value: String!
}
```
