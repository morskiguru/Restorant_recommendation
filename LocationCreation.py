class Restaurants:
    def __init__(self, res_name, location_address, res_location_value, price_category, quality_of_service):
        self.name = res_name
        self.location_address = location_address
        self.location_value = res_location_value
        self.price_category = price_category
        self.quality_of_service = quality_of_service

    def get_name(self):
        return self.name

    def get_location_address(self):
        return self.location_address

    def get_location_value(self):
        return self.location_value

    def get_price_category(self):
        return self.price_category

    def get_quality_of_service(self):
        return self.quality_of_service

    def update_information(self, update_name, update_address, update_location_value,
                           update_price_category,
                           update_quality_of_service):
        if update_name != None:
            self.name = update_name
        if update_address != None:
            self.location_address = update_address
        if update_location_value != None:
            self.location = update_location_value
        if update_price_category != None:
            self.price_category = update_price_category
        if update_quality_of_service != None:
            self.quality_of_service = update_quality_of_service
