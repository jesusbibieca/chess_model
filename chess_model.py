'''    Hola!
	He aqui tu proyecto:
	Desarrollar la logica de dos ficha (Reina y Peon) del juego de ajedrez
	Se me olvido aclararte lo sgte:
	Investiga sobre en que consiste el juego, te vas a basar lo aprendido en el 
	curso programacion enfocado a objeto, no tienes que enfocarte en grafico ni 
	nada parecido solo a nivel de logica .
	
	Cualquier pregunta puedes contactar a Ismael 
	Tienes 1 mes para entregar el proyecto 

    Suerte!
'''
from random import choice

class Piece(object):
	"""Initialize the basic attributes of a chess piece"""
	
	def __init__(self, color=None):
		self.captured = False
		self.color = color
		self.actual_pos = None
		self.valid_movements = None
		self.initial_pos = None
		# self.pieceCount = 1
			
	def get_color(self):
		return self.color

	def get_status(self):
		"""Returns the color, actual pos. (expect to add also if it is been attacked)"""
		try:
			if self.captured == False:
				return 'This piece is ' + self.color + " and It's actual position is " + self.actual_pos
			elif self.captured == True:
				return "Piece was captured already."
		except:
			return "The initial values have not been initialized yet."

	def set_initial_position(self, position):
		self.initial_pos = position
		if self.actual_pos == None:
			self.actual_pos = position

	def move(self, where):
		self.actual_pos = where

	def get_position(self):
		return self.actual_pos

class Pawn(Piece):
	def __str__(self):
		return "This is a Pawn's instance."

	def promotion(self):
		self.captured = True
		return "This pawn got promoted to a better piece."

	def available_moves(self):
		current = self.get_position()
		availability = []
		temp = int(current[1])
		if self.get_color() == 'white' and current == self.initial_pos:
			availability.append(current[0] + str(temp + 1))
			availability.append(current[0] + str(temp + 2))
		elif self.get_color() == 'white' and current != self.initial_pos:
			availability.append(current[0] + str(temp + 1))
		elif self.get_color() == 'black' and current == self.initial_pos:
			availability.append(current[0] + str(temp - 1))
			availability.append(current[0] + str(temp - 2))
		else:
			availability.append(current[0] + str(temp - 1))
		return availability
			
class Queen(Piece):
	def __str__(self):
		return "This is a Queen's instance."

	def available_moves(self, chess):
		pass
	
	def index_2d(self, myList, target):
		for i, x in enumerate(myList):
			if target in x:
				return (i, x.index(target))

	def rook():
	    chess = Board().get_board()
	    position = 'a8'
	    result = []
	    result = [x for each in chess if position in each for x in each 
	              if x not in result and x != position]
	    
	    tar1 = position[0]
	    for each in chess:
	        for x in each:
	            if tar1 in x and x != position:
	                result.append(x)
   
    return result

    def magicBishop(array, x_init, y_init):
	    pass

	def bishop():#ok so far
	    # result = rook()
	    result = []
	    actual_pos = 'e4' #set the actual_pos
	    x_init, y_init = index_2d(chess, actual_pos) # set the indexes of the actual_pos
	    magicBishop(result, x_init, y_init)

	    return result	

class Board(object):
	def __init__(self):
		self.color_board = [['BW'[(i + j + 8 % 2 + 1) % 2] for i in range(8)] for j in range(8)]
		self.notation_board = []
		# board = []
		temp = []
		for x in '87654321':
		    for y in 'abcdefgh':
		        temp.append(y + x)
		    self.notation_board.append(temp)	
		    temp = []

	def get_board(self, type=""):
		if type == "color":	return self.color_board
		return self.notation_board

chess = Board().get_board()
position_setter = choice(chess[1])
position_setter = "b2"


#testing pawns
# p1 = Pawn('black')
# p2 = Pawn('white')
# p1.set_initial_position(position_setter)
# print p1.get_position()
# new_move = raw_input("Move the pawn ")
# p1.move(new_move)
# print p1.get_position()
# print p1.available_moves()

#testing queen
q1 = Queen('black')
print q1.get_color()
if q1.get_color() == 'white':
	q1.set_initial_position('d1')
else:
	q1.set_initial_position('d8')


print q1.get_position()
# new_move = raw_input("Move the Queen ")
q1.move(position_setter)
print q1.available_moves()

