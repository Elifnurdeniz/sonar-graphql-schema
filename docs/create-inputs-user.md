```graphql
"""The input object that defines the fields for the createUser mutation."""
input CreateUserMutationInput {
  """A descriptive name."""
  name: String!
  """A username, used for authentication."""
  username: String!
  """
  Super admins receive all system permissions automatically, regardless of their
  role. Only a super admin can create another super admin. If you submit this
  property when you are not a super admin, the mutation will fail.
  """
  super_admin: Boolean
  """The ID of a Role."""
  role_id: Int64Bit
  """An email address."""
  email_address: EmailAddress!
  """A mobile phone number. This will be used to send SMS messages."""
  mobile_number: Numeric
  """
  The preferred language for this user. If none is set, then the system default
  will be used. This will affect the interface, as well as communications sent to this user.
  """
  language: Language
  """The publicly viewable name of this user."""
  public_name: String!
  """Whether or not this is enabled."""
  enabled: Boolean = true
}
```
