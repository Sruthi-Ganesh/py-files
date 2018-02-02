import webbrowser
import time
i=0
print("The program started at " +time.ctime())
while(i<3):
   time.sleep(2*60*60)
   webbrowser.open("https://www.youtube.com/watch?v=h--P8HzYZ74")
   i=i+1
