Grammar ={'RS':'S','RYS':'S','RYYS':'S','R':'S','RY':'S','RYY':'S'}

Inputstring=input("enter a string:")

stack=''


def  SHIFT(Inputstring,stack,i):
	#print("\nshift {0:4} -> stack\n".format(Inputstring[:i:]))
	
	stack+=Inputstring[:i:];
	Inputstring=""+Inputstring[i:]
	
	#print("\nstack contains: {0:4}\n ".format(stack))
	
	return (Inputstring,stack);

def SPECIALSHIFT(Inputstring,stack):

	#print("\nshift the whole string  {0:4} -> stack\n".format(Inputstring))
	
	stack=Inputstring+stack;
	Inputstring=""
	
	stack=REDUCE(stack,Grammar)

	return(Inputstring,stack);

def REDUCE(stack,Grammar):
	
	if stack[-4::] in Grammar:
		#print("reduce1 {0:3} -> {1:3}".format(stack[-4::],Grammar[stack[-4::]]))
		
		stack=stack.replace(stack[-4::],Grammar[stack[-4::]])
		
		#print("\nstack contains: {0:4}\n ".format(stack))	
	
	return stack;

def ERROR():
		print("NO!")
		exit();

while 1:

	if Inputstring!="":

		if Inputstring+stack in Grammar:

			Inputstring,stack = SPECIALSHIFT(Inputstring,stack)
			
		else:
			
			i=1;			
			
			while 1:
				i=i+1
				
				if stack[-3::]+Inputstring[:i:] in Grammar:															
					continue
				elif Inputstring[:i:]+stack[-3::] in Grammar:
					continue
				else:
					i=i-1
					break
				
				if i==len(Inputstring):
					break;
			
			Inputstring,stack = SHIFT(Inputstring,stack,i)


	if Inputstring=="":
		
		if len(stack)==1 and stack[0]=='S':
			break;
	
	if len(stack)>1:
		
		if stack[1:len(stack):]+stack[0] in Grammar:
			stack=stack[1:len(stack):]+stack[0]
	
	if (stack[-4::] in Grammar):
		
		stack = REDUCE(stack,Grammar)

		if len(Inputstring)>0:
			
			if stack[0]=='S':
				stack=stack[:0:-1] + stack[0]
			continue;
	
	if stack!='S' and len(stack)>=1:
		ERROR();

print("\n{0:1} --> YES".format(stack))
