```graphql
"""
The input object that defines the fields for the createEmailCategory mutation.
"""
input CreateEmailCategoryMutationInput {
  """A descriptive name."""
  name: String!
  """
  If this is `true`, then any contacts created will have this category associated with them by default.
  """
  default: Boolean!
  """If `true`, this category will be added to all existing contacts."""
  apply_to_existing_contacts: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createEmailDomain mutation.
"""
input CreateEmailDomainMutationInput {
  """A domain name."""
  domain: DomainName!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createEmailMessageContent mutation.
"""
input CreateEmailMessageContentMutationInput {
  """A supported language."""
  language: Language!
  """
  A short sentence that will be shown as a preview in compatible email clients.
  """
  inbox_preview: String
  """The subject."""
  subject: String!
  """The body."""
  body: Text!
  """The ID of an EmailMessage."""
  email_message_id: Int64Bit!
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}

"""
The input object that defines the fields for the createEmailMessage mutation.
"""
input CreateEmailMessageMutationInput {
  """A descriptive name."""
  name: String!
  """
  The name to send from when using this email message. If `null`, then the system default will be used.
  """
  from_name: String
  """
  The email address to send from when using this email message. If `null`, then the system default will be used.
  """
  from_email_address: EmailAddress!
  """ID of the Saved Message Category."""
  saved_message_category_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
