```graphql
"""Input of an integration field mapping"""
input IntegrationFieldMappingInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """The ID of an `InventoryModelField`."""
  inventory_model_field_id: Int64Bit!
  """The vendor specific type for field."""
  integration_field_type: IntegrationFieldType!
}

"""The input object that defines the fields for the  mutation."""
input IntegrationServiceMappingAdtranMosaicInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """The profile vector name in Adtran Mosaic this mapping refers to."""
  adtran_mosaic_profile_vector: String
}

"""The input object that defines the fields for the  mutation."""
input IntegrationServiceMappingInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """The service name in vendor system this mapping refers to."""
  service_template_name: String!
  """Policy Map."""
  policy_map: String
}
```
