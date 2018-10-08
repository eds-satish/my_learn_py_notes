class Files:
    def __init__(self, **kwargs):
        print("Initialized __init__")
        self.properties = kwargs
        print(type(self.properties)) 
        print(dir(self.properties))

    def copy(self):
        print("copying")

    def move(self):
        print("moving")


    def remove(self):
        print("deleting")

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

def main():
    imageDoc = Files(privacy="secret")
    print(type(imageDoc))
    print(dir(imageDoc))
    print(imageDoc)
    print(imageDoc.get_property("privacy"))

main()
