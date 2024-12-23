from math import sqrt

class KnnModel:
    data = []
    target = []
    number_of_neighbors = 0

    def __init__(self, number_of_neighbors):
        self.number_of_neighbors = number_of_neighbors

    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)):
            distance += (row1[i] - row2[1]) ** 2
        return sqrt(distance)

    def hello(self):
        print("Hello, World")

    def fit(self, train, target):
        self.data = train
        self.target = target

    def get_neightors(self, test_row):
        distance = list()
        for train_row in self.data:
            dist = self.euclidean_distance(test_row, train_row)
            distance.append((train_row, dist))
        distance.sort(key = lambda tup: tup[1])
        neighbors = list()
        for i in range(self.number_of_neighbors):
            neighbors.append(distance[i][0])
        return neighbors

    def predict(self, row):
        neighbors = self.get_neightors(row)
        for neighbor in neighbors:
            print(neighbor)
        output_values = [row[-1] for row in neighbors]
        prediction = max(set(output_values), key=output_values.count)
        return prediction

if __name__ == "__main__":
    h = KnnModel(1)
    h.hello()

# https://firework-ham.tistory.com/27