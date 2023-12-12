grammar ShellGrammar;

// Parser rules
command : subCommand (SEMI subCommand)*;

subCommand : pipe | call;

call : WS? (redirection WS?)* arg (redirection WS?)*;
pipe: call PIPE pipe | call PIPE call;
arg : (( quoted | UNQUOTED) WS?)+;
redirection: left_redirection | right_redirection;
left_redirection: OUT WS? arg;
right_redirection: IN WS? arg;

quoted : single_quoted | double_quoted | back_quoted;
single_quoted : SINGLE_QUOTE ~( SINGLE_QUOTE | NEW_LINE )* SINGLE_QUOTE;
back_quoted : BACK_QUOTE ~( BACK_QUOTE | NEW_LINE )* BACK_QUOTE;
double_quoted : DOUBLE_QUOTE (back_quoted | ~(DOUBLE_QUOTE | NEW_LINE))* DOUBLE_QUOTE;

// Lexer rules
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';
BACK_QUOTE : '`';
OUT :'<';
IN :'>';
SEMI: ';';
UNQUOTED: ~[\t\n "';<>`|]+;
PIPE: '|';
NEW_LINE: '\r'? '\n';
WS: [ \t]+;
