f = open("Hello.txt", "r")
data = f.read()
f.close()

fw = open("Hello.txt", "w")
data = "Hello World!"
fw.write(data)
fw.close()

