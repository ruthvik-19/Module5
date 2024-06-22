
# user input for the number of books purchased
books_purchased = int(input("Please enter the total number of books you purchased this month: "))

# points awarded based on number of books purchased
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30                 
elif books_purchased >= 8:
    points = 60
else:
    points = 0 


# print number of points earned
print("You purchased {} books this month so you earned {} points this month".format(books_purchased, points))              