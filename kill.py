import psutil

def pkill(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
