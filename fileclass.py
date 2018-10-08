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

    @property
    def privacy(self):
        return self.properties.get('privacy', None)

    @privacy.setter
    def privacy(self, c):
        self.properties['privacy'] = c

    @privacy.deleter
    def privacy(self):
        del self.properties['privacy']

def main():
    imageDoc = Files()
    print(type(imageDoc))
    print(dir(imageDoc))
    print(imageDoc)
    
    imageDoc.privacy="archive"
    print(type(imageDoc.privacy))
    print(dir(imageDoc.privacy)) 
    print(imageDoc.privacy)
    print(imageDoc.get_property("privacy"))


main()

