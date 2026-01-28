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

print(f"{'Variable': <10} {'Value': <10} {'Threshold': <10} {'Result': <10}")
print("-"*40)
H = (1.25*D3)+((D1+D2)/2)

def value_check(value, threshold):
  if value < threshold:
    return bold+italic+green+"Passed"+end
  else:
    return bold+italic+red+"Failed"+end

rows = [
  ("D1", f"{D1:.4f}", "0.066", value_check(D1, 0.066)),
  ("D2", f"{D2:.4f}", "0.066", value_check(D2, 0.066)),
  ("D1", f"{D3:.4f}", "0.056", value_check(D3, 0.056)),
  ("H", f"{H:.4f}", "0.078", value_check(H, 0.078)),
]

for var, value, limit, result in rows:
  print(f"{var:<10} {value:<10} {limit:<10} {result:<10}")
