class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"


class SmartFeaturePhone(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Battery Life: {self.battery_life} hours"

    def play_music(self):
        return f"Playing music on {self.model}."


class SmartFlagshipPhone(Smartphone):
    def __init__(self, brand, model, price, camera_quality):
        super().__init__(brand, model, price)
        self.camera_quality = camera_quality

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Camera Quality: {self.camera_quality} MP"

    def take_photo(self):
        return f"Taking a photo with {self.camera_quality} MP camera."


if __name__ == "__main__":
    basic_phone = SmartFeaturePhone("Nokia", "3310", 50, 48)
    flagship_phone = SmartFlagshipPhone("Apple", "iPhone 14", 999, 48)

    print(basic_phone.get_info())
    print(basic_phone.play_music())

    print(flagship_phone.get_info())
    print(flagship_phone.take_photo())