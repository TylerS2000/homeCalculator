homePrice = 400000
interestRate = .05875/12
insurance = 184
propertyTaxes = (.01608*homePrice)/12
downPayment = 90000
monthlyIncome = 9000
term = 360

principal = homePrice - downPayment

mortgageBeforeTaxesAndInsurance = (((interestRate*(1+interestRate)**term))/(((1+interestRate)**term)-1))*principal

mortgageAfterTaxesAndInsurance = mortgageBeforeTaxesAndInsurance + insurance + propertyTaxes

percentOfMonthlyIncome = mortgageAfterTaxesAndInsurance/monthlyIncome

print("Payment: "+str(mortgageAfterTaxesAndInsurance) + "\n" + "Percent of Monthly Payment: " + str(percentOfMonthlyIncome))