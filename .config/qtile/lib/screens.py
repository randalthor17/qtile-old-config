from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen
from .colors import load_colors
from .widgets.volume_fixes import Volume as pamixer_volume
from .widgets.hdd import HDD


class screenObject:
    def __init__(self, widget_defaults, wallpaper_path, mode):
        colors = load_colors()
        self.screens = self.gen_screens(widget_defaults, colors, wallpaper_path, mode)

    def gen_top_bar(self, widget_defaults, colors):
        top = bar.Bar(
            [
                widget.LaunchBar(
                    progs=[
                        (
                            "",
                            "rofi-launchpad",
                            "Applications Menu",
                        )
                    ],
                    default_icon="",
                    fontsize=18,
                ),
                widget.CurrentLayout(),
                widget.GroupBox(highlight_method="block"),
                widget.Prompt(),
                # widget.TaskList(
                #     highlight_method="block", parse_text=remove_window_name
                # ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Spacer(),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    mouse_callbacks={
                        "Button1": lazy.group["5"].dropdown_toggle("calendar"),
                    },
                ),
                widget.Spacer(),
                widget.Systray(),
                # widget.Spacer(length=10),
                widget.Spacer(length=10),
                pamixer_volume(
                    **widget_defaults,
                    fmt=" {}",
                    # Control volume with pamixer
                    get_volume_command="pamixer --get-volume-human",
                    check_mute_command="pamixer --get-mute",
                    check_mute_string="true",
                    volume_up_command="pamixer -i 2",
                    volume_down_command="pamixer -d 2",
                    mute_command="pamixer -t",
                    mouse_callbacks={
                        "Button3": lazy.group["5"].dropdown_toggle("pavucontrol")
                    },
                ),
                # widget.LaunchBar(
                #     progs=[
                #         (
                #             "",
                #             "rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'",
                #             "Clipboard Manager (GreenClip)",
                #         )
                #     ],
                #     default_icon="",
                #     fontsize=18,
                # ),
                widget.LaunchBar(
                    progs=[("", "rofi-power-menu", "Power Menu")],
                    default_icon="",
                    fontsize=18,
                ),
                # widget.QuickExit(),
            ],
            30,
            background=colors[0],
            opacity=0.7,
            margin=5,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )
        return top

    def gen_bottom_bar(self, colors):
        bottom = bar.Bar(
            [
                widget.WindowName(width=bar.CALCULATED, max_chars=50),
                widget.Spacer(),
                widget.TextBox(text="", foreground=colors[6], fontsize=20, padding=0),
                widget.CPU(
                    format=" {freq_current}GHz {load_percent}%",
                    background=colors[6],
                    padding=5,
                ),
                widget.TextBox(text=" ", foreground=colors[6], fontsize=20, padding=0),
                widget.TextBox(text="", foreground=colors[5], fontsize=20, padding=0),
                widget.Memory(
                    format=" {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm} {SwapUsed: .0f}{mm}/{SwapTotal: .0f}{mm}",
                    background=colors[5],
                    padding=5,
                ),
                widget.TextBox(text=" ", foreground=colors[5], fontsize=20, padding=0),
                widget.TextBox(text="", foreground=colors[4], fontsize=20, padding=0),
                widget.Net(
                    format="<big></big> {down} ↓↑ {up}",
                    background=colors[4],
                    padding=5,
                ),
                widget.TextBox(text=" ", foreground=colors[4], fontsize=20, padding=0),
                widget.TextBox(text="", foreground=colors[3], fontsize=20, padding=0),
                HDD(format=" R {read_bytes} W {write_bytes}", background=colors[3]),
                widget.TextBox(text=" ", foreground=colors[3], fontsize=20, padding=0),
            ],
            20,
            background=colors[0],
            opacity=0.7,
            margin=5,
        )
        return bottom

    def gen_screens(self, widget_defaults, colors, wallpaper_path, mode):
        top_bar = self.gen_top_bar(widget_defaults, colors)
        bottom_bar = self.gen_bottom_bar(colors)
        screens = [
            Screen(
                top=top_bar,
                bottom=bottom_bar,
                wallpaper=wallpaper_path,
                wallpaper_mode=mode,
            )
        ]
        return screens
