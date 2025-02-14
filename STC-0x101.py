import sys
import requests
import json
import time
import urllib





G , R = "\033[1;32m" , "\033[1;31m"
print(R+"""
________________________________________________
  / ____|__   __/ ____|     / _ \    /_ |/ _ \_ |
 | (___    | | | |   ______| | | |_  __ | | | | |
  \___ \   | | | |  |______| | | \ \/ / | | | | |
  ____) |  | | | |____     | |_| |>  <| | |_| | |
 |_____/   |_|  \_____|     \___//_/\_\_|\___/|_|
 _______________________________________________|
	""")
class config:
	key = "4a1ede76e87d9e64682b284e8620ad68"
	number = sys.argv[1] 
	kod = "SA"

  # https://numverify.com/

		

with urllib.request.urlopen ("http://146.148.112.105/caller/index.php/UserManagement/search_number?number="+  config.number +"&country_code="+ config.kod +"") as url:
		data = json.loads ( url.read ( ).decode ( ) )
print ( data )
def main():
	if len(sys.argv) == 2:
		number = sys.argv[1]
		API = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=966" + number + "&country_code=&format=1"
		output = requests.get(API)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print ("[+] " + "معلومات رقم الهاتف")
		print ("--------------------------------------")
		time.sleep(0.2)
		if country_code == "":
			print (" - [ " + "فشل " + "] الحصول على اسم البلد")
		else:
			print (" - الحصول على البلد [ " + "نعم " + "]")
	
		time.sleep(0.2)
		if country_name == "":
			print (" - اسم الدوله [ " + "فشل " + "]")
		else:
			print (" - الحصول على اسم الدوله [ " + "نعم " + "]")

		time.sleep(0.2)
		if location == "":
			print (" - الموقع [ " + "فشل " + "]")
		else:
			print (" - الحصول على الموقع [ " + "نعم " + "]")

		time.sleep(0.2)
		if carrier == None:
			print (" - الحصول على الخدمه [ " + "فشل " + "]")
		else:
			print (" - الحصول على الخدمه [ " + "نعم " + "]")

		time.sleep(0.2)
		if line_type == None:
			print (" -   نوع الحهاز [ " + "فشل " + "]")
		else:
			print (" - الحصول على نوع الجهاز [ " + "نعم " + "]")

		print ("")
		print ("[+] " + "ترتيب البيانات")
		print("+==================================+")
		print (" [+] رقم الهاتف: " + str(number))
		print("====================================")
		print (" [+] الدولة: " + str(carrier ))
		print("====================================")
		print (" [+] اسم الدوله: " + str(country_name))
		print("=====================================")
		print (" [-] الموقع: " + str(location))
		print("=====================================")
		print (" [+] الناقل: " + str(carrier))
		print("=====================================")
		print (" [+] نوع الجهاز: " + str(line_type))
		print("+===================================+")
	else:
		print ("[+] Usage:")
		print ("	./%s < ضروري رمز الدوله لأي رقم >" % (sys.argv[0]))
		print ("	./%s +966555555555" % (sys.argv[0]))

def Erorr():
	try:
		main()
	except str():
		if '"Error":catching classes that do not inherit from BaseException is not allowed' in Erorr():
			print('استخدم ارقام من فضلك')
Erorr()





