# Question 9:- Ask the user for:
# Principal (P)
# Rate (R)
# Time (T)
# Convert all to float and calculate simple interest:
# SI = (P × R × T) / 100

P = float(input("Enter the Principal value: "))
R = float(input("Enter the Rate Value: "))
T = float(input("Enter the time: "))

SI = (P*R*T) / 100

print("SI value: ", SI)