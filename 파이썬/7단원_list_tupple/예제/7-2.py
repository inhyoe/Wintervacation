bts = []
bts.append("v") # append함수로 추가할 수 있다.
print(bts)

# ---------------------------------------------------------------------------

print(list(range(5))) # range함수를 이용해서 리스트를 생성 할 수 있다.

# ---------------------------------------------------------------------------

numbers = [10,20,30] + [40,50,60]
print(numbers)  # 리스트를 합칠 수도 있다,

# ---------------------------------------------------------------------------

bts = ['a','b','c','d','e','f','g']
print('a' in bts) # true     원소가 리스트 안에 있는지 검사하는 함수.
print('k' in bts) # false
print('k' not in bts) # true 