#EXPERIMENT(2)_CADIDATE_ELIMINATION
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]
# Initialize S and G
S = data[0][:-1]
G = [['?' for _ in range(len(S))]]

for instance in data:
    if instance[-1] == "Yes":
        for i in range(len(S)):
            if S[i] != instance[i]:
                S[i] = '?'
        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(len(S)))]
    else:
        new_G = []
        for g in G:
            for i in range(len(S)):
                if g[i] == '?' and S[i] != instance[i]:
                    temp = g.copy()
                    temp[i] = S[i]
                    new_G.append(temp)
        G = new_G
print("Specific Boundary (S):", S)
print("General Boundary (G):", G)
