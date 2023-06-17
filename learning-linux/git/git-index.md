# Version Control Systems
- Used to track history of changes to typically source code/some set of documents
- Facilitate collaboration
- Work using commits that contain the entire directory
- Also maintain metadata alongside commits, including author of commit, message associated with commit

## Why is it useful to me?
- Can work with different things in parallel without conflicts
- See why you made a change long ago
- Back-up Data
- Keeping work on bug fixes independent from work on features
- Sending data around 
- Resolving conflicts when multiple people work on the same piece of code

# Git Internally
## Terminology
- Trees are directories
- Blobs are files
- Uses a directed acyclic graph

## Commits, Branches and Merges
- Commits are a version of the project at a specific point in time
- Branches are seperate commits that are related to a previous commits
- Merges are combining two commits together into a new commits

## Blobs
- Blobs are stored as arrays of bytes
## Trees
- Trees are mappings from the dirname to the contents
## Commits
- Commits have parents, typically one but merge commits can have multiple, stored as an array
- Author: String
- Message: String
- Snapshot: Tree
## Object
- Blobs, Trees and Commits are all objects
- All objects are stored as mappings (dictionaries) where the key is the SHA-1 hash of the object
- To retrieve an object you use the hash of the object
- All the objects store a pointer to the actual data, so they are pointers
- Each object has a unique (SHA-1 Hash) ID corresponding to it
## References
- Maps a human-readable name to a SHA-1 Hash
- Allows to refer to ID by a human-readable string
## (Im)uttability
- Commits are immutable while references are not
- You can change the name of a commit but not the ID
## End
- The two pieces of data Git stores are references and objects, this is what makes up a git repository
- All git command-line commands are manipulations of object data or reference data

## Staging Area
- Specify what changes are to be added in the next commit
## Branches
- master refers to the default branch created when you initialize a git repository
- It is typically the main branch
## HEAD
- Pointer to the most recent commit of the branch you are currently on (doesn't mean your files are synced up e.g. if you have uncomitted files)

# Git Commands
## git init
- Initializies an empty .git repository 
## git help COMMAND
- Pass a COMMAND to get more info on specified COMMAND
## git status
- Shows the current state of "what is going on"
## git add FILE
- Change FILE's state from the staging area into ready to be committed
## git restore FILE
- Change FILE's state back to the staging area
## git commit
- Creates a new snaphot of all files ready to be committed
- Opens a text-editor to add a message
- Outputs \[branch (root-commit) ID (hash of commit)] commit message
- -a -> Include all non-added blobs that have been modified, but not deleted or added
## git config
- --global core.editor "name" (vim)
## git log
- Used to visualize the history of commits
- By default shows a linear and not graphical history
- Recent commits are shown at the top
- --all --graph --decorate -> Magic incantation that displays a graphical view
## git cat-file ID
- -p (pretty-print)
    - Can be done on any object
    - When done on a blob, acts as regular cat
    - When done on a tree, displays all blobs within the tree (similar to ls)
    - When done on a commit, displays root tree, author, commiter
## git checkout ID/REFERENCE
- Moves HEAD pointer to specified ID and changes state of working directory to reflect commit 
- ID can be only a few characters, it only works if one ID matches
- Enters a DETACHED HEAD state, minimal effect on other branches
- If you have uncommitted files, will prompt you with error
- -f -> Force checkout, ignoring errors
## git diff FILE/ID \[ID] \[ID] 
- Shows changes in FILE with respect to HEAD
- Specify ID to see changes with respect to specified commit
- Specify commit ID to see changes between commit
- Specify two ID's to compare between them, note swapping the two ID's will result in all + swapping to - and vice versa
