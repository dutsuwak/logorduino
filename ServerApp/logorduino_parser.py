

import logorduino_lexer
import sys

import ply.yacc as yacc


# Get the token map from the lexer.  This is required.
from logorduino_lexer import tokens

num = 0

def p_program(p):
	'program : expression'
	p[0] = p[1]


def p_expression_PARA_1(p):
    'expression :  PARA ID DOUPOINT term expression FIN'
    global num
    num = p[4]
    p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3]) + " " + str(p[4]) + " " + str(p[5])+ "" + str(p[6])

def p_expression_PARA_2(p):
    'expression :  PARA ID expression FIN'
    p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3]) + "" + str(p[4])


def p_expression_AVANZA_1(p):
    'expression : AVANZA DOUPOINT ID expression'
    global num
    # print(p[1])
    p[0] = str(p[1]) + " " + str(p[2] + num) + " " + str(p[3])


def p_expression_AVANZA_2(p):

    'expression : AVANZA term expression'
    global num
    #print(p[1])
    p[0] = str(p[1]) +" "+ str(p[2] + num )+ " "+str(p[3])

def p_expression_RETROCEDE(p):
    'expression :  RETROCEDE term expression '
    p[0] = str(p[1]) + " " + str(p[2])+" "+str(p[3])


def p_expression_GIRADERECHA(p):
    'expression :  GIRADERECHA term expression '
    p[0] = str(p[1])+ " "+str(p[2])+ " "+str(p[3])

def p_expression_GIRAIZQUIERDA(p):
    'expression :  GIRAIZQUIERDA term expression '
    p[0] = str(p[1]) + " " +str(p[2])+ " "+str(p[3])


def p_expression_REPITE(p):
    'expression :  REPITE term LBRACKET expression RBRACKET '
    p[0] = str(p[1]) + " " +str(p[2])+ " " +str(p[3])+ " " +str(p[4])+ "" +str(p[5])

def p_expression_PONPOS(p):
    'expression :  PONPOS LBRACKET term term RBRACKET'
    p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3]) + " " + str(p[4]) + " " + str(p[5])


def p_expression_PONRUMBO(p):
    '''expression : PONRUMBO MINUS term
                  | PONRUMBO term'''
    if p[2] == '-':
        p[0] = str(p[1]) + " " + str(360 - p[3])
    else:
        p[0] = str(p[1]) + " " + str(p[2])

def p_expression_CENTRO(p):
    'expression :  CENTRO '
    p[0] = str(p[1]) + " " +str(p[2])


def p_expression_empty(p):
    'expression : '
    p[0] = ""

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

#def p_expression_term(p):
##    'expression : term'
#    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print ("Syntax error in input!")

# Build the parser
yacc.yacc()


# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")

#while 1:
#   try:
#       s = input()
#   except EOFError:
#       break
#   if not s: continue
#   result = yacc.parse(s)
#   print (result)

