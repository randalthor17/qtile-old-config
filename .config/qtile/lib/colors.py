import os


def load_colors(cache="~/.cache/wal/colors"):
    colors = []
    cache = os.path.expanduser(cache)
    with open(cache, "r") as file:
        for line in file:
            colors.append(line.strip())
    colors.append("#ffffff")
    return colors
