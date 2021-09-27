# %% 
r = 123_456 + 1_000_000 + 1000
print(r)

# %%
f = 1.0e-3
print(f)

# %%
s = """
This is the first line.
This is the second line.
"""

print(s)
type(s)
# %% 
# SyntaxError: EOL while scanning string literal
s2 = '''
This is the first line.\
This is the second line.
'''
print(s2)

# %%
s3 = "This is the first line.\nThis is the second line."
print(s3)

# %%
name = "Henny"
# # print(name[0])
# # name[0] = "P"
# print(name.replace("H", "P"))
print(name)
print(name.replace('H', 'P'))
print(name)

# %%
name2 = name.replace("H", "P")
print(name2)
print("memory address for name: {}".format(hex(id(name))))
print("memory address for name2: {}".format(hex(id(name2))))

# %%
# slicing
print(name[1:])
name3 = "P" + name[1:]  
print("name3: {}".format(name3))
print("memory address for name: {}".format(hex(id(name))))
print("memory address for name3: {}".format(hex(id(name3))))


# %%
