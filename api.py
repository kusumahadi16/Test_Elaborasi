from importlib.resources import path
import socket, json, mysql.connector as conn, jwt
from tkinter import E
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from types import SimpleNamespace
from urllib.parse import urlparse
from urllib.parse import parse_qs

from requests import patch


hostn = socket.gethostname()
ipp = socket.gethostbyname(hostn)
port = 1234

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

class req_Handler(BaseHTTPRequestHandler):

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Credentials", True)
        self.send_header("Access-Control-Allow-Methods", "GET,POST")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Authorization,Content-Type")
    
    def header_json(self):
        self.send_response(200)
        req_Handler._send_cors_headers(self)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_POST(self):
        try:
            if self.path == '/register':
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                decoded = post_body.decode("utf-8")
                data = json.loads(decoded, object_hook=lambda d: SimpleNamespace(**d))
                nama = data.NAMA
                username = data.USERNAME
                password = data.PASSWORD

                queryString = f"select * from users where username='{username}';"
                is_exist = db(queryString)
                if len(is_exist) == 0:
                    queryString = f"insert into users (nama, username, password) values ('{nama}', '{username}', '{password}'); select last_insert_id()"
                    result = db(queryString)
                    if len(result) > 0:
                        for r in result:
                            reg = Register(r['last_insert_id()'], nama, username)
                        res = response(True, "Berhasil Register", reg.__dict__)
                    else:
                        res = response(False, "Gagal Insert Ke Database", None)
                else:
                    res = response(False, "Username Sudah Digunakan", None)
                req_Handler.header_json(self)
                self.wfile.write(bytearray(json.dumps(res.__dict__),'utf-8'))
            elif self.path == '/login':
                content_len = int(self.headers.get('Content-Length'))
                post_body = self.rfile.read(content_len)
                decoded = post_body.decode("utf-8")
                data = json.loads(decoded, object_hook=lambda d: SimpleNamespace(**d))
                username = data.USERNAME
                password = data.PASSWORD
                
                queryString = f"select nama from users where username='{username}' and password='{password}';"
                is_true = db(queryString)
                if len(is_true) > 0:
                    nama = is_true[0]['nama']
                    now = datetime.now()
                    jam = '%d-%02d-%02d %02d:%02d:%02d' % (now.year,now.month,now.day,now.hour,now.minute,now.second)
                    encoded_jwt = jwt.encode({"USERNAME":username,"NAMA":nama,"Jam":jam}, "T3chn!c4l.T3st?", algorithm="HS256")
                    if isinstance(encoded_jwt, bytes):
                        encoded_jwt = encoded_jwt.decode()
                    queryString = f"update users set token=concat('Bearer ', '{encoded_jwt}') where username='{username}' and password='{password}';"
                    db(queryString)
                    log = Login(nama, username, encoded_jwt)
                    res = response(True, "Berhasil Login", log.__dict__)
                else:
                    res = response(False, "Username and Password Doesn't Match", log.__dict__)
                req_Handler.header_json(self)
                self.wfile.write(bytearray(json.dumps(res.__dict__),'utf-8'))
            else:
                token = self.headers.get('Authorization')
                queryString = f"select id from users where token = '{token}';"
                is_exist = db(queryString)
                if len(is_exist) > 0:
                    if self.path == '/data_pegawai':
                        queryString = "select p.id, p.nama, p.tanggal_lahir, j.nama_jabatan, p.jenis_kelamin from pegawai p left join jabatan j on p.id_jabatan=j.id;"
                        result = db(queryString)
                        workers = []
                        if len(result) > 0:
                            for r in result:
                                worker = get_pegawai(r)
                                workers.append(worker.__dict__)
                            res = response(True, "Data Pegawai Berhasil Ditemukan", workers)
                        else:
                            res = response(False, "Data Pegawai Tidak Ditemukan", None)
                        req_Handler.header_json(self)
                        self.wfile.write(bytearray(json.dumps(res.__dict__),'utf-8'))
                    elif 'data_pegawai' in self.path:
                        urlParsed = urlparse(self.path)
                        extendedFilter = ''
                        if 'jenis_kelamin' in self.path:
                            jenis_kelamin = parse_qs(urlParsed.query)['jenis_kelamin'][0]
                            extendedFilter += f"p.jenis_kelamin = '{jenis_kelamin}' "
                        if 'jabatan' in self.path:
                            jabatan = parse_qs(urlParsed.query)['jabatan'][0]
                            extendedFilter += f"j.nama_jabatan = '{jabatan}' "
                        if 'numbers' in self.path:
                            numbers = parse_qs(urlParsed.query)['numbers'][0]
                            now = datetime.now()
                            yearStart = now.year - int(numbers) - 1
                            yearEnd = now.year - int(numbers)
                            birthStart = '%d-%02d-%02d' % (yearStart, now.month, now.day)
                            birthEnd = '%d-%02d-%02d' % (yearEnd, now.month, now.day)
                            extendedFilter += f"p.tanggal_lahir >= '{birthStart}' and p.tanggal_lahir <= '{birthEnd}' "
                        urlParsed = urlparse(self.path)
                        queryString = f"select p.id, p.nama, p.tanggal_lahir, j.nama_jabatan, p.jenis_kelamin from pegawai p left join jabatan j on p.id_jabatan=j.id where {extendedFilter};"
                        result = db(queryString)
                        workers = []
                        if len(result) > 0:
                            for r in result:
                                worker = get_pegawai(r)
                                workers.append(worker.__dict__)
                            res = response(True, "Data Pegawai Berhasil Ditemukan", workers)
                        else:
                            res = response(False, "Data Pegawai Tidak Ditemukan", None)
                        req_Handler.header_json(self)
                        self.wfile.write(bytearray(json.dumps(res.__dict__),'utf-8'))
                    else:
                        self.send_response(404)
                        req_Handler._send_cors_headers(self)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                else:
                    self.send_response(401)
                    req_Handler._send_cors_headers(self)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
        except Exception as e:
            print(e)
    def do_GET(self):
        pass

def run(server_class=ThreadingHTTPServer, handler_class=req_Handler):
    try:
        server_address = (ipp, port)
        httpd = server_class(server_address, handler_class)
        httpd.timeout = 60
        print (f"Started HTTPServer on {ipp}:{port} ")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ("^C recieved, shutting down the web server")
        httpd.server_close()

def con():
    try:
        db = conn.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root3st!',
            database = 'kepegawaian'
        )
        return db
    except Exception as e:
        print(str(e))

def db(queryString):
    try:
        db = con()
        query = db.cursor(dictionary=True)
        for i in queryString.split(';'):
            if i != '':
                query.execute(i)
                r = query.fetchall()
        db.commit()
        db.close()
        return r
    except Exception as e:
        print (str(e))

def get_pegawai(r):
    try:
        now = datetime.now()
        tahun_sekarang = now.year
        bulan_sekarang = now.month
        tanggal_sekarang = now.day
        tahun_lahir = r['tanggal_lahir'].year
        bulan_lahir = r['tanggal_lahir'].month
        tanggal_lahir = r['tanggal_lahir'].day
        if tanggal_lahir > tanggal_sekarang:
            tanggal_sekarang = tanggal_sekarang + 30
            bulan_sekarang = bulan_sekarang - 1
        if bulan_lahir > bulan_sekarang:
            tahun_sekarang = tahun_sekarang - 1
            bulan_sekarang = bulan_sekarang + 12
        tahun = tahun_sekarang - tahun_lahir
        worker = Pegawai(r['id'], r['nama'], tahun, r['nama_jabatan'], r['jenis_kelamin'])

        return worker
    except Exception as e:
        print(e)

class Register:
    def __init__(self, id, nama, username):
        self.ID = id
        self.NAMA = nama
        self.USERNAME = username

class Pegawai:
    def __init__(self, id, nama, usia, jabatan, jenis_kelamin):
        self.ID = id
        self.NAMA = nama
        self.USIA = usia
        self.JABATAN = jabatan
        self.JENIS_KELAMIN = jenis_kelamin

class Login:
    def __init__(self, nama, username, token):
        self.NAMA = nama
        self.USERNAME = username
        self.TOKEN = token

class response:
    def __init__(self, status, keterangan, data):
        self.STATUS = status
        self.KETERANGAN = keterangan
        self.DATA = data

if __name__ == '__main__':
    run()