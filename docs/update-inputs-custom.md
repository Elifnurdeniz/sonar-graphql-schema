```graphql
"""
The input object that defines the fields for the updateCustomField mutation.
"""
input UpdateCustomFieldMutationInput {
  """A descriptive name."""
  name: String
  """
  Whether or not the value of this custom field must be unique throughout the system.
  """
  unique: Boolean
  """
  Whether or not this custom field must be filled in upon creation of an entity.
  """
  required: Boolean
  """
  A list of values that are valid for this field, if this is a TEXT field. If
  this is empty, and the field is a TEXT type, then any value will be allowed.
  """
  enum_options: [String]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateCustomLink mutation.
"""
input UpdateCustomLinkMutationInput {
  """A descriptive name."""
  name: String
  """A title that will be displayed for this item."""
  label: String
  """The URL to navigate to."""
  url: String
  """An icon."""
  icon: Icon
  """A 6 character hexadecimal string, representing a color used in HTML."""
  icon_color: HtmlHexColor
  """The model."""
  model: CustomLinkModel
  """Setting this value to `true` will set `label` to null."""
  unset_label: Boolean
  """Setting this value to `true` will set `icon_color` to null."""
  unset_icon_color: Boolean
}
```
