```graphql
"""Different types of `CustomField`s."""
enum CustomFieldType {
  """A boolean value"""
  BOOLEAN
  """A date input"""
  DATE
  """A text input"""
  TEXT
}

"""A vendor specific field type that is used by Sonar"""
enum IntegrationFieldType {
  """Model name"""
  MODEL_NAME
  """Profile ID"""
  PROFILE_ID
  """Serial number"""
  SERIAL_NUMBER
  """ONT ID"""
  ONT_ID
  """MAC address"""
  MAC_ADDRESS
}
```
