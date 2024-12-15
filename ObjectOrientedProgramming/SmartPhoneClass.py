class SmartPhone:
    def __init__(self, serial_no, model):
        self.serial_no = serial_no
        self.model = model       

    def aboutPhone(self):
        print(f"\nSN: {self.serial_no}\nModel: {self.model}")

    def switchOn(self):
        print(f"\n>>>{self.model}\nSwitching on....")

    def switchOff(self):        
        print("Switching off....")
        
    def call(self):
        no = input("\nEnter the number to call\n")
        print(f"Calling {no}...")

    def installApp(self):
        print("\nAccess AppStore to install app")

    def __flash(self):
        print("The phone is flashed!!")

#Android
class Android(SmartPhone):
    def __init__(self, maker, serial_no, model):
        super().__init__(serial_no, model)
        self.maker = maker

    def switchOff(self):
        op = input("\nDo you really want to switch off? (y / n): ")
        if op == 'y' or op == 'yes':
            print(f"\n>>>\n^^^^^^^^^^^{self.maker}^^^^^^^^^^\n{self.model}\nSwitching off....")
        elif op == 'n' or op == 'no':
            print("\nStill on")
        else:
            print("\nInvalid input \nStill on")

    def switchOn(self):
        print(f"\n>>>\n^^^^^^^^^^^{self.maker}^^^^^^^^^^\n{self.model}\nSwitching on....")

    def installApp(self):
        print("\nAccess Google Play Store to install app")
        print("Or Use an apk")

#IOS
class IOS(SmartPhone):
    def switchOff(self):
        op = input("\nDo you really want to switch off? (y / n): ")
        if op == 'y' or op == 'yes':
            print(f"\n**********Apple Ltd**********\n>>>{self.model}\nSwitching off....")
        elif op == 'n' or op == 'no':
            print("\nStill on")
        else:
            print("\nInvalid input \nStill on")

    def switchOn(self):
        print(f"\n**********Apple Ltd**********\n>>>{self.model}\nSwitching on....")

    def installApp(self):
        print("\nAccess an Apple Store to install app")

S10plus = Android("Samsung", 1234, "Galaxy S10")
S10plus.switchOn()
S10plus.installApp()
S10plus.call()
S10plus.aboutPhone()
S10plus.switchOff()



my_iphone = IOS(4231, "Iphone X")
my_iphone.switchOn()
my_iphone.call()
my_iphone.installApp()
my_iphone.aboutPhone()
my_iphone.switchOff()

Techno = Android("Techno", 4328, "Techno Spark 2")
Techno.switchOn()
Techno.installApp()
Techno.call()
Techno.aboutPhone()
Techno.switchOff()
