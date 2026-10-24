# Exercise 1: Campus Resource Tracker

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(res_list):
    if not res_list:
        print("No resources found.")
        return
    print(f"\n{'ID':<6} {'Name':<15} {'Category':<15} {'Quantity':<10}")
    print("-" * 50)
    for item in res_list:
        print(f"{item[0]:<6} {item[1]:<15} {item[2]:<15} {item[3]:<10}")

def search_by_category(res_list, category):
    matches = [item for item in res_list if item[2].lower() == category.lower()]
    print(f"\n--- Category: {category} ---")
    display_resources(matches)

def find_unavailable(res_list):
    unavailable = [item for item in res_list if item[3] <= 0]
    print("\n--- Unavailable Resources (Quantity <= 0) ---")
    display_resources(unavailable)

# Test run
if __name__ == "__main__":
    display_resources(resources)
    search_by_category(resources, "Electronics")
    find_unavailable(resources)