class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    flag = False
    @staticmethod
    def get_max_capacity():
        if Cache.flag == False:
                while True:
                            try:
                                Cache._MAX_CAPACITY = int(input("Enter the Cache max capacity: "))
                                if Cache._MAX_CAPACITY > 0:
                                    Cache.flag = True
                                    break
                                else:
                                    print("Please enter a positive integer.")
                            except ValueError:
                                    print("Invalid input. Please enter an integer value.")
                print("Returning MAX_CAPACITY")
                return Cache._MAX_CAPACITY
        else:
              print("Returning MAX_CAPACITY")
              return Cache._MAX_CAPACITY
