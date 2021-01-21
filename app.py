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
    data = {
        'code': 200,
        'status': 'success',
        'data': 'API CEK TENDER'
    }
    return data
@app.route('/data-tender', methods=["GET"])
def data():
    urls = [
        # ACEH
        "https://lpse.acehprov.go.id",
        "http://lpse.acehbaratkab.go.id",
        "http://lpse.acehbaratdayakab.go.id",
        "http://lpse.acehbesarkab.go.id/",
        "http://lpse.acehjayakab.go.id",
        "http://lpse.acehselatankab.go.id",
        "http://lpse.acehsingkilkab.go.id",
        "https://lpse.acehtamiangkab.go.id",
        "https://lpse.acehtengahkab.go.id",
        "http://lpse.acehtenggarakab.go.id",
        "http://lpse.acehtimurkab.go.id",
        "http://lpse.acehutara.go.id",
        "http://lpse.benermeriahkab.go.id",
        "http://lpse.bireuenkab.go.id",
        "http://lpse.gayolueskab.go.id",
        "http://lpse.naganrayakab.go.id",
        "http://lpse.pidiekab.go.id",
        "https://lpse.pidiejayakab.go.id",
        "http://lpse.simeuluekab.go.id",
        "https://lpse.bandaacehkota.go.id",
        "http://lpse.langsakota.go.id",
        "http://lpse.lhokseumawekota.go.id",
        "https://lpse.sabangkota.go.id",
        "http://www.lpse.subulussalamkota.go.id",
        "http://lpse.aceh.polri.go.id",

        # BALI
        "http://lpse.badungkab.go.id",
        "http://lpse.banglikab.go.id",
        "https://eproc.bulelengkab.go.id",
        "http://lpse.gianyarkab.go.id",
        "https://lpse.jembranakab.go.id",
        "http://lpse.karangasemkab.go.id",
        "https://lpse.klungkungkab.go.id",
        "https://lpse.tabanankab.go.id",
        "http://eproc.denpasarkota.go.id",
        "https://lpse.baliprov.go.id",
        "http://lpse.bali.polri.go.id",

        # BANTEN
        "https://lpse.lebakkab.go.id",
        "http://lpse.pandeglangkab.go.id",
        "http://lpse.serangkab.go.id",
        "https://lpse.tangerangkab.go.id",
        "http://lpse.cilegon.go.id",
        "https://lpse.serangkota.go.id",
        "https://lpse.tangerangkota.go.id",
        "http://lpse.tangerangselatankota.go.id",
        "https://lpse.bantenprov.go.id",
        "http://lpse.banten.polri.go.id",

        # BENGKULU
        "http://lpse.bengkuluselatankab.go.id",
        "http://lpse.bengkulutengahkab.go.id",
        "https://lpse.bengkuluutarakab.go.id",
        "http://lpse.kaurkab.go.id",
        "https://lpse.kepahiangkab.go.id",
        "http://lpse.lebongkab.go.id",
        "http://lpse.mukomukokab.go.id",
        "http://lpse.rejanglebongkab.go.id",
        "http://lpse.selumakab.go.id",
        "http://lpse.bengkulukota.go.id",
        "https://lpse.bengkuluprov.go.id",

        # JAKARTA
        "https://lpse.jakarta.go.id",
        "http://lpse.metro.polri.go.id",

        # GORONTALO
        "http://lpse.boalemokab.go.id",
        "http://lpse.bonebolangokab.go.id",
        "http://lpse.gorontalokab.go.id",
        "http://lpse.gorutkab.go.id",
        "https://lpse.pohuwatokab.go.id",
        "https://lpse.gorontalokota.go.id",
        "https://lpse.gorontaloprov.go.id",
        "http://lpse.gorontalo.polri.go.id",

        # JAMBI
        "http://lpse.batangharikab.go.id",
        "http://lpse.bungokab.go.id",
        "http://lpse.kerincikab.go.id",
        "http://lpse.meranginkab.go.id",
        "http://lpse.muarojambikab.go.id",
        "http://lpse.sarolangunkab.go.id",
        "http://lpse.tanjabbarkab.go.id",
        "http://lpse.tanjabtimkab.go.id",
        "http://lpse.tebokab.go.id",
        "http://lpse.jambikota.go.id",
        "http://lpse.jambiprov.go.id",
        "http://lpse.sungaipenuhkota.go.id",
        "http://lpse.jambi.polri.go.id",

        # JAWA BARAT
        "http://lpse.bandungkab.go.id",
        "http://lpse.bandungbaratkab.go.id",
        "https://lpse.bekasikab.go.id",
        "https://lpse.bogorkab.go.id",
        "https://lpse.ciamiskab.go.id",
        "http://lpse.cianjurkab.go.id",
        "http://lpse.cirebonkab.go.id",
        "http://lpse.indramayukab.go.id",
        "http://lpse.karawangkab.go.id",
        "http://lpse.kuningankab.go.id",
        "http://lpse.majalengkakab.go.id",
        "http://lpse.purwakartakab.go.id",
        "http://lpse.subang.go.id",
        "http://lpse.sukabumikab.go.id",
        "http://lpse.sumedangkab.go.id",
        "http://lpse.tasikmalayakab.go.id",
        "http://lpse.bandung.go.id",
        "http://lpse.banjarkota.go.id",
        "http://lpse.bekasikota.go.id",
        "https://eproc.kotabogor.go.id",
        "http://lpse.cimahikota.go.id",
        "http://lpse.cirebonkota.go.id",
        "https://lpse.depok.go.id",
        "http://lpse.tasikmalayakota.go.id",
        "https://lpse.jabarprov.go.id",
        "http://www.lpse.jabar.polri.go.id",

        # JAWA TENGAH
        "http://lpse.banjarnegarakab.go.id",
        "http://lpse.banyumaskab.go.id",
        "http://lpse.batangkab.go.id",
        "https://lpse.blorakab.go.id",
        "https://lpse.boyolali.go.id",
        "http://lpse.brebeskab.go.id",
        "https://lpse.cilacapkab.go.id",
        "http://lpse.demakkab.go.id",
        "http://lpse.grobogan.go.id",
        "http://lpse.jepara.go.id",
        "http://lpse.karanganyarkab.go.id",
        "https://lpse.kebumenkab.go.id",
        "https://lpse.kendalkab.go.id",
        "http://lpse.klatenkab.go.id",
        "http://lpse.kuduskab.go.id",
        "http://lpse.magelangkab.go.id",
        "http://lpsepatikab.org",
        "https://lpse.pekalongankab.go.id",
        "http://lpse.pemalangkab.go.id",
        "https://lpse.purbalinggakab.go.id",
        "https://lpse.purworejokab.go.id",
        "http://lpse.rembangkab.go.id",
        "http://lpse.semarangkab.go.id",
        "http://lpse.sragenkab.go.id",
        "http://lpse.sukoharjokab.go.id",
        "http://lpse.tegalkab.go.id",
        "http://lpse.temanggungkab.go.id",
        "https://www.lpse.wonogirikab.go.id",
        "http://lpse.wonosobokab.go.id",
        "https://lpse.magelangkota.go.id",
        "http://lpse.pekalongankota.go.id",
        "https://lpse.salatiga.go.id",
        "https://lpse.semarangkota.go.id",
        "https://lpse.surakarta.go.id",
        "https://lpse.tegalkota.go.id",
        "http://lpse.jatengprov.go.id",
        "http://lpse.jateng.polri.go.id",

        # JAWA TIMUR
        "https://lpse.bangkalankab.go.id",
        "https://lpse.banyuwangikab.go.id",
        "http://lpse.blitarkab.go.id",
        "http://lpse.bojonegorokab.go.id",
        "http://lpse.bondowosokab.go.id",
        "http://lpse.gresikkab.go.id",
        "https://lpse.jemberkab.go.id",
        "http://lpse.jombangkab.go.id",
        "http://lpse.kedirikab.go.id",
        "http://lpse.lamongankab.go.id",
        "http://lpse.lumajangkab.go.id",
        "http://lpse.madiunkab.go.id",
        "http://lpse.magetan.go.id",
        "https://lpse.malangkab.go.id",
        "http://lpse.mojokertokab.go.id",
        "https://lpse.nganjukkab.go.id",
        "https://lpse.ngawikab.go.id",
        "https://lpse.pacitankab.go.id",
        "https://lpse.pamekasankab.go.id",
        "https://lpse.pasuruankab.go.id",
        "https://lpse.ponorogo.go.id",
        "http://lpse.sampangkab.go.id",
        "https://lpse.sidoarjokab.go.id",
        "http://lpse.situbondokab.go.id",
        "http://lpse.sumenepkab.go.id",
        "http://lpse.trenggalekkab.go.id",
        "https://lpse.tubankab.go.id",
        "http://lpse.tulungagung.go.id",
        "http://lpse.batukota.go.id",
        "http://lpse.blitarkota.go.id",
        "http://lpse.kedirikota.go.id",
        "http://lpse.madiunkota.go.id",
        "https://lpse.malangkota.go.id",
        "https://lpse.mojokertokota.go.id",
        "https://lpse.pasuruankota.go.id",
        "https://lpse.probolinggokota.go.id",
        "https://lpse.surabaya.go.id",
        "https://lpse.jatimprov.go.id",
        "http://lpse.jatim.polri.go.id",

        # KALIMANTAN BARAT
        "http://lpse.bengkayangkab.go.id",
        "http://lpse.kapuashulukab.go.id",
        "http://118.97.211.5",
        "http://lpse.ketapangkab.go.id",
        "http://lpse.kuburayakab.go.id",
        "http://lpse.landakkab.go.id",
        "https://lpse.melawikab.go.id",
        "http://lpse.mempawahkab.go.id",
        "http://lpse.sambas.go.id",
        "http://lpse.sanggau.go.id",
        "http://lpse.sekadaukab.go.id",
        "http://lpse.sintang.go.id",
        "https://lpse.pontianakkota.go.id",
        "http://lpse.singkawangkota.go.id",
        "https://lpse.kalbarprov.go.id",
        "http://lpse.kalbar.polri.go.id",

        # KALIMANTAN SELATAN
        "https://lpse.balangankab.go.id",
        "https://lpse.banjarkab.go.id",
        "http://www.lpse.baritokualakab.go.id",
        "http://lpse.hulusungaiselatankab.go.id",
        "http://lpse.hulusungaitengahkab.go.id",
        "http://lpse.hulusungaiutarakab.go.id",
        "http://lpse.kotabarukab.go.id",
        "https://lpse.tabalongkab.go.id",
        "http://lpse.tanahbumbukab.go.id",
        "https://lpse.tanahlautkab.go.id",
        "http://lpse.tapinkab.go.id",
        "http://lpse.banjarbarukota.go.id",
        "http://lpse.kalselprov.go.id",
        "http://lpse.kalsel.polri.go.id",

        # KALIMANTAN TENGAH
        "http://lpse.banjarmasinkota.go.id",
        "https://lpse.baritoselatankab.go.id",
        "https://lpse.baritotimurkab.go.id",
        "https://lpse.baritoutarakab.go.id",
        "https://lpse.gunungmaskab.go.id",
        "http://lpse.kapuaskab.go.id",
        "http://lpse.katingankab.go.id",
        "http://lpse.kotawaringinbaratkab.go.id/eproc4",
        "https://lpse.kotimkab.go.id",
        "http://lpse.lamandaukab.go.id",
        "http://lpse.kabmurungraya.go.id",
        "http://lpse.pulangpisaukab.go.id",
        "https://lpse.sukamarakab.go.id",
        "http://lpse.seruyankab.go.id",
        "https://lpse.palangkaraya.go.id",
        "https://lpse.kalteng.go.id",
        "http://lpse.banggaikab.go.id",
        "http://lpse.kalteng.polri.go.id",

        # KALIMANTAN TIMUR
        "https://spse.beraukab.go.id",
        "https://lpse.kutaibaratkab.go.id",
        "http://lpse.kutaikartanegarakab.go.id",
        "http://lpse.kutaitimurkab.go.id",
        "http://lpse.mahakamulukab.go.id",
        "http://lpse.paserkab.go.id",
        "https://lpse.penajamkab.go.id",
        "http://lpse.balikpapan.go.id",
        "http://lpse.bontangkota.go.id",
        "http://lpse.samarindakota.go.id",
        "https://lpse.kaltimprov.go.id",
        "http://lpse.kaltim.polri.go.id",

        # KALIMANTAN UTARA
        "http://spse.bulungan.go.id",
        "http://lpse.malinau.go.id",
        "http://lpse.nunukankab.go.id",
        "http://lpse.tanatidungkab.go.id",
        "http://lpse.tarakankota.go.id",
        "https://lpse.kaltaraprov.go.id",

        # KEMENTRIAN
        "https://lpse.kemendagri.go.id",
        "https://lpse.kemlu.go.id",
        "https://lpse.kemhan.go.id",
        "https://lpse.kemenag.go.id",
        "http://lpse.atrbpn.go.id",
        "https://lpse.kemendesa.go.id",
        "https://eproc.esdm.go.id",
        "https://lpse.kemenkumham.go.id",
        "http://lpse.kkp.go.id",
        "http://www.lpse.kemkes.go.id",
        "https://lpse.kemnaker.go.id",
        "https://www.lpse.kemenkeu.go.id",
        "https://lpse.kominfo.go.id",
        "http://lpse.menlhk.go.id",
        "https://lpse.pu.go.id",
        "https://lpse.kemdikbud.go.id",
        "http://lpse.kemendag.go.id",
        "https://lpse.dephub.go.id",
        "https://lpse.kemenperin.go.id",
        "https://lpse.pertanian.go.id",
        "https://lpse.ristekbrin.go.id",
        "http://lpse.depkop.go.id",
        "https://lpse.menpan.go.id",
        "http://lpse.kemenpora.go.id",
        "https://lpse.kemenparekraf.go.id",

        # KEP. BANGKA BELITUNG
        "https://lpse.bangka.go.id",
        "https://lpse.bangkabaratkab.go.id",
        "http://lpse.bangkaselatankab.go.id",
        "https://lpse.bangkatengahkab.go.id",
        "https://lpse.belitungkab.go.id",
        "http://lpse.belitungtimurkab.go.id",
        "https://lpse.pangkalpinangkota.go.id",
        "https://lpse.babelprov.go.id",

        # KEP. RIAU
        "http://lpse.bintankab.go.id",
        "http://lpsetbk.karimunkab.go.id",
        "http://lpse.anambaskab.go.id",
        "http://lpse.linggakab.go.id",
        "http://lpse.natunakab.go.id",
        "https://lpse.batam.go.id",
        "http://lpse.tanjungpinangkota.go.id",
        "http://lpse.kepriprov.go.id",
        "http://lpse.kepri.polri.go.id",

        # LAMPUNG 
        "https://lpse.lampungbaratkab.go.id",
        "https://lpse.lampungselatankab.go.id",
        "https://lpse.lampungtengahkab.go.id",
        "https://lpse.lampungtimurkab.go.id",
        "http://lpse.lampungutarakab.go.id",
        "https://lpse.mesujikab.go.id",
        "http://www.lpse.pesawarankab.go.id",
        "https://lpse.pesisirbaratkab.go.id",
        "http://lpse.pringsewukab.go.id",
        "http://lpse.tanggamus.go.id",
        "https://lpse.tulangbawangbaratkab.go.id",
        "http://lpse.waykanankab.go.id",
        "https://lpse.bandarlampungkota.go.id",
        "http://lpse.metrokota.go.id",
        "https://lpse.lampungprov.go.id",
        "http://lpse.lampung.polri.go.id",

        # LEMBAGA
        "http://lpse.bnpb.go.id",
        "https://lpse.lapan.go.id",
        "http://lpse.bekraf.go.id",
        "http://lpse.big.go.id",
        "http://lpse.bakamla.go.id",
        "http://lpse.bkn.go.id",
        "http://lpse.bkkbn.go.id",
        "http://lpse.bkpm.go.id",
        "http://lpse.bmkg.go.id",
        "https://lpse.bnn.go.id",
        "http://lpse.bnpt.go.id",
        "http://www.lpse.basarnas.go.id",
        "https://lpse.bp2mi.go.id/eproc4",
        "http://lpse.pom.go.id",
        "https://lpse.bppt.go.id",
        "http://lpse.bps.go.id",
        "https://lpse.bssn.go.id",
        "https://lpse.lipi.go.id",
        "https://lpse.lkpp.go.id",
        "http://lpse.lemhannas.go.id",
        "https://lpse.dpr.go.id",
        "http://lpse.dpd.go.id",
        "http://lpse.mpr.go.id",
        "http://lpse.mahkamahkonstitusi.go.id",
        "https://lpse.mahkamahagung.go.id",
        "http://lpse.kpu.go.id",

        # MALUKU
        "http://103.60.181.130",
        "http://103.131.61.8",
        "http://lpse.kepulauanarukab.go.id",
        "http://lpse.malukubaratdayakab.go.id",
        "http://lpse.maltengkab.go.id",
        "http://lpse.malukutenggarakab.go.id",
        "http://lpse.mtbkab.go.id",
        "http://lpse.sbbkab.go.id",
        "http://lpse.serambagiantimurkab.go.id",
        "http://lpse.ambon.go.id",
        "http://lpse.tualkota.go.id",
        "https://lpse.malukuprov.go.id",
        "http://lpse.maluku.polri.go.id",

        # MALUKU UTARA
        "http://lpse.halbarkab.go.id",
        "http://lpse.haltengkab.go.id",
        "http://lpse-haltimkab.go.id",
        "http://lpse.halmaheraselatankab.go.id",
        "http://lpse.halmaherautarakab.go.id",
        "http://lpse.kepulauansulakab.go.id",
        "http://lpse.pulaumorotaikab.go.id",
        "http://103.60.181.134",
        "http://lpse.ternatekota.go.id",
        "http://lpse.tidorekota.org",
        "http://lpse.malutprov.go.id",
        "http://www.lpse.malut.polri.go.id",

        # NUSA TENGGARA BARAT
        "http://lpse.bimakab.go.id",
        "http://www.lpse.dompukab.go.id",
        "http://lpse.lombokbaratkab.go.id",
        "https://www.lpse.lomboktengahkab.go.id",
        "http://lpse.lomboktimurkab.go.id",
        "http://lpse.lombokutarakab.go.id",
        "http://lpse.sumbawakab.go.id",
        "https://lpse.sumbawabaratkab.go.id",
        "http://lpse.bimakota.go.id",
        "http://103.206.245.248",
        "https://lpse.ntbprov.go.id",
        "http://lpse.ntb.polri.go.id",

        # NUSA TENGGARA TIMUR
        "http://www.lpse.alorkab.go.id",
        "http://lpse.belukab.go.id",
        "http://www.lpse.endekab.go.id",
        "http://lpse.florestimurkab.go.id",
        "http://lpse.kupangkab.go.id",
        "http://www.lpse.lembatakab.go.id",
        "http://180.250.181.178",
        "https://lpse.manggaraikab.go.id",
        "https://lpse.manggaraibaratkab.go.id",
        "http://www.lpse.manggaraitimurkab.go.id",
        "http://36.89.112.35",
        "http://lpse.ngadakab.go.id",
        "http://lpse.rotendaokab.go.id",
        "http://lpse.saburaijuakab.go.id",
        "http://lpse.sikkakab.go.id",
        "http://lpse.sumbabaratkab.go.id",
        "http://lpse.sbdkab.go.id",
        "http://lpse.sumbatengahkab.go.id",
        "http://www.lpse.sumbatimurkab.go.id",
        "http://lpse.ttskab.go.id",
        "http://www.lpse.ttukab.go.id",
        "http://lpse.kupangkota.go.id",
        "http://lpse.nttprov.go.id",
        "http://lpse.ntt.polri.go.id",

        # PAPUA
        "http://lpse.asmatkab.go.id",
        "http://lpse.biakkab.go.id",
        "http://lpse.dogiyaikab.go.id",
        "http://36.89.9.186",
        "http://lpse.jayapurakab.go.id",
        "http://lpse.jayawijayakab.go.id",
        "http://103.131.61.19",
        "http://lpse.kepyapenkab.go.id",
        "http://lpse.lannyjayakab.go.id",
        "http://lpse.mamberamotengahkab.go.id",
        "http://lpse.merauke.go.id",
        "http://lpse.mimikakab.go.id",
        "http://lpse.nabirekab.go.id",
        "http://36.94.6.212",
        "http://lpse.puncakkab.go.id",
        "https://lpse.puncakjayakab.go.id",
        "http://lpse.sarmikab.go.id",
        "http://lpse.supiorikab.go.id",
        "http://lpse.jayapurakota.go.id",
        "https://lpse.papua.go.id",
        "http://lpse.papua.polri.go.id",

        # PAPUA BARAT
        "http://lpse.fakfakkab.go.id",
        "http://lpse.kaimanakab.go.id",
        "http://lpse.manokwarikab.go.id",
        "http://lpse.maybratkab.go.id",
        "https://lpse.rajaampatkab.go.id",
        "http://lpse.sorongkab.go.id",
        "http://lpse.sorongselatankab.go.id",
        "http://lpse.telukbintunikab.go.id",
        "http://103.60.180.250",
        "https://lpse.sorongkota.go.id",
        "http://lelang.papuabaratprov.go.id",

        # RIAU
        "http://lpse.bengkaliskab.go.id",
        "http://lpse.inhilkab.go.id",
        "http://lpse.inhukab.go.id",
        "https://lpse.kamparkab.go.id",
        "http://lpse.merantikab.go.id",
        "http://lpse.kuansing.go.id",
        "http://lpse.pelalawankab.go.id",
        "https://lpse.rohilkab.go.id",
        "http://lpse.siakkab.go.id",
        "http://lpse.dumaikota.go.id",
        "http://www.lpse.pekanbaru.go.id",
        "http://lpse.riau.go.id",

        # SULAWESI BARAT
        "http://lpse.majenekab.go.id",
        "http://lpse.mamasakab.go.id",
        "http://lpse.mamujukab.go.id",
        "http://lpse.mamujutengahkab.go.id",
        "http://lpse.pasangkayukab.go.id",
        "http://lpse.polmankab.go.id",
        "http://lpse.sulbarprov.go.id",

        # SULAWESI SELATAN
        "http://lpse.bantaengkab.go.id",
        "http://lpse.barrukab.go.id",
        "http://lpse.bone.go.id",
        "http://lpse.bulukumbakab.go.id",
        "http://lpse.enrekangkab.go.id",
        "http://lpse.gowakab.go.id",
        "https://lpse.jenepontokab.go.id",
        "http://lpse.kepulauanselayarkab.go.id",
        "http://lpse.luwukab.go.id",
        "https://lpse.luwutimurkab.go.id",
        "http://lpse.luwuutarakab.go.id",
        "http://lpse.maroskab.go.id",
        "http://lpse.pangkepkab.go.id",
        "http://lpse.pinrangkab.go.id",
        "http://lpse.sidrapkab.go.id",
        "http://lpse.sinjaikab.go.id",
        "http://lpse.soppengkab.go.id",
        "http://lpse.takalarkab.go.id",
        "http://lpse.tanatorajakab.go.id",
        "http://lpse-wajokab.go.id",
        "https://lpse.makassar.go.id",
        "http://lpse.palopokota.go.id",
        "http://112.78.46.114",
        "https://lpse.sulselprov.go.id",

        # SULAWESI TENGAH 
        "http://www.lpse-torajautara.go.id",
        "http://lpse.bangkepkab.go.id",
        "http://lpse.banggailautkab.go.id",
        "http://lpse.buolkab.go.id",
        "http://lpse.donggala.go.id",
        "http://lpse.morowalikab.go.id",
        "http://lpse.morowaliutarakab.go.id",
        "http://lpse.parigimoutongkab.go.id",
        "http://lpse.posokab.go.id",
        "http://lpse.sigikab.go.id",
        "http://lpse.tojounaunakab.go.id",
        "http://27.50.16.54",
        "http://lpse.palukota.go.id",
        "http://lpse.sultraprov.go.id",
        "http://lpse.sulteng.polri.go.id",

        # SULEWESI TENGGARA
        "http://lpse.bombanakab.go.id",
        "http://lpse.butonkab.go.id",
        "http://lpse.butonselatankab.go.id",
        "http://www.lpse.butontengahkab.go.id",
        "http://lpse.butonutarakab.go.id",
        "http://lpse.kolakakab.go.id",
        "http://lpse.kolakatimurkab.go.id",
        "https://lpse.kolutkab.go.id",
        "http://103.85.61.253",
        "http://103.22.250.222",
        "http://lpse.konaweselatankab.go.id",
        "http://lpse.konaweutarakab.go.id",
        "http://lpse.munakab.go.id",
        "http://www.lpse.munakab.go.id",
        "http://lpse.wakatobikab.go.id",
        "http://lpse.baubaukota.go.id",
        "https://lpse.kendarikota.net",
        "http://lpse.sultengprov.go.id",

        # SULAWESI UTARA
        "http://lpse.bolmongkab.go.id",
        "http://lpse.bolselkab.go.id",
        "http://lpse.boltimkab.go.id",
        "http://180.250.123.107",
        "http://lpse.sangihekab.go.id",
        "http://lpse.sitarokab.go.id",
        "http://lpse.talaudkab.go.id",
        "http://www.lpse.minahasa.go.id",
        "http://lpse.minselkab.go.id",
        "http://www.lpse.mitrakab.go.id",
        "http://lpse.minutkab.go.id",
        "http://lpse.bitungkota.go.id",
        "https://lpse.kotamobagukota.go.id",
        "http://lpse.manadokota.go.id",
        "http://lpse.tomohon.go.id",
        "http://lpse.sulutprov.go.id",
        "http://lpse.sulut.polri.go.id",

        # SUMATERA BARAT
        "http://lpse.agamkab.go.id",
        "http://lpse.dharmasrayakab.go.id",
        "https://lpse.mentawaikab.go.id",
        "http://lpse.limapuluhkotakab.go.id",
        "http://lpse.padangpariamankab.go.id",
        "http://lpse.pasamankab.go.id",
        "http://lpse.pasamanbaratkab.go.id",
        "http://lpse.pesisirselatankab.go.id",
        "http://lpse.sijunjung.go.id",
        "http://lpse.solokkab.go.id",
        "http://www.lpse.solselkab.go.id",
        "http://lpse.tanahdatar.go.id",
        "http://www.lpse.bukittinggikota.go.id",
        "http://lpse.padang.go.id",
        "http://lpse.padangpanjang.go.id",
        "http://lpse.pariamankota.go.id",
        "http://www.lpse.payakumbuhkota.go.id",
        "http://lpse.sawahluntokota.go.id",
        "http://lpse.solokkota.go.id",
        "http://lpse.sumbarprov.go.id",
        "http://lpse.sumbar.polri.go.id",

        # SUMATERA SELATAN
        "http://lpse.banyuasinkab.go.id",
        "http://lpse.empatlawangkab.go.id",
        "http://lpse.lahatkab.go.id",
        "http://lpse.muaraenimkab.go.id",
        "http://lpse.mubakab.go.id",
        "http://lpse.musirawaskab.go.id",
        "http://www.lpse.muratarakab.go.id",
        "http://lpse.oganilirkab.go.id",
        "http://lpse.kaboki.go.id",
        "http://lpse.okukab.go.id",
        "http://lpse.okuselatankab.go.id",
        "http://lpse.okutimurkab.go.id",
        "http://lpse.palikab.go.id",
        "http://lpse.lubuklinggaukota.go.id",
        "http://lpse.pagaralamkota.go.id",
        "http://lpse.palembang.go.id",
        "http://lpse.kotaprabumulih.go.id",
        "http://lpse.sumselprov.go.id",
        "http://lpse.sumsel.polri.go.id",

        # SUMATERA UTARA
        "http://103.15.243.151",
        "http://lpse.batubarakab.go.id",
        "https://lpse.dairikab.go.id",
        "https://lpse.deliserdangkab.go.id",
        "https://lpse.humbanghasundutankab.go.id",
        "http://lpse.karokab.go.id",
        "http://lpse.labuhanbatukab.go.id",
        "http://lpse.labuhanbatuselatankab.go.id",
        "http://lpse.labura.go.id",
        "https://lpse.langkatkab.go.id",
        "http://www.lpse.madina.go.id",
        "http://lpse.niaskab.go.id",
        "http://lpse.niasbaratkab.go.id",
        "https://lpse.niasselatankab.go.id",
        "http://lpse.niasutarakab.go.id",
        "http://lpse.padanglawaskab.go.id",
        "http://lpse.padanglawasutarakab.go.id",
        "http://lpse.pakpakbharatkab.go.id",
        "http://lpse.samosirkab.go.id",
        "https://lpse.serdangbedagaikab.go.id",
        "https://lpse.simalungunkab.go.id",
        "http://lpse.tapselkab.go.id",
        "http://lpse.tapteng.go.id",
        "http://lpse.taputkab.go.id",
        "http://lpse.tobasamosirkab.go.id",
        "http://lpse.binjaikota.go.id",
        "https://lpse.gunungsitolikota.go.id",
        "http://lpse.pemkomedan.go.id",
        "http://lpse.padangsidimpuankota.go.id",
        "http://lpse.pematangsiantarkota.go.id",
        "http://lpse.sibolgakota.go.id",
        "http://lpse.tanjungbalaikota.go.id",
        "https://lpse.tebingtinggikota.go.id",
        "http://lpse.sumutprov.go.id",
        "http://lpse.sumut.polri.go.id",

        # TNI / POLRI
        "https://lpse.tniad.org",
        "http://lpse.tnial.mil.id",
        "http://110.138.137.229",
        "http://lpse.polri.go.id",

        # YOGYAKARTA
        "http://lpse.bantulkab.go.id",
        "http://lpse.gunungkidulkab.go.id",
        "http://lpse.kulonprogokab.go.id",
        "https://lpse.slemankab.go.id",
        "http://lpse.jogjakota.go.id",
        "https://lpse.jogjaprov.go.id",
        "http://lpse.jogja.polri.go.id"

    ]
    hasil = []
    for url in urls:
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
            tipe = ["Pengadaan_Barang","Jasa_Konsultansi_Badan_Usaha","Pekerjaan_Konstruksi","Jasa_Lainnya","Jasa_Konsultansi_Perorangan"]
            for t in tipe:
                barang = doc.find_all("tr", t)
                for target_list in barang:
                    nama = (target_list.find('a').get_text())
                    hps = (target_list.find('td','table-hps').get_text())
                    exp = (target_list.find('td','center').get_text())
                    scrap = {'lpse' : url,'nama_tender': nama, 'hps_tender': hps, 'tanggal_akhir': exp }
                    print(scrap)
                    hasil.append(scrap)
    data = {
        'code': 200,
        'status': 'success',
        'data': hasil
    }
    return data
if __name__ == "__main__":
    app.run(debug=True, port=8000)