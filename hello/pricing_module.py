class pricing():

    def __init__(self, gallonsN, location, rate_history=False):
        self.gallonsTotal = gallonsN
        self.location = location
        self.rate_history = rate_history

    def suggestedPrice(self):
        self.currentPrice = 1.50 + margin()
        return self.currentPrice

    def margin(self):
        if self.location == "Texas":
            location_factor = 0.02
        else:
            location_factor = 0.04
        
        if self.rate_history == True:
            rate_history_factor = 0.01
        else:
            rate_history_factor = 0.00
        if self.gallonsTotal > 1000:
            gallons_requested_factor = 0.02
        else: 
            gallons_requested_factor = 0.03
        
        return 1.50 * (location_factor - rate_history_factor + gallons_requested_factor + 0.10)


    