# Having just started college, Bob has been busy
# looking for a part-time job to fund his new college social life
# and after only two weeks of looking he has managed to get
# two job offers! Each job comes with different hours, basic rates
# of pay and over-time rates so he needs to work out which
# would get him the most money. Develop an application that
# would allow Bob to enter his basic pay rate, his number of
# regular hours work per week and his number of overtime
# hours per week. The application should then calculate and
# display Bob’s total basic pay for the week, his overtime pay for
# the week and his total pay including overtime. Note: The
# overtime rate is 1.5 times the basic rate of pay



def basicpay():
    pay_input = int(input("Enter the basic pay rate\n"))
    hours = int(input("Enter number of hours per week in integer\n"))
    overtime_hours = int(input("Enter overtime hours in integer"))

    basicpay = pay_input * hours
    overtime_pay = (pay_input * 1.5) * overtime_hours
    total_pay = basicpay + overtime_pay

    return f"Basic pay is {basicpay} \novertime pay is {overtime_pay}\n Total pay is {total_pay} "



print(basicpay())

