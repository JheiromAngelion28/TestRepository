
total = int(input('Enter your balance'))
amount = 50
discount = .10
if total > 50:
    print (total - discount)
else: 
    print(total)
    

total_bill  = float(input('Enter the total bill'))
if total > 50:
    discount = total_bill * 0.1
    final_bill = total_bill - discount
    print(f'Discount applied! Your final bill is f{final_bill}.')
else:
    print(f'No accountd applied. Your total bill is{total_bill}')



total = int(input('Enter your age'))
age= 65 
age= 18 and 64
age= 13 and 17
age= 0 and 12
if age <= 12:
    print('Price is 15 pounds')
elif age <= 17:
    print('Price is 10 pounds')
elif age <= 64:
    print('Price is 7 pounds')
elif age >= 65:
    print('Price is 5 pounds')
else:
    print("invalid input")
