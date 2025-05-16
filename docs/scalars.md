```graphql
"""A string with a maximum length of 100000 characters."""
scalar Base64Clob

"""A string with a maximum length of 2^20 (1MB) characters."""
scalar Clob

"""A date in YYYY-MM-DD format (e.g. 2017-01-01)."""
scalar Date

"""
A date and time string, in ISO8601 format (e.g. 2017-01-01T12:33:12+04:00).
"""
scalar Datetime

"""A domain name (e.g. example.com.)"""
scalar DomainName

"""An email address in user@domain format."""
scalar EmailAddress

"""A Unix timestamp."""
scalar EpochTimestamp

"""A geo-point (lat, lon)."""
scalar Geopoint

"""A 6 character hexadecimal color code for HTML."""
scalar HtmlHexColor

"""A valid URL beginning with https://."""
scalar HttpsUrl

"""
The Int64Bit scalar type represents non-fractional signed whole numeric values.
Int64Bit can represent values between -(2^63) and 2^63 - 1. Anything with this
type is always output as a string, so that it can be handled properly in Javascript.
"""
scalar Int64Bit

"""An IPv4 or IPv6 address."""
scalar IP

"""A range of IPv4 addresses, represented as "x.x.x.x-y.y.y.y"."""
scalar IpRange

"""A geographical latitude."""
scalar Latitude

"""A geographical longitude."""
scalar Longitude

"""A MAC address."""
scalar MacAddress

"""
A string that is numeric. This differs from a float in that it can have leading 0s, and it is output as a string.
"""
scalar Numeric

"""A TCP port."""
scalar Port

"""An IPv4 or IPv6 subnet represented using CIDR notation."""
scalar SubnetScalar

"""A string with a maximum length of 100000 characters."""
scalar Text

"""Time of day."""
scalar Time

"""A valid URL beginning with http:// or https://."""
scalar URL
```
