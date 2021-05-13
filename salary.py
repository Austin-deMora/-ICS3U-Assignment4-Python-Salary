#!/usr/bin/env python3
#
# Created by: Austin de Mora
# Created on: May 2021
# This program finds the bonus net amount of yearly salaries

import math


def main():
    # This function calculates the bonus net amount of yearly salaries

    # Input
    service_years = input("Enter years of service: ")
    yearly_salary_string = input("Enter yearly salary: ")
    print("")

    # process
    try:
        yearly_salary = int(yearly_salary_string)
        net_amount = yearly_salary * 1.05

        assert yearly_salary > 0

        if (int(service_years) > 5):
            if (int(yearly_salary) * 1.05):
                print("Your net amount with bonus is ${}".format(net_amount))
        else:
            print("You haven't worked long enough")
    except AssertionError:
        print("Integer wasn't positive")
    except Exception:
        print("Invalid Input")


if __name__ == "__main__":
    main()
