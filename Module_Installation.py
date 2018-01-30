import pip

def install(package):
    pip.main(['install',package])

required = ['numpy','sklearn','pandas']
for i in required:
    install(i)

print("All good to go!!!")
raw_input("Press Anything to Continue...")