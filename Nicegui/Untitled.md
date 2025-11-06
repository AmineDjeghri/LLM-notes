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