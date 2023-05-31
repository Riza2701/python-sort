def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

players = [
    {
        "nama": "Kylian Mbappe",
        "klub": "Paris Saint Germain",
        "gol": 28
    },
    {
        "nama": "Victor Osimhen",
        "klub": "Napoli",
        "gol": 22
    },
    {
        "nama": "Robert Lewandowski",
        "klub": "Bayern Munich",
        "gol": 40
    },
    {
        "nama": "Erling Haaland",
        "klub": "Borussia Dortmund",
        "gol": 52
    },
    {
        "nama": "Christopher Nkunku",
        "klub": "RB Leipzig",
        "gol": 33
    }
]

goals = [player["gol"] for player in players]
selection_sort(goals)

sorted_players = []
for goal in goals:
    for player in players:
        if player["gol"] == goal:
            sorted_players.append(player)
            break

# Menampilkan daftar pemain yang telah diurutkan
for i, player in enumerate(sorted_players):
    print(f'{i+1}. {player["nama"]} - {player["klub"]} - {player["gol"]} goals')