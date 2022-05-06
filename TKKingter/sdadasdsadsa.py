dictionary = {

    0: 
    {
    "UserName": "",
    "Surname": "Jones",
    "Forename": "Helen",
    "YearofBirth": "2001",
    "MonthofBirth": "6"},

    1:
    {
    "UserName": "",
    "Surname": "Rees",
    "Forename": "Ceryl",
    "YearofBirth": "1990",
    "MonthofBirth": "10"},

    2:
    {
    "UserName": "",
    "Surname": "Philips",
    "Forename": "Ann",
    "YearofBirth": "2002",
    "MonthofBirth": "1"},

    3: {
    "UserName": "",
    "Surname": "Leech",
    "Forename": "Fred",
    "YearofBirth": "2003",
    "MonthofBirth": "5"},


}

for i in range(len(dictionary)):

    Surname=dictionary[i]['Surname']
    Forename=dictionary[i]['Forename']
    YearofBirth=dictionary[i]['YearofBirth']
    MonthofBirth=dictionary[i]['MonthofBirth']
    UserName=(Surname[:2]+Forename[:1]+YearofBirth[2:]+MonthofBirth)
    print(UserName)
