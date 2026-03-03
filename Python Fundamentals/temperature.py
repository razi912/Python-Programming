'''Ask the user for a temperature in Celsius (string input). Convert it to ,
then calculate and print temperature in Fahrenheit.
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32'''

c = input("enter temperature in celsius: ")
c = int(c)

f = (c*(9/5))+32
print(int(f))

