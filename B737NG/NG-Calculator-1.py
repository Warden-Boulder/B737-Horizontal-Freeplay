# Cosmetic
bold = '\033[1m'
end = '\033[0m'
green = '\033[92m'
italic = '\033[3m'
red = '\033[31m'

# Input Values
D1 = float(input(bold+italic+"D1 = "+end))
D2 = float(input(bold+italic+"D2 = "+end))
D3 = float(input(bold+italic+"D3 = "+end))

# Pass/Fail Storage
Pass = 0
Fail = 0
Results = [] 

# Calculations
H = (1.25*D3)+((D1+D2)/2)
print(bold+italic+f"H = {H:.4f}"+end)

# Threshold Messages, Checks, Storage
def check_value(name, value, threshold):
  global Pass, Fail
  if value > threshold:
    Fail += 1
    Results.append(bold+italic+red+ f"{name} Failed"+end)
  else:
    Pass += 1
    Results.append(bold+italic+green +f"{name} Passed"+end)
# Check Values against Threshold Conditins                 
check_value("D1", D1, 0.066)
check_value("D2", D2, 0.066)
check_value("D3", D3, 0.056)
check_value("H", H, 0.078)

# Summary of Results                  
if Pass == 4:
  print(bold+italic+green+"All values passed"+end)
elif Fail == 4: 
  print(bold+italic+red+"All values failed"+end)
else:
  for Result in Results:
    print(Result)
