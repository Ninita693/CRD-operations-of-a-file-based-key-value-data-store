import sys
import threading #this is for python 3.0 
from threading import*
import time

d={} #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_mailid,name.phno,timeout_value)" timeout is optional you can continue by passing  arguments without timeout

def create(key,name,phno,timeout=0):
    if key not in d:
            if len(d)<(1024*1020*1024) and sys.getsizeof(name)+sys.getsizeof(phno)<=(16*1024*1024): #constraints for file size less than 1GB and sizeof(name + phno) value less than 16KB 
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
        
#for read operation
#use syntax "read(key_mailid)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[2]!=0:
            if time.time()<b[2]: #comparing the present time with expiry time
                stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"#to return the value in the format of JasonObject i.e.,"key_mailid:name,phno"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"
            return stri

#for delete operation
#use syntax "delete(key_mailid)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[2]!=0:
            if time.time()<b[2]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")
