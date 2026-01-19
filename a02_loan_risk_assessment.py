# Name: Porter Johnson
# Enter your python code below. Replace this line with a description.
#establishes and asks for variables
category = ""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
annual_income = float(input("Enter your annual income in dollars: "))
total_monthly_debt = float(input("Enter your total monthly debt payments in dollars: "))
dti = total_monthly_debt / (annual_income/12)
#Rounds Dti to nearest hundreth.
round(dti, 2)
#Assigns a category to the DTI dependant on the DTI amount.
if dti < .20:
    category = "Low Risk"
elif .20 <= dti < .36:
    category = "Moderate Risk"
elif .36 <= dti < .50:
    category = "Elevated Risk"
elif dti >= .50: 
    category = "High Risk"
#print statement
print(f"{first_name} {last_name} has a DTI of {dti}. The associated category is: {category}")
