---
date modified: Thursday, November 6th 2025, 4:54:05 am
---

```table-of-contents
```
### CSS
- Nicegui supports quasar ad tailwind CSS
- Nicegui uses  [Quasar](https://quasar.dev/) element
### layout and width positionning (and responsive design)
- (Prefered) Use Tailwind’s `max-w-xl mx-auto`. It’s simpler and yields a readable, centered single-column layout. (for example the global page). for example : 
	-     with ui.column().classes("max-w-xl mx-auto p-4 gap-4"):
	- or : with ui.card().classes("max-w-xl mx-auto p-4 gap-4"):
	- or with row 
- Use `col-12 col-sm-4` only when you’re inside a Quasar grid row and actually want a 1/3-width column on small+ screens. like this :

```
with ui.row().classes("w-full justify-center"):  
    with ui.column().classes("col-12 col-md-8 gap-5 p-20 mt-10 bg-white rounded-2xl shadow-xl"):
```


- if you use a row, you need to have a column inside it and not a column inside a column 
- don’t use gutter, but instead use gap-5, and padding
- charts needs columns to define width and also height : 

```
    with ui.column().classes("col-12 col-md-4 items-center"):  
        self.radar = ui.echart(self._radar_options()).classes("h-96")
```


- `ui.row() , card and column` (flex container), will adapt to children size (label width for example, buttons) unless you force width .  They are not w-full per default.

### row vs column: 
- invert justify-center and items-center

### events
- An event object is sometimes given to a function (check the doc of that element/component)
- Most elements also support asynchronous event handlers
- use cpu_bound and io_bound functions when needed


```python
async def handle_pdf_upload(e: Any) -> None:  
    upload: Any = getattr(e, 'file', None)  
    filename = getattr(upload, 'name', '')
    ...

ui.upload(on_upload=handle_pdf_upload).props('accept=.pdf')
```

#### on_click()
- you should always use an async function if the function is slow. If the function has parameters, you need to wrap it in an async function: 
	
```python
async def _on_load_click(self) -> None:  
    await self._load_scores(force=True)
    
self.load_button = ui.button("Load", on_click=self._on_load_click)
```

#### on_change()

```python
ui.select(  
    options=models,  
    label='Select model',  
    on_change=lambda e: (state.__setitem__('selected', e.value), refresh_markdown()),  
).classes('w-full')

```


### navbar and pages
You can use a function displaying the navbar on each page

```python
@ui.page('/generate')  
def generate_page() -> None:  
    ui.page_title('Generate')  
    top_bar()

```

No need to create a class for a component that doesn’t manage states, a function is sufficient


```python
def top_bar() -> None:  
    with ui.header().classes('items-center justify-between bg-primary text-white px-6'):  
        ui.label('GenAI').classes('text-h6 text-white')  
        with ui.row().classes('items-center gap-4'):  
            ui.link('Show', '/').classes('text-sm text-white font-medium opacity-90 hover:opacity-100 px-3 '  
                                                 'py-1 rounded hover:bg-white/10')  
            ui.link('Generate', '/generate').classes('text-sm text-white font-medium opacity-90 '  
                                                           'hover:opacity-100 px-3 py-1 rounded hover:bg-white/10')  

```


### Queue in logging
Do not use a simple list instead of a queue to gather logs because it is not thread safety, and is more expensive.

```python

queue: SimpleQueue[str] = SimpleQueue()  
  
def drain_log() -> None:  
    while not queue.empty():  
        log.push(queue.get())  
  
def enqueue(message: str) -> None:  
    queue.put(message)
    
# pass this to functions to gather logs
def progress(message: str) -> None:  
    enqueue(message)
    
# later
log = ui.log(max_lines=500).classes('w-full')
# drain logs
ui.timer(0.2, drain_log)

# pass here the progress to the other functions: the timer will automatically put the logs in the log component, you can also use logger in the same time to emit in the console
```
