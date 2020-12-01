d={} #'d' is the dictionary in which we store data in key-value format

#for create operation 

#use syntax "create(key_name,name,phno,timeout_value)" timeout is optional you can continue by passing arguments without timeout

def create(key,name,phno,timeout=0):
    if key not in d:
            if len(d)<(1024*1020*1024) and sys.getsizeof(name)+sys.getsizeof(phno)<=(16*1024*1024): #constraints for file size less than 1GB and sizeof (name + phno) value less than 16KB 
                if timeout==0:
                    l=[name,phno,timeout]
                else:
                    l=[name,phno,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                    print("successfully created")
            else:
                print("error: Memory limit exceeded!! ")#error message2
        
    else:
      print("error: this key already exists") #error message1
        
