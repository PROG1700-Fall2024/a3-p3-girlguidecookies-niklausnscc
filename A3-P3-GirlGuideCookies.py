#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:w0414211      
#Student Name: niklaus guenther 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #Asks for the number of guides
    while True:
        try:
            numGuides = int(input("Enter the number of guides who sold cookies: "))
            if numGuides < 0:
                print("Number of guides cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    #Collects names and sales data
    names = []
    sales = []

    for i in range(numGuides):
        name = input(f"Enter the name of guide {i + 1}: ")
        while True:
            try:
                boxes = int(input(f"Enter the number of boxes sold by {name}: "))
                if boxes < 0:
                    print("Number of boxes cannot be negative. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        names.append(name)
        sales.append(boxes)

    #Calculates average sales
    if numGuides > 0:
        totalSales = sum(sales)
        averageSales = totalSales / numGuides
    else:
        totalSales = 0
        averageSales = 0

    #Determine prizes
    highestSales = max(sales) if sales else 0
    prizes = []

    for i in range(numGuides):
        if sales[i] == highestSales:
            prizes.append("Trip to the Girl Guide Jamboree")
        elif sales[i] > averageSales:
            prizes.append("Badge")
        elif sales[i] > 0:
            prizes.append("Share of leftover cookies")
        else:
            prizes.append("No prize")

    print("\n=== Girl Guide Cookie Sell-off Results ===")
    for i in range(numGuides):
        print(f"{names[i]} sold {sales[i]} boxes and won: {prizes[i]}")
    print(f"\nTotal boxes sold: {totalSales}")
    print(f"Average boxes sold: {averageSales:.2f}")
    # YOUR CODE ENDS HERE

main()