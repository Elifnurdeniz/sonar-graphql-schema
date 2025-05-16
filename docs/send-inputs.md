```graphql
"""
The input object that defines the fields for the sendEmailDomainVerificationEmail mutation.
"""
input SendEmailDomainVerificationEmailMutationInput {
  """
  The mailbox to send the verification to. E.g. if the domain is example.com and
  you want to send to foo@example.com, this would be `foo`.
  """
  mailbox: String!
}

"""
The input object that defines the fields for the sendTestEmail mutation.
"""
input SendTestEmailMutationInput {
  """
  The mailbox to send the verification to. E.g. if the domain is example.com and
  you want to send to foo@example.com, this would be `foo`.
  """
  mailbox: String!
}

"""
The input object that defines the fields for the sendTestTriggeredEmail mutation.
"""
input SendTestTriggeredEmailMutationInput {
  """The variables for this triggered email."""
  variables: [TestTriggeredEmailVariableInput]!
}
```
