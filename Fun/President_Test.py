#Import
import os
#Set window size and get rid of Script Terminal Auto-Prints
os.system('clear')
raw_input("type anything to start: ")
os.system('clear')
#Setting Defaults
R_points = 18
A_points = 30
O_points = 0
J_points = 5
V_points = 14
alist = [A_points, "Alexander"]
olist = [O_points, "Olivia"]
vlist = [V_points, "Vince"]
rlist = [R_points, "Rebecca"]
jlist = [J_points, "Jonathan"]
while True:
	#Special Effects
	print "President Quiz 4.4.1(2017 Standard Edition)"
	print "By Alexander Greco"
	print "Sponsored by BusinessRate"
	print "      $$$$$$$$$"
	print "      $$o$o$$$$"
	print "      $$$L$$$$$"
	print "      $$___$$$$"
	print "      $$$$$$$$$"
	print " $$       $$"
	print " $$       $$"
	print " $$       $$"
	print " $$$$$$$$$$$$$$$$$$$$"
	print "          $$       $$"
	print "          $$       $$"
	print "          $$       $$"
	print "          $$"
	print "         $$$$           $$$$$"
	print "        $$  $$          $$"
	print "       $$    $$        $$"
	print "      $$      $$$$$$$$$$"
	print "     $$"
	print "    $$"
	print "   $$"
	print "$$$$$"
	#Lets the user read status or take the test
	menu = raw_input("What do you want to do? (Take the test, Study, Repitition or Read the leaderboard)")
	#If the user would like to test themself
	if menu == "Take the test":
		name = raw_input("Please enter your name: ")
		#Tests the individuals separately so they can have there own scores
		if name == "Olivia":
			while True:
				ifUserStart = raw_input("Are you ready? ")
				if ifUserStart == "yes":
					break
				if ifUserStart == "Yes":
					break
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			percent1 = float(points)/45.0
			percent2 = int((percent1 * 100)+0.5)
			print str(percent2) + "%"
			if points >= 40:
				print "A+"
				print "You are a Genius, or maybe just a cheater."
			elif points >= 35:
				print "A"
				print "You are a Super Star, or did you have a peek for a few?"
			elif points >= 30:
				print "B+"
				print "Awesome Job! You beat the Creater!"
			elif points >= 25:
				print "B"
				print "Great Job!"
			elif points >= 20:
				print "C+"
				print "You did pretty well!"
			elif points >= 15:
				print "C"
				print "You are starting to get the hang of this!"
			elif points >= 10:
				print "D+"
				print "Slightly Smarter than the average American"
			elif points >= 5:
				print "D"
				print "You are an average American, try studying who the leaders of your own country were instead of watching TV!"
			elif points >= 0:
				print "F"
				print "What are you, a rock?"
			raw_input("Press anything to continue: ")
			if O_points < points:
				O_points = points
		if name == "Jonathan":
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes":
					break
				if ggez== "Yes":
					break
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			percent1 = float(points)/45.0
			percent2 = int((percent1 * 100)+0.5)
			print str(percent2) + "%"
			if points >= 40:
				print "A+"
				print "You are a Genius, or maybe just a cheater."
			elif points >= 35:
				print "A"
				print "You are a Super Star, or did you have a peek for a few?"
			elif points >= 30:
				print "B+"
				print "Awesome Job! You beat the Creater!"
			elif points >= 25:
				print "B"
				print "Great Job!"
			elif points >= 20:
				print "C+"
				print "You did pretty well!"
			elif points >= 15:
				print "C"
				print "You are starting to get the hang of this!"
			elif points >= 10:
				print "D+"
				print "Slightly Smarter than the average American"
			elif points >= 5:
				print "D"
				print "You are an average American, try studying who the leaders of your own country were instead of watchnig TV!"
			elif points >= 0:
				print "F"
				print "What are you, a rock?"
			raw_input("Press anything to continue: ")
			if J_points < points:
				 J_points = points
		if name == "Vince":
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes":
					break
				if ggez== "Yes":
					break
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			percent1 = float(points)/45.0
			percent2 = int((percent1 * 100)+0.5)
			print str(percent2) + "%"
			if points >= 40:
				print "A+"
				print "You are a Genius, or maybe just a cheater."
			elif points >= 35:
				print "A"
				print "You are a Super Star, or did you have a peek for a few?"
			elif points >= 30:
				print "B+"
				print "Awesome Job! You beat the Creater!"
			elif points >= 25:
				print "B"
				print "Great Job!"
			elif points >= 20:
				print "C+"
				print "You did pretty well!"
			elif points >= 15:
				print "C"
				print "You are starting to get the hang of this!"
			elif points >= 10:
				print "D+"
				print "Slightly Smarter than the average American"
			elif points >= 5:
				print "D"
				print "You are an average American, try studying who the leaders of your own country were instead of watching TV!"
			elif points >= 0:
				print "F"
				print "What are you, a rock?"
			raw_input("Press anything to continue: ")
			if V_points < points:
				V_points = points
		if name == "Rebecca":
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes":
					break
				if ggez== "Yes":
					break
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			percent1 = float(points)/45.0
			percent2 = int((percent1 * 100)+0.5)
			print str(percent2) + "%"
			if points >= 40:
				print "A+"
				print "You are a Genius, or maybe just a cheater."
			elif points >= 35:
				print "A"
				print "You are a Super Star, or did you have a peek for a few?"
			elif points >= 30:
				print "B+"
				print "Awesome Job! You beat the Creater!"
			elif points >= 25:
				print "B"
				print "Great Job!"
			elif points >= 20:
				print "C+"
				print "You did pretty well!"
			elif points >= 15:
				print "C"
				print "You are starting to get the hang of this!"
			elif points >= 10:
				print "D+"
				print "Slightly Smarter than the average American"
			elif points >= 5:
				print "D"
				print "You are an average American, try studying who the leaders of your own country were instead of watching TV!"
			elif points >= 0:
				print "F"
				print "What are you, a rock?"
			raw_input("Press anything to continue: ")
			if R_points < points:
				R_points = points
		if name == "Alexander":
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes":
					break
				if ggez== "Yes":
					break
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			percent1 = float(points)/45.0
			percent2 = int((percent1 * 100)+0.5)
			print str(percent2) + "%"
			if points >= 40:
				print "A+"
				print "You are a Genius, or maybe just a cheater."
			elif points >= 35:
				print "A"
				print "You are a Super Star, or did you have a peek for a few?"
			elif points >= 30:
				print "B+"
				print "Awesome Job! You beat the Creater!!"
			elif points >= 25:
				print "B"
				print "Great Job!"
			elif points >= 20:
				print "C+"
				print "You did pretty well!"
			elif points >= 15:
				print "C"
				print "You are starting to get the hang of this!"
			elif points >= 10:
				print "D+"
				print "Slightly Smarter than the average American"
			elif points >= 5:
				print "D"
				print "You are an average American, try studying who the leaders of your own country were instaed of watching TV!"
			elif points >= 0:
				print "F"
				print "What are you, a rock?"
			raw_input("Press anything to continue: ")
			if A_points < points:
				 A_points = points
	if menu == "Repetition":
		if 1==1:
			while True:
				ggez = raw_input("Are you ready? ")
				if ggez == "yes":
					break
				if ggez== "Yes":
					break
			points = 0
			while True:
				QA = raw_input("Who is the 45th President? ")
				if QA == "Donald Trump":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 44th President? ")
				if QA == "Barack Obama":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 43rd President? ")
				if QA == "George Bush":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 42nd President? ")
				if QA == "Bill Clinton":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 41st President? ")
				if QA == "George Bush":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 40th President? ")
				if 	QA == "Ronald Reagan":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 39th President? ")
				if QA == "Jimmy Carter":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 38th President? ")
				if QA == "Gerald Ford":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 37th President? ")
				if QA == "Richard Nixon":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 36th President? ")
				if QA == "Lyndon Johnson":
					points = points + 1
					print "Correct!"
					break

			while True:
				QA = raw_input("Who is the 35th President? ")
				if QA == "John Kennedy":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 34th President? ")
				if QA == "Dwight Eisenhower":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 33th President? ")

				if QA == "Harry Truman":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 32nd President? ")
				if 	QA == "Franklin Roosevelt":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 31st President? ")
				if 	QA == "Herbert Hoover":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 30th President? ")
				if 	QA == "Calvin Coolidge":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 29th President? ")
				if 	QA == "Warren Harding":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 28th President? ")
				if 	QA == "Woodrow Wilson":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 27th President? ")
				if 	QA == "William Taft":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 26th President? ")
				if 	QA == "Theodore Roosevelt":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 25th President? ")
				if 	QA == "William McKinley":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 24th President? ")
				if 	QA == "Grover Cleveland":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 23th President? ")
				if 	QA == "Benjamin Harrison":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 22nd President? ")
				if 	QA == "Grover Cleveland":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 21st President? ")
				if 	QA == "Chester Arthur":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 20th President? ")
				if 	QA == "James Garfield":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 19th President? ")
				if 	QA == "Ruthford Hayes":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 18th President? ")
				if 	QA == "Ulysses Grant":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 17th President? ")
				if 	QA == "Andrew Johnson":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 16th President? ")
				if 	QA == "Abraham Lincoln":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 15th President? ")
				if 	QA == "James Buchanan":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 14th President? ")
				if 	QA == "Franklin Pierce":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 13th President? ")
				if 	QA == "Millard Fillmore":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 12th President? ")
				if 	QA == "Zachary Taylor":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 11th President? ")
				if 	QA == "James Polk":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 10th President? ")
				if 	QA == "John Tyler":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 9th President? ")
				if 	QA == "William Harrison":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 8th President? ")
				if 	QA == "Martin Van Buren":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 7th President? ")
				if 	QA == "Andrew Jackson":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 6th President? ")
				if 	QA == "John Adams":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 5th President? ")
				if 	QA == "James Monroe":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 4th President? ")
				if 	QA == "James Madison":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 3rd President? ")
				if 	QA == "Thomas Jefferson":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 2nd President? ")
				if 	QA == "John Adams":
					points = points + 1
					print "Correct!"
					break
			while True:
				QA = raw_input("Who is the 1st President? ")
				if 	QA == "George Washington":
					points = points + 1
					print "Correct!"
					break
	if menu == "Study":
		while True:
			ggez = raw_input("Are you ready? ")
			if ggez == "yes":
				target = raw_input("What is your Goal?(How many presidents you would like to get correct in this session) ")
				try:
					int(target)
					break
				except ValueError:
					print "Scammer"
			if ggez== "Yes":
				target = raw_input("What is your Goal?(How many presidents you would like to get correct in this session) ")
				if target.isint():
					break
		while True:
			points = 0
			QA = raw_input("Who is the 45th President? ")
			if QA == "Donald Trump":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Donald Trump"
			QA = raw_input("Who is the 44th President? ")
			if QA == "Barack Obama":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Barack Obama"
			QA = raw_input("Who is the 43rd President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 42nd President? ")
			if QA == "Bill Clinton":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Bill Clinton"
			QA = raw_input("Who is the 41st President? ")
			if QA == "George Bush":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Bush"
			QA = raw_input("Who is the 40th President? ")
			if 	QA == "Ronald Reagan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ronald Reagan"
			QA = raw_input("Who is the 39th President? ")
			if 	QA == "Jimmy Carter":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Jimmy Carter"
			QA = raw_input("Who is the 38th President? ")
			if 	QA == "Gerald Ford":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Gerald Ford"
			QA = raw_input("Who is the 37th President? ")
			if 	QA == "Richard Nixon":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Richard Nixon"
			QA = raw_input("Who is the 36th President? ")
			if 	QA == "Lyndon Johnson":
				points = points + 1
				print "Correct!"
				print "Lyndon Johnson"
			else:
				print "WRONG!!!"
				print "Lyndon Johnson"
			QA = raw_input("Who is the 35th President? ")
			if 	QA == "John Kennedy":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Kennedy"
			QA = raw_input("Who is the 34th President? ")
			if 	QA == "Dwight Eisenhower":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Dwight Eisenhower"
			QA = raw_input("Who is the 33th President? ")
			if 	QA == "Harry Truman":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Harry Truman"
			QA = raw_input("Who is the 32nd President? ")
			if 	QA == "Franklin Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Roosevelt"
			QA = raw_input("Who is the 31st President? ")
			if 	QA == "Herbert Hoover":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Herbert Hoover"
			QA = raw_input("Who is the 30th President? ")
			if 	QA == "Calvin Coolidge":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Calvin Coolidge"
			QA = raw_input("Who is the 29th President? ")
			if 	QA == "Warren Harding":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Warren Harding"
			QA = raw_input("Who is the 28th President? ")
			if 	QA == "Woodrow Wilson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Woodrow Wilson"
			QA = raw_input("Who is the 27th President? ")
			if 	QA == "William Taft":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Taft"
			QA = raw_input("Who is the 26th President? ")
			if 	QA == "Theodore Roosevelt":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Theodore Roosevelt"
			QA = raw_input("Who is the 25th President? ")
			if 	QA == "William McKinley":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William McKinley"
			QA = raw_input("Who is the 24th President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 23th President? ")
			if 	QA == "Benjamin Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Benjamin Harrison"
			QA = raw_input("Who is the 22nd President? ")
			if 	QA == "Grover Cleveland":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Grover Cleveland"
			QA = raw_input("Who is the 21st President? ")
			if 	QA == "Chester Arthur":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Chester Arthur"
			QA = raw_input("Who is the 20th President? ")
			if 	QA == "James Garfield":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Garfield"
			QA = raw_input("Who is the 19th President? ")
			if 	QA == "Ruthford Hayes":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ruthford Hayes"
			QA = raw_input("Who is the 18th President? ")
			if 	QA == "Ulysses Grant":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Ulysses Grant"
			QA = raw_input("Who is the 17th President? ")
			if 	QA == "Andrew Johnson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Johnson"
			QA = raw_input("Who is the 16th President? ")
			if 	QA == "Abraham Lincoln":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Abraham Lincoln"
			QA = raw_input("Who is the 15th President? ")
			if 	QA == "James Buchanan":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Buchanan"
			QA = raw_input("Who is the 14th President? ")
			if 	QA == "Franklin Pierce":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Franklin Pierce"
			QA = raw_input("Who is the 13th President? ")
			if 	QA == "Millard Fillmore":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Millard Fillmore"
			QA = raw_input("Who is the 12th President? ")
			if 	QA == "Zachary Taylor":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Zachary Taylor"
			QA = raw_input("Who is the 11th President? ")
			if 	QA == "James Polk":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Polk"
			QA = raw_input("Who is the 10th President? ")
			if 	QA == "John Tyler":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Tyler"
			QA = raw_input("Who is the 9th President? ")
			if 	QA == "William Harrison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "William Harrison"
			QA = raw_input("Who is the 8th President? ")
			if 	QA == "Martin Van Buren":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Martin Van Buren"
			QA = raw_input("Who is the 7th President? ")
			if 	QA == "Andrew Jackson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Andrew Jackson"
			QA = raw_input("Who is the 6th President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 5th President? ")
			if 	QA == "James Monroe":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Monroe"
			QA = raw_input("Who is the 4th President? ")
			if 	QA == "James Madison":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "James Madison"
			QA = raw_input("Who is the 3rd President? ")
			if 	QA == "Thomas Jefferson":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "Thomas Jefferson"
			QA = raw_input("Who is the 2nd President? ")
			if 	QA == "John Adams":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "John Adams"
			QA = raw_input("Who is the 1st President? ")
			if 	QA == "George Washington":
				points = points + 1
				print "Correct!"
			else:
				print "WRONG!!!"
				print "George Washington"
			print str(points) + "/45"
			if int(target) > points:
				raw_input("Try Again :(")
			else:
				print "Success!!!"
				break
		raw_input("Press anything to continue: ")
	if menu == "Read the leaderboard": #Set the stats
		alist = [A_points, "Alexander"]
		olist = [O_points, "Olivia"]
		vlist = [V_points, "Vince"]
		rlist = [R_points, "Rebecca"]
		jlist = [J_points, "Jonathan"]
		#Combine the stats
		leaderboard = [alist,
		olist,
		jlist, vlist,
		 rlist]
		#Order the stats
		leaderboard2 = sorted(leaderboard)
		#Print out the stats([-*] goes backwards in the stats because it is in asending order)
		print "1. "
		print leaderboard2[-1]
		print "2. "
		print leaderboard2[-2]
		print "3. "
		print leaderboard2[-3]
		print "4. "
		print leaderboard2[-4]
		print "5. "
		print leaderboard2[-5]
		#Moves on when user is ready
		raw_input("Press anything to continue: ")
