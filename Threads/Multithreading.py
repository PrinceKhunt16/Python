import time
import threading

def print_number():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letter():
    for letter in "ABCDE":
        time.sleep(1)
        print(letter)

# create 2 threads 
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

# Measure execution time
start_time = time.time()  # Start time

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()  # End time

# Print the time taken
print(f"Time taken: {end_time - start_time:.10f} seconds")