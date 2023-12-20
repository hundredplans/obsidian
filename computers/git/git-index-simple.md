# git checkout BRANCH/COMMIT-NAME
- Moves HEAD to BRANCH/COMMIT
- -b -> Option to also create a new branch and checkout to it

# git commit
- Creates a new commit from HEAD
- --amend -> Rewrite history

# git branch BRANCH-NAME
- Creates a new branch from HEAD
- -f BRANCH-NAME COMMIT-NAME -> Moves BRANCH to a specified commit in its history

# git add PATH
- Add files in the working directory to the staging area

# git merge BRANCH-NAME
- Combines HEAD and the HEAD of branch
- If current HEAD is an ancestor of BRANCH-NAME just moves HEAD to the BRANCH-NAME HEAD

# git rebase BRANCH-NAME
- Creates a commit ahead of HEAD in BRANCH-NAME and dissapears the branch
- If current HEAD is an ancestor of BRANCH-NAME just moves HEAD to the BRANCH-NAME HEAD
- Add -i for an interactive rebase, allows you to move around commits

# git log
- Shows the history of your git commits

# git init
- Create an empty git repository

# git reset HASH
- Unadds a file from the staging area
- \--soft HASH -> Moves HEAD to specified commit and leaves all changed files in the staging area
- \--hard HASH -> Moves HEAD to specified commit and removes all changed files
- If HASH is a commit will move HEAD to the commit as if the future commits haven't been made yet

# git revert HASH
- Creates a new commit from HEAD that introduces changes that revert the changes since HASH
- Used for remote branches where you don't want to rewrite history

# git cherrypick HASH
- Commits specified HASH in front of HEAD without changing history

# On The Topic of HEAD
- Usually HEAD is attached to the top-most commit in your branch
- Deatching HEAD means attaching it to a commit

# On The Topic of HASHES
- You only have to specify enough of the hash to uniquely identify it

# On The Topic of Relative Commits
- You can move upward one commit by using ^ (main^ is the first parent of main, ^^ is grandparent)
- You can move up num times using ~n -> git checkout main~5
- You can also use HEAD as a relative ref -> git checkout HEAD^