import threading 
def fun():         # user defined function which adds +10 to given number
    
    print ("Hey u called me")

delay = int(input("Enter the delay time :"))
while True:  
    start_time = threading.Timer(delay,fun)
    start_time.start()
    print ("End of the code")