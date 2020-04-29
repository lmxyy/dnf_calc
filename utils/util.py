def format_time(ftime):
    days, remainder = divmod(ftime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    remaining_time_str = ""
    if days > 0:
        remaining_time_str += "{}d".format(int(days))
    if days > 0 or hours > 0:
        remaining_time_str += "{:02}h".format(int(hours))
    if hours > 0 or minutes > 0:
        remaining_time_str += "{:02}m".format(int(minutes))
    remaining_time_str += "{:02.2f}s".format(seconds)

    return remaining_time_str


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb