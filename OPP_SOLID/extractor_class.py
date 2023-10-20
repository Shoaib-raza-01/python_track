class DataExtractor:
    def __init__(self, file_name, col1, col2):
        self.file_name = file_name
        self.col1 = col1
        self.col2 = col2

    def extract_data(self):
        data = []
        with open(self.file_name, 'r') as file:
            next(file)
            for line in file:
                cols = line.strip().split(',')
                if len(cols) >= max(self.col1, self.col2):
                    data.append((float(cols[self.col1]), float(cols[self.col2])))
        return data