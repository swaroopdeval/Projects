
import sys
import ply.lex as lex
reserved =( 
  # Reserved words
    'ABSTRACT', 'ALIAS', 'ALIGN', 'ASM', 'ASSERT', 'AUTO', 'BODY', 'BOOL', 'BREAK', 'BYTE',
     'CASE', 'CAST', 'CATCH', 'CDOUBLE', 'CENT', 'CFLOAT', 'CHAR', 'CLASS', 'CONST', 'CONTINUE',
      'CREAL', 'DCHAR', 'DEBUG', 'DEFAULT', 'DELEGATE', 'DELETE', 'DEPRECATED', 'DO', 'DOUBLE', 'ELSE',
       'ENUM', 'EXPORT', 'EXTERN', 'FALSE', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'FOREACH', 'FOREACH_REVERSE', 
       'FUNCTION', 'GOTO', 'IDOUBLE', 'IF', 'IFLOAT', 'IMMUTABLE', 'IMPORT', 'IN', 'INOUT', 'INT', 'INTERFACE', 
       'INVARIANT', 'IREAL', 'IS', 'LAZY', 'LONG', 'MACRO', 'MIXIN', 'MODULE', 'NEW', 'NOTHROW', 'NULL', 'OUT',
        'OVERRIDE', 'PACKAGE', 'PRAGMA', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'PURE', 'REAL', 'REF', 'RETURN', 'SCOPE',
         'SHARED', 'SHORT', 'STATIC', 'STRUCT', 'SUPER', 'SWITCH', 'SYNCHRONIZED', 'TEMPLATE', 'THIS', 'THROW',
          'TRUE', 'TRY', 'TYPEDEF', 'TYPEID', 'TYPEOF', 'UBYTE', 'UCENT', 'UINT', 'ULONG', 'UNION', 'UNITTEST', 
          'USHORT', 'VERSION', 'VOID', 'VOLATILE', 'WCHAR', 'WHILE', 'WITH', '__FILE__', '__MODULE__', '__LINE__',
           '__FUNCTION__', '__PRETTY_FUNCTION__', '__GSHARED', '__TRAITS', '__VECTOR', '__PARAMETERS'
           )         
tokens = reserved + (
  #Literals 
   'IDENTIFIER', 'CHAR_CONSTANT', 'FLOAT_CONSTANT','INT_CONSTANT', 'STRING_CONSTANT',
     'TYPE_ID',

  #Arithmetic Operators in this order: + - * / % ++ --      
        'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MOD', 'PLUSPLUS','MINUSMINUS',
  #Relational Operators : == != > < >= <=
        'EQUALEQUAL','NOTEQUAL','GREATER','LESSER','GREATEREQ','LESSEREQ'
  #Logical Operators : && || !
        'AND','OR','NOT',
  #Bitwise Operators: & | ^  ~ << >>
        'BITWISEAND', 'BITWISEOR', 'BITWISEXOR' ,'BITWISENOR', 'LEFTSHIFT', 'RIGHTSHIFT',
  #Assignment Operators : = += -= *= /= %= <<= >>= &= ^= |= ,~=,     

       'EQUALS', 'PLUSEQUAL','MINUSEQUAL','MULTEQUAL','DIVEQUAL'
        'MODEQUAL', 'LSHIFTEQUAL','RSHIFTEQUAL','ANDEQUAL','XOREQUAL',
        'OREQUAL', 'NOREQUAL',
  #Other Operators:  ; , . : { } ( ) [ ] ? -> # @
      'SEMICOLON', 'COMMA','DOT', 'COLON', 'LEFTPAR',
       'RIGHTPAR', 'LEFTBRACKET','RIGHTBRACKET', 'LEFTBRACE',
       'RIGHTBRACE','CONDITIONOP' , 'HASH', 'AT'       
       )

# For reserved keywords
reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

# Defination for assignment operators  = += -= *= /= %= <<= >>= &= ^= |= ,~=,
def t_EQUALS(p):
  r'='
  p.value = [p.value,'EQUALS']
  return p

 #Arithmetic Operators Rules
def t_PLUS(p):
  r'\+'
  p.value = [p.value,'PLUS']
  return p

def t_MINUS(p):
  r'\-'
  p.value = [p.value,'MINUS']
  return p

def t_LEFTBRACE(p):
  r'{'
  p.value = [p.value,'LEFTBRACE']
  return p

def t_RIGHTBRACE(p):
  r'}'
  p.value = [p.value,'RIGHTBRACE']
  return p

def t_MOD(p):
  r'%'
  p.value = [p.value,'MOD']
  return p

def  t_PLUSPLUS(p):
  r'\+\+'
  p.value = [p.value,'PLUSPLUS']
  return p

def t_MINUSMINUS(p):
  r'\-\-'
  p.value = [p.value,'MINUSMINUS']
  return p

#Relational Operators 

def t_EQUALEQUAL(p):
  r'=='
  p.value = [p.value,'EQUALEQUAL']
  return p

def t_NOTEQUAL(p):
  r'!='
  p.value = [p.value,'NOTEQUAL']
  return p

def t_GREATER(p):
  r'\>'
  p.value = [p.value,'GREATER']
  return p

def t_LESSER(p):
  r'\<'
  p.value = [p.value,'LESSER']
  return p

def t_GRETEAREQUAL(p):
  r'\>='
  p.value = [p.value,'GREATEREQUAL']
  return p
  
def t_LESSEREQUAL(p):
  r'\<='
  p.value = [p.value,'LESSEREQUAL']
  return p

  #Bitwise Operator Rules & | ^  ~ << >>

# ..........................................................#
def t_BITWISE_AND(p):
  r'(?<=([A-Za-z0-9_]))&'
  p.value = [p.value,'BITWISE_AND']
  return p

def t_BITWISEOR(p):
  r'\|'
  p.value = [p.value,'BITWISEOR']
  return p

def t_BITWISEXOR(p):
  r'\^'
  p.value = [p.value,'BITWISEXOR']
  return p

def t_BITWISENOT(p):
  r'~'
  p.value = [p.value,'BITWISENOT']
  return p

def t_LSHIFT(p):
  r'\<\<'
  p.value = [p.value,'LSHIFT']
  return p

def t_RSHIFT(p):
  r'\>\>'
  p.value = [p.value,'RSHIFT']
  return p

  #Logical Operator Rules : && || !

def t_AND(p):
  r'&&'
  p.value = [p.value,'AND']
  return p

def t_OR(p):
  r'\|\|'
  p.value = [p.value,'OR']
  return p

def t_NOT(p):
  r'!'
  p.value = [p.value,'NOT']
  return p

#Other Operators:  ; , . : { } ( ) [ ] ? -> # @

def t_SEMICOLON(p):
  r';'
  p.value = [p.value,'SEMICOLON']
  return p

def t_COMMA(p):
  r','
  p.value = [p.value,'COMMA']
  return p

def t_DOT(p):
  r'\.'
  p.value = [p.value,'DOT']
  return p

def t_COLON(p):
  r':'
  p.value = [p.value,'COLON']
  return p



def t_LEFTPAR(p):
  r'\('
  p.value = [p.value,'LEFTPAR']
  return p

def t_RIGHTPAR(p):
  r'\)'
  p.value = [p.value,'RIGHTPAR']
  return p

def t_LEFTBRACKET(p):
  r'\['
  p.value = [p.value,'LEFTBRACKET']
  return p

def t_RIGHTBRACKET(p):
  r'\]'
  p.value = [p.value,'RIGHTBRACKET']
  return p

def t_CONDITIONOP(p):
  r'\?'
  p.value = [p.value,'CONDITIONOP']
  return p


def t_AT(p):
  r'\@'
  p.value = [p.value,'AT']
  return p

def t_PLUSEQUAL(p):
  r'\+\='
  p.type = reserved_map.get(p.value,"PLUSEQUAL")
  return p

def t_MINUSEQUAL(p):
  r'\-\='
  p.type = reserved_map.get(p.value,"MINUSEQUAL")
  return p

def t_MULTEQUAL(p):
  r'\*\='
  p.type = reserved_map.get(p.value,"MULTEQUAL")
  return p

def t_DIVEQUAL(p):
  r'\/\='
  p.type = reserved_map.get(p.value,"DIVEQUAL")
  return p

def t_MODEQUAL(p):
  r'\%\='
  p.type = reserved_map.get(p.value,"MODEQUAL")
  return p

def t_LSHIFTEQUAL(p):
  r'\<\<\='
  p.type = reserved_map.get(p.value,"LSHIFTEQUAL")
  return p

def t_RSHIFTEQUAL(p):
  r'\>\>\='
  p.type = reserved_map.get(p.value,"RSHIFTEQUAL")
  return p

def t_ANDEQUAL(p):
  r'\&\='
  p.type = reserved_map.get(p.value,"ANDEQUAL")
  return p

def t_XOREQUAL(p):
  r'\^\='
  p.type = reserved_map.get(p.value,"XOREQUAL")
  return p

def t_OREQUAL(p):
  r'\|\='
  p.type = reserved_map.get(p.value,"OREQUAL")
  return p

def t_NOREQUAL(p):
  r'\~\='
  p.type = reserved_map.get(p.value,"NOREQUAL")
  return p
#Literals 

def t_IDENTIFIER(p):
    r'[A-Za-z_][\w_]*'
    p.type = reserved_map.get(p.value,"IDENTIFIER")
    return p

def t_INT_CONSTANT(p):
  r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
  p.value = [p.value,'INT_CONSTANT']
  return p

def t_FLOAT_CONSTANT(p):
  r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
  p.value = [p.value,'FLOAT_CONSTANT']
  return p  

def t_STRING_CONSTANT(p):
  r'\"([^\\\n]|(\\.))*?\"'
  p.value = [p.value,'STRING_CONSTANT']
  return p

def t_CHAR_CONSTANT(p):
  r'(L)?\'([^\\\n]|(\\.))*?\''
  p.value = [p.value,'CHAR_CONSTANT']
  return p

# correctly working now
def t_comment(t):
    r'((/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)|(/\+([^+]|[\r\n]|(\++([^+/]|[\r\n])))*\++/) )'
    t.lineno += t.value.count('\n')

def t_MULTIPLY(p):
  r'\*'
  p.value = [p.value,'MULTIPLY']
  return p

def t_DIVIDE(p):
  r'\/'
  p.value = [p.value,'DIVIDE']
  return p

def t_error(p):
    print " %s not defined:" % repr(t.value[0])
    t.lexer.skip(1)
t_ignore = " \t"

def t_newline(p):
  r'\n'
  print "\n"
# ......................................................... type const def? #


# Build the lexer
lexer = lex.lex()

with open("file.txt", "r") as ins:
    data = "";
    for line in ins:
      data += (line)
    print data
    D = data.split('\n')
    print D
    i=0  
    lexer.input(data)    
    while True:
      tok = lexer.token()
      if not tok: break      # No more input
      sys.stdout.write(tok.type +' ') 
