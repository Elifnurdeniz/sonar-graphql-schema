```graphql
"""
The input object that defines the fields for the updateTriggeredEmail mutation.
"""
input UpdateTriggeredEmailMutationInput {
  """A descriptive name."""
  name: String
  """The trigger for this message."""
  trigger: EmailTrigger
  """Whether or not this is enabled."""
  enabled: Boolean
  """The ID of an EmailMessage."""
  email_message_id: Int64Bit
  """
  A list of MessageCategory IDs to apply to this triggered email. If this
  triggered email sends to account contacts, then the contact must have at least
  one of the message categories defined here in order to receive this email.
  """
  message_category_ids: [Int64Bit]
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  email_category_ids: [Int64Bit]
  """
  The count associated with this `TriggeredEmail`. This is defined by the
  trigger, and could be something like a number of days, months, gigabytes, etc.
  """
  count: Int
  """
  The `Job` ID for this `TriggeredEmail`. This will only be saved for triggered emails using the trigger `JOB_SCHEDULED`.
  """
  job_type_id: Int64Bit
  """Whether or not child accounts are allowed."""
  allow_children: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateTriggeredMessage mutation.
"""
input UpdateTriggeredMessageMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Whether or not child accounts are allowed."""
  allow_children: Boolean
  """The trigger for this message."""
  trigger: MessageTrigger
  """The ID of an EmailMessage."""
  email_message_id: Int64Bit
  """The ID of the SMS message."""
  sms_message_id: Int64Bit
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  message_category_ids: [Int64Bit]
  """The ID of a signature."""
  signature_id: Int64Bit
  """The ID of a `JobType`."""
  job_type_id: Int64Bit
  """
  The count associated with this `TriggeredMessage`. This is defined by the
  trigger, and could be something like a number of days, months, gigabytes, etc.
  """
  count: Int
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `email_message_id` to null."""
  unset_email_message_id: Boolean
  """Setting this value to `true` will set `sms_message_id` to null."""
  unset_sms_message_id: Boolean
  """Setting this value to `true` will set `signature_id` to null."""
  unset_signature_id: Boolean
}
```
