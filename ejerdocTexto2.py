""" with open("abc.txt", "r", encoding='utf-8') as f:  #lee un archivo
    for line in f.readlines():
        print(line) """
 
with open("abc.txt", "r", encoding='utf-8') as f:
    s = f.read()
with open("xyz.txt", "a") as f:  #lee un archivo
    f.write(s + "agurrr!")

