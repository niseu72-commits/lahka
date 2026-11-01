# Ask for a temperature in °C (it may have decimals). 
# Print the temperature in °F  using F = C × 9 / 5 + 32, and print True/False for whether it is hotter than 35 °C. 
# Test: 36.5 


celsuis = float(input("Enter a temperature in °C: "))
farenheit = celsuis * 9 / 5 + 32
is_hotter_than_35 = celsuis > 35

print(f"The temperature in °F is: {farenheit}")
print(f"Is the temperature hotter than 35 °C? {is_hotter_than_35}")