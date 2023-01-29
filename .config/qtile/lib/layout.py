from libqtile.layout.floating import Floating
from .layouts.bsp import Bsp
from libqtile.layout.max import Max
from libqtile.config import Match
from .colors import load_colors


class layoutObject:
    def __init__(self):
        colors = load_colors()
        floating_layout = self.floating_layout_rules(colors)
        self.layout = self.layout_gen(floating_layout, colors)

    def floating_layout_rules(self, colors):
        floating_layout = Floating(
            float_rules=[
                # Run the utility of `xprop` to see the wm class and name of an X client.
                *Floating.default_float_rules,
                Match(wm_class="confirmreset"),  # gitk
                Match(wm_class="makebranch"),  # gitk
                Match(wm_class="maketag"),  # gitk
                Match(wm_class="ssh-askpass"),  # ssh-askpass
                Match(title="branchdialog"),  # gitk
                Match(title="pinentry"),  # GPG key password entry
                Match(wm_class="Yad"),  # calendar
            ],
            border_focus=colors[11],
            border_normal=colors[7],
            border_width=3,
        )
        return floating_layout

    def layout_gen(self, floating_layout, colors):
        layouts = [
            Bsp(
                margin=5,
                # margin_on_single=0,
                border_focus=colors[11],
                border_normal=colors[7],
                border_width=3,
            ),
            Max(),
            # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
            # Try more layouts by unleashing below layouts.
            # layout.Stack(num_stacks=2),
            # layout.Matrix(),
            # layout.MonadTall(),
            # layout.MonadWide(),
            # layout.RatioTile(),
            # layout.Tile(),
            # layout.TreeTab(),
            # layout.VerticalTile(),
            # layout.Zoomy(),
            floating_layout,
        ]
        return layouts
