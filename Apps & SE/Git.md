---
date modified: Thursday, October 30th 2025, 6:56:42 pm
---
### Rebase vs Merge
> [!tip]
> The golden rule of git rebase is to not rebase on any public branch that has shared commit history!
- https://medium.com/@shikha.ritu17/git-rebase-vs-merge-vs-squash-choosing-the-right-strategy-for-version-control-a9c9bb97040e
- https://medium.com/@xiaominghu19922/git-merge-vs-scary-git-rebase-5eceead4badc
- https://www.datacamp.com/blog/git-merge-vs-git-rebase
	- Before merging into main, merge main into your branche to fix conflicts in your branche and not in the main branche.
	- There are also Git squash merge, git merge fast-forward

- Merge:
	-  + easy to use
	-  + complete history of each branch is retained
	-  - commit history on the main branch of your project will inevitably become messy
	- - especially when your team is large
	- → Git merge should be used when team collaboration is more important than maintaining a clean history on the main branch of your project. Typically its resulting workflow is easy to adopt and can rarely go wrong.
- Rebase:
	- +  keep the commit history of your project’s main branch clean.
	- +  allow others to easily follow the history of your code base
	- -  less intuitive than git merge
	- - rewrites the history of your branch

Personally :
- Git merge develop → feature
- Git merge (merge Squash) feature → develop
- Git merge fast forward or Squash develop → main