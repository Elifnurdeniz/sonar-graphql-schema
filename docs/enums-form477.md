```graphql
"""
The source of the company field for the FCC Form 477 report. This can be either the account or system wide default company.
"""
enum FccForm477CompanySource {
  """Company of the account."""
  ACCOUNT
  """System-wide default company."""
  DEFAULT
}

"""The format of the FIPS for the FCC Form 477 report."""
enum FccForm477Format {
  """The FCC Form 477 report in the California FIPS format."""
  CALIFORNIA
  """The FCC Form 477 report in the standard FIPS format."""
  OTHER
}
```
