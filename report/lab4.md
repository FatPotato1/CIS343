Lab 4 Report

Test files are under test/lab4, can run with "python src/spaghetti.py test/lab4/(either valid or invalid).spaghetti"
The following tests were run (same ones listed in instructions):


test 1: 
"one"
true;
print 2 +

test 2:
4 + 2;
print "one";
print true;
print 1 + 2;
print nil;

<br>

The output:

PS C:\Users\ljurm\PycharmProjects\CIS343> python src/spaghetti.py test/lab4/valid.spaghetti  

one
true
3
nil

PS C:\Users\ljurm\PycharmProjects\CIS343> python src/spaghetti.py test/lab4/invalid.spaghetti

[line 2] Expected SEMICOLON, got TRUE ('true')

[line 3] Expected a literal or '(', got EOF ('')
PS C:\Users\ljurm\PycharmProjects\CIS343> 
