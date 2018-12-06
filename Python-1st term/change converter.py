##jared Mcmahon

def change(total_change):
    
    total_change = total_change
    q = total_change // 25
    whats_left = total_change % 25
    d = whats_left / 10
    whats_left = whats_left % 10
    n = whats_left / 5
    whats_left = whats_left % 5
    p = whats_left
    print("quarters: ",q, "\nDimes: ",d, "\nNickles: ",n, "\nCents: ",p)

total_change=int(input("how much change do you have in your pocket: "))
change(total_change)
