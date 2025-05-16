```graphql
"""Department information for a company."""
input CompanyDepartmentInput {
  """The ID of a department."""
  department_id: Int64Bit!
  """The number."""
  number: Numeric
  """The extension."""
  extension: Numeric
  """A two character country code for this phone number."""
  country: Country
  """An email address."""
  email_address: EmailAddress
}
```
