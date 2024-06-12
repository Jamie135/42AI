class CsvReader:

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.data = []
        self.header_data = None


    # open/created filename as read mode and parse it using parse_file 
    def __enter__(self):
        try:
            self.file = open(self.filename, mode='r')
            self.parse_file()
        except FileNotFoundError:
            return None
        except Exception as e:
            return None
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
    

    # our approach will be to store all data (header or values) in a list
    # trim them and split them by sep
    def parse_file(self):
        # store each line of the file in a list []
        lines = self.file.readlines()
        if not lines:
            raise ValueError("Empty file")

        # remove skipped lines with slicing notation [x:y]
        lines = lines[self.skip_top:len(lines) - self.skip_bottom]

        # store header data by splitting based on sep and trimming all the border spaces
        # update lines by excluding the header from the data
        if self.header:
            self.header_data = lines[0].strip().split(self.sep)
            lines = lines[1:]

        # process data
        for line in lines:
            line_data = line.strip().split(self.sep)
            if self.header and len(line_data) != len(self.header_data):
                raise ValueError("Mismatch between number of fields and number of records")
            self.data.append(line_data)

        # Check for consistency in data length
        if not all(len(row) == len(self.data[0]) for row in self.data):
            raise ValueError("Records have different lengths")
    

    def getdata(self):
        return self.data


    def getheader(self):
        if self.header:
            return self.header_data
        return None


# Example usage:
if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        if file:
            data = file.getdata()
            header = file.getheader()
            print("Header:", header)
            print("Data:", data)
        else:
            print("File is corrupted or not found")

    with CsvReader('bad.csv', header=True) as file:
        if file is None:
            print("File is corrupted or not found")
