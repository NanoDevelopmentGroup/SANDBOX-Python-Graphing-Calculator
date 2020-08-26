import ply.lex as lex
import ply.yacc as yacc


# TO DO
# Please see Parser

# ---------------------------------------------------------

# Lexer


# List all potential tokens

tokens = [

    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'LPAREN',
    'RPAREN'

]

# Define all tokens for arithemetic operators

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# defince the token to ignore spaces 

t_ignore = r' '

# Verfies if token is a float

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Verifies if token is an integer

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Verifies if token is a variable    

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

# Pulls an error and describes what character pulls the error

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Initialize lexer

lexer = lex.lex()

# ------------------------------------------------------------------------

 # Create Parser

# To Do
# Implement LPAREN AND RPAREN in parser, currently basic arithmetic 
# and variable assignement is available.
# Remove the None that appears when variable is assigned a value.


# Give precedence to operators

precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')


)

# Evaluate the expression 

def p_calc(p): 
    '''
    calc : expression
        | empty
        | var_assign
    '''
    print(run(p[1]))

# Evaluate variable assignment

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''

    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression PLUS expression
                | expression DIVIDE expression
                | expression MULTIPLY expression
                | expression MINUS expression
    '''
    p[0] = (p[2] , p[1] , p[3])

# Define int or float expression

def p_expression_int_float(p):
    '''
    expression : INT
                | FLOAT
    '''
    p[0] = p[1]

# Define variable expression

def p_expression_var(p):
    '''
    expression : NAME
    '''

    p[0] = ('var', p[1])

# Defne error 

def p_error(p):
    print('Syntax error found in the input!')


# Define empty value

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None



parser = yacc.yacc()
env = {}

# Define run function to evaluate the arithmatic 

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return ("Undeclared Variable %s" % p[1])
            else:
                return env[p[1]]
    else:
        return p

# Recieve input from user

while True:
    try:
        s = input('Input expression here:')
    except EOFError: # when u press contorl D on keyboard
        break
    parser.parse(s)