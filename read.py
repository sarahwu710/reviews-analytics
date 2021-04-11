data = []
count = 0
with open('reviews.txt', 'r', encoding="utf-8") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 2 == 0:
		    print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d) # len(d) = 所有留言的長度
print('留言的平均長度為', sum_len/len(data))
