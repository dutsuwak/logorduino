import ply.lex as lex

#lista de TOKENS
#Estas son todas las palabras que el lenguaje va a tener
tokens = (

	# Palabras reservadas, estas deberiamos de verificarlas y convertirlas en reservadas
	'AVANZA',
    'AV',
	'RETROCEDE',
    'RE',
	'GIRAIZQUIERDA',
    'GI',
	'GIRADERECHA',
    'GD',
	'REPITE',
	'PARA',
    'PONPOS',
    'PONRUMBO',
    'CENTRO',
    'SUBELAPIZ',
    'BAJALAPIZ',
    'FIN',
    'SI',


	# Simbolos
	###De aqui muchos no se necesitan, los podemos quitar cuendo estemos seguros
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'LESS',
	'LESSEQUAL',
	'GREATER',
	'GREATEREQUAL',
	'EQUAL',
	'DEQUAL',
	'DISTINT',
	'SEMICOLON',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LBLOCK',
	'RBLOCK',
	'DOUPOINT',
	'ID', ## Nombre de funciones "CUADRO, TRIANGULO"
	'NUMBER',##Atributos
)
#Aqui todos llevan t_**** porque lex reconoce el t_,   son r'*' porque son raw
# Expresiones Regulare simples
t_PLUS 	 = r'\+'
t_MINUS	 = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESS 	 = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA	 = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_DOUPOINT = r':'

##Aqui tenemos que poner las reservadas porque en t_ID se verifica que sea reservada o no
reserved = {
'avanza' : 'AVANZA',
'av':'AV',
'retrocede' : 'RETROCEDE',
're': 'RE',
'giraderecha' : 'GIRADERECHA',
'gd': 'GD',
'giraizquierda' : 'GIRAIZQUIERDA',
'gi': 'GI',
'repite' : 'REPITE',
'para' : 'PARA',
'ponpos' : 'PONPOS',
'ponrumbo' : 'PONRUMBO',
'centro' : 'CENTRO',
'subelapiz' : 'SUBELAPIZ',
'bajalapiz' : 'BAJALAPIZ',
'fin' : 'FIN',
'si' : 'SI'

}

##Aca se asignan las mas complejas

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_ID(t):
	r'\w+(_\d\w)*'
	t.type = reserved.get(t.value,'ID')    # Check for reserved words
	return t


def t_AVANZA(t):
	r'avanza'
	return t
def t_AV(t):
	r'av'
	return t

def t_RETROCEDE(t):
    r'retrocede'
    return t
def t_RE(t):
    r're'
    return t

def t_GIRAIZQUIERDA(t):
    r'giraizquierda'
    return t
def t_GI(t):
    r'gi'
    return t

def t_GIRADERECHA(t):
    r'giraderecha'
    return t
def t_GD(t):
    r'gd'
    return t

def t_REPITE(t):
    r'repite'
    return t

def t_PARA(t):
    r'para'
    return t

def t_PONPOS(t):
    r'ponpos'
    return t

def t_PONRUMBO(t):
    r'ponrumbo'
    return t

def t_CENTRO(t):
    r'centro'
    return t

def t_SUBELAPIZ(t):
    r'subelapiz'
    return t

def t_BAJALAPIZ(t):
    r'bajalapiz'
    return t

def t_FIN(t):
    r'fin'
    return t

def t_SI(t):
    r'si'
    return t




def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
	print "Lexical error: " + str(t.value[0])
	t.lexer.skip(1)




def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print tok

lexer = lex.lex()

# Test
if __name__ == '__main__':

	# Test
	data = '''avanza  90
	          giraizquierda 90
	          av 30
	          gi 90
	          para cuadro 90
	          centro 80
	          '''

	# Build lexer and try on
	lexer.input(data)
	test(data, lexer)
