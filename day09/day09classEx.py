from collections import deque
class Branch:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.children = []

    def add_child(self, branch):
        self.children.append(branch)

    def total_balance(self):
        """
        Recursively calculate the total balance
        of this branch and all its children.
        """
        total = self.balance

        for child in self.children:
            total += child.total_balance()

        return total

head_office = Branch("Head Office", 1_000_000)

# Regions
north_region = Branch("North Region", 400_000)
south_region = Branch("South Region", 350_000)

head_office.add_child(north_region)
head_office.add_child(south_region)

# North Branches
cbe1 = Branch("CBE-1", 150_000)
cbe2 = Branch("CBE-2", 180_000)

north_region.add_child(cbe1)
north_region.add_child(cbe2)

# South Branches
cbe3 = Branch("CBE-3", 120_000)
cbe4 = Branch("CBE-4", 160_000)

south_region.add_child(cbe3)
south_region.add_child(cbe4)
transfers = {
    "CBE-1": ["CBE-2", "CBE-3"],
    "CBE-2": ["CBE-4"],
    "CBE-3": ["CBE-4"],
    "CBE-4": []
}


# -------------------------------
# Breadth-First Search (BFS)
# -------------------------------

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            order.append(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


# -------------------------------
# Main Program
# -------------------------------

print("=" * 45)
print("        BANK HIERARCHY REPORT")
print("=" * 45)

print(f"\nTotal Bank Balance: ${head_office.total_balance():,}")

reachable = bfs(transfers, "CBE-1")

print("\nBranches reachable from CBE-1:")
for branch in reachable:
    print(f"  -> {branch}")