from requests import get
from re import findall
from rubika_lib.lib import Bot
import time
green='\033[32m'
red='\033[31m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'
yellow='\033[33m'
print(f"{blue} ")
print("Good luck buddy{'π¨π»βπ»'}")
print(f"{yellow} ")

print("""    Subscribe to the channel --> : @heruyny""")
#hosein-naaji
print(f"{green} ")
bot = Bot(input("Please enter your ((Auth))π₯Ά:"))
target=input("Please Enter Your Guid ((Group)): ")
print("ππΎπ±π°π ππ°π½ ππ·πΎπ³π¨π»βπ»")

while True:
	
	time.sleep(120)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f"Ϊ©Ψ§ΩΨ§Ω Ψ¬ΩΪ© ΩΨ§ \n @kerbazi"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("GUID", jok)
	print('sended')
