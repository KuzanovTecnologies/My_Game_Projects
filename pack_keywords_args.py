#code is written as script
pack_keyword_args.py

def about(name,age,like):
    info = "I am {}. I am {} years old and I like {}.
".format(name,age,like)
    return info

dictionary = {"name": "Ross", "age": 55, "like": "Python"}
print(about(**dictionary))

#unpacking_key_args.py
def about(**kwargs):
    for key, value in kwargs.items():
          print("f{} is{}".format(key,value))
about(Python = "Easy", Java = "Hard")

Python is Easy
Java is Hard

dict_items([('Python', 'Easy'), ('Java', 'Hard')])

lambda arguments: expression

To find factorial of 5= 5! = 5*4*3*2*1! = 5*4*3*2*1 = 120