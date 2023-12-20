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
- Branches are seperate commits that are related to a previous commit
- Merges are combining two commits together into a new commit

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
- --bare -> Initialize a "bare" repository, used for storage rather than development
## git help COMMAND
- Pass a COMMAND to get more info on specified COMMAND
## git status
- Shows the current state of "what is going on"
## git add FILE
- Change FILE's state from the staging area into ready to be committed
- -p -> Interactively stage specific changes in a FILE
    - y -> Stage specific line
    - n -> Don't stage specific line
    - s -> Split into a smaller subsegment
## git restore FILE
- Change FILE's state back to the staging area
## git commit
- Creates a new snaphot of all files ready to be committed
- Opens a text-editor to add a message
- Outputs \[branch (root-commit) ID (hash of commit)] commit message
- -a -> Include all non-added blobs that have been modified, but not deleted or added
- --amend -> Edit a commit's contents/messages
## git config
- Is a plain text file, can be accessed via command line or accessed as a file in ~/.gitconfig
- --global core.editor "name" (vim)
## git log
- Used to visualize the history of commits
- By default shows a linear and not graphical history
- Recent commits are shown at the top
- --all --graph --decorate -> Magic incantation that displays a graphical view
- --oneline -> Prints each branch on a seperate line
- Blue indicates HEAD, Green indicates local branch, Red indicates remote branch
- use glog to access magical incantation
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
- If ID points to a file, modified files in the working directory are reset to the state they were in the HEAD commit, same as git restore
- If ID points to a branch, checkout switches to that branch
- -b -> Equivalent to git branch BRANCH-NAME; git checkout BRANCH-NAME
## git diff FILE/ID \[ID] \[ID] 
- Shows changes in FILE with respect to HEAD
- Specify ID to see changes with respect to specified commit
- Specify commit ID to see changes between commit
- Specify two ID's to compare between them, note swapping the two ID's will result in all + swapping to - and vice versa
- --cached -> Show what is staged for commit, useful when you manually removed some code from staging 
## git branch \[BRANCH]
- Lists created branches in local repository
- -vv -> Extra verbose, shows ID, commit message and upstreamed repositories
- If a branch-name is provided, a new branch is created, copying files from HEAD
- --set-upstream=NAME/REMOTE BRANCH -> Set HEAD branch to push to REMOTE branc without specifying NAME (origin) and REMOTE BRANCH (master)
## git merge \[ID]
- Merges specified branch with HEAD
- Can provide multiple space-seperated branch IDs
- If the specified branch has the HEAD branch as a predecessor, HEAD is moved to point to the branch's most recent commit, this is called Fast-Forward
- --abort -> Aborts current merge (if merge conflicts occured)
- When a merge conflict occurs conflict markers seperate non-resolvable code (====, >>>>) on HEAD
- -- continue -> After merge conflicts are dealt with use to continue merge
## git mergetool
- To set to a specific text editor use --tool=TOOL
- To list available tools use --tool-help
- nvim tool layout
  ╔═══════╦══════╦════════╗
  ║       ║      ║        ║
  ║ LOCAL ║ BASE ║ REMOTE ║
  ║       ║      ║        ║
  ╠═══════╩══════╩════════╣
  ║                       ║
  ║        MERGED         ║
  ║                       ║
  ╚═══════════════════════╝
    - Local: Current branch file
    - Base: Common ancestor commit
    - Remote: Remote branch file
    - Merged: What's saved in the merge
    - Navigate among views using Ctrl-W and HJKL
## git reset ID
- If ID is file un-adds a file from the staging area
- --hard COMMIT\_ID -> Discard any changes in the working tree since COMMIT\_ID, un-tracked files are deleted
- --soft COMMIT\_ID -> Resets HEAD to specified COMMIT\_ID and your changed files are placed in the staging area
## git blame FILE
- Shows who edited a particular file in which commit
- Displays commit id, name of author, date edited, timezone of author, line number and code on line number for HEAD commit
## git show ID
- Shows information for a commit/tree/blob
## git stash pop
- Reverts working directory to HEAD commit and saves any changes
- Specify pop to revert to git stash working directory
## git bisect
- Used to manually search history for a specific change
- Can also pass in script to find a specific change
- e.g. used to find the first commit where a unit test doesn't pass

# Remote Git Commands
## git remote
- Lists all remotes git is aware of in this repository
## git remote add NAME URL
- Add a remote repository with specified NAME found on URL
- By convention origin is used as the NAME if there is only one remote repository
- URL can be a path to another folder 
## git push NAME LOCAL BRANCH:REMOTE BRANCH
- If the local branch and remote branch have the same name only write LOCAL BRANCH
- Creates/updates REMOTE BRANCH on the remote repository with the contents of LOCAL BRANCH
- If upstream is set to remote branch, you can just type git push with no extra arguments
## git clone URL FOLDER
- Copy a repository found at URL into specified FOLDER
- URL can be a path to another folder
- Initializes a local repository from the remote copy
- --shallow -> Only copies latest commit, used to quickly copy large git repositories
## git fetch REMOTE NAME REMOTE BRANCH
- Updates local branch to match remote branch
- REMOTE NAME and REMOTE BRANCH only needs to be specified if more than one remote branch or remote repository is present
- Does not move HEAD so use git merge to synchronize with HEAD (or use git pull)
## git pull REMOTE NAME REMOTE BRANCH
- Merges local branch to match remote branch 
- REMOTE NAME and REMOTE BRANCH only needs to be specified if more than one remote branch or remote repository is present
- Moves HEAD to match remote repository
- Equivalent to git fetch; git merge
## git rebase
- -i -> Interactive rebasing, similar to git add -p
# Related Concepts
## .gitignore
- Used to ignore specified file names or specified patterns of file names
- Line seperated
- Use \*.extension to ignore a specific extension
## Shell Integrations
- Can be used to display git status after each change in a succint way
## Vim Integrations
- Vim plugins that help with git, they exist so search them up!
- fugitive.vim
## Pro Git
- Free book, check it out!
