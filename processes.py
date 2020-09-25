import psutil
import datetime
from settings.config import TIME_TO_WAIT, PROCESSES_TO_MONITORING


class Processes:
    def __init__(self):
        self.pid = None
        self.name = None
        self.cpu = None
        self.memory = None
        self.record_processes_list()

    def record_processes_list(self):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] in PROCESSES_TO_MONITORING:
                if psutil.pid_exists(proc.info['pid']) is True:
                    p = psutil.Process(proc.info['pid'])
                    with p.oneshot():
                        self.pid = str(proc.info['pid'])
                        self.name = str(p.name())
                        self.cpu = str(p.cpu_percent())
                        self.memory = str(p.memory_percent())
                        time_take = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        filename = proc.info['name'] + ".csv"
                        f = open(filename, 'a')
                        row_data = str(time_take) + "," + \
                                   str(self.pid) + "," + str(self.name) + "," + \
                                   str(self.cpu) + "," + str(self.memory)
                        f.write('\n' + row_data)
                        f.close()
                        f.close()
