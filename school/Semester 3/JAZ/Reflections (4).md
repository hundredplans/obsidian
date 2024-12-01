Get class name as string
```java
// Ways to obtain class name
Class.forName(myObject)
Class c = Class.forName("java.lang.String")

myObject.getClass() // Also gets class
Class.class // Gets class

c.getSuperClass()
c.getName() // Returns name + package
c.getSimpleName() // Return just name

c.getDeclaredMethods() // Gets array of all methods
c.getMethods() // Gets only public methods
c.getPackageName()
c.getInterfaces() // Doesn't return superclass implements

c.isInstance(myObject) // Bool if it's an object
c.getDeclaringClass() // Returns where the class was called
c.getDeclaredConstructors()
c.getDeclaredFields() // Inspects private fields
c.getField("myField")

fld.getModifiers() // Returns private, public etc
modifier.toString() // String representation

Class[] parameters = method.getParameterTypes() // Returns types of parameters
parameters.stream().forEach(param -> System.out.println(param.getName())) // Prints names of parameters

method.getReturnType()
method.getExceptionTypes()
```

```java
Object obj = new Object()
Class myClass = obj.getClass()

Class[] parameters = [Integer.TYPE, Integer.TYPE]
Method method = cls.getMethod("nameOfMethod", parameters)

Object[] arguments = [new Integer(50), new Integer(33)]
int return_value = method.invoke(obj, arguments)
```

```java
// To create a new object dynamically
Constructor constructor = cls.getConstructor(parameters)
Object return_object = constructor.newInstance(arguments)
```

```java
// Set fields dynamically
Field field = cls.getField("myDoubleValue")
field.setAccesible(true)
field.set(myObject, 30.2)

field.getType() // Returns double

field.setDouble(new Field(), 12.50) // A new field object has to be created
```

```java
Object arr = Array.newInstance(myClass, 20) // Size of array, can be [] for multi-dimensional arrays
Array.set(arr, 5, "value") // Index 5 set to "value"
arr.getClass().getComponentType() // Returns <Integer> if it's an array of ints
```

```java
int modifiers = myClass.getModifiers() // Gets modifiers as a flag
Modifier.isPublic(modifiers)
Modifier.isAbstract(modifiers)
```

```java
Package myPackage = myClass.getPackage()
assertEquals("com.mypackage.this", myPackage.getName())
```

```java
Method myMethod = myClass.getMethod("bla", parameters)
myMethod.setAccesible(true) // Even if method is private works
```

Facade -> An API for the API