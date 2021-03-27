from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import ssl
from socket import timeout
import requests


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/',methods=["GET"])
def get():
    data = {
        'code': 200,
        'status': 'success',
        'data': 'API CEK TENDER'
    }
    return data
@app.route('/lpse', methods=["GET"])
def data():
    url = request.args.get('url')
    hasil = []
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        html = urlopen(url, timeout=60).read()
    except HTTPError as error:
        print(error)
    except Exception as e:
        print(e)
    except timeout:
        print('socket timed out - URL %s', url)
    else:
        doc = BeautifulSoup(html, 'html.parser')
        tipe = ["Pengadaan_Barang","Jasa_Konsultansi_Badan_Usaha","Pekerjaan_Konstruksi","Jasa_Lainnya","Jasa_Konsultansi_Perorangan","Jasa_Konsultansi_Badan_Usaha_Konstruksi","Jasa_Konsultansi_Badan_Usaha_Non_Konstruksi"]
        for t in tipe:
            barang = doc.find_all("tr", t)
            for target_list in barang:
                nama = (target_list.find('a').get_text())
                link = (target_list.find('a', href=True))
                hps = (target_list.find('td','table-hps').get_text())
                exp = (target_list.find('td','center').get_text())
                scrap = {'lpse' : url, 'link': link['href'], 'nama_tender': nama, 'hps': hps, 'tanggal_akhir': exp, 'type' : t }
                hasil.append(scrap)
    data = {
        'code': 200,
        'status': 'success',
        'data': hasil
    }
    return data

if __name__ == "__main__":
    app.run(debug=True, port=8000)