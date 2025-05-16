```graphql
"""User settings for a `Notification` type."""
input NotificationSettingMutationInput {
  """The type of notification."""
  notification_type: NotificationType!
  """The notification channels."""
  channels: [NotificationChannel]
}
```
