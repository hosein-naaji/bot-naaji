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
print("Good luck buddy{'👨🏻‍💻'}")
print(f"{yellow} ")

print("""    Subscribe to the channel --> : @heruyny""")
#hosein-naaji
print(f"{green} ")
bot = Bot(input("Please enter your ((Auth))🥶:"))
target=input("Please Enter Your Guid ((Group)): ")
print("𝚁𝙾𝙱𝙰𝚃 𝚁𝙰𝙽 𝚂𝙷𝙾𝙳👨🏻‍💻")

while True:
	
	time.sleep(120)
	x = get("https://api.codebazan.ir/jok/").text
	cp = f"کانال جوک ما \n @kerbazi"
	jok = f"{x}  \n {cp} \n "
	bot.sendMessage("GUID", jok)
	print('sended')
