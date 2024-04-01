import sys

total_rmse = 0
br = 0

for rmse_arg in sys.argv[1:]:
    rmse = float(rmse_arg)
    print(f"RMSE: {rmse}")
    
    total_rmse += rmse
    br += 1

print(f"\n\nFinal RMSE: {total_rmse/br}")