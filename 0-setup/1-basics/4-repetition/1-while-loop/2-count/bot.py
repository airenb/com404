print("How many live cables must I avoid?")
cables_avoided = int(input())

live_cables = 0

while (live_cables < cables_avoided):
    live_cables = live_cables + 1 
    print("Avoiding... Done!" ,live_cables, "live cables avoided")
    
    
print("All live cables have been avoided.")
