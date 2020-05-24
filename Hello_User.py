import os
import time
record = {
    "morning" : 'CreateObject("SAPI.SpVoice").Speak "Good morning ',
    "afternoon" : 'CreateObject("SAPI.SpVoice").Speak "Good Afternoon ',
    "evening" : 'CreateObject("SAPI.SpVoice").Speak "Good Evening ',
    "night" : 'CreateObject("SAPI.SpVoice").Speak "Why working late night . You shuld take a sleep" '
}
name = ' '
def create():
    os.chdir( 'c:\\' )
    os.mkdir("audio")
    my_name = open("audio/name.txt","w")
    name = input("Enter your name : ")
    my_name.write(name)
    my_name.close()
    f_one = open("audio/morning.vbs","w")
    f_two = open("audio/afternoon.vbs","w")
    f_three = open("audio/evening.vbs","w")
    f_four = open("audio/night.vbs","w")
    name += '"'
    f_one.write(record["morning"] + name)
    f_two.write(record["afternoon"] + name)
    f_three.write(record["evening"] + name)
    f_four.write(name + record["night"])
    os.chdir( 'c:\\audio' )
    f_one.close()
    f_two.close()
    f_three.close()
    f_four.close()

cur = time.localtime()
cur = cur.tm_hour
os.chdir( 'c:\\' )
check = os.path.isdir("audio")
if check == True:
    my_name = open("audio/name.txt","r")
    if cur >= 6 and cur < 12:
          os.chdir( 'c:\\audio' )
          os.system("morning.vbs")

    elif cur >= 12 and cur< 17:
          os.chdir( 'c:\\audio' )
          os.system("afternoon.vbs" )

    elif cur >= 17 and cur < 24:
         os.chdir( 'c:\\audio' )
         os.system("evening.vbs" )
    
    else:
         os.chdir( 'c:\\audio' )
         os.system("night.vbs")

else:
        create()
        os.system("cls")
        print("""Thanks for given your name in our database.\n
        "'Rick' will tell you Hello whenever you open the computer.""")
        os.system("pause")