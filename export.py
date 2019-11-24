import csv

class CSV:
    
    def __init__(self, gamelogs, year):
        self.gamelogs = gamelogs
        self.year = year

    def generate_csv(self):
        file_name = str(self.year)+'-to-latest_gamelogs.csv'
        if self.gamelogs:   
            try:
                with open(file_name, 'w', newline='') as csv_doc:
                    writer = csv.writer(csv_doc)
                    for data in self.gamelogs:
                        for logs in data:
                            writer.writerow(logs)
            except:
                print('file write error')
        else:
            print('no data... try a different year')

        
