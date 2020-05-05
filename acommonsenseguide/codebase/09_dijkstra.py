class City:

    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price_info):
        self.routes[city] = price_info


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)


def dijkstra(starting_city, other_cities):
    routes_from_city = {starting_city: [0, starting_city]}

    for city in other_cities:
        routes_from_city[city] = [None, None]

    visited_cities = []
    current_city = starting_city

    while current_city:
        visited_cities.append(current_city)
        for city, price_info in current_city.routes.items():
            if routes_from_city[city][0] is None or \
                    routes_from_city[city][0] > price_info + routes_from_city[current_city][0]:
                routes_from_city[city] = [price_info + routes_from_city[current_city][0], current_city]
        current_city = None
        cheapest_route_from_current_city = None

        for city, routes_info in routes_from_city.items():
            if city is starting_city or routes_info[0] is None or city in visited_cities:
                pass
            elif cheapest_route_from_current_city is None or routes_info[0] < cheapest_route_from_current_city:
                cheapest_route_from_current_city = routes_info[0]
                current_city = city

    return routes_from_city


routes = dijkstra(atlanta, [boston, chicago, denver, el_paso])
for city_to_print, route_to_print in routes.items():
    print("{0} : {1}".format(city_to_print.name, route_to_print[0]))
