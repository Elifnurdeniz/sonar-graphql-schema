```graphql
"""
The input object that defines the fields for the updateTicketingSettings mutation.
"""
input UpdateTicketingSettingsMutationInput {
  """
  The number of days a ticket needs to be closed before new inbound emails will
  create a new ticket rather than re-open the existing one.
  """
  days_closed_before_inbound_email_creates_new_ticket: Int
  """The highest spam score a ticket can have to be auto-replied."""
  spam_score_maximum_for_autoreply: Int
  """The lowest spam score a ticket must pass or else be rejected."""
  spam_score_minimum_for_reject: Int
  """
  Setting this value to `true` will set `days_closed_before_inbound_email_creates_new_ticket` to null.
  """
  unset_days_closed_before_inbound_email_creates_new_ticket: Boolean
}
```
