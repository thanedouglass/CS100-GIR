def solution(company, months):
    if company == "Facebook":
        result = "All employees earn 20 days of vacation per year"
    elif company == "Amazon":
        if months >= 12:
            result = "After 1 year, employees earn 15 days of vacation per year"
        else:
            result = "New employees earn 10 days of vacation per year"
    elif company == "Apple":
        if months >= 48:
            result = "After 4 years, and every year after that, it is increased by 1 more day. Earning 16 days of vacation per year."
        elif months >= 36:
            result = "After 4 years, and every year after that, it is increased by 1 more day. Earning 16 days of vacation per year."
        else:
            result = "New employees earn 12 days of vacation per year."
    elif company == "Microsoft":
        if months >= 60:
            result = "After every 5 years, this is increased by 5 more days, to a maximum of 30 days total per year."
        else:
            result = "New employees earn 15 days of vacation per year."
    elif company == "Google":
        if months >= 60:
            result = "After", 3, "years this is increased to", 20, "days"
        elif months >= 36:
            result = "After", 5, "years this is increased to", 25 ,"days"
        else:
            result = "New employees earn", 15 ,"days of vacation per year."
    else:
        result = "Company not recognized"
    return result
company = input("Enter the company name: ")
months = int(input("Enter the number of months worked: "))
result=solution(company, months)
print(result)
#        if company == "Facebook":
#            print("All employees earn", 20, "days of vacation per year")
#        elif company == "Amazon":
#            if months >= 12:
#                print("After", 1, "year employees earn", 15, "days of vacation per year")
#            else:
#                print("New employees earn", 10, "days of vacation per year")
#        elif company == "Apple":
#            if months >= 48:
#                print("After", 4, "years and every year after that, it is increased by", 1 ,"more day. Earning", 16 ,"days of vacation per year.")
#            elif months >= 36:
#                print("After", 3, "years this is increased to", 15, "days.")
#            else:
#                print("New employees earn", 12, "days of vacation per year.")
#        elif company == "Microsoft":
#            if months >= 60:
#                print("After every", 5, "years this is increased by 5 more days, to a maximum of 30 days total per year.")
#            else:
#                print("New employees earn", 15, "days of vacation per year.")
#        elif company == "Google":
#            if months >= 36:
#                print("After", 3, "years this is increased to", 20, "days")
#            elif months >= 60:
#               print("After", 5, "years this is increased to", 25 ,"days")
#           else:
#               print("New employees earn", 15 ,"days of vacation per year.")
#       else:
#           print("Company not recognized")
#company = input("Enter the company name: ")
#months = int(input("Enter the number of months worked: "))
#solution(company, months)
