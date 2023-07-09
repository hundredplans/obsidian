# Tuples
- Can contain multiple types, denoted by ()
- Tuples have a predefined size, each size is considered a different object by lists
- This is useful when storing vectors -> [(1,2),(7,11),(4,5)]
- Tuples containing one string and one number are also considered different objects to a tuple of two numbers
- Use Tuples when you know the types and how many components a piece of data should have
- Empty tuples e.g. () are similar to void

## Comparing Tuples
- fst (8, 11) -> Return first component
- snd (5, 20) -> Return second component
- The commands above only operate on pairs not triples or higher

## Zip
- zip list1 list2 -> Creates one list where each index becomes a tuple of the two values
- If the lists have different sizes the longer list gets cut off
- You can even zip infinite lists this way
