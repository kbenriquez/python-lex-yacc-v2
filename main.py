# Kyle Marcus Enriquez
#
# This program uses PLY to read tokens as operators.
# This program takes as input a text file with user inputs similar to code.
# User inputs must always be enclosed in brackets (in a block).

import math

# ALL THE CLASSES
class Node:
    def __init__(self):
        print("init node")
    def evaluate(self):
        return 0
    def execute(self):
        return 0
class BlockNode(Node):
    def __init__(self, v):
        self.value = v
    def execute(self):
        self.value.execute()
class SmtListNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def execute(self):
        if self.v1 != None:
            self.v1.execute()
            self.v1.evaluate()
        if self.v2 != None:
            self.v2.execute()
            self.v2.evaluate()
class IfNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def execute(self):
        if self.v1.evaluate():
            self.v2.execute()
class IfElseNode(Node):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
    def execute(self):
        if self.v1.evaluate():
            self.v2.execute()
        else:
            self.v3.execute()
class WhileNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def execute(self):
        if self.v1.evaluate():
            self.v2.execute()
            WhileNode(self.v1, self.v2)
class NumberNode(Node):
    def __init__(self, v):
        if ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)
    def evaluate(self):
        return self.value
class StringNode(Node):
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return self.value
class ListNode(Node):
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return self.value
class ListGetNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1.evaluate()
        self.v2 = v2.evaluate()
    def evaluate(self):
        self.value = self.v1[self.v2]
        return self.value
class PrintNode(Node):
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        self.value = self.value.evaluate()
        print(self.value)
class AssignNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def evaluate(self):
        self.v1 = self.v1
        self.v2 = self.v2.evaluate()
        names[self.v1] = self.v2
class NameNode(Node):
    def __init__(self, v):
        self.value = v
    def evaluate(self):
        return names[self.value]
class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op
    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == '%'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '//'):
            return math.floor(self.v1.evaluate() / self.v2.evaluate())
        elif (self.op == '**'):
            return math.pow(self.v1.evaluate(), self.v2.evaluate())
        elif (self.op == '>'):
            if self.v1.evaluate() > self.v2.evaluate() == True:
                return 1
            else:
                return 0
        elif (self.op == '>='):
            if self.v1.evaluate() >= self.v2.evaluate():
                return 1
            else:
                return 0
        elif (self.op == '=='):
            if self.v1.evaluate() == self.v2.evaluate():
                return 1
            else:
                return 0
        elif (self.op == '<>'):
            if self.v1.evaluate() != self.v2.evaluate():
                return 1
            else:
                return 0
        elif (self.op == '<'):
            if self.v1.evaluate() < self.v2.evaluate():
                return 1
            else:
                return 0
        elif (self.op == '<='):
            if self.v1.evaluate() <= self.v2.evaluate():
                return 1
            else:
                return 0
        elif (self.op == 'and'):
            if self.v1.evaluate() and self.v2.evaluate() != 0:
                return 1
            else:
                return 0
        elif (self.op == 'or'):
            if self.v1.evaluate() or self.v2.evaluate() != 0:
                return 1
            else:
                return 0
        elif (self.op == 'not'):
            return not self.v1.evaluate()
        elif (self.op == 'in'):
            return self.v1.evaluate() in self.v2.evaluate()
class BooleanNotNode(Node):
    def __init__(self, op, v1):
        self.v1 = v1
        self.op = op
    def evaluate(self):
        if (self.op == 'not'):
            if not self.v1.evaluate() == True:
                return 1
            elif not self.v1.evaluate() == False:
                return 0

# Tokens list
tokens = (
    'PRINT', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY',
    'NUMBER', 'STRING', 'NAME', 'EQUALS',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'FDIVIDE', 'EXPONENT',
    'LT', 'LTE', 'IE','INE', 'GT', 'GTE',
    'AND', 'OR', 'NOT', 'IN', 'ID', 'IF', 'ELSE', 'WHILE',
    'COMMA', 'SEMICOLON'
)

# Reserved keywords
reserved = {
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'in': 'IN',
    'print': 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

# Tokens definition
t_NAME = r'[A-Za-z][A-Za-z0-9_]*'
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'
t_FDIVIDE = r'//'
t_EXPONENT = r'\*\*'
t_LT = r'<'
t_LTE = r'<='
t_IE = r'=='
t_INE = r'<>'
t_GT = r'>'
t_GTE = r'>='

# Parsing rules
precedence = (
    ('right', 'EQUALS'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'GT', 'GTE', 'IE', 'INE', 'LT', 'LTE'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FDIVIDE'),
    ('right', 'EXPONENT'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE')
)

#dictionary of names
names = {}

#ALL THE DEF Ts
def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        print("----------  ", t.value)
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t
def t_STRING(t):
    r'\".[^"]*\"'
    t.value = t.value.replace("\"", "")
    #t.value = "\'" + t.value + "\'"
    t.value = StringNode(str(t.value))
    return t
def t_ID(t):
    r'and|or|not|in|print|if|else|while'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Syntax error at '%s'" % t.value)

# Build the lexer
import ply.lex as lex
lex.lex()

#ALL THE DEF Ps
def p_block_smt(t):
    'block : LCURLY smtList RCURLY'
    t[0] = BlockNode(t[2])
def p_if_else_smt(t):
    '''
    if_else_smt : IF LPAREN expression RPAREN block ELSE block
    '''
    t[0] = IfElseNode(t[3], t[5], t[7])
def p_if_smt(t):
    '''
    if_smt : IF LPAREN expression RPAREN block
    '''
    t[0] = IfNode(t[3],t[5])
def p_while_smt(t):
    '''
    while_smt : WHILE LPAREN expression RPAREN block
    '''
    t[0] = WhileNode(t[3], t[5])
def p_smt_list(t):
    'smtList : smt smtList'
    t[0] = SmtListNode(t[1], t[2])
def p_smt_smt(t):
    'smtList : smt'
    t[0] = SmtListNode(t[1], None)
def p_expression_expression(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]
def p_print_smt(t):
    """
    smt : PRINT LPAREN expression RPAREN SEMICOLON
    """
    t[0] = PrintNode(t[3])
def p_assign(t):
    '''
    smt : NAME EQUALS expression SEMICOLON
    '''
    t[0] = AssignNode(t[1], t[3])
def p_expression_name(t):
    'expression : NAME'
    t[0] = NameNode(t[1])
def p_factor_name(t):
    'factor : NAME'
    t[0] = NameNode(t[1])
def p_list_name(t):
    'list : NAME'
    t[0] = NameNode(t[1])
def p_smt_if_smt(t):
    'smt : if_smt'
    t[0] = t[1]
def p_smt_if_else_smt(t):
    'smt : if_else_smt'
    t[0] = t[1]
def p_smt_while_smt(t):
    'smt : while_smt'
    t[0] = t[1]
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression FDIVIDE expression
                  | expression EXPONENT expression
                  | expression LT expression
                  | expression LTE expression
                  | expression IE expression
                  | expression INE expression
                  | expression GT expression
                  | expression GTE expression
                  | expression AND expression
                  | expression OR expression
                  | expression IN word
                  | expression IN list
                  | NOT expression'''
    if t[1] == 'not':
        t[0] = BooleanNotNode(t[1], t[2])
    else:
        t[0] = BopNode(t[2], t[1], t[3])
def p_word_binop(t):
    '''expression : word PLUS word'''
    t[0] = BopNode(t[2], t[1], t[3])
def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]
def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]
def p_expression_string(t):
    '''expression : word'''
    t[0] = t[1]
def p_word_string(t):
    'word : STRING'
    t[0] = t[1]
def p_list(t):
    'list : LBRACKET content RBRACKET'
    t[0] = ListNode(t[2])
def p_list_content(t):
    'content : expression'
    t[0] = [t[1].evaluate()]
def p_list_repeat(t):
    'content : expression COMMA content'
    t[0] = [t[1].evaluate()] + t[3]
def p_list_get(t):
    '''expression : list LBRACKET NUMBER RBRACKET
                  | word LBRACKET NUMBER RBRACKET'''
    t[0] = ListGetNode(t[1],t[3])
def p_expression_list(t):
    'expression : list'
    t[0] = t[1]
def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc

yacc.yacc()

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""

for line in fd:
    code += line.strip()

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
    ast = yacc.parse(code)
    ast.execute()
except Exception:
    print("ERROR")
