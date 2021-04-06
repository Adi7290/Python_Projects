Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(0,100):
	if i%2==1:
		print(i)
	elif i%2 ==0:
		pass
	i=i+1

	
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 



>>> 
>>> 



>>> 

>>> 


>>> 
>>> 



>>> 
>>> 




>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 
>>> 
>>> for i in range(0,100):
	if i%(2,3,5,7,9)==0:
		pass
	elif i%(2,3,5,7,9)==1:
		print(i)
	i+=1

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    if i%(2,3,5,7,9)==0:
TypeError: unsupported operand type(s) for %: 'int' and 'tuple'
>>> for i in range(0,100):
	if i%2,3,5,7==0:
		
SyntaxError: invalid syntax
>>> for i in range(0,100):
	if i%2==0 and i%3==0 and i%5==0 and i %7==0:
		pass
	elif i%2==1 and i%3==1 and i%5==1 and i%7==1:
		print(i)
	i+=1

	
1
>>> for i in range(0,1000):
	if i%2==0 and i%3==0 and i%5==0 and i%7==0:
		print(i)
	i+=1

	
0
210
420
630
840
>>> for i in range(0,1000):
	if i % i ==0:
		print(i)
	elif i%i==1:
		pass
	i+=1

	
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    if i % i ==0:
ZeroDivisionError: integer division or modulo by zero
>>> for i in range(2,150):
	if i%i ==0
	
SyntaxError: invalid syntax
>>> for i in range(2,150):
	if i%i ==0:
		print(i)
	elif i%i ==1:
		pass
	i+=1

	
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
>>> for i in range(2,150):
	if i%i ==0:
		pass
	elif i%i ==1:
		print(i)
	i+=1

	
>>> 
>>> 
>>> 
>>> 
>>> for i in range(0,100):
	if i%1==0 and i%i==0:
		print(i)
	elif i%2==0:
		pass

	
Traceback (most recent call last):
  File "<pyshell#77>", line 2, in <module>
    if i%1==0 and i%i==0:
ZeroDivisionError: integer division or modulo by zero
>>> 
KeyboardInterrupt
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	elif:
		
SyntaxError: invalid syntax
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	elif:
		
SyntaxError: invalid syntax
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		elif i%5==0 and i%7==0:
			pass
	elif:
		
SyntaxError: invalid syntax
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	else:
		print(i)
	i+=1

	
1
2
3
4
5
7
8
9
10
11
13
14
15
16
17
19
20
21
22
23
25
26
27
28
29
31
32
33
34
35
37
38
39
40
41
43
44
45
46
47
49
50
51
52
53
55
56
57
58
59
61
62
63
64
65
67
68
69
70
71
73
74
75
76
77
79
80
81
82
83
85
86
87
88
89
91
92
93
94
95
97
98
99
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	else i%3==1 and i%2 ==1:
		if i%5==1 and i%7==1:
		print(i)
	i+=1
	
SyntaxError: invalid syntax
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	elif i%3==1 and i%2 ==1:
		if i%5==1 and i%7==1:
		print(i)
	i+=1
	
SyntaxError: expected an indented block
>>> 
>>> for i in range(0,100):
	if i%3==0 and i%2 ==0:
		if i%5==0 and i%7==0:
			pass
	elif i%3==1 and i%2 ==1:
		if i%5==1 and i%7==1:
			print(i)
	i+=1

	
1
>>> for i in range(0,100):
	if i//2 ==0:
		pass
	elif i//2==1:
		print(i)
	i+=1

	
2
3
>>> 
>>> 
>>> for i in range(2,101):
	if i%2==0:
		elif i%3==0:
			
SyntaxError: invalid syntax
>>> for i in range(2,101):
	if i%1==True and i%i == True:
		print(i)
	elif i%2==True:
		elif i%3==True:
			
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 


>>> 


>>> 

>>> 


>>> 
>>> 



>>> 

>>> for i in range(0,100):
	if i%2 and 3 and 5 and 7 ==0:
		print(i)

		
>>> if i%2 and 3 and 5 and 7==0:
	print('h')

	
>>> 
>>> a = 1
>>> b=2
>>> c=3
>>> d=4
>>> a,b,c,d
(1, 2, 3, 4)
>>> a,b,c,d==0
(1, 2, 3, False)
>>> a and b and c and d ==0
False
>>> a and b==0
False
>>> c and d ==0
False
>>> a and c ==0
False
>>> a = i%2==0
>>> b = i%3==0
>>> c = i%5==0
>>> d = i%7==0
>>> for i in range(2,101):
	if a and b and c and d ==True:
		pass
	elif a and b and c and d ==False:
		print(i)
	i+=1

	
>>> a and b and c and d
False
>>> for i in range(2,101):
	a = i%2==0
>>> b = i%3==0
>>> c = i%5==0
>>> d = i%7==0
SyntaxError: invalid syntax
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(2,101):
	if i %2 and i%3 and i%5 and i%7==0:
		pass
	elif i %2 and i%3 and i%5 and i%7==1:
		print(i)
	i+=1

	
29
43
71
>>> for i in range(0,100):
	if i%2 or i%3 or i %5 or i%7==0:
		print(i)
	elif i%2 or i%3 or i%5 or i%7 ==1:
		pass
	i+=1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
91
92
93
94
95
96
97
98
99
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 