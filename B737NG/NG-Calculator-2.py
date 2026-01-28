# Cosmetic 
bold = '\033[1m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'

# Allows the Tech to input the individual values of each portion
D1 = float(input(bold+italic+"D1 = "+end))
D2 = float(input(bold+italic+"D2 = "+end))
D3 = float(input(bold+italic+"D3 = "+end))

# Calculates and displays the overall freeplay and rounds it to the fourth decimal place
H = (1.25*D3)+((D1+D2)/2)
print(bold+italic+f"H = {H:.4f}"+end)

# Allows for Pass and Fail counting while storing each result
Pass = 0
Fail = 0
Results = []
# Thresholds Dictionary defines max values, while Values Dictionary stores the user inputs for later comparison
Thresholds = {
  "D1": 0.066, 
  "D2": 0.066, 
  "D3": 0.056, 
  "H": 0.078
}
Values = {
  "D1": D1, 
  "D2": D2, 
  "D3": D3, 
  "H": H
}

# Checking each value against its threshold, adds to the approriate counter and stores the results
for name, value in Values.items():
  if value > Thresholds[name]:
    Fail+= 1
    Results.append(bold+italic+red+f"{name} failed"+end)
  else:
   Pass +=1
   Results.append(bold+italic+green+f"{name} passed")

# To display either all passed, all failed, or mix of both
if Pass == 4:
  print(bold+italic+green+"All values passed")
elif Fail == 4:
  print(bold+italic+red+"All values failed"+end)
else:
  for result in Results:
    print(result)
