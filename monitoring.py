import psutil
import time
import datetime
from settings.config import TIME_TO_WAIT
from processes import Processes

class Monitoring:
    def __init__(self):
        self.memory_available = None
        self.memory_percent = None
        self.memory_swap_available = None
        self.memory_swap_percent = None
        self.disk_available = None
        self.disk_percent = None
        self.cpu_percent = None

    def memory_physical(self):
        mem = psutil.virtual_memory()
        self.memory_available = mem.available
        self.memory_percent = mem.percent
        return True

    def memory_virtual_swap(self):
        mem = psutil.swap_memory()
        self.memory_swap_available = mem.free
        self.memory_swap_percent = mem.percent

    def disk(self):
        disk = psutil.disk_usage('/')
        self.disk_available = disk.free
        self.disk_percent = disk.percent

    def cpu(self):
        cpu = psutil.cpu_percent()
        self.cpu_percent = cpu

    def save_data(self):
        f = open('data.csv', 'a')
        row_names = "Fecha de muestreo" + "," + \
                    "RAM libre" + "," + \
                    "% RAM en uso" + "," + \
                    "Swap libre" + "," + \
                    "% Swap en uso" + "," + \
                    "Disco libre" + "," + \
                    "% Disco en uso" + "," + \
                    "% CPU en uso"
        f.write('\n' + row_names)
        f.close()
        pro = Processes()
        while True:
            self.memory_physical()
            self.memory_virtual_swap()
            self.disk()
            self.cpu()
            time_take = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f = open('data.csv', 'a')
            row_data = str(time_take) + "," + \
                str(self.memory_available) + "," + str(self.memory_percent) + "," + \
                str(self.memory_swap_available) + "," + str(self.memory_swap_percent) + "," + \
                str(self.disk_available) + "," + str(self.disk_percent) + "," + \
                str(self.cpu_percent)
            f.write('\n' + row_data)
            f.close()
            f.close()
            pro.record_processes_list()
            time.sleep(TIME_TO_WAIT)


if __name__ == "__main__":
    Monitoring().save_data()
