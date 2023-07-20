data Type = value constructor -> Declare type with data keyword followed by type name then the possible values the type can have

    data Bool = False | True

Circle and Rectangle are data constructors used to define a Type (Shape)
    data Shape = Circle float float float | Rectangle float float float float

Since Circle and Rectangle aren't types they can't be used when defining a function, instead Shape has to be used
Constructors can be used to create instances of the data type e.g. Circle 5 5 6
Data Constructors are just functions so you can do all that good stuff

To become part of a Typeclass use derive
    data Shape = Circle float float float | Rectangle float float float float deriving (Show)

Record Syntax allows us to automatically create data-types to look up properties
Use curly brackets and define type with ::
    data Person = { 
        firstName :: String,
        lastName :: String,
        age :: int
        } deriving(Show)

When using record syntax you can also create a var like so
The arguments don't have to be in order
    Person {age=42, firstName="Kazinski", lastName="Zorian"}

Type constructors can take parameters to define themself
(a is a Type itself, e.g. Maybe Int, Maybe Char)
You can't create a Maybe value without passing a type parameter
In the example above Nothing is a data constructor of the type of Maybe a, so a function that expects a Maybe a doesn't fail
    data Maybe a = Nothing | Just a 

When comparing the values of the same type from a declared type the values specified first are LT than the ones after
    data Bool = False | True deriving (Ord)
    compare True False
    GT

    True > False
    True

    True < False
    False

Example of Enum, Bounded typeclass
    data day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday deriving (Enum, Bounded)

    minBound :: day 
    Monday

    maxBound :: day
    Sunday

    succ Monday
    Tuesday
    
    [Monday..Thursday]
    [Monday, Tuesday, Wednesday, Thursday]

Type synonyms can be declared with type, act like aliases (first value is desired alias)
    type String = [Char]

You can give String types synonyms to convey more info on what a String does
    type PhoneNumber = String
    type FirstName = String
    type PhoneBook = [(FirstName, PhoneNumber)] 

Type synonyms can be parameterized (you don't know the types in advance)
    type PhoneBook k v = [(k, v)]

You can specify a Type constructor with too few parameters to get a partially applied Type constructor
    type IntMap v = Map Int v (Map is usually k v)
    type IntMap = Map Int (also works)
