from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
  print('')
  # Not Inside the for loop, or it will mess the program

printt("Hello, my name is Chris",.15)