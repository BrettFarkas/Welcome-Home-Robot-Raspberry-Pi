import pygame
import random
import RPi.GPIO as GPIO
pygame.init()
pygame.mixer.init() 
import time

from datetime import datetime


#setup GPIO using Board numbering
GPIO.setmode(GPIO.BCM)

PIR_PIN = 13

# pin 6, Ground
# pin 14, Input
#

#GPIO.setup(15, GPIO.OUT)
#GPIO.output(15,True) #turn pin ON
GPIO.setup(PIR_PIN, GPIO.IN)




#GPIO.cleanup() #use this when exiting



playing = 0
i = 0
ib = 0
ih = 0
im = 0
ic = 0
ir = 0

random.seed()

Randlist = ["aaclub.ogg","aaholdmyhand.ogg","aalanded.ogg","aamelancholy.ogg","aanurseryrhyme.ogg","aarosemary.ogg",
"aawalls.ogg","aaovertherainbow.ogg","aatheweight.ogg","aawonderwall.ogg","aabuiltthiscity.ogg",
"aachaingang.ogg","aafeelagain.ogg","aahereigo.ogg","aastand.ogg","aaccrrain.ogg","aafastball.ogg","aakodachrome.ogg",
"aamemphis.ogg","aanorain.ogg","aaviva.ogg","aaboston.ogg","aadaydreambeliever.ogg","aaeverybodychanging.ogg","aalayla.ogg",
"aalumineers.ogg","aaphiladelphia.ogg","aapraiseyou.ogg","aasomewhereonly.ogg","aawalkoflife.ogg","aayougotit.ogg",
"aabuttercup.ogg", "aaherecomesmybaby.ogg", "aaherecomesthesun.ogg", "aashambala.ogg", "aashewas.ogg",
"aanoreservations.ogg", "aasoprano.ogg","aaworld.ogg", "aajump.ogg", "aafree.ogg","aasolsbury.ogg","aalongdecember.ogg","aaabc.ogg", "aacorner.ogg",
"aaeileen.ogg", "aahome.ogg", "aawantyouback.ogg","aarollingstone.ogg","aaneverletyougo.ogg", "aastarted.ogg",
"aaclearlynow.ogg","aarightnow.ogg","aasunshine.ogg","aajude.ogg","aahellogoodbye.ogg",
"aabluesky.ogg","aagardenparty.ogg","aaobladi.ogg","aaalright.ogg","aajessica.ogg","aafunk.ogg","aarunning.ogg","aabelieving.ogg","aaallstar.ogg","aalittlethings.ogg",
"aafloaton.ogg","aawhileyousee.ogg", "aamidnightrider.ogg","aaalabama.ogg","aadynamite.ogg","aarightback.ogg", "athirdwalk.ogg",
"aacrazy.ogg", "aamakingtime.ogg", "aamotleycrue.ogg", "aasupertramp.ogg", "aaeverydaypeople.ogg", "aacountryroad.ogg", "aaforeveryoung.ogg", "aashout.ogg",
"aafollowtheday.ogg","aabastille.ogg","aagotaname.ogg","aacaroline.ogg",
"aabojangles.ogg","aachild.ogg","aagirls.ogg","aathereshegoes.ogg"]

christmaslist = ["achristmasjinglerock.ogg", "achristmasletitsnow.ogg", "achristmasmostwonderful.ogg", "achristmasnutcracker.ogg", "achristmassleighride.ogg", "achristmaswinterwonderland.ogg", "achristmashomealone.ogg", "achristmasrockingaround.ogg", "achristmasdarlene.ogg"]

Byelist = ["raspbye1.ogg","raspbye2.ogg","raspbye3.ogg","raspbye4.ogg","raspbye5.ogg","raspbye6.ogg",
"raspbye7.ogg"]

Hellolist = ["raswelcome1.ogg","raswelcome2.ogg","raswelcome3.ogg","raswelcome4.ogg","raswelcome5.ogg"]

Morninglist = ["brm1.ogg", "brm2.ogg", "brm3.ogg", "brm4.ogg", "brm5.ogg", "brm6.ogg", "brm7.ogg", "brm9.ogg", "brm10.ogg", 
"brm11.ogg", "brm12.ogg"]

# the list of songs

Coldlist = ["brcold1.ogg", "brcold2.ogg", "brcold3.ogg", "brcold4.ogg", "brcold5.ogg", "brcold6.ogg", "brcold7.ogg"]

Rainlist = ["brrain1.ogg", "brrain2.ogg", "brrain3.ogg", "brrain4.ogg", "brrain5.ogg"]

Newlist = []
Newhellolist = []
Newbyelist = []
Newmorninglist = []
Newcoldlist = []
Newrainlist = []
Newchristmaslist = []

while len(Randlist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Randlist)
	Randlist.remove(variablerandom)
	Newlist.append(variablerandom)

while len(Hellolist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Hellolist)
	Hellolist.remove(variablerandom)
	Newhellolist.append(variablerandom)

while len(Byelist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Byelist)
	Byelist.remove(variablerandom)
	Newbyelist.append(variablerandom)

while len(Morninglist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Morninglist)
	Morninglist.remove(variablerandom)
	Newmorninglist.append(variablerandom)

while len(Coldlist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Coldlist)
	Coldlist.remove(variablerandom)
	Newcoldlist.append(variablerandom)

while len(Rainlist) >= 1:     #randomize the playlist
	variablerandom = random.choice(Rainlist)
	Rainlist.remove(variablerandom)
	Newrainlist.append(variablerandom)

while len(christmaslist) >= 1:     #randomize the playlist
	variablerandom = random.choice(christmaslist)
	christmaslist.remove(variablerandom)
	Newchristmaslist.append(variablerandom)


numvar = 0
GPIO.setwarnings(False)

now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second

playing = 0
firstwakeup = 0
alarmvariable = 0
afternoonoff = 0
nightturnoff = 0
weekendcounter = 0
c = 0

import urllib2
import json

def gettemp():
    """ call openweathermap api"""
    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?id=xxxxxxxxxxxxxxxxx') #put your city ID number at the end
    mydata = response.read()
    return mydata
 

##########################################################################
def tempmethod (temperature):
	song = "no value"
	if temperature >= 90:
		song = "br90.ogg"
	elif temperature >= 80:
		song = "br80.ogg"
	elif temperature >= 70:
		song = "br70.ogg"
	elif temperature >= 60:
		song = "br60.ogg"
	elif temperature >= 50:
		song = "br50.ogg"
	elif temperature >= 40:
		song = "br40.ogg"
	elif temperature >= 30:
		song = "br30.ogg"
	elif temperature >= 20:
		song = "br20.ogg"
	elif temperature >= 10:
		if temperature == 10:
			song = "br10.ogg"
		elif temperature == 11:
			song = "br11.ogg"
		elif temperature == 12:
			song = "br12.ogg"
		elif temperature == 13:
			song = "br13.ogg"
		elif temperature == 14:
			song = "br14.ogg"
		elif temperature == 15:
			song = "br15.ogg"
		elif temperature == 16:
			song = "br16.ogg"
		elif temperature == 17:
			song = "br17.ogg"
		elif temperature == 18:
			song = "br18.ogg"
		elif temperature == 19:
			song = "br19.ogg"

	if song != "no value":
		pygame.mixer.music.load(song) # load the song
		pygame.mixer.music.play() #play the song
		playing = 1
		while (playing == 1): #stay stuck in this loop until the song finishes
			playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing


	song = "no value"
	if temperature > 20:
		ones = temperature % 10
	else:
		ones = 100 #no value
	
	if ones == 9:
		song = "br9.ogg"
	elif ones == 8:
		song = "br8.ogg"
	elif ones == 7:
		song = "br7.ogg"
	elif ones == 6:
		song = "br6.ogg"
	elif ones == 5:
		song = "br5.ogg"
	elif ones == 4:
		song = "br4.ogg"
	elif ones == 3:
		song = "br3.ogg"
	elif ones == 2:
		song = "br2.ogg"
	elif ones == 1:
		song = "br1.ogg"
	elif ones == 0:
		pass

	if song != "no value":
		pygame.mixer.music.load(song) # load the song
		pygame.mixer.music.play() #play the song
		playing = 1
		while (playing == 1): #stay stuck in this loop until the song finishes
			playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing




while (1):
	




########################################
	now = datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second

	day = datetime.today().weekday()

	#0 = monday
	#1 = tuesday
	#2 = wednesday
	#3 = thursday
	#4 = friday
	#5 = saturday
	#6 = sunday

	calendarday = datetime.today().day
	month = datetime.today().month


	#RESET VARIABLES AT NIGHT
	if hour == 4 and firstwakeup == 1: 
		firstwakeup = 0
		afternoonoff = 0
		nightturnoff = 0
		weekendcounter = 0
##################################################################### Re-Randomizing the list 
	if i == len(Newlist): #reset i if it gets larger than the list
		i = 0
		
		Randlist = Newlist[:]#resetting things for re-randomization
		
		del Newlist[:]
		
		while len(Randlist) >= 1: #re-randomize if all songs have played	
			variablerandom = random.choice(Randlist)
			Newlist.append(variablerandom)
			Randlist.remove(variablerandom)
					
	

	if c == len(Newchristmaslist): #reset i if it gets larger than the list
		c = 0
		
		Randlist = Newchristmaslist[:]#resetting things for re-randomization
		
		del Newchristmaslist[:]
		
		while len(Randlist) >= 1: #re-randomize if all songs have played	
			variablerandom = random.choice(Randlist)
			Newchristmaslist.append(variablerandom)	
			Randlist.remove(variablerandom)
					
			

	if ih == len(Newhellolist): #reset i if it gets larger than the list
		ih = 0
		
		Hellolist = Newhellolist[:]#resetting things for re-randomization
		
		del Newhellolist[:]
		
		while len(Hellolist) >= 1: #re-randomize if all songs have played	
			hellorandom = random.choice(Hellolist)
			Newhellolist.append(hellorandom)
			Hellolist.remove(hellorandom)
						
			



	if ib == len(Newbyelist): #reset i if it gets larger than the list
		ib = 0
		
		Byelist = Newbyelist[:]#resetting things for re-randomization
		
		del Newbyelist[:]
		
		while len(Byelist) >= 1: #re-randomize if all songs have played	
			byerandom = random.choice(Byelist)
			Newbyelist.append(byerandom)
			Byelist.remove(byerandom)
						
			
	if im == len(Newmorninglist): #reset i if it gets larger than the list
		im = 0
		
		Morninglist = Newmorninglist[:]#resetting things for re-randomization
		
		del Newmorninglist[:]
		
		while len(Morninglist) >= 1: #re-randomize if all songs have played	
			morningrandom = random.choice(Morninglist)
			Newmorninglist.append(morningrandom)
			Morninglist.remove(morningrandom)
				
	
	if ic == len(Newcoldlist): #reset i if it gets larger than the list
		ic = 0
		
		Coldlist = Newcoldlist[:]#resetting things for re-randomization
		
		del Newcoldlist[:]
		
		while len(Coldlist) >= 1: #re-randomize if all songs have played	
			coldrandom = random.choice(Coldlist)
			Newcoldlist.append(coldrandom)
			Coldlist.remove(coldrandom)
				

	if ir == len(Newrainlist): #reset i if it gets larger than the list
		ir = 0
		
		Rainlist = Newrainlist[:]#resetting things for re-randomization
		
		del Newrainlist[:]
		
		while len(Rainlist) >= 1: #re-randomize if all songs have played	
			rainrandom = random.choice(Rainlist)
			Newrainlist.append(rainrandom)	
			Rainlist.remove(rainrandom)
			


#####################################################################
	#ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM ALARM 
	if hour == 7 and minute >= 10 and firstwakeup == 0 and day < 5:
		alarmvariable = 1
	
	if month == 12 and calendarday > 18 and hour < 10:
		alarmvariable = 0

#####################################################################
	if GPIO.input(PIR_PIN) == 1 or alarmvariable == 1: 
		alarmvariable = 0
		print ("Motion Activated")
		#GOOD MORNING GOOD MORNING GOOD MORNING GOOD MORNING

                
		if hour > 6 and hour < 11 and firstwakeup == 0 and playing == 0: 
                        firstwakeup = 1
			morningrandom = Newmorninglist[im] 
			im += 1 #increment the bye list
			pygame.mixer.music.load(morningrandom) # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
			firstwakeup == 1

			weather = gettemp()
			w = json.loads(weather)
			#print w['main']['temp'] #in kelvin
			temperature = float(w['main']['temp'])
			temperature = ((temperature - 273) * 1.8) + 32 #convert from kelvin to Farenheit
			#print ("Current Temp:")
			temperature = round(temperature)
			temperature =  int(temperature)

			pygame.mixer.music.load("brtemp1iscurrently.ogg") # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing

			tempmethod(temperature)

			#FORECAST
			def getforecast():
			    """ call openweathermap api"""
			    response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/forecast/daily?id=4196586&APPID=8d465a96dfe620a273abd9335abb417d') #put your city ID number at the end
			    mydata = response.read()
			    return mydata
 
			weather = getforecast()
			w = json.loads(weather)


			#HIGH 
			temperature = float(w['list'][1]['temp']['max'])
			temperature = ((temperature - 273) * 1.8) + 32
			#print ("Daily High: ")
			temperature = round(temperature)
			temperature =  int(temperature)

			pygame.mixer.music.load("brtemp2afternoon.ogg") # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
			
			if temperature < 45:
				coldrandom = Newcoldlist[ic] 
				ic += 1 #increment the bye list
				pygame.mixer.music.load(coldrandom) # load the song
				pygame.mixer.music.play() #play the song
				playing = 1
				while (playing == 1): #stay stuck in this loop until the song finishes
					playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing


			tempmethod(temperature) #call the method

			#LOW
			temperature = float(w['list'][1]['temp']['min'])
			temperature = ((temperature - 273) * 1.8) + 32
			#print ("Daily Low: ")
			temperature = round(temperature)
			temperature =  int(temperature)

			pygame.mixer.music.load("brtemp3tonight.ogg") # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing

			tempmethod(temperature) #call the method

			pygame.mixer.music.load("brtemp4degrees.ogg") # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing

			#rain or clear?
			todayforecast = w['list'][0]['weather'][0]['main']
			#print ("The weather is: ")
			#print todayforecast

			if todayforecast == 'Clear':
				pass
			if todayforecast == 'Rain':
				rainrandom = Newrainlist[ir] 
				ir += 1 #increment the bye list
				pygame.mixer.music.load(rainrandom) # load the song
				pygame.mixer.music.play() #play the song
				playing = 1
				while (playing == 1): #stay stuck in this loop until the song finishes
					playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing


			if todayforecast == 'Clouds':
				pass
			if todayforecast == 'Snow':
				pass


			#PLAY A SONG
                        playing = 1
			variablerandom = Newlist[i]
			i += 1

			#christmas version		
			if month == 12 and calendarday < 26:
				variablerandom = Newchristmaslist[c]
				c += 1

			pygame.mixer.music.load(variablerandom) # load the song
			pygame.mixer.music.play() #play the song

			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing


		#AFTER FIRST WAKE UP DATA WEEKDAYS 
		elif hour > 6 and hour < 11 and firstwakeup == 1 and playing == 0 and day < 5: 
			byerandom = Newbyelist[ib] 
			ib += 1 #increment the bye list




			pygame.mixer.music.load(byerandom) # load the song
			pygame.mixer.music.play() #play the song
			playing = 1
			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
			#PLAY A SONG
                        playing = 1
			variablerandom = Newlist[i]
			i += 1

			#christmas version		
			if month == 12 and calendarday < 26:
				variablerandom = Newchristmaslist[c]
				c += 1


			pygame.mixer.music.load(variablerandom) # load the song
			pygame.mixer.music.play() #play the song

			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing

		#AFTER FIRST WAKE UP DATA WEEKDAYS WEEKEND 
		#elif hour > 5 and hour < 12 and firstwakeup == 1 and playing == 0 and day >= 5 and weekendcounter < 1:
		#	weekendcounter += 1 
		#	byerandom = Newlist[ib] 
		#	ib += 1 #increment the bye list
		#	pygame.mixer.music.load(byerandom) # load the song
		#	pygame.mixer.music.play() #play the song
		#	playing = 1
		#	while (playing == 1): #stay stuck in this loop until the song finishes
		#		playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
			#PLAY A SONG
                 #       playing = 1
		#	variablerandom = Newlist[i]
		#	i += 1
		#	pygame.mixer.music.load(variablerandom) # load the song
		#	pygame.mixer.music.play() #play the song

		#	while (playing == 1): #stay stuck in this loop until the song finishes
		#		playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing


#12 
#13 1
#14 2
#15 3
#16 4
#17 5
#18 6 
#19 7
#20 8
#21 9
#22 10
#23 11
###########################################################################################################
		# HELLO WELCOME HOME AFTERNOON AND NIGHT
		if (hour >= 15 and playing == 0 and day < 5 and afternoonoff == 0) or (hour >= 23 and playing == 0 and day <= 4 and nightturnoff == 0):

			if hour == 23:
				nightturnoff = 1
		#if after 3:00 weekday or after 11:00 mon-thurs
			afternoonoff = 1
                        playing = 1
			if hour < 22:
				print ("Hello Activated")
				hellorandom = Newhellolist[ih] 
				ih += 1 #increment the hello list
				#SAY WELCOME HOME
				pygame.mixer.music.load(hellorandom) # load the song
				pygame.mixer.music.play() #play the song

				while (playing == 1): #stay stuck in this loop until the song finishes
					playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
			#PLAY A SONG
                        playing = 1
			variablerandom = Newlist[i]
			i += 1

			#christmasversion
			if month == 12 and calendarday < 26:
				variablerandom = Newchristmaslist[c]
				c += 1


			pygame.mixer.music.load(variablerandom) # load the song
			pygame.mixer.music.play() #play the song

			while (playing == 1): #stay stuck in this loop until the song finishes
				playing = pygame.mixer.music.get_busy() #returns a 1 while music is playing
		
		
		
#time.sleep(1)	

#	pygame.mixer.music.stop()
#	pygame.mixer.music.load("aasoul.ogg")
#	pygame.mixer.music.play()
#	pygame.event.wait()





#set_volume(value)       THE VALUE IS BETWEEN 0 AND 1.0
