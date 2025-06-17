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
5. git branch -M branch-name
6. git push origin main