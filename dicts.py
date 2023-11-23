d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d1)   
print(type(d1))
print(repr(d1))

# repr(): https://realpython.com/python-repr-vs-str/ see datetime example.
# repr(): in short: use .__repr__() for programmers and .__str__() for users

def f():
    """una funcion"""
    pass

print(f)   
print(type(f))
print(repr(f))

### ...
print(d1["brand"])  # get item by key ( key -> value )
print(d1["year"])   # get item by key ( key -> value )
print(len(d1))      # get #items. now 3

### ... construction:

d2 = dict(name = "John", age = 36, country = "Norway")  # args: lista de 1+ asignaciones
print(d2)

dvacio1 = dict()
print(dvacio1)

dvacio2 = {}
print(dvacio2)

### ...

print(d1.get("name"))  # if key not exists, get() returns None -no raise exception-
print(d1.get("model")) # key exists

kk = d1.keys()  # the set of keys. not as list object. As dict_keys object
print(type(kk)) # the set of keys. not as list object. As dict_keys object
print(kk)       # the set of keys. not as list object. As dict_keys object

song = {
  "name": "manuel",
  "ap1": "sanche",
  "ap2": "sanche",
  "url": "https://www.youtube.com/watch?v=-sMa0C8mgl4",
  "year": 1985
}

songvv = song.values() # the NO-set of values. not as list object. As dict_values object. 
                       # A LINK TO THE GET METHOD, NOT TO A REAL (UPDATABLE) LIST !!!

print(type(songvv)) # the NO-set of keys. not as list object. As dict_values object
print(songvv)       # the NO-set of keys. not as list object. As dict_values object

### ... ++ new pair (k,v)

song["discografica"] = "Patatus Records"
#song["ape2"] = "Castejon"  # typo-error
print(songvv)  # dict_values object UPDATED

song["name"] = "Tiranosaurio"
song["ap2"] = "Castejon"

### ... update value in pair

song["discografica"] = "LoPais"
print(songvv)

### ... check if key exists

if not "partido" in song:
    print("no esta el partido del canalla, se lo indicamos")
    song["partido"] = "P$O€"
print(songvv)

### ... change value by key

song.update({"url": "https://www.youtube.com/watch?v=o_UZvO-PW0M"})
print(songvv)
