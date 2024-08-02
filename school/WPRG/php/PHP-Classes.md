```php
# Basics
class Name {
	public int $age;
	public string $var2;	
	public function funcName(): string # Specifies return type
	{

	}
	public function __construct($age, $var2) # Constrctor
	{
		$this->age = $age;
		$this->var2 = $var2;
	}
}
obj = new Name();
obj->Age = x; # To access variables
```

```php
# Inheritance
class Animal {
	protected string $species;
	private int $id;
}

class Capybara extends Animal {}
```
```php
# As seperate files
require # Joins file, gives error
require_once # Doesn't override if multiple classes?
include # Joins file, gives warning
include_once

require_once 'Class.php'
```
```php
# Static functions
class Name{
	private static int $class_name;
	public static info() {return "My class name is Name" . self::$class_name}
}
Name::info(); # To call a static method
self::$class_name; # To access a static variable
```
```php
class Name {
	private int $value;
	public function getAge() {return $this->value;}
	public function setAge($value) {$this->value = $value}
	public function __toString(): string {return $this->value;}
}
```