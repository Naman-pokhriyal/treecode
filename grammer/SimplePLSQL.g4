grammar SimplePLSQL;

/*
 Corrected SimplePLSQL.g4
 - Includes IS token, DOT, RANGE '..', and ignores trailing '/'
 - Simplified but consistent with the sample_full.sql constructs
*/

program
    : (unit)* EOF
    ;

unit
    : proc_decl
    | block
    | statement SEMI
    ;

proc_decl
    : (PROCEDURE | FUNCTION) ID param_list? (RETURN ID)? IS proc_body (ID)? SEMI?
    ;

param_list
    : '(' param (',' param)* ')'
    ;

param
    : ID (IN | OUT | IN OUT)? (':'? ID)?  // name, optional mode, optional type
    ;


proc_body
    : (DECLARE decl_list)? BEGIN stmt_list END
    ;

block
    : proc_body (SEMI)?
    ;

decl_list
    : decl (decl)*
    ;

decl
    : ID (':' ID)? (ASSIGN expr)? SEMI
    ;

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
    : ID '(' (expr (',' expr)*)? ')'
    ;

proc_call
    : func_call
    ;

select_into
    : SELECT expr INTO target FROM ID (WHERE expr)?
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

// Expressions: arithmetic, comparisons, boolean
expr
    : expr op=('*'|'/') expr        # MulDivExpr
    | expr op=('+'|'-') expr        # AddSubExpr
    | expr op=('>'|'>='|'<'|'<='|'='|'<>') expr  # CompExpr
    | expr op=('AND'|'OR') expr     # LogicExpr
    | NOT expr                      # NotExpr
    | INT                           # IntExpr
    | func_call                     # FuncCallExpr
    | target                        # IdExprOrTarget
    | '(' expr ')'                  # ParenExpr
    ;

// Keywords / tokens
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

// Other tokens
ASSIGN  : ':=';
SEMI    : ';';
COMMA   : ',';
DOT     : '.';
RANGE   : '..';
LPAREN  : '(';
RPAREN  : ')';

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
INT     : [0-9]+ ;

SCRIPT_TERMINATOR: '/' [ \t]* ( '\r'? '\n' | EOF ) -> skip ;   // ignore slash that's alone on a line as script terminator

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '--' ~[\r\n]* -> skip ;
