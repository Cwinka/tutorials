import os
os.chdir(r'D:/Scripts')
try:
    f = open('demo.txt')
    if f.name == "demo.txt":
        raise Exception
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Idi na xuy")
else:
    print(f.read())
    f.close()
finally:
    f.close()
    print('Executed')
