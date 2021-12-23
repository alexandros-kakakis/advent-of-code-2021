from day_19_func import load_scanners, return_scanner_graph, find_zero_position

scanners = load_scanners()
scanner_graph = return_scanner_graph(scanners)

for i in range(len(scanners)):
    print(i, find_zero_position(i, scanner_graph))

