from libqtile.lazy import lazy
from libqtile import bar, layout, widget, hook
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupImage, PopupText
import os, subprocess


def show_power_menu(qtile):

    controls = [
        PopupText(
            text="",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            h_align="center",
            mouse_callbacks={
                "Button1": lazy.spawn(
                    "loginctl lock-session " + os.environ["XDG_SESSION_ID-"]
                )
            },
        ),
        PopupText(
            text="",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            h_align="center",
            mouse_callbacks={"Button1": lazy.spawn("loginctl suspend")},
        ),
        PopupText(
            text="",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            h_align="center",
            highlight="A00000",
            mouse_callbacks={"Button1": lazy.shutdown()},
        ),
        PopupText(
            text="Lock", pos_x=0.1, pos_y=0.7, width=0.2, height=0.2, h_align="center"
        ),
        PopupText(
            text="Sleep", pos_x=0.4, pos_y=0.7, width=0.2, height=0.2, h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center",
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
