import ctypes
import winshell

def extract_command(command_to_execute):
    command_to_execute = command_to_execute.lower()
    final_command = '' 
    if command_to_execute.startswith('regarder') == True:
        final_command = 'regarder'
    if command_to_execute.startswith('vider') == True:
        final_command = 'vider'

    return final_command


def lock_desktop_screen():
    try:
        ctypes.windll.user32.LockWorkStation()
        return 1
    except:
        return 0

def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
        return 1
    except Exception:
        return 0






