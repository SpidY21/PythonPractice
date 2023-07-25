myfile = open('file.txt')
print(myfile)
print(myfile.read())
print(":")
print(myfile.read())
print(":")
myfile.seek(0)
print(myfile.read())
# coverLatter=open('C:\\Users\\Yash\\Desktop\\Industrial\\Resume\\Link.txt')
# print(coverLatter.read())
# coverLatter.close()

with open('file.txt', mode='a') as f:    # a means append
    f.write('\n  this 4th line')
with open('file.txt', mode= 'w') as f:    # w means write if file does not exist then create new file
    f.write('/nHello new line')
with open('file.txt', mode='r') as f:    # r means read
    print(f.read())
