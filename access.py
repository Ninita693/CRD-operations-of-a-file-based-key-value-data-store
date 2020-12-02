import libraries
import create
import read
import delete


d={} #'d' is the dictionary in which we store data in key-value format

create("ninni21@gmail.com","Nini",998797833) ##to create a key with key_name,name,phno given and with no time-to-live property

read("ninni21@gmail.com") #it returns the Name and phno of the respective key in Jasonobject format 'key_name:name,phno'

delete("ninni21@gmail.com") #it deletes the respective key and its name and phno from the database(memory is also freed)


#we can access these using multiple threads like
t1=Thread(target=(create),args=("ninni21@gmail.com","ninni",9989325416)) 
t1.start()
time.sleep(1)
t2=Thread(target=(create),args=("kittu21@gmail.com","kittu",9903674890))
t2.start()
time.sleep(10)
