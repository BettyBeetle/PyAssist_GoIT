class Address: # można to jeszcze rozdzielić na osobne pliki street itd.
    '''
    Class for address object
    '''
    def __init__(self, street, city, zip_code, country):
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country
    
    def __str__(self):
        return f"Address:\nStreet {self.street}\nZIP Code: {self.zip_code}\nCity: {self.city}\Country: {self.country}"