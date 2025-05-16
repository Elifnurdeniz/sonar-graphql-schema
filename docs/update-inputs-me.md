```graphql
"""The input object that defines the fields for the updateMe mutation."""
input UpdateMeMutationInput {
  """A descriptive name."""
  name: String
  """A username, used for authentication."""
  username: String
  """An email address."""
  email_address: EmailAddress
  """A mobile phone number. This will be used to send SMS messages."""
  mobile_number: Numeric
  """A password."""
  password: String
  """The publicly viewable name of this user."""
  public_name: String
  """
  The preferred language for this user. If none is set, then the system default
  will be used. This will affect the interface, as well as communications sent to this user.
  """
  language: Language
  """The number of records shown in a paginated table at once."""
  table_paginator_size: Int64Bit
  """
  Whether or not the navigation bar on the side is loaded in an expanded state.
  """
  navigation_expanded: Boolean
  """
  Saved settings for the web application. This field is meant to be user configurable.
  """
  ui_preferences: Text
  """Your notification settings."""
  notification_settings: [NotificationSettingMutationInput]
  """Setting this value to `true` will set `mobile_number` to null."""
  unset_mobile_number: Boolean
}
```
