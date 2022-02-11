import os
import sys
import re
import random


price=25
qty = random.randint(50,500)
amount=qty*price

if amount>=10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
elif amount>=5000:
    print ("5% discount applicable")
    discount=amount*5/100
    amount=amount-discount
elif amount>=2000:
    print ("2% discount applicable")
    discount=amount*2/100
    amount=amount-discount
elif amount>=1000:
    print ("1% discount applicable")
    discount=amount*1/10011
    amount=amount-discount
else:
    print("go to hell")

print ("amount payable:",amount)