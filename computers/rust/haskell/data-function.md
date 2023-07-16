on :: (b -> b -> c) -> (a -> b) -> a -> a -> c    
    Takes two functions (f and g) and a list
    
When used in sortBy
    Typically in order f `on` g and the list is curried
    Where f is a comparison function and g returns some sort of data from element (e.g. length, snd)
    Then f compares the returned element for n and n+1
    The result is used to sort the list
