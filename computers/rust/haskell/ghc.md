# GHCI
- Invoke with ghci
## General Commands
- :cd path -> Change working dir

## Loading Functions
- :l myfunction
- :r -> Reloads whole script (and functions)
## Define Variables in GHCI
- let foo = bar
- Equivalent to loading in a variable from a script
## View  Operator Precedence
- :info (operator)
- infixl/infixr -> Read left to right if operator has higher preference
## Loading Modules
- :module/:m + module-name
## GHCI Specific Vars
- it -> Stores result of last function, doesn't change if last evaluation fails
## Set/Unset
### +t
- Lets you see the type of your command input
- Format is input :: Type
## GHCI Show
- :show bindings -> Show types of loaded variables

## Showing Type Declarations (Typeclasses, Funcs)
- :info Typeclass -> Shows what functions (type-declartion) Typeclass has defined
- :info Type -> Shows what Typeclass functions Type is part of
- :info func -> Shows type declaration for a func and (what differs it from :t) where it's defined

## Examining Kind
- :k Type

## Compiling
- --make file -> Compiles file, allows us to do [I/O](IO.md)
- To avoid compiling you can use runhaskell to run on the fly
