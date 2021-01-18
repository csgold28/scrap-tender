from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import ssl
from socket import timeout


app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/',methods=["GET"])
def get():
    
    # hasil = []
    # for url in urls:
    #     try:
        
    #         ssl._create_default_https_context = ssl._create_unverified_context
    #         html = urlopen(url, timeout=60).read()
    #     except HTTPError as error:
    #         print(error)
    #     except Exception as e:
    #         print(e)
    #     except timeout:
    #         print('socket timed out - URL %s', url)
    #     else:
    #         doc = BeautifulSoup(html, 'html.parser')
    #         tipe = ["Pengadaan_Barang","Jasa_Konsultansi_Badan_Usaha","Pekerjaan_Konstruksi","Jasa_Lainnya","Jasa_Konsultansi_Perorangan"]
    #         for t in tipe:
    #             barang = doc.find_all("tr", t)
    #             for target_list in barang:
    #                 nama = (target_list.find('a').get_text())
    #                 hps = (target_list.find('td','table-hps').get_text())
    #                 exp = (target_list.find('td','center').get_text())
    #                 scrap = {'lpse' : url,'nama_tender': nama, 'hps_tender': hps, 'tanggal_akhir': exp }
    #                 hasil.append(scrap)
    data = {
        'code': 200,
        'status': 'success',
        'data': 'API Cek Tender'
    }
    return data
if __name__ == "__main__":
    app.run(debug=True, port=8000)