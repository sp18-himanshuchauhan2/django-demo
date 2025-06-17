# Git Commands

## For configuring
1. git config --global user.name "Your Name"
2. git config --global user.email "Your Email"
3. git config --list

## For clone & status
1. git clone <--url-->
2. git status

## For add & commit
1. git add <--file_name-->
2. git add .  (add all the files)
3. git commit -m "message"

## For push
1. git push origin main
2. git push -u origin main (to set upstream)
3. git push

## Create a new repo in your local system and upload it globally
1. git init
2. git remote add origin <--url-->
3. git remote -v (to verify the remote)
4. git branch (to check the branch)
5. git branch -M branch-name (to rename the branch)
6. git push origin main

## To see the commits
1. git log
2. git log -p -n (to see only n commits)

## For undo commands
1. git checkout <--file-name-->
2. git checkout -f (for multiple files)

## For branches
1. git branch
2. git checkout branch-name (to switch branches)
3. git checkout -b new-branch-name (to create new branch & switch)
4. git branch -d branch-name (to delete branch)
5. git branch branch-name (to create a new branch)

## For merge the branches
1. git diff branch-name (to compare the changes between 2 branches)
2. git merge branch-name
3. Or we can simply create a pull request (PR) on github.

## For pull (to fetch the content from remote repo to local repo)
1. git pull origin main

## To check the difference in same file
1. git diff             (working dir. & staging area)
2. git diff --staged    (last commit & staging area)