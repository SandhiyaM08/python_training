'''from abc import ABC ,abstractmethod
class PaymentSystem(ABC):
        @abstractmethod
        def process_payment(self,amount):
            pass
class CreditCardPayment(PaymentSystem):
        def process_payment(self,amount):
                print(f"Processing credit card payment of ${amount}")
class UpiPayment(PaymentSystem):
        def process_payment(self,amount):
                print(f"Processing UPI payment of ${amount}")
pay=PaymentSystem()
pay.process_payment(250)'''

class TV:
	def power_on(self):
		print("TV is now on")
class Airconditioner:
	def power_on(self):
		print("Air conditioner is now ON")
class Speaker:
	def power_on(self):
		print("Speaker is now ON")
def remote_control(device):
	device.power_on()
tv=TV()
ac=Airconditioner()
speaker=Speaker()

speaker=Speaker()
for device in [tv,ac,speaker]:
	remote_control(device)

print(id(tv),id(ac),id(speaker))