price = int(input("How much did the meal cost?"))

tip_1 = price*0.10
final_1 = price + tip_1

tip_2 = price*0.05
final_2 = price + tip_2

if price > 100:
    print("The final sum to pay is", final_1 , "SEK")

else:
    print("The final sum to pay is", final_2 , "SEK")





#ask a question
#if price lower than 100 SEK - tip 5%
#otherwise - tip 10%
#