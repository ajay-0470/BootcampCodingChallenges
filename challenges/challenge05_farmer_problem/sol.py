land = 80
parts = 5
acres = land / parts

tomato_yield = (0.3 * acres * 10) + (0.7 * acres * 12)
tomato_sales = tomato_yield * 1000 * 7

potato_yield = acres * 10
potato_sales = potato_yield * 1000 * 20

cabbage_yield = acres * 14
cabbage_sales = cabbage_yield * 1000 * 24

sunflower_yield = acres * 0.7
sunflower_sales = sunflower_yield * 1000 * 200

sugarcane_yield = acres * 45
sugarcane_sales = sugarcane_yield *4000

total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
organic_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

print("Total sales =", total_sales)
print("Chemical-free sales after 11 months =", organic_sales)