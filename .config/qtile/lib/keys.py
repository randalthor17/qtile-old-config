from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from .groups import groupObject


class keyObject:
    def __init__(self, mod="mod4", terminal=guess_terminal()):
        self.mod = mod
        self.terminal = terminal
        vim_keylist = self.vim_keys()
        arrow_keylist = self.arrow_keys()
        spawn_keylist = self.window_spawn_keys()
        layout_keylist = self.window_layout_keys()
        misc_keylist = self.misc_keys()
        group_keylist = self.group_keys()
        scratchpad_keylist = self.scratchpad_keys()
        self.keys = (
            vim_keylist
            + arrow_keylist
            + spawn_keylist
            + layout_keylist
            + misc_keylist
            + group_keylist
            + scratchpad_keylist
        )

    def window_focus_keys(self, direction_obj):
        keys = [
            # A list of available commands that can be bound to keys can be found
            # at https://docs.qtile.org/en/latest/manual/config/lazy.html
            # Switch between windows
            Key(
                [self.mod],
                direction_obj["left"],
                lazy.layout.left(),
                desc="Move focus to left",
            ),
            Key(
                [self.mod],
                direction_obj["right"],
                lazy.layout.right(),
                desc="Move focus to right",
            ),
            Key(
                [self.mod],
                direction_obj["down"],
                lazy.layout.down(),
                desc="Move focus down",
            ),
            Key(
                [self.mod], direction_obj["up"], lazy.layout.up(), desc="Move focus up"
            ),
        ]
        return keys

    def window_move_keys(self, direction_obj):
        keys = [
            Key(
                [self.mod, "shift"],
                direction_obj["left"],
                lazy.layout.shuffle_left(),
                desc="Move window to the left",
            ),
            Key(
                [self.mod, "shift"],
                direction_obj["right"],
                lazy.layout.shuffle_right(),
                desc="Move window to the right",
            ),
            Key(
                [self.mod, "shift"],
                direction_obj["down"],
                lazy.layout.shuffle_down(),
                desc="Move window down",
            ),
            Key(
                [self.mod, "shift"],
                direction_obj["up"],
                lazy.layout.shuffle_up(),
                desc="Move window up",
            ),
        ]
        return keys

    def window_grow_keys(self, direction_obj):
        keys = [
            # Grow windows. If current window is on the edge of screen and direction
            # will be to screen edge - window would shrink.
            Key(
                [self.mod, "mod1"],
                direction_obj["left"],
                lazy.layout.grow_left(),
                desc="Grow window to the left",
            ),
            Key(
                [self.mod, "mod1"],
                direction_obj["right"],
                lazy.layout.grow_right(),
                desc="Grow window to the right",
            ),
            Key(
                [self.mod, "mod1"],
                direction_obj["down"],
                lazy.layout.grow_down(),
                desc="Grow window down",
            ),
            Key(
                [self.mod, "mod1"],
                direction_obj["up"],
                lazy.layout.grow_up(),
                desc="Grow window up",
            ),
        ]
        return keys

    def window_spawn_keys(self):
        keys = [
            Key(
                [self.mod], "Return", lazy.spawn(self.terminal), desc="Launch terminal"
            ),
            Key(
                [self.mod, "shift"],
                "End",
                # lazy.spawn("rofi -show p -modi p:rofi-power-menu"),
                lazy.spawn("rofi-power-menu"),
                desc="Open power menu",
            ),
            Key(
                [self.mod],
                "d",
                # lazy.spawn("rofi -i -combi-modi window,drun,run -show combi -show-icons"),
                lazy.spawn("rofi-launchpad"),
                desc="Open application launcher",
            ),
            Key(
                [self.mod, "shift"],
                "s",
                lazy.spawn("flameshot gui"),
                desc="Take a selection screenshot",
            ),
            Key(
                [self.mod],
                "c",
                lazy.spawn("xfce4-clipman-history"),
                desc="Open clipboard manager",
            ),
            Key(
                [self.mod],
                "F1",
                lazy.spawn("show_keybindings.sh"),
                desc="Print keybindings",
            ),
            Key(
                [self.mod, "shift"],
                "c",
                lazy.spawn("rofi-calc"),
                desc="Open rofi-calculator",
            ),
            Key(
                [self.mod],
                "period",
                lazy.spawn("rofi -modi emoji -show emoji"),
                desc="Open rofi-emoji",
            ),
        ]
        return keys

    def window_layout_keys(self):
        keys = [
            Key(
                [self.mod, "shift"],
                "Return",
                lazy.layout.toggle_split(),
                desc="Toggle between split and unsplit sides of stack",
            ),
            Key([self.mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([self.mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
            Key([], "F11", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
        ]
        return keys

    def vim_keys(self):
        vim_key_obj = {"left": "h", "right": "l", "down": "j", "up": "k"}
        keys = []
        keys.extend(self.window_focus_keys(vim_key_obj))
        keys.extend(self.window_move_keys(vim_key_obj))
        keys.extend(self.window_grow_keys(vim_key_obj))
        return keys

    def arrow_keys(self):
        arrow_key_obj = {"left": "Left", "right": "Right", "down": "Down", "up": "Up"}
        keys = []
        keys.extend(self.window_focus_keys(arrow_key_obj))
        keys.extend(self.window_move_keys(arrow_key_obj))
        keys.extend(self.window_grow_keys(arrow_key_obj))
        return keys

    def misc_keys(self):
        keys = [
            Key(
                [self.mod],
                "space",
                lazy.layout.next(),
                desc="Move window focus to other window",
            ),
            Key([self.mod], "m", lazy.window.toggle_minimize(), desc="Toggle minimize"),
            Key(
                [self.mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"
            ),
            Key(
                [self.mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"
            ),
            Key(
                [self.mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"
            ),
            Key([self.mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
            Key([self.mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        ]
        return keys

    def group_keys(self):
        groupObject_imported = groupObject()
        keys = []
        for i in groupObject_imported.groups:
            keys.extend(
                [
                    # mod1 + letter of group = switch to group
                    Key(
                        [self.mod],
                        i.name,
                        lazy.group[i.name].toscreen(),
                        desc="Switch to group {}".format(i.name),
                    ),
                    # mod1 + shift + letter of group = switch to & move focused window to group
                    Key(
                        [self.mod, "shift"],
                        i.name,
                        lazy.window.togroup(i.name, switch_group=True),
                        desc="Switch to & move focused window to group {}".format(
                            i.name
                        ),
                    ),
                    # Or, use below if you prefer not to switch to that group.
                    # # mod1 + shift + letter of group = move focused window to group
                    Key(
                        [self.mod, "control"],
                        i.name,
                        lazy.window.togroup(i.name),
                        desc="Move focused window to group {}".format(i.name),
                    ),
                ]
            )
        return keys

    def scratchpad_keys(self):
        groupObject_imported = groupObject()
        groups = groupObject_imported.groups
        keys = [Key([self.mod], "F11", lazy.group["5"].dropdown_toggle("calendar"))]
        return keys
