import multiprocessing
import time

def square_time():
    for i in range(5):
        time.sleep(1)
        print(i * i)

def cube_time():
    for i in range(5):
        time.sleep(1)
        print(i * i * i)

if __name__ == '__main__':
    # create 2 processes
    p1 = multiprocessing.Process(target=square_time)
    p2 = multiprocessing.Process(target=cube_time)

    # Measure execution time
    start_time = time.time()  # Start time
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end_time = time.time()  # End time

    # Print the time taken
    print(f"Time taken: {end_time - start_time} seconds")