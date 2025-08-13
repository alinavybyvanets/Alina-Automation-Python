from datetime import datetime, timedelta
import logging
from typing import List, Tuple, Optional
KEY_TO_ANALYZE = "Key TSTFEED0300|7E3E|0400"
TS_MARK = "Timestamp "
def _extract_timestamp(line: str) -> Optional[datetime]:
    i = line.find(TS_MARK)
    if i == -1:
        return None
    start = i + len(TS_MARK)
    ts_str = line[start:start+8]
    try:

        t = datetime.strptime(ts_str, "%H:%M:%S").time()
        return datetime.combine(datetime.today().date(), t)
    except ValueError:
        return None
def _setup_logger(out_path: str) -> logging.Logger:
    logger = logging.getLogger("hb_test")
    logger.handlers.clear()
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(out_path, mode="w", encoding="utf-8")
    fmt = logging.Formatter("%(levelname)s|%(message)s")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger
def analyze_heartbeat_log(input_path: str, key: str = KEY_TO_ANALYZE, out_path: str = "hb_test.log") -> str:
    logger = _setup_logger(out_path)
    times: List[Tuple[datetime, str]] = []
    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if key in line:
                ts = _extract_timestamp(line)
                if ts is not None:
                    times.append((ts, line.rstrip("\n")))
    if len(times) < 2:
        return out_path
    for i in range(len(times) - 1):
        cur_time, cur_line = times[i]
        nxt_time, nxt_line = times[i+1]

        if nxt_time > cur_time:
            nxt_time_adj = nxt_time - timedelta(days=1)
        else: nxt_time_adj = nxt_time

        delta =(cur_time - nxt_time_adj).total_seconds()
        if 31 < delta < 33:
            msg = (f'{cur_time.time()} | Heartbeat={int(delta)}s | '
                   f'between {cur_time.time()} and {nxt_time.time()} | {key}' )
            logger.warning(msg)
        elif delta >= 33:
            msg = (f'{cur_time.time()} | Heartbeat={int(delta)}s | '
                   f'between {cur_time.time()} and {nxt_time.time()} | {key}')
            logger.error(msg)
    return out_path
if __name__ == "__main__":
    result_path = analyze_heartbeat_log("hblog.txt")
    print(f'Готово. Результат у файлі: {result_path}')

