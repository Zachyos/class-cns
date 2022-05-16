import os
os.system('cls')
Fahrenheit_1 = float( input("Temperature value in degree Fahrenheit: " ))  
  

celsius_1 = (Fahrenheit_1 - 32)  / 1.8  
    

print ('The %.2f degree Fahrenheit is equivalent to: %.2f in Celsius'  
      %(Fahrenheit_1, celsius_1))  
  
print("OR")  
Fahrenheit_2 = float( input("Temperature value in degree Fahrenheit: " ))  
celsius_2 = (Fahrenheit_2 - 32) * 5/9  
    

print ('The %.2f degree Fahrenheit is equivalent to: %.2f in Celsius'  
      %(Fahrenheit_2, celsius_2))  