import time
try:
    f = open("test.txt")
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            
            time.sleep(3)
            print(con)
    except:
        print("stopped by someone")
except:
    print("this document does not exists")