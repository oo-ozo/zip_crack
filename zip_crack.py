import zipfile

fi = input("entet zipfile name :")
zi = input("enter pass.txt :")


with open(zi, 'rb') as file:
    for pa in file.readlines():
        pas = pa.strip()
        try:
            with zipfile.ZipFile(fi) as z:
                z.extractall(pwd=pas)
                print("\npass found :", pas.decode()+"\n")
                break
        except:
            print("pass not founs :", pas.decode())
        
        
