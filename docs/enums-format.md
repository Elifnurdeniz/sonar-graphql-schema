```graphql
"""The way in which a date is formatted in Sonar."""
enum DateFormat {
  """A date in YYYY-MM-DD format"""
  YEAR_MONTH_DAY
  """A date in DD/MM/YYYY format"""
  DAY_MONTH_YEAR
  """A date in MM/DD/YYYY format"""
  MONTH_DAY_YEAR
  """A human readable format (e.g. Wednesday, January 4th, 2020.)"""
  HUMAN_FORMAT
}

"""How time is formatted when displayed."""
enum TimeFormat {
  """Twelve hour time (e.g. 1:23PM)"""
  TWELVE_HOUR
  """Twenty four hour time (e.g. 13:23)"""
  TWENTY_FOUR_HOUR
}
```
