```table-of-contents
```
## Easy guides
- item 1
- item 2
- Backend+Frontend+GenA Tempalte   (https://github.com/AmineDjeghri/generative-ai-project-template)
- Package library Template https://github.com/AmineDjeghri/python-package-template/



## Tips and tricks 
- Comprehension list : 
	- 
```python

new_text = "" 
for i in range(200): 
	new_text += text
	
# - Using string multiplication (fast and clear)
new_text = text * 200

# Using join (avoids creating many intermediate strings; useful if you want separators):
new_text = "".join([text] * 200)

```


- Use pathlib instead of os.path since it’s more pythonic
- If you use functions with nested lists/ dictionnaries, add in the docstring an example of how it looks like to make things easier for contributors.
### Mutable 
- ensure to deepcopy a list of list or dict of list …etc because of inner mutable objects 
- Lists are mutable, so don’t initialize them in a function’s definition


### Linters and formaters
- https://nono.ma/linter-vs-formatter


## Tools / libraries 
- leetcode
- chatgpt
- 

## Papers and research
- item 1


## Other resources 
- item 1