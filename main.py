import pytumblr
import sys
from random import randint
import time


# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'XYkT1UZu6zgriJrd1jj9TUkLdMFpOWbIXGgt8efXKZzGlCbvCl',
  'CkPibQLz8kOkAKOI4wXdG4TYTAwIpLjdv41Ng5fIzdsVhzaVMc',
  'jgS74UqvYLUf4MNoNUcOPig70sOvluHXJGUyhEtmGboQoZn4wN',
  '9cxhZgDJasO4HdV7gbix4eR41NvtKyCIsksiYHEFKsUcc5nQ4c'
)


while 1 == 1:
	# Verb #

	vrb = randint(1, 21)							# Generiert eine Zahl zwischen 1 und 21 und sucht sich
	pfad = "words/Verb/" + str(vrb) + ".txt"		# Dann die Textdatei Dazu raus

	verb = open(pfad, "r").read()

	# Adjektiv #

	adj = randint(1, 13)								# Generiert eine Zahl zwischen 1 und 5 und sucht sich
	pfad = "words/Adjektiv/" + str(adj) + ".txt" 	# Dann die Textdatei Dazu raus

	adjektiv = open(pfad, "r").read()

	# Objekt #

	obj = randint(1, 20)							# Generiert eine Zahl zwischen 1 und 20 und sucht sich
	pfad = "words/Objekt/" + str(obj) + ".txt" 		# Dann die Textdatei Dazu raus

	objekt = open(pfad, "r").read()

	satz = "Ich"+verb+adjektiv+objekt

	#Creating a text post
	client.create_text("marvin-robot", state="published", slug="", title="", body=satz)
	time.sleep(120) # delays for 120 seconds