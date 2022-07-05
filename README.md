# ffn

Algorithm taken from ("adapted" would be too weak a word, though there are
some modifications here) Modern Compiler Implementation in C (Appel and
Ginsburg, 2005).

Run using filepath to grammar as command-line argument:

python3 ffn.py grammar.txt

Grammar file should be laid out as follows:

- First line is whitespace delimited terminal symbols
- Second line is whitespace delimited non-terminal symbols
- Remaining lines are productions of the form E xE
- A production whose right-hand side is the empty string is written
  as a standalone left-hand side. E.g., if the grammar contains the
  production E -> empty string, the production would be represented
  in the text file by a line consisting solely of E

For example, take the following grammar (from Appel):

Z -> d
Z -> XYZ
Y ->
Y -> c
X -> Y
X -> a

The grammar text file should look like:

a c d
X Y Z
Z d
Z XYZ
Y
Y c
X Y
X a

Note: Needs modification to accept multi-character symbols (at least terminals).

