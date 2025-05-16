```graphql
"""You!"""
type Me {
  """The ID of the entity."""
  id: Int64Bit!
  """A descriptive name."""
  name: String!
  """A username, used for authentication."""
  username: String!
  """The publicly viewable name of this user."""
  public_name: String!
  """
  Super admins receive all system permissions automatically, regardless of their role.
  """
  super_admin: Boolean!
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
  language: Language!
  """A role defines the permission set that a user has."""
  role: Role
  """Your personal notification settings."""
  notification_settings(
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
  ): NotificationSettingConnection!
  """
  Your personal preferences. Affects the look and behavior of Sonar specifically for you.
  """
  user_preferences: UserPreference!
  """Whether or not a report builder license is granted."""
  report_builder: Boolean!
  """Whether or not a report viewer license is granted."""
  report_viewer: Boolean!
  """A list of `RecentItem`s that you've viewed."""
  recent_items(
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
  ): RecentItemConnection!
  """A vehicle."""
  vehicles(
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
  ): VehicleConnection!
  """Your personal authentication factors."""
  authentication_factors(
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
  ): AuthenticationFactorConnection!
}
```
