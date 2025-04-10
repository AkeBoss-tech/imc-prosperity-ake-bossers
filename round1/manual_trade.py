trading_table = [
    [1, 1.45, 0.52, 0.72],
    [0.7, 1, 0.31, 0.48],
    [1.95, 3.1, 1, 1.49],
    [1.34, 1.98, 0.64, 1]
]

#Snowball = 0, Pizza = 1, Silicon Nugget = 2, Seashells = 3
seashells = 3
max_amount = 0 
trading_order = []

for i in range(4):
    amount1 = trading_table[seashells][i]
    for j in range(4):
        amount2 = amount1 * trading_table[i][j]
        for k in range(4):
            amount3 = amount2 * trading_table[j][k]
            for l in range(4):
                amount4 = amount3 * trading_table[k][l]
                final_amount = amount4 * trading_table[l][seashells]

                if final_amount > max_amount:
                    max_amount = final_amount
                    trading_order = [i, j , k , l]

print(f"Number of Seashells: {max_amount}")
print(f"Trading Order: {trading_order}")


