import psutil
import re
from pypresence import Presence
from time import time, sleep
from win32gui import GetForegroundWindow, GetWindowText
from win32process import GetWindowThreadProcessId

client = Presence(659889732939022366)
client.connect()

last_activity = ''

def get_current_process():
    fw = GetForegroundWindow()
    pid = GetWindowThreadProcessId(fw)

    window_title = GetWindowText(fw)
    proc_name = psutil.Process(pid[-1]).name()
    return window_title, proc_name


while True:
    w_t, p_n = get_current_process()
    activity = w_t or 'desktop'

    # cleaned_pn = p_n.split('.')[0]

    # if re.match(r'^[a-z]', cleaned_pn):
    #     cleaned_pn = cleaned_pn.title()

    if activity != last_activity:
        last_activity = activity
        client.update(details=activity[:128], state=p_n, start=time(), instance=False)
        sleep(15)
    else:
        sleep(2)
