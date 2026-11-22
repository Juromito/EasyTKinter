# easytkinter

`easytkinter` is a small module in development that wraps a few common `tkinter` tasks in short helper functions. Its API may change as the project grows.

## Requirements

- Python 3
- `tkinter` available in your Python installation

## Getting started

Keep `easytkinter.py` next to your Python script, then import it as `etk`:

```python
import easytkinter as etk

etk.window(400, 300, "My first window")

message = etk.rlabel("Hello!")
etk.rbutton("Change message", command=lambda: message.config(text="Button clicked!"))

etk.run()
```

Call `window()` before creating widgets or Tk variables. Call `run()` after setting up the interface to start Tk's event loop.

## Available functions

### Window

- `window(x=400, y=300, text="ETK window")` — creates the root window with the given width, height, and title.
- `geometry(x, y)` — changes the root window size.
- `title(text)` — changes the root window title.
- `run()` — starts the root window's event loop.

### Widgets

The `r` prefix means the widget is created directly in the root window. These helpers call `pack()` automatically and return the created widget.

- `rlabel(text="", font=None, fg=None, bg=None, padx=1, pady=1)` — creates a label.
- `rbutton(text="", command=None, bg=None, fg=None, font=None, state="normal", width=None, height=None, activebackground=None, activeforeground=None)` — creates a button. `command` is called when the button is clicked.
- `rcheckbtn(text="", variable=None, onvalue=None, offvalue=None, command=None)` — creates a checkbutton. Pass a Tk variable with `variable`; `onvalue` and `offvalue` set the values for its checked and unchecked states.
- `rradiobtn(text="", variable=None, value=None, command=None, state=None)` — creates a radio button. Radio buttons in the same group share a variable and each have a different `value`.

### Tk variables

- `boolvar(value=None)` — creates and returns a `tkinter.BooleanVar`, commonly used with a checkbutton.
- `strvar(value="")` — creates and returns a `tkinter.StringVar`, commonly used with radio buttons or text values.

Create Tk variables after calling `window()` so they use the module's root window.

## Demo

Run `python testhere.py` to see the current functions together: window setup, title and geometry changes, labels, a button callback, a checkbutton with a `BooleanVar`, radio buttons sharing a `StringVar`, and the event loop.

The module is still at an early stage; more widgets, layout options, and examples may be added later.
