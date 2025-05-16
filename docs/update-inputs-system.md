```graphql
"""
The input object that defines the fields for the updateSystemBackupDestination mutation.
"""
input UpdateSystemBackupDestinationMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """The base path to the directory that the file will be stored in."""
  base_path: String
  """
  The credentials used to authenticate against a system backup destination provider.
  """
  system_backup_destination_credentials: [SystemBackupDestinationCredentialInput]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `base_path` to null."""
  unset_base_path: Boolean
}

"""
The input object that defines the fields for the updateSystemBackupSettings mutation.
"""
input UpdateSystemBackupSettingsMutationInput {
  """Whether or not to automatically perform a backup every day."""
  automatic_backups: Boolean
  """
  Whether or not to automatically export backups to configured destinations every day.
  """
  automatic_exports: Boolean
  """
  Whether or not to automatically delete an exported system backup on a
  destination configured by a client when pruning exports.
  """
  delete_exported_backups: Boolean
  """The maximum number of backups allowed to exist at any given time."""
  maximum_backups: Int
  """
  The maximum number of backup exports allowed to exist at any given time.
  """
  maximum_exports: Int
  """
  The number of minutes to wait until a backup in progress is considered to have failed and is ready to be marked as such.
  """
  in_progress_backup_expire_minutes: Int
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateSystemSettings mutation.
"""
input UpdateSystemSettingsMutationInput {
  """A supported language."""
  language: Language
  """The currency the system displays money in."""
  currency: Currency
  """The date format to use."""
  date_format: DateFormat
  """The time format to use."""
  time_format: TimeFormat
  """The character used to separate digits in numbers."""
  digit_separator: DigitSeparator
  """The character used to separate decimals in numbers."""
  decimal_separator: DecimalSeparator
  """The timezone you want times in the system displayed in."""
  timezone: Timezone
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A two character country code."""
  country: Country
  """A city."""
  city: String
  """Automatically create a RADIUS account when a new account is created."""
  create_radius_account_on_account_creation: Boolean
  """A text prefix to use when automatically creating a new RADIUS account."""
  radius_account_prefix: String
  """Application firewall enabled."""
  application_firewall_enabled: Boolean
  """The system of units."""
  units: Units
  """Whether all or only primary contacts may access the customer portal."""
  customer_portal_contact_access: CustomerPortalContactAccess
  """The date and time to suppress inventory item status alerts until."""
  suppress_alerts_until_datetime: Datetime
  """Invoices will be created in both English and French for all customers."""
  bilingual_invoices: Boolean
  """
  The source for the company used to populate the DBA name on the FCC Form 477.
  Supports one of service, account, or default.
  """
  fcc_form_477_company_source: FccForm477CompanySource
  """
  If an invoice is past due, will include red watermark stamp saying "Past Due" in the local language.
  """
  past_due_stamp_invoice: Boolean = false
  """
  If true then DHCP leases with Option82 remote_id will assign the IP address to
  a matching customer MAC address instead of a matching remote_id MAC address.
  """
  option_82_assign_to_customer_mac: Boolean
  """The default name to use in email From fields"""
  default_message_from_name: String
  """
  The default user name to use in email From address.  For example the 'jane' in jane@domain.com
  """
  default_message_from_email_user_prefix: String
  """The id of the Email Domain to use in email From address."""
  default_message_from_email_domain_id: Int64Bit
  """the id of the Phone Number to use as default sender for SMS messages."""
  default_message_from_phone_number_id: Int64Bit
  """The default language for messages."""
  default_message_language: Language
  """The id of the default signature to use for Single Recipient Messages."""
  single_recipient_signature_id: Int64Bit
  """The id of the default signature to use for Mass Messages."""
  mass_message_signature_id: Int64Bit
  """The id of the default signature to use for Triggered Messages."""
  triggered_message_signature_id: Int64Bit
  """
  Whether or not to disable the default sonar login and require the use of SSO.
  """
  force_sso_login_web: Boolean
  """Setting this value to `true` will set `city` to null."""
  unset_city: Boolean
  """
  Setting this value to `true` will set `suppress_alerts_until_datetime` to null.
  """
  unset_suppress_alerts_until_datetime: Boolean
  """
  Setting this value to `true` will set `default_message_from_email_domain_id` to null.
  """
  unset_default_message_from_email_domain_id: Boolean
  """
  Setting this value to `true` will set `default_message_from_phone_number_id` to null.
  """
  unset_default_message_from_phone_number_id: Boolean
  """
  Setting this value to `true` will set `default_message_language` to null.
  """
  unset_default_message_language: Boolean
  """
  Setting this value to `true` will set `single_recipient_signature_id` to null.
  """
  unset_single_recipient_signature_id: Boolean
  """
  Setting this value to `true` will set `mass_message_signature_id` to null.
  """
  unset_mass_message_signature_id: Boolean
  """
  Setting this value to `true` will set `triggered_message_signature_id` to null.
  """
  unset_triggered_message_signature_id: Boolean
}
```
