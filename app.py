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

class DateTimeValidation():

    def load_file(self, file):
        '''
        
        '''
        self.data = []
        try:
            with open(file, "r") as open_file:
                    for line in open_file:
                        self.data.append(line.strip())
        except FileNotFoundError:
            self.data = []
        

    def unique_or_not(self, iterable) -> bool:
        '''
        This method is only meant to be used on self.data to ensure that all the data that was loaded in from self.load_file is unique. 
        '''
        
        if len(iterable) == 0 or not iterable:
            return False
        uniques = {}
        for date_time in iterable:
            if date_time not in uniques:
                uniques[date_time] = 1
            else:
                return False
        return True


    def in_iso8601_format(self, datetime_string: str) -> bool:
        # Most of the format checking work will be done in this function with the help of format_checker_helper.
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

        if len(datetime_string) < 20:
            return False

        if datetime_string[10] != "T" or datetime_string[4] != "-" or datetime_string[7] != "-" \
            or datetime_string[13] != ":" or datetime_string[16] != ":":
            return False
        
        if len(datetime_string) == 20 or len(datetime_string) == 25:
            return self.format_checker_helper(datetime_string)
        return False
    
    def format_checker_helper(self, datetime_string: str) -> bool:
    
        # Grabbing the individual components of the format for easier referencing
        try:
            year = int(datetime_string[:4]) # Except should catch the valueError if anything besides a number is in the year splice.
            month = int(datetime_string[5:7]) if self.range_checker(int(datetime_string[5:7]), 1, 12) else -1 
            day = int(datetime_string[8:10]) if self.range_checker(int(datetime_string[8:10]), 1, 31) else -1 
            hour = int(datetime_string[11:13]) if self.range_checker(int(datetime_string[11:13]), 0, 23) else -1 
            minutes = int(datetime_string[14:16]) if self.range_checker(int(datetime_string[14:16]), 0, 59) else -1
            seconds = int(datetime_string[17:19]) if self.range_checker(int(datetime_string[17:19]), 0, 59) else -1

            # Explicitly checking the datetimes with 25 len because there is the added +/-hh:mm which would require boundary checks.
            if len(datetime_string) == 25:
                if datetime_string[19] not in ("+", "-"):
                    return False
                timezone_hour = int(datetime_string[20:22]) if self.range_checker(int(datetime_string[20:22]), 0, 23) else -1
                timezone_minutes = int(datetime_string[24:]) if self.range_checker(int(datetime_string[24:]), 0, 59) else -1

                if -1 in (timezone_hour, timezone_minutes):
                    return False
        except ValueError as e: # Incase there is something else besides an int inside of the array splice for any conversion, then we know that the format is invalid. 
            print(e)
            return False
        else:
            if -1 in (month, day, hour, minutes, seconds):
                return False
            else:
                return True
    
    def range_checker(self, num, a, b):
        if b < a:
            a, b = b, a
        if num in range(a,b + 1):
            return True
        else:
            return False

# DateTimeValidation("data/data_nodups.txt")

def main():
    dtValid1 = DateTimeValidation()
    # Valid date-times
    print("Valid Date-times:")
    print("1: 222-10-15T08:33:12-06:00 | ",dtValid1.in_iso8601_format("2022-10-15T08:33:12-06:00"))
    print("2: 2022-10-15T09:33:15Z | ",dtValid1.in_iso8601_format("2022-10-15T09:33:15Z"))
    print("3: 2019-05-26T11:59:32+03:00 | ",dtValid1.in_iso8601_format("2019-05-26T11:59:32+03:00"))
    print("5: 2065-01-01T08:54:33Z | ",dtValid1.in_iso8601_format("2065-01-01T08:54:33Z"))
    print()
    
    # Invalid Date-Times
    print("Expected Falses:")
    print("1: ",dtValid1.in_iso8601_format("2022-10-15T08:33:12-06:001111")) # False, Length is too long
    print("2: ",dtValid1.in_iso8601_format("2022-10-15T09:33:15.343")) # False, invalid format at end of string
    print("3: ",dtValid1.in_iso8601_format("2019-05-26T11:59:32 03:00")) # False, no +/- before hh:mm at end of string
    print("4: ",dtValid1.in_iso8601_format("2065-01-01T08:54:61-04:00")) # False, seconds is out of range between 0-59
    print("5: ",dtValid1.in_iso8601_format("2064-06-29T09:55:22 05:00")) # False, all but the +/- for the hh:mm are included
    print()
    
    # Valid date times in different formats.
    print("Expected Falses, datetimes in different formats")
    print("1: ",dtValid1.in_iso8601_format("06-15-2025T08:54:33-04:00"))
    print("2: ", dtValid1.in_iso8601_format(""))

if __name__ == "__main__":
    main()





