grammar SimplePLSQL;

/*
 Extended SimplePLSQL.g4
 - Phase 1: Declarations & Types (CONSTANT, %TYPE/%ROWTYPE, NUMBER(p[,s]), VARCHAR2(n), NOT NULL, DEFAULT)
 - Adds TYPE declarations (RECORD, COLLECTION, REF CURSOR), top-level cursor and PRAGMA
 - Keeps existing structure and naming; drop-in replacement for your previous file
*/

program
    : (unit)* EOF
    ;

unit
    : proc_decl
    | type_decl
    | cursor_decl
    | pragma_stmt
    | block
    | statement SEMI
    ;

// ----------------- Procedures / Blocks -----------------
proc_decl
    : (PROCEDURE | FUNCTION) ID param_list? (RETURN type_spec)? IS proc_body (ID)? SEMI?
    ;

param_list
    : LPAREN param (COMMA param)* RPAREN
    ;

param
    : ID (IN | OUT | IN OUT)? type_spec?  // name, optional mode, optional type
    ;

proc_body
    : (DECLARE decl_list)? BEGIN stmt_list END
    ;

block
    : proc_body (SEMI)?
    ;

// ----------------- Declarations -----------------
decl_list
    : decl (decl)*
    ;

// Variable declaration: explicit type required (Option B)
decl
    : ID init SEMI
    | ID ':' type_spec constant_modifier? not_null? init? SEMI
    ;

// constant modifier
constant_modifier
    : CONSTANT
    ;

// NOT NULL
not_null
    : NOT NULL_STMT
    ;

// initialization forms: ':=' or 'DEFAULT'
init
    : (ASSIGN | DEFAULT) expr
    ;

// ----------------- Type declarations (TYPE ... IS ...) -----------------
type_decl
    : TYPE ID IS ( record_type_body | collection_type_body | ref_cursor_body ) SEMI
    ;

record_type_body
    : RECORD LPAREN record_fields RPAREN
    ;

record_fields
    : field (COMMA field)*
    ;

field
    : ID type_spec
    ;

// Collection type bodies
collection_type_body
    : VARRAY LPAREN INT RPAREN 'OF' type_spec
    | TABLE 'OF' type_spec
    | type_spec INDEX BY (ID | PLS_INTEGER | BINARY_INTEGER)
    ;

// REF CURSOR TYPE
ref_cursor_body
    : 'REF' CURSOR
    ;

// ----------------- Cursor & PRAGMA -----------------
cursor_decl
    : CURSOR ID (LPAREN cursor_params RPAREN)? IS cursor_select SEMI
    ;

cursor_params
    : param (COMMA param)*
    ;

cursor_select
    : SELECT select_list FROM qualified_name ( WHERE expr )?
    ;

select_list
    : '*'
    | expr (COMMA expr)*
    ;

pragma_stmt
    : PRAGMA ID (LPAREN ID RPAREN)? SEMI
    ;

// ----------------- Statements -----------------
stmt_list
    : (statement SEMI)*
    ;

statement
    : assignment
    | if_stmt
    | while_stmt
    | for_stmt
    | proc_call
    | select_into
    | return_stmt
    | exit_stmt
    | empty_stmt
    ;

assignment
    : target ASSIGN expr
    ;

// target: allow dotted names e.g., r.f or r.f.g
target
    : ID (DOT ID)*
    ;

if_stmt
    : IF expr THEN stmt_list (ELSE stmt_list)? END IF
    ;

while_stmt
    : WHILE expr LOOP stmt_list END LOOP
    ;

for_stmt
    : FOR ID IN expr_range LOOP stmt_list END LOOP
    ;

expr_range
    : expr RANGE expr
    ;

func_call
    : ID LPAREN (expr (COMMA expr)*)? RPAREN
    ;

proc_call
    : func_call
    ;

select_into
    : SELECT expr INTO target FROM qualified_name (WHERE expr)?
    ;

return_stmt
    : RETURN expr?
    ;
exit_stmt
    : EXIT
    ;
empty_stmt
    : NULL_STMT
    ;

// ----------------- Expressions -----------------
expr
    : expr op=('*'|'/') expr        # MulDivExpr
    | expr op=('+'|'-') expr        # AddSubExpr
    | expr op=('>'|'>='|'<'|'<='|'='|'<>') expr  # CompExpr
    | expr op=(AND|OR) expr         # LogicExpr
    | NOT expr                      # NotExpr
    | INT                           # IntExpr
    | func_call                     # FuncCallExpr
    | target                        # IdExprOrTarget
    | LPAREN expr RPAREN            # ParenExpr
    ;

// ----------------- Type specifications -----------------
type_spec
    : simple_type
    | numeric_type
    | char_type
    | pct_attr
    | ID                // user-defined type name
    ;

simple_type
    : DATE
    | BOOLEAN
    | INTEGER
    ;

numeric_type
    : NUMBER LPAREN INT (COMMA INT)? RPAREN
    ;

char_type
    : (VARCHAR2 | CHAR) LPAREN INT RPAREN
    ;

// %TYPE / %ROWTYPE attribute (schema-qualified allowed)
pct_attr
    : qualified_name '%' ( TYPE | 'ROWTYPE' )
    ;

qualified_name
    : ID (DOT ID)*
    ;

// ----------------- Keywords / tokens -----------------
PROCEDURE : 'PROCEDURE';
FUNCTION  : 'FUNCTION';
IN        : 'IN';
OUT       : 'OUT';
RETURN    : 'RETURN';
SELECT    : 'SELECT';
INTO      : 'INTO';
FROM      : 'FROM';
WHERE     : 'WHERE';
FOR       : 'FOR';
LOOP      : 'LOOP';
EXIT      : 'EXIT';
NULL_STMT : 'NULL';
BEGIN     : 'BEGIN';
DECLARE   : 'DECLARE';
END       : 'END';
IF        : 'IF';
THEN      : 'THEN';
ELSE      : 'ELSE';
WHILE     : 'WHILE';
AND       : 'AND';
OR        : 'OR';
NOT       : 'NOT';
IS        : 'IS';
CONSTANT  : 'CONSTANT';
DEFAULT   : 'DEFAULT';
TYPE      : 'TYPE';
RECORD    : 'RECORD';
VARRAY    : 'VARRAY';
TABLE     : 'TABLE';
INDEX     : 'INDEX';
BY        : 'BY';
PLS_INTEGER : 'PLS_INTEGER';
BINARY_INTEGER : 'BINARY_INTEGER';
CURSOR    : 'CURSOR';
PRAGMA    : 'PRAGMA';
NUMBER    : 'NUMBER';
VARCHAR2  : 'VARCHAR2';
CHAR      : 'CHAR';
DATE      : 'DATE';
BOOLEAN   : 'BOOLEAN';
INTEGER   : 'INTEGER';

// ----------------- Other tokens -----------------
ASSIGN  : ':=' ;
SEMI    : ';' ;
COMMA   : ',' ;
DOT     : '.' ;
RANGE   : '..' ;
LPAREN  : '(' ;
RPAREN  : ')' ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
INT     : [0-9]+ ;

// Script terminator (ignore slash alone on a line)
SCRIPT_TERMINATOR : '/' [ \t]* ( '\r'? '\n' | EOF ) -> skip ;

// Whitespace / comments
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
