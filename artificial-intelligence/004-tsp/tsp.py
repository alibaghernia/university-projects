def solver(graph, start_city=0):
    current_city = start_city
    passed_city = [current_city]

    next_city = None
    min_cost = None

    for _ in range(len(graph)):
        city = graph[current_city]

        for city_index, city_cost in enumerate(city):

            if city_index in passed_city:
                continue

            if min_cost == None:
                min_cost = city_cost
                next_city = city_index

            if min_cost > city_cost:
                min_cost = city_cost
                next_city = city_index

        if next_city != None:
            current_city = next_city
            passed_city.append(current_city)
            next_city = None
            min_cost = None

    return passed_city


if __name__ == "__main__":

    # matrix representation of graph
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    start_from = 0
    print(solver(graph, start_from))
