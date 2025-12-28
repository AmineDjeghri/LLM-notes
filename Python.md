---
date modified: Saturday, November 8th 2025, 4:57:14 am
---
```table-of-contents
```
## Easy guides
- Backend+Frontend+GenA Tempalte   (https://github.com/AmineDjeghri/generative-ai-project-template)
- Package library Template https://github.com/AmineDjeghri/python-package-template/
- Stremio package library 



## Tips and tricks 
- If you are on Windows, you do not need WSL to run python apps. Just use UV on windows.
	- For heavy development stuff like deep learning, I recommand using WSL(ubuntu) with UV and not windows.
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

-  **[or short-circuit]** : - `value = provided or default` . In Python, `A or B` returns:
    - `A` if `A` is truthy.
    - otherwise `B`.
-  [Why dict.get(key) instead of dict[key]?] : 
		
```python
dictionary.get("bogus")  # <-- No default specified -- defaults to None
dictionary.get("bogus", None) # returns `None` just like the previous one


dictionary["bogus"] # will raise a KeyError if key is missing 

```
- Same thing for ‘getatt’ in class instead of ‘dot’. They are equivalent (unless a third argument is provided to suppress the `AttributeError` when the attribute is not present).

- Use pathlib instead of os.path since it’s more pythonic
- If you use functions with nested lists/ dictionnaries, add in the docstring an example of how it looks like to make things easier for contributors.
- Asterix and Slash : https://realpython.com/python-asterisk-and-slash-special-parameters
### Mutable 
- ensure to deepcopy a list of list or dict of list …etc because of inner mutable objects 
- Lists are mutable, so don’t initialize them in a function’s definition

### Use Default values if None instead of a condition 
- Use `_dictionary_.setdefault(_keyname, value_)` : If the key ‘keyname’ doesn't exist in data, it creates it with the value as the default value. If it already exists, it does nothing.
- same with get and set items etc…
### Linters and formaters
- https://nono.ma/linter-vs-formatter

### max workers (threadpool, async…)
- Use pydantic env var to control the max workers :
	- `Field(default=4, gt=0, validation_alias='LLM_MAX_WORKERS')`

- **keep the `min(..., nb_steps)`** because it avoids spawning more threads than tasks (no benefit, only overhead) :
	- `max_workers = min(int(settings.llm_max_workers), nb_steps) if nb_steps else 1`

### # Inheritence, Static Duck Typing and Python’s Protocols
**Inheritance**
- Base class defines _implementation_ + shared data
- Subclasses extend or slightly modify behavior
- You control the class hierarchy
**Protocols**
- https://www.turingtaco.com/static-duck-typing-with-pythons-protocols/
- Multiple unrelated types should work the same way
- Duck typing with static type safety
- You don’t control the classes
## Tools / libraries 
- leetcode
- chatgpt
- Tell gemini/chatgpt to generate some code that can be optimized and try to optimize it

## Papers and research
- item 1


## Other resources 
- item 1