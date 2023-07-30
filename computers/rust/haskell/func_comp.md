- Create a new function that returns a value out of two functions
- Is right associative, you can compose many functions at a time
- Can only take functions that take on argument, use partial application to negate this
- Definition below

(.) :: (b -> c) -> (a -> b) -> a -> c  
f . g = (\x -> f (g x))
f (g x) == (f . g) x

- Apply func1 then func2 and create a new function out of that    
- The return value of func1 must match argument of func2
newFunc = func2 . func1

map (\x -> negate (abs x)) [5,-3,-6,7,-3,2,-19,24]  
[-5,-3,-6,-7,-3,-2,-19,-24]  

map (negate . abs) [5,-3,-6,7,-3,2,-19,24]  
[-5,-3,-6,-7,-3,-2,-19,-24]  

- Displaying right associatve below
map (\xs -> negate (sum (tail xs))) [[1..5],[3..6],[1..7]]  
[-14,-15,-27]

map (negate . sum . tail) [[1..5],[3..6],[1..7]]  
[-14,-15,-27]  

- Displaying using partial application

sum (replicate 5 (max 6.7 8.9))
(sum . replicate 5 . max 6.7) 8.9

- If an expression ends in 3 parantheses, oftentimes you'll need 3 composition operators
replicate 100 (product (map (\*3) (zipWith max \[1,2,3,4,5] [4,5,6,7,8])))
replicate 100 . product . map (\*3) . zipWith max [1,2,3,4,5] $ [4,5,6,7,8]

- Point-free style is omitting duplication of arguments due to currying 
- You can generally get rid of arguments if they're right-most and non paranthesised

sum' xs = foldl (+) 0 xs 
sum' = foldl (+) 0

fn x = ceiling (negate (tan (cos (max 50 x))))
fn = ceiling . negate . tan . cos . max 50  
