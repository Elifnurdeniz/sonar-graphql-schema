```graphql
"""
The input object that defines the fields for the updateEmailCategory mutation.
"""
input UpdateEmailCategoryMutationInput {
  """A descriptive name."""
  name: String
  """
  If this is `true`, then any contacts created will have this category associated with them by default.
  """
  default: Boolean
  """If `true`, this category will be added to all existing contacts."""
  apply_to_existing_contacts: Boolean
  """
  If `true`, this category will be removed from all existing contacts. Ignored if apply_to_existing_contacts is `true`
  """
  remove_from_existing_contacts: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateEmailMessageContent mutation.
"""
input UpdateEmailMessageContentMutationInput {
  """A supported language."""
  language: Language
  """
  A short sentence that will be shown as a preview in compatible email clients.
  """
  inbox_preview: String
  """The subject."""
  subject: String
  """The body."""
  body: Text
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """Setting this value to `true` will set `inbox_preview` to null."""
  unset_inbox_preview: Boolean
}

"""
The input object that defines the fields for the updateEmailMessage mutation.
"""
input UpdateEmailMessageMutationInput {
  """A descriptive name."""
  name: String
  """
  The name to send from when using this email message. If `null`, then the system default will be used.
  """
  from_name: String
  """
  The email address to send from when using this email message. If `null`, then the system default will be used.
  """
  from_email_address: EmailAddress
  """ID of the Saved Message Category."""
  saved_message_category_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `saved_message_category_id` to null.
  """
  unset_saved_message_category_id: Boolean
}
```
