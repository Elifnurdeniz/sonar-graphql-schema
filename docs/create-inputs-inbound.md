```graphql
"""
The input object that defines the fields for the createInboundMailbox mutation.
"""
input CreateInboundMailboxMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean = true
  """
  The name to send from when using this email message. If `null`, then the system default will be used.
  """
  from_name: String!
  """The mailbox email is sent from."""
  from_mailbox: String!
  """The ID of an `EmailDomain`."""
  email_domain_id: Int64Bit!
  """The priority of a `Ticket`."""
  priority: TicketPriority!
  """The ID of a `TicketGroup`."""
  ticket_group_id: Int64Bit!
  """Whether or not an auto reply should be sent."""
  send_auto_reply: Boolean!
  """The auto reply to send."""
  auto_reply: Text
  """Whether or not to append a signature."""
  append_signature: Boolean!
  """
  The signature to append. You can include `[PUBLIC_NAME]` as a variable to
  insert the user's public name when the signature is appended.
  """
  signature: Text
  """Whether or not to enable Slack integration."""
  enable_slack_integration: Boolean!
  """
  Whether the email body should be posted to Slack, or just the email subject.
  """
  post_email_body_to_slack: Boolean
  """
  The URL of a Slack webhook. You can generate one at https://my.slack.com/services/new/incoming-webhook.
  """
  slack_webhook_url: URL
  """A note about this entity."""
  note: NoteMutationInput
}
```
