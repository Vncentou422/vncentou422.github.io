import os

import cgi



def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
def main():	
	form = cgi.FieldStorage()
	s1 =  form.getvalue('s1')
	s2 = form.getvalue('s2')
	x = {}
	x["Better Now"] = ["Ashley", "Jennie", "Nicole", "Pyke", "Stefanie", "Harry"]
	x["IDOL"] = ["Eugene", "Gabby", "Julia", "Vincent", "Silver", "Paige", "Sam"]
	x["God is A Woman"] = ["Alicia", "Celina", "Hannah", "Jennie", "Nia", "Mona"]
	x["Hann"] = ["Kenji", "Alicia", "Celina", "Hannah", "Marin", "Nia"]
	x["Baam"] = ["Eisa","Kenji","Muqing","Alicia","Hannah","Jennie","Nia","Pyke","Mona"]
	x["Lullaby"] = ["Helios", "Kelly L", "Silver", "Gabby", "Julia", "Stefanie", "Harry"]
	x["La Vie En Rose"] = ["Eisa", "Grace", "Kelly A", "Kelly L", "Muqing", "Serena", "Alicia", "Hannah","Lucy", "Marin", "Michelle", "Nicole"]
	x["16 Shots"] = ["Lauren","Sam","Gabby","Julia", "Pyke","Harry"]
	x["Look Alive"] = ["Eugene", "Marissa", "Sam"]
	x["Millions"] = ["Eugene", "Pyke", "Marin", "Gabby"]
	x["I Love You"] = ["Nia", "Mona", "Nia", "Julia", "Celina"]
	x["RBB"] = ["Hannah", "Jennie", "Alicia", "Eisa", "Serena"]
	x["Yes or Yes"] = ["Nicole", "Marin", "Jennie", "Phoebe", "Paige", "Kelly L", "Kelly A", "Helen", "Eisa"]
	x["Eung Eung"] = ["Nia", "Michelle", "Hannah", "Jennie", "Alicia", "Eisa"]
	x["Dalla Dalla"] = ["Nia", "Hannah", "Mona", "Marin", "Jennie"]
	x["Bang Bang Bang"] = ["Eisa", "Paige", "Silver", "Serena", "Ashley", "Eugene", "Marin", "Michelle", "Pyke", "Vincent", "Harry"]
	x["Show"] = ["Helen", "Hannah", "Jennie", "Marin", "Michelle", "Nicole", "Mona"]
	x["Rude Boy"] = ["Julia", "Nicole", "Celina", "Vincent", "Ashley"]
	x["idontwannabeyouanymore"] = ["Julia", "Mona", "Stefanie"]
	x["Bad Liar"] = ["Muqing", "Alicia", "Grace", "Kelly A", "Kelly L", "Marissa", "Muqing", "Phoebe", "Yuanna", "Alicia", "Jennie", "Nicole"]
	x["C'Est La Vie"] = ["Marin", "Eisa", "Mona", "Marin"]
	x["Little Man"] = ["Grace", "Marissa", "Sam", "Silver", "Gabby", "Stefanie"]
	x["Down in the DM"] = ["Marissa", "Sam", "Silver", "Eugene", "Gabby", "Marin", "Stefanie"]
	x["Get It"] = ["Muqing", "Alicia", "Ashley", "Jennie", "Nicole", "Stefanie"]
	x["7 Rings"] = ["Phoebe", "Celina", "Hannah", "Jennie", "Julia", "Michelle", "Nia", "Harry", "Mona"]
	x["Boyfriend"] = ["Vincent", "Alicia", "Jennie", "Kyle", "Harry", "Eisa", "Yuanna", "Pyke"]
	x["Bikini Body"] = ["Vincent", "Alicia", "Hannah", "Pyke", "Marin", "Eugene", "Harry", "Mona"]
	x["Pose"] = ["Eisa", "Nia", "Pyke", "Ashley", "Hannah"]
	x["Feeling"] = ["Stefanie", "Lauren", "Harry", "Vincent", "Grace", "Yuanna", "Gabby", "Kyle", "Marissa", "Serena"]
	# s1 = input("First Song: ")
	# s2 = input("Second Song: ")
	
	print("Intersects: ", intersection(x[s1], x[s2]))

if __name__ == "__main__":
	main()
