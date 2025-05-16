```graphql
"""A credential to authenticate against a DHCP server."""
enum DhcpServerAuthenticationCredential {
  """A username for a MikroTik DHCP server."""
  MIKROTIK_USERNAME
  """A password for a MikroTik DHCP server."""
  MIKROTIK_PASSWORD
}

"""A type of DHCP server."""
enum DhcpServerType {
  """MikroTik DHCP server (SSL API)."""
  MIKROTIK
}

"""A RADIUS server authentication credential."""
enum RadiusServerAuthCredential {
  """FreeRADIUS MySQL database port."""
  FREERADIUS_MYSQL_DATABASE_PORT
  """FreeRADIUS MySQL database name."""
  FREERADIUS_MYSQL_DATABASE_NAME
  """FreeRADIUS MySQL database username."""
  FREERADIUS_MYSQL_DATABASE_USERNAME
  """FreeRADIUS MySQL database password."""
  FREERADIUS_MYSQL_DATABASE_PASSWORD
  """FreeRADIUS COA Port."""
  FREERADIUS_MYSQL_COA_PORT
}

"""A RADIUS server type."""
enum RadiusServerType {
  """FreeRADIUS MySQL."""
  FREERADIUS_MYSQL
}
```
