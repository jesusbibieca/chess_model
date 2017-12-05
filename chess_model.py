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

class Piece(object):
	"""Initialize the basic attributes of a chess piece"""
	
	def __init__(self, color=None):
		self.captured = False
		self.color = color
		self.actual_pos = None
		self.valid_movements = None
		self.initial_pos = None
		# self.pieceCount = 1

class Pawn(Piece):
	def set_position(self, position):
		self.actual_pos = position

	def get_status(self):
		"""Returns the color, actual pos, if its been attacked"""
		try:
			if self.captured == False:
				return 'This pawn is ' + self.color + ' and Its actual position is ' + self.actual_pos
		except:
			return "The initial values have not been initialized yet."
	

class Queen(Piece):
	pass

p1 = Pawn('white')
p2 = Pawn('white')
p2.set_position("A2")
print p2.get_status()
