last_days = {1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30,2:28}
week = {1:"MON",2:"TUE",3:"WED",4:"THU",5:"FRI",6:"SAT",0:"SUN"}

input_month, input_day = map(int, input().split())
cumsum = 0
if input_month == 1:
    cumsum = input_day
else:
    for month in range(1,input_month):
        last_day = last_days[month]
        cumsum = cumsum + last_day
    cumsum = cumsum + input_day
print(week[cumsum%7])
# ref https://blog.naver.com/PostView.nhn?blogId=tfj0531&logNo=221179098424&parentCategoryNo=&categoryNo=73&viewDate=&isShowPopularPosts=true&from=search