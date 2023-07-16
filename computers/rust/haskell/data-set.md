Allows use to use Sets
Sets are ordered and can't contain duplicates
Often faster than lists
Use a qualified import

# Function
    fromList list -> Returns list converted to set
    intersection set1 set2 -> Return shared items found in both sets
    difference set1 set2 -> Return difference of sets
    union set1 set2 -> Return combined of sets
    null
    size
    member elem
    singleton elem
    insert elem
    delete elem
    map
    filter
    setNub list -> Removes duplicates from a list, faster than nub on big lists but doesn't preserve order of elements

# Subsets
You can check for subsets, a subset is a set that contains all elements of another set but the sets aren't identical (one has more)
    isSubsetOf set1 set2 -> Return true if set1 is a subset of set2 (returns True if identical)
    isProperSubSetOf set1 set2 -> Return false if identical sets



