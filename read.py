import libraries

#for read operation

#use syntax "read(key_name)"

def read(d,key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[2]!=0:
            if time.time()<b[2]: #comparing the present time with expiry time
                stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"#to return the value in the format of JasonObject i.e.,"key_name:Name,phno"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri="{"+"name"+":"+str(b[0])+","+"phno"+":"+str(b[1])+"}"
            return stri
