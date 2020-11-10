import paramiko
import subprocess
import time

HOST = "127.0.0.1"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username="diman", password="user", port=22)


def get_data_from_docker_process():
    process = subprocess.Popen(["docker", "ps"], stdout=subprocess.PIPE)
    data = process.communicate()
    data = data[0].decode('utf-8')
    return data


def test_stop_phpadmin():
    data = get_data_from_docker_process()
    assert 'opencart_phpadmin_1' in data
    ssh.exec_command("docker kill opencart_phpadmin_1", timeout=3000)
    time.sleep(5)
    data = get_data_from_docker_process()
    assert 'opencart_phpadmin_1' not in data


def test_stop_opencart():
    data = get_data_from_docker_process()
    assert 'opencart_opencart_1' in data
    ssh.exec_command("docker kill opencart_opencart_1", timeout=3000)
    time.sleep(5)
    data = get_data_from_docker_process()
    assert 'opencart_opencart_1' not in data


def test_stop_mariadb():
    data = get_data_from_docker_process()
    assert 'opencart_mariadb_1' in data
    ssh.exec_command("docker kill opencart_mariadb_1", timeout=3000)
    time.sleep(5)
    data = get_data_from_docker_process()
    assert 'opencart_mariadb_1' not in data


def test_start_all_service():
    subprocess.call(["./start_all_services.sh"])
    time.sleep(5)
    data = get_data_from_docker_process()
    assert 'opencart_mariadb_1' in data
    assert 'opencart_opencart_1' in data
    assert 'opencart_phpadmin_1' in data
