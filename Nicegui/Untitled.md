- always use a column inside a row, and not a column inside a column 
```
with ui.row().classes("w-full justify-center"):  
    with ui.column().classes("col-12 col-md-8 gap-5 p-20 mt-10 bg-white rounded-2xl shadow-xl"):
```


- always use this for responsive design  : col-12 col-md-8 
- don’t use gutter, but instead use gap-5, and padding
- charts needs columns to define width and also height : 

```
    with ui.column().classes("col-12 col-md-4 items-center"):  
        self.radar = ui.echart(self._radar_options()).classes("h-96")
```
