import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import psutil
import tensorflow as tf
from tensorflow.python.client import device_lib


def human_size(bytes , units=('bytes' , 'KB' , 'MB' , 'GB' , 'TB' , 'PB' , 'EB')) :
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes >> 10 , units[1 :])


def device_memory_info() :
    print('\nDEVICE MEMORY INFO:')
    
    mem = psutil.virtual_memory().total
    free_mem = psutil.virtual_memory().available
    hdd = psutil.disk_usage('/')
    
    print(f'\tCPU Count: {os.cpu_count()}')
    print(f'\tMemory (RAM): {human_size(mem)}')
    print(f'\tFree memory (RAM): {human_size(free_mem)}')
    print(f'\tHD Total: {human_size(hdd.total)}')
    print(f'\tHD Used: {human_size(hdd.used)}')
    print(f'\tHD Free: {human_size(hdd.free)}')


def video_memory_info() :
    print('\nVIDEO MEMORY INFO:')
    
    devices = device_lib.list_local_devices()
    
    for d in devices :
        t = d.device_type
        name = d.physical_device_desc
        l = [item.split(':' , 1) for item in name.split(', ')]
        name_attr = dict([x for x in l if len(x) == 2])
        dev = name_attr.get('name' , 'Unnamed device')
        print(f'\t{d.name} || {dev} || {t} || {human_size(d.memory_limit)}')


def get_info() :
    device_memory_info()
    video_memory_info()
