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
	sum_len = sum_len + len(d) # len(d) = 每筆單獨留言的長度
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
    if len(d) < 500:
    	new.append(d)
print('一共有', len(new), '筆留言長度小於500')
print(new[0])
print(new[1])
print(new[2])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])