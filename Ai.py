import time
import datetime
import os
import subprocess



os.system('screenfetch')
print('\033[1m' + '\033[91m'+'     ///   CREATED BY Timmy   ///')
def wish():
  h=int(datetime.datetime.now().hour)
  if h<12:
     subprocess.call(["termux-tts-speak","Good morning sir","I am JARVIS how may I help you"])
  else:
     if h>=12 and h<17:
       subprocess.call(["termux-tts-speak","good afternoon sir","how may i help you"])
     elif h>=17 and h<20:
       subprocess.call(["termux-tts-speak","good evening sir,how may i help you"])
     else:
       subprocess.call(["termux-tts-speak","welcome sir how may i help you"])
wish()
time.sleep(1)

def commands():
    inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please say something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hey sir I am JARVIS an AI Assistant by Timmy"])
         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a second"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir thanks to you"])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep chat with me later"])
         os.system("exit")
         
     elif "call me" in inp:
           cn = subprocess.call(["termux-tts-speak","sir ur country code"])
         time.sleep(2)
         os.system("termux-telephony-call +91")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
         
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
         
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am JARVIS  sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am chatting with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me JARVIS "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by Timmy"])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     elif "age" in inp:
          subprocess.call(["termux-tts-speak","I am 1 year old sir"])
       
   elif "who am i" in inp:
        
     subprocess.call(["termux-tts-speak","you are my owner"])
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
       
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()
