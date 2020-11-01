
def scraper():
    f = open("user_input.txt", "r")
    names = []
    prices = []
    for x in f:
        # get the name from the file
        name = x.split(' , ')[0]
        names.append(name)
        # Get the price
        price_string = x.split(' , ')[1]
        price = price_string.replace('\n','')
        prices.append(price)
    def checker():
        search_this = str(input('Please Enter Employee Name ? \n'))
        if search_this in names:
            print("We Have Found Employee With name \n" + search_this)
            return
        else:
            print("Sorry We Can Not Find Employee With name \n" + search_this)
            checker()
            
    checker() 
            
