source = input()
destination = input()

maxFlights = int(input())
numTickets = int(input())

tickets = {}

for i in range(numTickets):
	src, dest, price = [x for x in input().strip().split(',')]
	price = int(price)

	tickets[(src, dest)] = price



from collections import defaultdict

goings = defaultdict(list)

for tkt in tickets:
	goings[tkt[0]].append(tkt[1])


ans = 2**31-1
path = []
def DFS(curr, count, currPrice, trav):
	global path
	global ans


	if curr==destination:
		if currPrice<ans:
			ans = currPrice
			path = trav.copy()
		return

	if count==maxFlights:
		return


	for dest in goings[curr]:
		if dest not in trav:
			DFS(dest, count+1, currPrice+tickets[(curr, dest)], trav+[dest])

			


DFS(source, 0, 0, [source])

if ans==2**31-1:
	print('Error')
else:
	print(ans, path)



