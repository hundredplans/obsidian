# Wildcards Upper Bound
extends -> The class itself or a subclass
```java
if (obj instanceof subobj)
List<?> myList = new ArrayList<Animal>() // Wildcard type
^ -> Identical to List <? extends Object>

List<?> myList = new ArrayList<Object>
myList = new ArrayList<Integer> // Can be assigned to a type later
// If assigned later you can't add elements to the list, but can remove

List<? extends Cars> cars = new ArrayList<Cars>
```

List\<?\> let's you use subclasses or the class to access a list whereas default behaviour does not
Best to use for a return value or parameters in a function

# Wildcards Lower Bound
super -> The class itself or a superclass
```java
List <? super Car> otherCars = new ArrayList<Car>()

```

# Generic Type
\<T\>
```java
public class Car<T> {
	private T t;
	public void set(T t) {this.t = T}
	public void get() {return t}
}
// Once we declare Car<String> it will only accept string parameters
```

# Mixing
```java
Class<? extends Subclass1, ? extends Subclass2, ? super Subclass3> obj = new Class<>()
```

# Generic Methods
```java
<NewType extends Class> void methodName(NewType obj) {}
// Can be used within the class for return, type declaration and during the function
// Any supertype can use this, whereas if you use specifically Class it can only be used on objects of Class
```

# Base Information
Wildcards shouldn't be used in generic classes, generic interfaces
Wildcards run during runtime
Generic types run during compile-time