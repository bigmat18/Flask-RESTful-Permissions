
class Permissions():
    
    def __init__(self):
        if not hasattr(self, "object"):
            raise Exception("No object attribute in class")