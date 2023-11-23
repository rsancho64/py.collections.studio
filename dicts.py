d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d1)   
print(type(d1))
print(repr(d1))
print(d1["brand"])  # get item by key

# repr(): https://realpython.com/python-repr-vs-str/ see datetime example.
# repr(): in short: use .__repr__() for programmers and .__str__() for users

def f():
    """una funcion"""
    pass

print(f)   
print(type(f))
print(repr(f))

