# Online-Piano-Player
Send keys in rhythm to the active window.
Used for pianos like https://virtualpiano.net/.
Change the "music" string to alter what the program plays. Every note is played at quarter a beat at the bpm (tempo). Spaces are a quarter rest.
F4 pauses the music, F5 stops the music entirely.

## Syntax
" " = A quarter rest.

" | " = A half rest.

"[abc]" or "{abc}" = A chord of notes, wherein each letter (a, b, c) equates to a note (in thise case: b, a, f).

Letters and numbers correspond to notes (see [letter index](#letter-index) for more).
Capital letters (and number equivalents) are a half-note above the "lowercase" version (e.g. q = f, Q = f#; 1 = c, ! = c#).

For compatibility with certain scores:
* {} are converted to []
* Newlines (\n) are converted to " "
* "-" are removed (i.e. converted to "")
* "-\n" (dashes with newlines) are removed (i.e. converted to "")
* " - " are converted to "&nbsp;&nbsp;&nbsp;" (three quarter rests)

## Letter index
Letter | Note
-------|------
1|c
!|c#
2|d
@|d#
3|e
4|f
$|f#
5|g
%|g#
6|a
^|a#
7|b
8|c
`*`|c#
9|d
(|d#
0|e
q|f
Q|f#
w|g
W|g#
e|a
E|a#
r|b
t|c
T|c#
y|d
Y|d#
u|e
i|f
I|f#
o|g
O|g#
p|a
P|a#
a|b
s|c
S|c#
d|d
D|d#
f|e
g|f
G|f#
h|g
H|g#
j|a
J|a#
k|b
l|c
L|c#
z|d
Z|d#
x|e
c|f
C|f#
v|g
V|g#
b|a
B|a#
n|b
m|c
