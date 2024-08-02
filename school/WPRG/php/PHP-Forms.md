# Get

```php
<form action="site-name">
	<input name="varName" type="text"> # name decides the var name
```

In website-name it will have the values of your form
website/site-name?val1=Val


```php
$_GET # Global array of all the form variables, stored as Dict
```

Get is used for short text data
Has history
# Post

```html
<form action="site-name" method="POST">
```

```php
$_POST
```

Post is used for sensitive information / images / large data
Doesn't have history
When refreshed will have to re-use the form