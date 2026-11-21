# easytkinter

A small module in development that aims to make building graphical interfaces with `tkinter` simpler.

> **Status:** This project is not finished, and its API may change. For now, the module includes functions to create a window, set its size and title, and add labels and buttons.

## Requirements

- Python 3
- `tkinter` available in your Python installation

## Example

Place `easytkinter.py` next to your program and import it as `etk`:

```python
import easytkinter as etk

etk.window(400, 300, "My window")

etk.rlabel("Hello!")
etk.rbutton("Exit", command=lambda: etk.root.destroy())

etk.run()
```

`window()` creates the main window. The `rlabel()` and `rbutton()` widgets are automatically placed with `pack()` and returned so you can configure them later.

## Available functions

### Window

- `window(x=400, y=300, text="ETK window")` — creates the main window with the given dimensions and title.
- `geometry(x, y)` — changes the dimensions of the existing window.
- `title(text)` — changes the title of the existing window.
- `run()` — starts the `tkinter` event loop; call this at the end of your program.

### Widgets

- `rlabel(text="", font=None, fg=None, bg=None, padx=1, pady=1)` — creates and adds a label.
- `rbutton(text="", command=None, bg=None, fg=None, font=None, state="normal", width=None, height=None, activebackground=None, activeforeground=None)` — creates and adds a button. `command` is the function to call when the button is clicked.
- `boolvar(value=None)` and `rcheckbtn(...)` — are present in the module, but still need work before they can be considered functional.

Style and behavior options generally correspond to those of the `tkinter` `Label` and `Button` widgets.

## Current example

The `testhere.py` file demonstrates creating a 400 × 300 pixel window and starting the event loop.

## Next steps

The module is at an early stage. The implementation and documentation will be updated as more features are added and verified.
