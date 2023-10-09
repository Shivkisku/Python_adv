class Singleton:

    _instances = {}
    _current_instance = 0

    def __new__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)
        return cls._instances[cls]

    def get_instance(self):
        self._current_instance += 1
        if self._current_instance % 2 == 0:
            return self
        else:
            return self

# Example usage:
instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)  # Output: True (Both instances are the same)
