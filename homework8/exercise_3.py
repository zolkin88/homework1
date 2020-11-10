import subprocess

HOST = "127.0.0.1"


# Проверям связь с каким то сервером
def test_ping():
    process = subprocess.Popen(['ping', '-c 2', HOST], stdout=subprocess.PIPE)
    data = process.communicate()
    data = data[0].decode('utf-8')
    data = data.split("\n")
    assert '64 bytes' in data[1]


# Проверям, что свободной памяти больше чем 100000
def test_check_memory():
    process = subprocess.check_output(['top', '-b', '-n1'])
    data = process.decode('utf-8').split("\n")
    data = data[3].split(',')
    mem = int(data[1][0:-5])
    assert mem > 100000


# Проверям, что нет зомби процессов
def test_check_zombie():
    process = subprocess.check_output(['top', '-b', '-n1'])
    data = process.decode('utf-8').split("\n")
    data = data[1].split(',')
    zombie = int(data[4][:-7])
    assert zombie == 0
