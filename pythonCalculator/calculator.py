homePrice = int(input("Enter the price of the home: "))
interestRate = float(input("Enter the interest rate: "))/12
downPayment = int(input("Enter your down payment: "))
# homePrice = 400000
# interestRate = .05875/12
# downPayment = 90000

insurance = 184
propertyTaxes = (.01608*homePrice)/12
monthlyIncome = 9000
term = 360

principal = homePrice - downPayment

mortgageBeforeTaxesAndInsurance = (((interestRate*(1+interestRate)**term))/(((1+interestRate)**term)-1))*principal

mortgageAfterTaxesAndInsurance = mortgageBeforeTaxesAndInsurance + insurance + propertyTaxes

percentOfMonthlyIncome = mortgageAfterTaxesAndInsurance/monthlyIncome
maxPayment = monthlyIncome*.28



print("\n"+"Results"+"---------------------"+"\n"
      "Payment: $"+str(mortgageAfterTaxesAndInsurance) + "\n" + 
      "Percent of Monthly Payment: " + str(percentOfMonthlyIncome*100)+"%" + "\n" +
      "Affordable: "+str(percentOfMonthlyIncome<=.28) + "\n" +
      "Max Affordable Payment Per Month: $" +str(maxPayment) + "\n")