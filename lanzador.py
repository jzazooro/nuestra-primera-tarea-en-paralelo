from ejercicio import*

def main():
    urls = ["a.com", "b.com", "c.com", "d.com"]
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()   
    print()
    for row in data:
        print(row)