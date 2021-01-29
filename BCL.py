		#####Disables#####
#pylint:disable=W0702
#pylint:disable=W0621
#pylint:disable=R1716
#pylint:disable=W0123

		#####Imports#####
import langlib as pll
from SMS_Bomber import main as SB
from requests import get
from datetime import datetime
from re import findall
from json import loads
from time import sleep
from random import randint
import os
  	##Shortcut Methods##
def reset():
	return pll.style("","white")

def api(url):
	try:
		return get(url).text
	except :
		return "failed to connection".center(43)

	##Read Long Texts from datas.txt##
path = 'datas.txt'
file = str(open(path).read()).split("_")
text = [i.strip() for i in file]


					###Body###
print(pll.style(text[0],"lgreen"),"\n")
command = input(">>> ").strip()
DB = []

while command != "exit":
	DB.append(command)
	
	if command == '?':
		print('\n'+text[1]+'\n')
	
	
	elif command == 'calc':
		print('=',str(eval(input('<<< result of: '))).center(40))
	
	
	elif command == 'jok':
		print(api('http://api.codebazan.ir/jok/'))
	
	
	elif command == 'time':
		print(datetime.now())
	
	
	elif command == 'password':
		length = input("<<< Enter Length for Password: ")
		print(api('http://api.codebazan.ir/password/?length='+length))
	
	
	elif command == 'api':
		print(api(input('<<< Enter URL: ')))
	
	
	elif command == 'search':
		print(pll.wiki(input("<<< search for: ")))


	elif command == 'trans':
		text = input("<<< translate: ")
		origin = input("<<< from: ")
		destination = input("<<< to: ")
		if text == "search":
			title = pll.wiki(input("<<< search for: "))
			print(pll.translate(title,origin,destination))
		else:
			print(pll.translate(text,origin,destination))
	
		
	elif command == 'abb':
		print(pll.abbreviation(input("<<< abbrevation: ")))
	
	
	elif command == 'bmi':
		height = int(input("<<< my height: "))
		weight = int(input("<<< my weight: "))
		BMI = (weight/(height*height))*10000
		print("BMI:",BMI)
		if BMI <= 18.5:
			print(pll.style('Low!','lyellow'),reset())
		elif BMI >= 18.5 and BMI <= 24.9:
			print(pll.style('Normal','dgreen'),reset())
		elif BMI >= 24.9 and BMI <= 29.9:
			print(pll.style('Up!','lpink'),reset())
		else:
			print(pll.style('Very Fat!!!','dred'),reset())
	
				
	elif command == "weather":
		print(loads(api("https://api.codebazan.ir/weather/?city="+input("<<< city: ")))["result"]["دما"])
	
	
	elif command == "finglish":
		print(loads(api("https://api.codebazan.ir/fintofa/?text="+input("<<< Finglish Text: ")))["result"])
	
		
	elif command == "events":
		events = loads(api("https://api.codebazan.ir/monasebat/"))
		for i in events:
			print(i["occasion"],"\n")
	
		
	elif command == "currency":
		currencys = loads(api("https://api.codebazan.ir/arz/?type=arz"))
		for currency in currencys:
			print(currency.get("name"),"\n",currency.get("price"),"\n\n")
	
	
	elif command == "font":
		fonts = loads(api("http://api.codebazan.ir/font/?text="+input("<<< Text: ")))["result"]
		for i in range(1,139):
			print(fonts.get(str(i)))
			sleep(0.01)
	
	
	elif command == "knowable":
		print(api("http://api.codebazan.ir/danestani/"))
	
			
	elif command == "whois":
		information = loads(api("http://api.codebazan.ir/whois/index.php?type=json&domain="+input("<<< which site? ")))
		Keys = list(information.keys())
		Values = list(information.values())
		for key,value in zip(Keys,Values):
			print("    •%s = %s "%(key,value))
	
	
	elif command == "info":
		information = loads(api("https://api.codebazan.ir/ipinfo/?ip="+input("<<< ip: ")))
		for key,value in zip(list(information.keys()),list(information.values())):
			print("    •%s = %s "%(key,value))
	
	
	elif command == "keys":
		keys = findall('\[\w*\]',file[1])
		for key in keys:
			print("\t•"+pll.style(key,"cyan"),reset(),end='\n')
	
	
	elif command == "fishing":
		print(loads(api("https://api.codebazan.ir/fishinfo/index.php?link="+input("<<< url (protocol + url): ")))["results"])


	elif command == "corona":
		info = loads(api("https://api.codebazan.ir/corona/?type=country&country="+input("<<< country: ")))["result"]
		for key,value in zip(list(info.keys()),list(info.values())):
			print("    - %s : %s "%(key,value))
	
	
	elif command == "EPG":
		count = int(input("<<< How many programs? "))
		EPG = loads(api("https://api.codebazan.ir/tv/?type="+input("<<< whice one? (tv1): ")))["Result"][count]
		print("   +",count,"th program:")
		for key,value in zip(list(EPG.keys()),list(EPG.values())):
			print("   - %s : %s"%(key,value))


	elif command == "fakemail":
		print(loads(api("https://api.codebazan.ir/fakemail/?a=newmail"))["result"]["mail"].center(40))
	
	
	elif command == "num2word":
		print(loads(api("https://api.codebazan.ir/num/?num="+input("<<< num: ")))["result"]["num"].center(40))
	
		
	elif command == "short":
		from pyshorteners import Shortener as sh
		print(">>>", sh().tinyurl.short(input("\n<<< URL: ")),"\n")
	
	
	elif command == "length":
		print(api("https://api.codebazan.ir/distance/index.php?mabda="+input("<<< from: ")+"&maghsad="+input("<<< to: ")))
	
		
	elif command == "conundrum":
		quess = loads(api("https://api.codebazan.ir/chistan/"))
		rand = randint(1,139)
		print("Question : "+quess.get("Result")[rand].get("soal"),"\n\n","Answer : "+quess.get("Result")[rand].get("javab"))
	
	
	elif command == "meaning":
		print(loads(api("https://api.codebazan.ir/vajehyab/?text="+input("<<< word: ")))['result']['mani'])

	
	elif command == "prime":
		num = int(input("<<< num: "))
		if num < 2: print("Not Exist")
		elif num == 2: print("just 2")
		else:
			primNum=[2]
			for i in range(3,num):
				for j in primNum:
					if i%j==0:break
					else:
						if not i in primNum:
							primNum.append(i)
			print(primNum)
	
	
	elif command == "last":
		print(DB[-2])
	
	
	elif command == "first":
		print(DB[0])
	
	
	elif command == "all":
		print(DB)
	
	
	elif command == "smsB":
		SB(c=int(input("count : ")), num=input("Enter phone number : "))

		
	elif command == "TTS":
		text = input("<<< what to say? ")
		
		if text == "search":
			pll.TTS(pll.wiki(input("<<< search for: ")),False,"/storage/emulated/0/Music/TTS_Files/"+input("<<< file name: ")+".mp3")
								
		else:
			pll.TTS(text,False,"/storage/emulated/0/Music/TTS_Files/"+input("<<< file name: ")+".mp3")
	
	
	elif command == "open":
		path = "/storage/emulated/0/"+input("from: ")
		print(open(path,"rb").read())
	
		
	elif command == "download":
		from pySmartDL import SmartDL	
		url = input("url: ")
		path = "/storage/emulated/0"+input("path (after root): ")
		obj = SmartDL(url, path)
		obj.start()
		obj.get_dest()
	
		
	elif command == "SendMail":
		import ssl, smtplib
		port = 465
		email = input("<<< Enter your email: ")
		password = input("<<< Enter your password: ")
		recipient = input("<<< send for: ")
		subject = input("<<< With subject: ")
		text = input("<<< Type your text here: ")
		message = "Subject: {}\n\n{}".format(subject, text)
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
			server.login(email,password)
			server.sendmail(email, recipient,message)
		print(">>> Successful <<<")
	
	
	elif command == "reverse":
		print(pll.reverse(input("<<< reverse: ")))
	
	
	elif command == "delete":
		TYPE = input("<<< dir or file? ").lower()
		if TYPE == "dir":
			os.rmdir(input("<<< path: "))
		else:
			path = input("<<< file: ")
			if os.path.exists(path):
				os.remove(path)
			else:
				print("The file does not exist")
	
	
	elif command == "clean":
		sleep(1)
		os.system("clear")
		sleep(1)
		print(pll.style(text[0],"lgreen"),"\n")


	elif command == "runpy":
		os.system("python -i")


	elif command == "terminal":
		BashCommand = input(">> ")
		while BashCommand != "exit":
			os.system(BashCommand)
			BashCommand = input(">> ")
		
	else:
		if command != "":
			print(pll.style('UndefindError: Command Not Found','lred'))
			print(reset(),end='')
	command = input(">>> ")
