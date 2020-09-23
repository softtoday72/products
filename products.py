products = []
while True: 
	name = input('請輸入商品名: ')
		if name == 'q':
			break
	price = input('請輸入價格: ')
	p = [name, price]       # p = []
	products.append(p)      # p.append(name)
	                        # p.append(price)
	                        # products.append(p)
	                        # 或寫成
	                        # products.append([name, price])
print(products)
for p in products:
	print(p[0])             #印出第一個商品名
	print(p[0], '的價格是', p[1])