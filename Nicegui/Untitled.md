
### layout and width positionning (and responsive design)
-  use Tailwind’s `max-w-xl w-full mx-auto`. It’s simpler and yields a readable, centered single-column layout. (for example the global page)
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


