"""Demo of the functions currently available in easytkinter.py."""

import easytkinter as etk


# Create the root window, then demonstrate its title and geometry helpers.
etk.window(420, 360, "easytkinter demo")
etk.title("easytkinter — function demo")
etk.geometry(420, 360)


# Tk variables must be created after the root window.
notifications_enabled = etk.boolvar(value=True)
selected_size = etk.strvar(value="M")


def update_size():
    selected_label.config(text=f"Selected size: {selected_size.get()}")


def update_notifications():
    state = "enabled" if notifications_enabled.get() else "disabled"
    notifications_label.config(text=f"Notifications are {state}.")


def button_clicked():
    action_label.config(text="The button was clicked.")


# Labels and a button. These helpers add widgets directly to the root and pack them.
etk.rlabel(
    text="easytkinter demo",
    font=("Arial", 16, "bold"),
    fg="navy",
    padx=8,
    pady=8,
)
action_label = etk.rlabel(text="Click the button below.")
etk.rbutton(
    text="Click me",
    command=button_clicked,
    width=18,
    activebackground="lightblue",
)


# Checkbutton with a BooleanVar.
etk.rcheckbtn(
    text="Enable notifications",
    variable=notifications_enabled,
    command=update_notifications,
)
notifications_label = etk.rlabel(text="Notifications are enabled.")


# Radio buttons share one StringVar and each use a different value.
etk.rlabel(text="Choose a size:", pady=4)
for option_text, option_value in (("Small", "S"), ("Medium", "M"), ("Large", "L")):
    etk.rradiobtn(
        text=option_text,
        variable=selected_size,
        value=option_value,
        command=update_size,
    )

selected_label = etk.rlabel(text="Selected size: M")

# Start Tk's event loop after creating the window and widgets.
etk.run()
