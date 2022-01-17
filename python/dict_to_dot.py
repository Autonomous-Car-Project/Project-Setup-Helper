# Python Function to Access Dict using dot operation

class dict_to_dot(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

if __name__ == "__main__":
    d = {"ayushman":"abc"}
    # Accessing like "d.ayushman" will throw error

    d = dict_to_dot(d)
    print(d.ayushman)  # Runs without any error