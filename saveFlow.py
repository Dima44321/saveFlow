import numpy as np
from pywinauto import Desktop


windows = np.array(Desktop(backend="uia").windows())
fname = 'ignoredWindows.txt'
with open(fname) as f:
    ignored_win_names = []
    for line in f:
        ignored_win_names.append(line.replace('\n', ''))

ignored_windows = np.array(
    [w.window_text() in ignored_win_names for w in windows])

selected_windows = windows[np.logical_not(ignored_windows)]

print(selected_windows)
