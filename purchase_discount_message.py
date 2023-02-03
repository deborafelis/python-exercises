purchase = int(input('Inform how much is the purchase: '))
if purchase >= 1000:
    discount = purchase * 0.10
    final_payment = purchase - discount
    print(f'You received a 10% discount for your ${purchase:.2f} purchase. For that, you will pay ${final_payment:.2f}. ') 
else:
    discount = purchase * 0.05
    final_payment = purchase - discount
    print(f'You received a 5% discount for your ${purchase:.2f} purchase. For that, you will pay ${final_payment:.2f}.')
