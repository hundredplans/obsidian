# Creating Mock Objects
```java
SomeClass myObject = Mockito.mock(SomeClass.class) // Creates a mock object, used outside of testclass

@Mock // Equivalent to above, different notation with annotation
SomeClass myObject;
```

# Assert
```java
Assert.assertEquals(service.func(arg1, arg2), y) // Bool function check if correct
```

# Test Class
```java
@RunWith(MockitoJUnitRunner.class) // Annotation to initialise the test
public testClass {} // New class created to test

@Test // Annotation used above the test class
func testFunc()

@Mock // Annotation for the service to be mocked in the class
SomeService myService 

@InjectMocks // Annotation used to create and inject mock object into class
RegularClass myObject = new RegularClass();

```

# When
```java
when(service.func(arg1, arg2)).thenReturn(y) // Adds the behaviour of the function
doThrow(new RuntimeException("add non existant")).when(service).add(10.0, 20.0) // Throws an exception
```

# Verify
```java
verify(service).func(arg1, arg2) // Verifies the arguments given are correct

verify(service, times(1)).func(arg1, arg2) // Func can only be called once
verify(service, atLeastOnce()).func(arg1, arg2) 
verify(service, atLeast(5)).func(arg1, arg2) 
verify(service, atMost(2)).func(arg1, arg2) 

InOrder inOrder = new InOrder(service) // Verifies verify's are called in order

inOrder.verify(service).func(arg1, arg2)
InOrder.verify(service).funcTwo(arg1, arg2)
```

# Spy
```java
	service = spy(object) // Uses object to create a class of object type and performs when operations on the real object
```

# Captor
```java
// Should only be used in verify
ArgumentCaptor <SomeClass> captor = ArgumentCaptor.forClass(SomeClass.class)
verify(servic).func(captor.capture()) // Captures argument type of function
SomeData object = captor.getValue() // Returns object of captor
```
