from threading import Thread
import psutil
from time import sleep
from datetime import datetime
import csv


class Memory:
    def __init__(self):
        self.memory = 0

    def collect_values(self):
        while status:
            self.memory = psutil.virtual_memory().available / 1_048_576
            now = datetime.now()
            with open("output.csv", 'a') as file:
                csv.writer(file, lineterminator="\r").writerow([now.strftime("%H:%M:%S"), "Available memory",
                                                                self.memory])
            sleep(60)


class Cpu_info:
    def __init__(self):
        self.count_process = 0
        self.cpu_percent = 0

    def collect_values(self):
        while status:
            self.count_process = len(list((psutil.process_iter())))  # количество запущенный процессов
            self.cpu_percent = psutil.cpu_percent(interval=None, percpu=False)  # нагрузка цп в процентах
            now = datetime.now()
            with open("output.csv", 'a') as file:
                csv.writer(file, lineterminator="\r").writerows([[now.strftime("%H:%M:%S"), "Count process",
                                                                  self.count_process],
                                                                 [now.strftime("%H:%M:%S"), "Cpu load",
                                                                  self.cpu_percent]])
            sleep(60)


def main():
    global status
    thread1 = Thread(target=Thread_CPU.collect_values, daemon=True)
    thread2 = Thread(target=Thread_Memory.collect_values, daemon=True)
    thread1.start()
    thread2.start()
    print("Подсчёт метрик начался...")
    while status:
        temp = input("> Введите stop для остановки подсчёта метрик: ")
        if temp == "stop":
            status = False
            print("Подсчёт метрик остановился")
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    status = True
    Thread_CPU = Cpu_info()
    Thread_Memory = Memory()
    main()
