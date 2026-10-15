# ---------- Part 1: City navigation using a weighted graph ----------

class CityMap:
    def __init__(self):
        self.cities = []
        self.roads = []

    def add_road(self, city1, city2, distance):
        if city1 not in self.cities:
            self.cities.append(city1)
        if city2 not in self.cities:
            self.cities.append(city2)

        # Each road connects two cities and has a distance.
        self.roads.append([city1, city2, distance])

    def shortest_route(self, start, destination):
        distances = {}
        previous = {}
        unvisited = self.cities.copy()

        for city in self.cities:
            distances[city] = float("inf")

        distances[start] = 0

        while unvisited:
            # Find the unvisited city with the smallest known distance.
            current = None
            for city in unvisited:
                if current is None or distances[city] < distances[current]:
                    current = city

            if distances[current] == float("inf"):
                break

            unvisited.remove(current)

            if current == destination:
                break

            # Check roads that lead from the current city.
            for road in self.roads:
                city1, city2, distance = road

                if city1 == current:
                    neighbor = city2
                elif city2 == current:
                    neighbor = city1
                else:
                    continue

                if neighbor in unvisited:
                    new_distance = distances[current] + distance

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current

        if distances[destination] == float("inf"):
            return None, float("inf")

        # Rebuild the route by following previous cities backward.
        route = []
        current = destination

        while current != start:
            route.append(current)
            current = previous[current]

        route.append(start)
        route.reverse()

        return route, distances[destination]


def demonstrate_navigation():
    city_map = CityMap()

    city_map.add_road("Central", "Museum", 4)
    city_map.add_road("Central", "Park", 2)
    city_map.add_road("Park", "Museum", 1)
    city_map.add_road("Park", "Airport", 7)
    city_map.add_road("Museum", "Airport", 3)

    route, distance = city_map.shortest_route("Central", "Airport")

    print("CITY NAVIGATION")
    print("Shortest route:", " -> ".join(route))
    print("Total distance:", distance, "km")


# ---------- Part 2: Text compression using a Huffman tree ----------

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


def count_frequencies(text):
    frequencies = {}

    for character in text:
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1

    return frequencies


def build_huffman_tree(text):
    frequencies = count_frequencies(text)
    nodes = []

    for character in frequencies:
        nodes.append(HuffmanNode(character, frequencies[character]))

    while len(nodes) > 1:
        # Find and remove the two nodes with the smallest frequencies.
        smallest = min(nodes, key=lambda node: node.frequency)
        nodes.remove(smallest)

        second_smallest = min(nodes, key=lambda node: node.frequency)
        nodes.remove(second_smallest)

        parent = HuffmanNode(
            None,
            smallest.frequency + second_smallest.frequency
        )
        parent.left = smallest
        parent.right = second_smallest
        nodes.append(parent)

    return nodes[0]


def make_codes(node, prefix, codes):
    if node.character is not None:
        codes[node.character] = prefix if prefix else "0"
        return

    make_codes(node.left, prefix + "0", codes)
    make_codes(node.right, prefix + "1", codes)


def demonstrate_huffman():
    text = "banana bandana"
    tree = build_huffman_tree(text)

    codes = {}
    make_codes(tree, "", codes)

    encoded_text = ""
    for character in text:
        encoded_text += codes[character]

    print("\nHUFFMAN CODING")
    print("Original text:", repr(text))
    print("Character codes:")

    for character in codes:
        label = "space" if character == " " else character
        print(label, ":", codes[character])

    print("Encoded bits:", encoded_text)


def main():
    demonstrate_navigation()
    demonstrate_huffman()


if __name__ == "__main__":
    main()