
Lab 5 report

Test files are under test/lab5, can run with "python src/spaghetti.py test/lab5/test(#).spaghetti"
The following tests were run (same ones listed in instructions):

test input:


var a = "global a";
var b = "global b";
var c = "global c";
{
var a = "outer a";
var b = "outer b";
{
var a = "inner a";
print a;
print b;
print c;
}
print a;
print b;
print c;
}
print a;
print b;
print c;

command and output:

PS C:\Users\ljurm\PycharmProjects\CIS343> python src/spaghetti.py test/lab5/test.spaghetti


inner a
outer b
global c
outer a
outer b
global c
global a
global b
global c
---
other tests showing errors:

test2:

{ var a = 1;

output:

[line 1] Expect '}' after block.

---
test3:

var a = 1;
a + 2 = 3;

output:

[line 2] Invalid assignment target.

---
test4:

print missing;

output:

[line 1] Undefined variable 'missing'.

