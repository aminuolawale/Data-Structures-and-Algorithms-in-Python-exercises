from time import  time, sleep

def some_func():
    sleep(5)

start = time()
some_func()
end = time()
print(end-start)


