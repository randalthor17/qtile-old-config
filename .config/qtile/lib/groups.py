from libqtile.config import Group, ScratchPad, DropDown


class groupObject:
    def __init__(self):
        self.groups = self.group_gen()
        self.groups.append(*self.gen_scratchpad())

    def group_gen(self):
        groups = [Group(i) for i in "1234"]
        return groups

    def gen_scratchpad(self):
        groups = [
            ScratchPad(
                "5",
                [
                    DropDown(
                        "calendar",
                        "yad --calendar --on-top --no-buttons --undecorated --skip-taskbar --close-on-unfocus --posy=0 --posx=500 --fixed",
                        x=0.4,
                        opacity=0.9,
                        on_focus_lost_hide=True,
                    ),
                    # DropDown(
                    #     "pavucontrol",
                    #     "pavucontrol",
                    #     x=0.69,
                    #     width=0.3,
                    #     opacity=0.9,
                    #     on_focus_lost_hide=True,
                    # ),
                ],
            )
        ]
        return groups
