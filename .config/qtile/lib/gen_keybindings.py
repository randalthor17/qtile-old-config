# import keys, mouse

# keyObj = keys.keyObject()
# keys = keyObj.keys
# mouse = mouse.gen_mouse_keys()


# def show_keys(keys, mouse):
#     key_help = ""
#     for k in keys:
#         mods = ""

#         for m in k.modifiers:
#             if m == "mod4":
#                 mods += "Super + "
#             else:
#                 mods += m.capitalize() + " + "

#         if len(k.key) > 1:
#             mods += k.key.capitalize()
#         else:
#             mods += k.key

#         key_help += "{:<30}\t{}".format(mods, k.desc + "\n")

#     for k in mouse:
#         mods = ""
#         for m in k.modifiers:
#             if m == "mod4":
#                 mods += "Super + "
#             else:
#                 mods += m.capitalize() + " + "
#         mods += k.button
#         desc = type(k).__name__ + " to " + k.commands[0].name.replace("_", " ")
#         key_help += "{:<30}\t{}".format(mods, desc + "\n")
#     key_help = key_help.expandtabs(20)
#     print(key_help)


# show_keys(keys, mouse)


from io import StringIO

import pandas as pd
from libqtile.ipc import find_sockfile, Client as IPCClient
from libqtile.command.interface import IPCCommandInterface
from libqtile.command.client import InteractiveCommandClient
from tabulate import tabulate


def Client():
    return InteractiveCommandClient(IPCCommandInterface(IPCClient(find_sockfile())))


if __name__ == "__main__":
    c = Client()
    stream = StringIO(c.display_kb())
    df = (
        pd.read_fwf(stream)
        .drop(0)
        .drop_duplicates()
        .reindex(columns=["Desc", "Mod", "KeySym"])
    )
    df_new = tabulate(df, headers=df.columns)
    # do whatever you want, e.g. df.to_csv, df.to_json, ...
    print(df_new)
