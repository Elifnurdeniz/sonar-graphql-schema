```graphql
"""
The input object that defines the fields for the toggleAllNotifications mutation.
"""
input ToggleAllNotificationsMutationInput {
  """Whether to mark these notifications as read or unread."""
  read: Boolean
}

"""
The input object that defines the fields for the toggleNotifications mutation.
"""
input ToggleNotificationsMutationInput {
  """A list of notification IDs."""
  notification_ids: [Int64Bit]
  """Whether to mark these notifications as read or unread."""
  read: Boolean
}
```
