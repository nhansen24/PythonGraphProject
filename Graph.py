# LAT LONG to miles (multiply dif by 69) No joke
# Euclidean Graph example (diagonal distance)
class Graph:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)


space_needle = Graph("Space needle", 47.620519, -122.349291)
delhi = Graph("New Delhi", 28.6448, 77.216721)
jaipur = Graph("Jaipur", 26.92207, 75.778885)
varanasi = Graph("Varanasi", 25.321684, 82.987289)
mumbai = Graph("Mumbai", 19.07283, 72.88261)
chennai = Graph("Chennai", 13.067439, 80.237617)
hyderabad = Graph("Hyderabad", 17.387140, 78.491684)
kolkata = Graph("Kolkata", 22.572645, 88.363892)
bengaluru = Graph("Bengaluru", 12.972442, 77.580643)

euclidean_graph = {

    delhi: {(jaipur, 2.243918), (varanasi, 6.65902), (mumbai, 10.507479), (chennai, 15.867576), (hyderabad, 11.329626),
            (kolkata, 12.693718), (bengaluru, 15.676582)},
    jaipur: {(mumbai, 8.366539), (delhi, 2.243918)},
    varanasi: {(delhi, 6.65902), (mumbai, 11.88077)},
    mumbai: {(delhi, 10.507479), (jaipur, 8.366539), (varanasi, 11.88077), (hyderabad, 5.856898), (kolkata, 15.87195),
             (bengaluru, 7.699756)},
    chennai: {(delhi, 15.867576), (kolkata, 12.50541), (hyderabad, 4.659195), (bengaluru, 2.658671)},
    hyderabad: {(delhi, 11.329626), (mumbai, 5.856898), (chennai, 4.659195), (bengaluru, 4.507721),
                (kolkata, 11.151231)},
    kolkata: {(delhi, 12.693718), (mumbai, 15.87195), (chennai, 12.50541), (hyderabad, 11.151231),
              (bengaluru, 14.437532)},
    bengaluru: {(delhi, 15.676582), (mumbai, 7.699756), (chennai, 2.658671), (hyderabad, 4.507721),
                (kolkata, 14.437532)}
}


# Manhattan structure only allows for x y movement through a grid structure.
class ManhattanGraph:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)

    def __lt__(self, other):
        return self.name < other.name


thirty_third_and_madison = ManhattanGraph("33rd Street and Madison Avenue", 33, 4)
thirty_third_and_fifth = ManhattanGraph("33rd Street and 5th Avenue", 33, 5)
manhattan_mall = ManhattanGraph("Manhattan Mall", 33, 6)
penn_station = ManhattanGraph('Penn Station', 33, 7)
thirty_fourth_and_madison = ManhattanGraph("34th Street and Madison Avenue", 34, 4)
empire_state_building = ManhattanGraph('Empire State Building', 34, 5)
herald_square = ManhattanGraph('Herald Square', 34, 6)
thirty_fourth_and_seventh = ManhattanGraph("34th Street and 7th Avenue", 34, 7)
thirty_fifth_and_madison = ManhattanGraph("35th Street and Madison Avenue", 35, 4)
cuny_grad_center = ManhattanGraph("CUNY Graduate Center", 35, 5)
thirty_fifth_and_sixth = ManhattanGraph("35th Street and 6th Avenue", 35, 6)
macys = ManhattanGraph("Macy's", 35, 7)
thirty_sixth_and_madison = ManhattanGraph("36th Street and Madison Avenue", 36, 4)
thirty_sixth_and_fifth = ManhattanGraph("36th Street and 5th Avenue", 36, 5)
thirty_sixth_and_sixth = ManhattanGraph("36th Street and 6th Avenue", 36, 6)
thirty_sixth_and_seventh = ManhattanGraph("36th Street and 7th Avenue", 36, 7)
morgan_library = ManhattanGraph("Morgan Library and Museum", 37, 4)
thirty_seventh_and_fifth = ManhattanGraph("37th Street and 5th Avenue", 37, 5)
thirty_seventh_and_sixth = ManhattanGraph("37th Street and 6th Avenue", 37, 6)
thirty_seventh_and_seventh = ManhattanGraph("37th Street and 7th Avenue", 37, 7)
thirty_eighth_and_madison = ManhattanGraph("38th Street and Madison Avenue", 38, 4)
thirty_eighth_and_fifth = ManhattanGraph("38th Street and Fifth Avenue", 38, 5)
thirty_eighth_and_sixth = ManhattanGraph("38th Street and Sixth Avenue", 38, 6)
thirty_eighth_and_seventh = ManhattanGraph("38th Street and Seventh Avenue", 38, 7)
mexican_consulate = ManhattanGraph("Mexican Consulate General", 39, 4)
thirty_ninth_and_fifth = ManhattanGraph("39th Street and Fifth Avenue", 39, 5)
thirty_ninth_and_sixth = ManhattanGraph("39th Street and Sixth Avenue", 39, 6)
thirty_ninth_and_seventh = ManhattanGraph("39th Street and Seventh Avenue", 39, 7)
fortieth_and_madison = ManhattanGraph("40th Street and Madison Avenue", 40, 4)
fortieth_and_fifth = ManhattanGraph("40th Street and Fifth Avenue", 40, 5)
bryant_park_south = ManhattanGraph("Bryant Park South", 40, 6)
times_square_south = ManhattanGraph("Times Square - South", 40, 7)
forty_first_and_madison = ManhattanGraph("41st Street and Madison Avenue", 41, 4)
mid_manhattan_library = ManhattanGraph("Mid-Manhattan Library", 41, 5)
kinokuniya = ManhattanGraph("Kinokuniya", 41, 6)
times_square = ManhattanGraph("Times Square", 41, 7)
grand_central_station = ManhattanGraph("Grand Central Station", 42, 4)
library = ManhattanGraph("New York Public Library", 42, 5)
bryant_park_north = ManhattanGraph("Bryant Park North", 42, 6)
times_square_north = ManhattanGraph("Times Square - North", 42, 7)

manhattan_graph = {
    thirty_third_and_madison: {(thirty_fourth_and_madison, 1), (thirty_third_and_fifth, 3)},
    thirty_third_and_fifth: {(thirty_third_and_madison, 3), (manhattan_mall, 3), (empire_state_building, 1)},
    manhattan_mall: {(thirty_third_and_fifth, 3), (penn_station, 3), (herald_square, 1)},
    penn_station: {(manhattan_mall, 3), (thirty_fourth_and_seventh, 1)},
    thirty_fourth_and_madison: {(thirty_third_and_madison, 1), (empire_state_building, 3),
                                (thirty_fifth_and_madison, 1)},
    empire_state_building: {(thirty_fourth_and_madison, 3), (herald_square, 3), (thirty_third_and_fifth, 1),
                            (cuny_grad_center, 1)},
    herald_square: {(empire_state_building, 3), (thirty_fourth_and_seventh, 3), (manhattan_mall, 1),
                    (thirty_fifth_and_sixth, 1)},
    thirty_fourth_and_seventh: {(herald_square, 3), (macys, 1), (penn_station, 1)},
    thirty_fifth_and_madison: {(thirty_fourth_and_madison, 1), (thirty_sixth_and_madison, 1), (cuny_grad_center, 3)},
    cuny_grad_center: {(thirty_fifth_and_madison, 3), (thirty_fifth_and_sixth, 3), (empire_state_building, 1),
                       (thirty_sixth_and_fifth, 1)},
    thirty_fifth_and_sixth: {(cuny_grad_center, 3), (macys, 3), (herald_square, 1), (thirty_sixth_and_sixth, 1)},
    macys: {(thirty_fifth_and_sixth, 3), (thirty_fourth_and_seventh, 1), (thirty_sixth_and_seventh, 1)},
    thirty_sixth_and_madison: {(thirty_sixth_and_fifth, 3), (thirty_fifth_and_madison, 1), (morgan_library, 1)},
    thirty_sixth_and_fifth: {(thirty_sixth_and_madison, 3), (thirty_sixth_and_sixth, 3), (cuny_grad_center, 1),
                             (thirty_seventh_and_fifth, 1)},
    thirty_sixth_and_sixth: {(thirty_sixth_and_fifth, 3), (thirty_sixth_and_seventh, 3), (thirty_fifth_and_sixth, 1),
                             (thirty_seventh_and_sixth, 1)},
    thirty_sixth_and_seventh: {(thirty_sixth_and_sixth, 3), (macys, 1), (thirty_seventh_and_seventh, 1)},
    morgan_library: {(thirty_seventh_and_fifth, 3), (thirty_sixth_and_madison, 1), (thirty_eighth_and_madison, 1)},
    thirty_seventh_and_fifth: {(morgan_library, 3), (thirty_seventh_and_sixth, 3), (thirty_sixth_and_fifth, 1),
                               (thirty_eighth_and_fifth, 1)},
    thirty_seventh_and_sixth: {(thirty_seventh_and_fifth, 3), (thirty_seventh_and_seventh, 3),
                               (thirty_sixth_and_sixth, 1)},
    thirty_seventh_and_seventh: {(thirty_seventh_and_sixth, 3), (thirty_sixth_and_seventh, 1),
                                 (thirty_eighth_and_seventh, 1)},
    thirty_eighth_and_madison: {(thirty_eighth_and_fifth, 3), (morgan_library, 1), (mexican_consulate, 1)},
    thirty_eighth_and_fifth: {(thirty_eighth_and_madison, 3), (thirty_eighth_and_sixth, 3),
                              (thirty_seventh_and_fifth, 1), (thirty_ninth_and_fifth, 1)},
    thirty_eighth_and_sixth: {(thirty_eighth_and_fifth, 3), (thirty_eighth_and_seventh, 3),
                              (thirty_seventh_and_sixth, 1), (thirty_ninth_and_sixth, 1)},
    thirty_eighth_and_seventh: {(thirty_eighth_and_sixth, 3), (thirty_seventh_and_seventh, 1),
                                (thirty_ninth_and_seventh, 1)},
    mexican_consulate: {(thirty_ninth_and_fifth, 3), (thirty_eighth_and_madison, 1), (fortieth_and_madison, 1)},
    thirty_ninth_and_fifth: {(mexican_consulate, 3), (thirty_ninth_and_sixth, 3), (thirty_eighth_and_fifth, 1),
                             (fortieth_and_fifth, 1)},
    thirty_ninth_and_sixth: {(thirty_ninth_and_fifth, 3), (thirty_ninth_and_seventh, 3), (thirty_eighth_and_sixth, 1),
                             (bryant_park_south, 1)},
    thirty_ninth_and_seventh: {(thirty_ninth_and_sixth, 3), (thirty_eighth_and_seventh, 1), (times_square_south, 1)},
    fortieth_and_madison: {(fortieth_and_fifth, 3), (mexican_consulate, 1), (forty_first_and_madison, 1)},
    fortieth_and_fifth: {(fortieth_and_madison, 3), (bryant_park_south, 3), (thirty_ninth_and_fifth, 1)},
    bryant_park_south: {(fortieth_and_fifth, 3), (times_square_south, 3), (thirty_ninth_and_sixth, 1), (kinokuniya, 1)},
    times_square_south: {(bryant_park_south, 3), (times_square, 1), (thirty_ninth_and_seventh, 1)},
    forty_first_and_madison: {(fortieth_and_madison, 1), (grand_central_station, 1), (mid_manhattan_library, 3)},
    mid_manhattan_library: {(forty_first_and_madison, 3), (library, 1), (fortieth_and_fifth, 1)},
    kinokuniya: {(times_square, 3), (bryant_park_north, 1), (bryant_park_south, 1)},
    times_square: {(kinokuniya, 3), (times_square_north, 1), (times_square_south, 1)},
    grand_central_station: {(library, 3), (forty_first_and_madison, 1)},
    library: {(mid_manhattan_library, 1), (grand_central_station, 3), (bryant_park_north, 3)},
    bryant_park_north: {(library, 3), (times_square_north, 3), (bryant_park_south, 1)},
    times_square_north: {(times_square, 1), (bryant_park_north, 3)}
}
