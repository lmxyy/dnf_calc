import time
from inspect import getframeinfo, stack

from utils.util import format_time


###########################################################
#                         调试函数                        #
###########################################################


def _debug_print_debug_timing_info(message):
    _debug_stats = []
    _debug_start_time = time.time()
    _debug_last_step_time = time.time()
    timeline = time.time() - _debug_start_time
    used_time_since_last_step = time.time() - _debug_last_step_time
    _debug_last_step_time = time.time()

    stat = {
        "lineno": getframeinfo(stack()[1][0]).lineno,
        "timeline": timeline,
        "step_used": used_time_since_last_step,
        "message": message,
    }

    _debug_stats.append(stat)

    print("line {:4}: timeline={} step_used={} message={}"
        .format(
        stat["lineno"],
        format_time(stat["timeline"]),
        format_time(stat["step_used"]),
        stat["message"]
    )
    )


def _debug_print_stats(debug_stats):
    if len(debug_stats) == 0:
        return

    total_used_time = debug_stats[-1]["timeline"]
    print("-----------------total={}-----------top 10 step----------------------------".format(
        format_time(total_used_time)))

    _debug_stats = sorted(debug_stats, key=lambda k: k['step_used'], reverse=True)
    if len(_debug_stats) > 10:
        _debug_stats = _debug_stats[:10]

    for stat in _debug_stats:
        step_used = stat["step_used"]
        step_percent = step_used / total_used_time * 100

        print("line {:4}: step_used={} percent={:.2f}% message={}"
            .format(
            stat["lineno"],
            format_time(stat["step_used"]),
            step_percent,
            stat["message"]
        )
        )
