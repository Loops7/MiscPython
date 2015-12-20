

f = open('stocksymbols.txt', 'w') 

with open('nasdaqlisted.txt', 'r') as nasdaq:
    for line in nasdaq:
        symbol = line.split("|")[0].strip()
        if len(symbol) < 6: 
            print >> f, symbol

f.close()    