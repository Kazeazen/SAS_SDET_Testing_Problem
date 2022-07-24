'''
Author: James Thomason
Date: 7/21/2022

Problem Description:

A developer has implemented a program that reads a large list of date-time values from a file and writes to a separate file the list of unique, valid date-time values (no duplicates). A valid date-time value matches the following format (ISO 8601):

YYYY-MM-DDThh:mm:ssTZD

Where:
• YYYY = four-digit year
• MM = two-digit month (01 through 12)
• DD = two-digit day of month (01 through 31)
• hh = two digits of hour (00 through 23)
• mm = two digits of minute (00 through 59)
• ss = two digits of second (00 through 59)
• TZD = time zone designator (“Z” for GMT or +hh:mm or -hh:mm)

The developer was told that it was not necessary to perform semantic validation of the data-time value. In other words, the date-time value "9999-02-31T12:34:56+12:34" should be considered valid by your program even though February 31, 9999 is not a legitimate date.

Your job is to validate the output of this application.

* Guidelines and Requirements
* You need to provide data from the proposed developer’s program that has no duplicates and that has duplicates.
* The test program can be implemented in either Java, C, Python, or Go (preferably).
* The validation logic may not use high-level library functions that perform format validation or regular expression parsing. However, low-level library functions may be used.
* Use development environment (IDE, OS platform) of your choice.
* Make sure your test data includes duplicate values, using both "Z" for GMT or +hh:mm or -hh:mm formats.
* Please commit the solution to a public git repository (eg, github), and let us know the location of the repository (preferably one day prior to your scheduled interview). Also be sure to commit your test data.
* Be prepared to present your solution and walk through how you designed, implemented, and tested the program.
* You will want to discuss assumptions you made and challenges you encountered.
* A more comprehensive solution is preferred, but the focus is on how you demonstrate your understanding of the solution and defend your design and implementation decisions.
'''

from datetime import datetime


class DateTimeValidation():

    def load_file(self, file):
        '''
        Test to see if the file loads correctly
        '''
        self.data = []
        with open(file, "r") as open_file:
                for line in open_file:
                    self.data.append(line.strip())
        

    def unique_or_not(self, iterable):
        # This function SHOULD return true for the data_nodups.txt file and false for the data_dupes.txt file.
        uniques = {}
        for date_time in iterable:
            if date_time not in uniques:
                uniques[date_time] = 1
            else:
                return False
        return True


    def in_iso8601_format(self, datetime_string):
        # Most of the format checking work will be done in this function.
        '''
        ISO-8601 Format for datetimes
        • YYYY = four-digit year
        • MM = two-digit month (01 through 12)
        • DD = two-digit day of month (01 through 31)
        • hh = two digits of hour (00 through 23)
        • mm = two digits of minute (00 through 59)
        • ss = two digits of second (00 through 59)
        • TZD = time zone designator (“Z” for GMT or +hh:mm or -hh:mm)

        EX: "2022-10-15T08:33:12-06:00"
        '''
        
        # Ensuring that at the very minimum, both hyphens for the iso-8601 format are in the correct spot 
        # as well as containing/having T in the string at the correct position
        if "T" not in datetime_string or datetime_string[10] != "T" or datetime_string[4] != "-" or datetime_string[7] != "-": 
            return False
        
        if len(datetime_string) == 24:
            if datetime_string[-1] == "Z":
                return self.format_checker_helper(datetime_string)

        if len(datetime_string) == 25:
            if datetime_string[-6] in ["-", "+"]:
                return self.format_checker_helper(datetime_string)

        return False
    
    def format_checker_helper(self, datetime_string):
    
        # Grabbing the individual components of the format for easier referencing
        try:
            year = datetime_string[:4]
            month = datetime_string[5:7] if self.range_checker(int(datetime_string[5:7]), 1, 12) else -1 # Check between 1 and 12
            day = datetime_string[8:10] if self.range_checker(int(datetime_string[8:10]), 1, 31) else -1 # Check between 1 and 31
        except ValueError:
            return False
        else:
            if month == -1 or day == -1: # Quick check to ensure that if either are false, immediately return False
                return False
            elif year.isnumeric() and month != -1 and day != -1:
                return True
    

        
        # Surround in a try except? return False if the number cannot be converted to an integer? should I only try to convert month and day to ints?
    def range_checker(self, num, a, b):
        if b < a:
            a, b = b, a
        if num in range(a,b):
            return True
        else:
            return False

# DateTimeValidation("data/data_nodups.txt")

def main():
    dtValid1 = DateTimeValidation()
    # Valid date-times
    '''print(dtValid1.in_iso8601_format("2022-10-15T08:33:12-06:00"))
    print(dtValid1.in_iso8601_format("2022-10-15T09:33:15.343Z"))
    print(dtValid1.in_iso8601_format("2019-05-26T11:59:32+03:00"))
    # Invalid Date-Times
    print(dtValid1.in_iso8601_format("2022-10-15T08:33:12-06:001111"))
    print(dtValid1.in_iso8601_format("2022-10-15T09:33:15.343"))
    print(dtValid1.in_iso8601_format("2019-05-26T11:59:32 03:00"))

    # Valid date times in different formats.
    print(dtValid1.in_iso8601_format("06-15-2025T08:54:33-04:00"))'''
    print(dtValid1.in_iso8601_format("2065-01-01T08:54:33-04:00"))

if __name__ == "__main__":
    main()





