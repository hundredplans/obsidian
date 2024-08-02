```php
header() # Changes how file is interpreted, text-plain
# Changes to specific site
# Must be called before any output is sent
header("WWW-Authenticate: challenge1, ..., challengeN")
header("WWW-Authenticate: Basic realm: 'My Realm'") # Defines a space for which your password scheme works
```

```php
$USERNAME = $_SERVER['PHP_AUTH_USER'] # Where authenticate's land
$PASSWORD = $_SERVER['PHP_AUTH_PW']
```