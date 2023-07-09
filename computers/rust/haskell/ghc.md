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
