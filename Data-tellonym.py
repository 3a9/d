import requests
import json
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"
print ("""


                 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁

⠀⠀⠀⠀🈵⠀There is no limit to this tool now 🈵⠀    

    ++ The developer : Falah - 0xfff080 ++ v4.0

            snapchat : flaah999

---------------------------------------
""")


url = "https://api.tellonym.me/tokens/create"
# Login API URL

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Accept-Language": "en",
	} 
# Login API Headers

email = input("Username/Email: ") 
# Email Or Username Input
password = input("Password: ") 
# Password Input

data = {
	"activeExperimentId": 0,
	"password": password,
	"country": "US",
	"deviceName": "Soud’s iPhone",
	"deviceType": "ios",
	"lang": "en",
	"limit": 16,
	"email": email
}
# Login API Data

req = requests.post(url, json=data, headers=headers)
# Login API Request

if "WRONG_CREDENTIALS" in req.text:
	print("Login Failed, Try Again")
	# Wrong Login Info

elif "PARAMETER_MISSING" in req.text:
	print("Missing Something, Try Again")
	# Missing Data

elif "accessToken" in req.text:
	print("Login Success")
	token = json.loads(req.text)["accessToken"]
	# Login Success And Parse Login Token

else:
	print("Error !")
	print(req)
	print(req.text)
	exit()
	# Error or Something Wrong

url = "https://api.tellonym.me/accounts/myself?adExpId=80&limit=16"

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Authorization": f"Bearer {token}",
	"Accept-Language": "en",
	} 
# Scrape API Headers

req = requests.get(url, headers=headers)
# Scrape API Request

scrape = json.loads(req.text)
# Parsing Json Data

user_id = scrape["id"]
email = scrape["email"]
display_name = scrape["displayName"]
username = scrape["username"]
account_type = scrape["type"]
account_lang = scrape["lang"]
account_location = scrape["location"]
twitter_username = scrape["twitterUsername"]
instagram_username = scrape["instagramUsername"]
account_creat = scrape["createdAt"]
account_bio = scrape["aboutMe"]
account_avatar = scrape["avatarFileName"]
account_avatar_url = "https://userimg.tellonym.me/xs/"+account_avatar
account_searchable = scrape["isSearchable"]
account_lastactiveat = scrape["lastActiveAt"]
account_likes = scrape["likesCount"]
account_followers = scrape["followerCount"]
account_anonfollowers = scrape["anonymousFollowerCount"]
account_following = scrape["followingCount"]
account_tell = scrape["tellCount"]
account_answer = scrape["answerCount"]
account_verified = scrape["isVerified"]
# Account Info Scrape

print(f"""
ID: {user_id}
Email: {email} 
Name: {display_name}
Username: {username}
Type: {account_type}
Language: {account_lang}
Location: {account_location}
Twitter: {twitter_username}
Instagram: {instagram_username}
Created At: {account_creat}
Bio: {account_bio}
Avatar: {account_avatar}
Avatar URL: {account_avatar_url}
Searchable: {account_searchable}
Last Active At: {account_lastactiveat}
Likes: {account_likes}
Followers: {account_followers}
Anon Followers: {account_anonfollowers}
Following: {account_following}
Tell: {account_tell}
Answers: {account_answer}
Verified: {account_verified}
""")

print("""

جلب الحسابات المسجله في سجل الهاتف مع الاسم

""")

iz = int(input(red_color+"How many followers do you want from phone history? : "))
url = "https://api.tellonym.me/suggestions/contacts?adExpId=92&limit=31"
# Scrape API URL

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Authorization": f"Bearer {token}",
	"Accept-Language": "en",
	} 
# Scrape API Headers

req = requests.get(url, headers=headers)
# Scrape API Request

scrape = json.loads(req.text)

for i in range (iz+0):
   

   print(end_banner_color+"________________________________")
   try:
      print(green_color+"aboutMe : " + scrape["contactsSuggestions"][i]["aboutMe"])
   except:
      print (red_color+"aboutMe : false")
   try:
      print(green_color+"username : " + scrape["contactsSuggestions"][i]["username"])
   except:
      print (red_color+"username : false")
   try:
      print(green_color+"cbName : " + scrape["contactsSuggestions"][i]["cbName"])
   except:
      print (red_color+"cbName : false")
   try:
      print(green_color+"instagramLink : " + scrape["contactsSuggestions"][i]["instagramLink"])
   except:
      print (red_color+"instagramLink : false")
   try:
      print(green_color+"twitterLink : " + scrape["contactsSuggestions"][i]["twitterLink"])
   except:
      print (red_color+"twitterLink : false")
   try:
      print(green_color+"snapchatLink : " + scrape["contactsSuggestions"][i]["snapchatLink"])
   except:
      print (red_color+"snapchatLink : false")
      

print(end_banner_color+"""

: ادخل احداثيات الموقع لجلب الحسابات مثال 

latitude -> 24.786182 
longitude -> 46.675641

https://www.google.com.sa/maps : تستخرج الاحداثيات من 

""")

ss = input ('latitude -> ')
ss1 = input ('longitude -> ')

url = "https://api.tellonym.me/suggestions/people?latitude="+ss+"&longitude="+ss1+"&adExpId=94&limit=31"

headers = {
	"Host": "api.tellonym.me",
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Connection": "keep-alive",
	"tellonym-client": "ios:2.65.0:488:14:iPhone13,3",
	"User-Agent": "Tellonym/488 CFNetwork/1206 Darwin/20.1.0",
	"Authorization": f"Bearer {token}",
	"Accept-Language": "en",
	} 
	
response = requests.get(url, headers=headers).text
info = json.loads(response)


for i in range(94):

  if 'peopleSuggestions' in response:
            try:
                print(red_color+"---------------------------------------")
                print(green_color +" --> Name : "+str(info["peopleSuggestions"][i]["displayName"]))
                print(green_color +" --> username : "+str(info["peopleSuggestions"][i]["username"]))
                print(green_color +" --> aboutMe : "+str(info["peopleSuggestions"][i]["aboutMe"]))
            except:
                print ("---E----N----D")
                exit()
