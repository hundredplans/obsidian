# Resources
- [Haskell Standard Module](www.haskell.org/ghc/docs/latest/html/libraries/)

# General
- Modules are collections of functions, types and typeclasses
- A Haskell program is just a main module that loads up sub-modules

# Importing
import module-name

- If you've loaded a script that imports modules, don't have to reload in GHCI
:m + module-name module-name2 -> Import multiple modules in GHCI with space seperated args

- To import/ignore specific functions
import module-name (nub)
import module-name hiding (nub)

- To always have to reference import when using a function
import qualified module-name

- To import with an alias
import qualified module-name as alias
