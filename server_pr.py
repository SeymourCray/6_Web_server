from os import extsep
import socket
from threading import Thread
import time
import re
import json
from os.path import sep, isfile


def write_log(date, ip, filename):
    with open('logs.txt', 'a') as file:
        file.write('\n'.join([date, ip, filename, '\n']))


def get_date():
    t = time.asctime(time.gmtime()).split(' ')
    t = f'{t[0]}, {t[2]} {t[1]} {t[4]} {t[3]} GMT'
    return t


def code(path):
    if not isfile(path):
        return "Not Found"
    elif not re.findall(r'\.html|\.js|\.css|\.png', path):
        return "Forbidden"
    else:
        return "OK"


def path(request):
    if request == '/':
        return dictionary["dir"]+sep+'index.html'
    else:
        return dictionary["dir"]+sep+request[1:].replace('/', sep)


def receive_answer(request, addr):
    this_path = path(request)
    this_code = code(this_path)
    requested_file = this_path.split(sep)[-1]
    extension = this_path.split(".")[-1]
    current_date = get_date()
    write_log(current_date, str(addr[0]), requested_file)
    with open(this_path, 'rb') as f:
        answer = f.read()  
        return dictionary["sample"].format(dictionary[this_code], this_code, current_date, dictionary[extension], len(answer)).encode() + answer
    

def work(conn, addr):
    user_answer = conn.recv(dictionary["max_byte"]).decode()
    print(user_answer)
    request = user_answer.split(" ")[1]
    conn.send(receive_answer(request, addr))


def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('', dictionary["port"]))
            print(f"Using port {dictionary['port']}")
        except:
            sock.bind(('', dictionary["second_port"]))
            print(f"Using port {dictionary['second_port']}")
        sock.listen(5)
        while True:
            conn, addr = sock.accept()
            thread = Thread(target=work, args=(conn, addr))
            thread.start()
            print("Connected", addr)
    except KeyboardInterrupt:
        sock.close()
        print('Server is closed...')


if __name__ == "__main__":
    dictionary = {}
    with open('settings.json', 'r') as file:
        dictionary = json.load(file)
    create_socket()
