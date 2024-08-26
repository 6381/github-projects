import time


def main(time_limit):
    start_time=time.time()
    time_running=True
    while time_running:
        remaining_time=time_limit-(time.time()-start_time)
        print("Time remaining: {:.2f} seconds".format(remaining_time))
        if remaining_time<=0:
         time_running=False
         print("time's up")
        user_input=input("enter the guess:")
        if user_input=='correct guess':
          print('Congratulations , you won')
          break
        time.sleep(1)
if __name__ == '__main__':
    main(10)

