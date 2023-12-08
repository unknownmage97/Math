
class Operations:

    def add(self, values) -> float | str:
        '''
        adds given values together
        :param values: string of values
        :return: float
        '''
        result = 0
        try:
            addition = values.split()
            for x in addition:
                result += float(x)
        except:
            return "List numbers you want to add e.g: 4 2 9 8"
        else:
            return result
   
    def subtract(self, values) -> float | str:
        '''
        subtracts all given values
        :param values: string of values
        :return: float
        '''
        result = 0
        try:
            addition = values.split()
            for x in addition:
                result -= float(x)
        except:
            return "List numbers you want to subtract e.g: 4 2 9 8"
        else:
            return result
   
    def multiply(self, values) -> float | str:
        '''
        multiplies all given values together
        :param values: string of values
        :return: float
        '''
        try:
            to_add = values.split()
            for x in range(len(to_add)):
                if x == 0:
                    result = float(to_add[x])
                else:
                    result *= float(to_add[x])
        except:
            return "List numbers you want to multiply e.g: 4 2 9 8"
        else:
            return result
   
    def divide(self, num1, num2) -> float | str:
        '''
        divides num1 by num2
        :param num1: string number
        :param num2: string number
        :return: float
        '''
        result = 0
        try:
            if int(num2) == 0:
                raise ZeroDivisionError
            else:
                result = float(num1) / float(num2)
        except ZeroDivisionError:
            return 'Cannot divide by zero'
        except:
            return 'List only one number in the numerator and denominator'
        else:
            return round(result, 3)

    def triangular(self, n) -> int | str:
        '''
        recurs to add all number from n to 1
        :param n: positive string integer
        :return: integer
        '''
        try:
            if int(n) < 0:
                raise TypeError
            elif int(n) == 0:
                return 0
            elif int(n) == 1:
                return 1
            elif int(n) > 1:
                return int(n) + self.triangular(int(n) - 1)
        except:
            return 'Can only accept single positive integers'

    def factorial(self, n) -> int | str:
        '''
        recurs to multiply all values from n to 1
        :param n: positive string integer
        :return: integer
        '''
        try:
            if int(n) < 0:
                raise TypeError
            elif int(n) == 0:
                return 0
            elif int(n) == 1:
                return 1
            elif int(n) > 1:
                return int(n) * self.factorial(int(n) - 1)
        except:
            return 'Can only accept single positive integers'
