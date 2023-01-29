import psutil, time

from libqtile.widget import base


class HDD(base.ThreadPoolText):
    """
    A simple widget to display disk load.

    Widget requirements: psutil_.

    .. _psutil: https://pypi.org/project/psutil/
    """

    defaults = [
        ("update_interval", 1.0, "Update interval for the HDD widget"),
        (
            "format",
            "HDD Read {read_bytes} Write {write_bytes}",
            "HDD display format",
        ),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(HDD.defaults)
        self.update_interval = self.update_interval * 3 / 4

    def bytes2human(self, bytes):
        # http://code.activestate.com/recipes/578019
        # >>> bytes2human(10000)
        # '9.8K'
        # >>> bytes2human(100001221)
        # '95.4M'
        symbols = ("K", "M", "G", "T", "P", "E", "Z", "Y")
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if bytes >= prefix[s]:
                value = float(bytes) / prefix[s]
                return "%.1f%s" % (value, s)
        return "%sB" % bytes

    def poll(self):
        variables = dict()

        io1 = psutil.disk_io_counters()
        time.sleep(self.update_interval / 3)
        io2 = psutil.disk_io_counters()
        # bytes which were read/written in the last (1) second
        read_bytes = (io2.read_bytes - io1.read_bytes) * 4
        read_count = (io2.read_count - io1.read_count) * 4
        write_bytes = (io2.write_bytes - io1.write_bytes) * 4
        write_count = (io2.read_count - io1.read_count) * 4

        variables["read_bytes"] = self.bytes2human(read_bytes)
        variables["write_bytes"] = self.bytes2human(write_bytes)
        variables["read_count"] = read_count
        variables["write_count"] = write_count

        return self.format.format(**variables)
