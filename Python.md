---
date modified: Saturday, November 8th 2025, 4:57:14 am
---
```table-of-contents
```
## Easy guides
- item 1
- item 2
- Backend+Frontend+GenA Tempalte   (https://github.com/AmineDjeghri/generative-ai-project-template)
- Package library Template https://github.com/AmineDjeghri/python-package-template/



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


### Linters and formaters
- https://nono.ma/linter-vs-formatter

### When should I use databases instead of files 

**Why not using JSON instead of a database ?**
- moving to SQLite as your first step. It’s local, so you don’t need to deal with remote connections and so on, but it’s optimised much more than a single JSON file.
- It is immediately slower. JSON is for representing data, not storing it. Additionally, if you have multiple users, how are you going to handle them reading and writing to the same file at the same time? Databases will handle data integrity, concurrency etc and they are heavily optimized. JSON is a data transfer format, not a storage format
- There's no real benefit to using a Json file rather than a database.

1. When durable writes matter
    
2. When more than one thing is updating it
    
3. When you're dealing with large data and updating it
    
4. When you want to have marketable life skills
    
5. When you need to ask the data complex questions

[source](https://www.reddit.com/r/node/comments/dfmrlj/when_should_i_consider_a_database_instead_of/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 

Redis vs SQL vs others ? 
|**Tool**|**Best For...**|**Architectural Role**|**Data Integrity**|
|---|---|---|---|
|**JSON (File)**|Configuration, Export/Import, Small static datasets.|**Serialization**|None (File System dependent)|
|**Redis**|Caching, Queues, Real-time counters, Ephemeral state.|**Speed / Buffer**|Variable (Speed > Consistency)|
|**SQL** (Postgres)|Financial data, Users, Relations, Structured Data.|**System of Record**|High (**ACID**)|
|**NoSQL** (Mongo)|Logs, Unstructured content, Rapid prototyping.|**Scale / Flexibility**|BASE (Basically Available, Soft state, Eventual consistency)|
## Tools / libraries 
- leetcode
- chatgpt
- 

## Papers and research
- item 1


## Other resources 
- item 1