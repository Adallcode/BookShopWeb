from datetime import datetime

from flask import flash

class Data:

    def __init__(self,):
        pass

    
    def isCorrect(self, numOfBook: str, extraCD: str, arriveDate: str, name: str,
        lastName: str, country: str, city: str, street: str, zip: str, phone: str) ->bool:
        
        
        # First convert this strings to integers and then check

        temp = arriveDate.split("-")
        d = datetime.now().day
        m = datetime.now().month
        y = datetime.now().year

        currentDate = [y, m, d]
        
        self.convertToInt(temp)

        # Whenever the year is less than current return false
        if temp[0] < currentDate[0]:
            return False

        # 1. Here year and month must be iqual and day bigger
        # 1.1 (elif statement) year must be iqual and month bigger 
        # 2 (else statement) means that the year is bigger and therefore the date is right
        if temp[0] == currentDate[0]:

            if temp[1] == currentDate[1]:

                if temp[2] > currentDate[2]:
                    self.mDate = ( numOfBook, extraCD, arriveDate, name, lastName, country, city, street,
                     zip, phone, )
                    return True
            elif temp[1] > currentDate[1]:
                self.mDate = ( numOfBook, extraCD, arriveDate, name, lastName, country, city, street,
                zip, phone, )
                return True
        else:
            self.mDate = ( numOfBook, extraCD, arriveDate, name, lastName, country, city, street,
            zip, phone, )
            return True
        
        # Show to the user a msg because the date is wrong
        flash("Your order can't arrive on date, please select another date", category="info")

        return False


    # Return this object tuple
    def getTuple(self, )-> tuple:
        return self.mDate
        

    

    """This function just convert to integer to make some calulation in ( isCorrect function )"""

    def convertToInt(self, a: list, ) -> None:

        for x in range(len(a)):

            a[x] = int(a[x])
            



