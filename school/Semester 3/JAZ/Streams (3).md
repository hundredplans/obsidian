Fluent Interface -> Chaining methods (have to return self)
Streams allow you to use functional programming on arrays
One stream returns another stream

\<R> -> Represents a return type
\<T> -> Represents a type

```java
Stream<T> stream;
Stream<R> map(Function<? super T, ? extends R> mapper)
// Takes any type that is a supertype of t and returns any type that extends R

List<Object> myList = new ArrayList<>()
myList.stream() // Transforms into a stream
myList.stream().map(obj -> obj.transform())
Stream<Integer> objSize = myList.stream().map(obj -> obj.size())

map()
filter()
flatMap() // Flattens array (FIND OUT MORE)
distinct() // Removes duplicates
sorted() // Sorts using default comparator
peek() // Does an action and return the element

// STREAM ENDERS
forEach() // Iterates through every element, doesn't need stream always
reduce() // Accumulator
count() // Size of stream
allMatch() // All
anyMatch() // Any
findFirst() // Returns first element of stream

.collect(Collectors.toList()) // Transform back into a list
.collect(Collectors.toMap(
	key -> key // Key
	key -> key + 5 // Value
)) // Transform stream into map

String::upperCase // Notation used for classes that take no parameters
```