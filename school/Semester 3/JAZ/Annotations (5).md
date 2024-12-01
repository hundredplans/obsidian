Used to associate metadata with objects

# Marker Annotations
- No members and no data
- Whether it's there or not is what's important
- @Deprecated when a class has been deprecated
- @Override for methods which have a superclass
- @Test

```java
@SupressWarnings("unchecked") // Value inside is name of warning, place above method
@SupressWarnings({"unchecked", "deprecated"})
@Target(ElementType.TYPE/METHOD/CONSTRUCTOR/FIELD/etc)

clazz.isAnnotationPresent(AnnotationObj.class)
method.getDeclaredAnnotations();


// Custom Annotations
@Repeatable // Can use the same annotation on the same method more than once
@Documented // Elements should be documented by auto doc tools
@Inherited // Superclass queried for annotation
@Target(ElementType.METHOD) // Limits a custom annotation to only target types
@Retention(RetentionPolicy.RUNTIME) // Retain annotation at runtime
public/private @interface<AnnotationName> {
	DataType <MethodName>() [default_value];
}
```

