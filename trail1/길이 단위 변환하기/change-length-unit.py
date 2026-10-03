ft_to_cm = 30.48
mile_to_cm = 160934

def my_cal():
    ft = 9.2
    mile = 1.3

    ft_res = ft * ft_to_cm
    mile_res = mile * mile_to_cm

    print(f"{ft}ft = {ft_res:.1f}cm")
    print(f"{mile}mi = {mile_res:.1f}cm")

my_cal()