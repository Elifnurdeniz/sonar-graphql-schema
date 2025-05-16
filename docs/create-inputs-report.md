```graphql
"""
The input object that defines the fields for the createReport mutation.
"""
input CreateReportMutationInput {
  """A descriptive name."""
  name: String!
  """The report category."""
  report_category: ReportCategory!
}
```
