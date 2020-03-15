print ("SCRIPTER: <~special~><esmit> ")
print ("Telegram Id Scripter: @AA_hacker")
print ("Team = union_honker")
print ("Channel Team id: @Union_Honker")
print ("Thank You")
from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
def Search():
        f = open("admpage.txt","r");
        link = raw_input("URL Target: ")
        print "\n\nOUTPUT : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "FOUND! = ",req_link
def Desktop():
       Space(7);  print "[------- ADMIN PAGE FINDER -------]"
       Space(7);  print "[----------- onion_honker -----------]"
       Space(7);  print "[----------- Spcial_esmit -----------]"
Desktop()
Search()
