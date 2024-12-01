You can instantiate an interface
```java
InterfaceClass obj = new InterfaceClass() {
	@Override
	public String description() {
		return "description"
	}	
}
```

If it's a one liner return is implicit and {} are unnecessary
```java
InterfaceClass<SomeClass> my Obj = (
	value -> value * 2,
	value -> other_value * 5
	)

MyClass<SomeClass> myObj = new GeneralClass<>( // This is a constructor
	value -> value * 2, // If first method goes through only then second does
	value -> value * 5);
)

MyClass<SomeClass> myObj = new GeneralClass<>( // This is a constructor
	MyClass::method, // Different way to show a lambda
	obj: obj.method() // Equivalent to above
)
```

Function, Predicate and Consumer are functional interfaces
```java
Function<String, Integer> parser = s -> Integer.parseInt(s) // Take parameter String and return an Integer (so kind of like map?)
Predicate<String> isEmpty = s -> s.is_empty() // Returns bool
Consumer<String> printString = s -> print(s) // Returns void

(parameters) -> expression or block of code
```

Map Implementation
```java
List<Integer> lengths = words.stream()\
	.map(s -> s.length())\
	.collect(Collectors.toList())
```

Generic Interface Implementation
```java
GenericFunction<Integer> squareFunction = (Integer value) -> value * value
GenericFunction<Integer> squareFunction = (Integer value) -> {
	return value * value}
squareFunction.apply(10) // Apply is defined in GenericFunction
```

