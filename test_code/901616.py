import sys
while True:
	for i in range(3):
		game = raw_input()
		if game == "0":sys.exit()
		game = game[1:]+game[-1]
		print game.count("A"),game.count("B")