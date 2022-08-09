# import pandas
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)
# print(myvar)


# //imporetd pandas as pd and print data
# import pandas as pd
# mydata={
#     'name':['saurabh','pranav','naeem','rajani'],
#     'age':[25,20,30,15]
# }
# myvard=pd.DataFrame(mydata)
# print(myvard)


# //panda Series
# import pandas as pd
# a=[10,20,25]
# myvar=pd.Series(a)
# print(myvar)
# print(myvar[1])


# //labels in pandas
# import pandas as pd
# a=[10,20,30,60]
# myvar=pd.Series(a,index=['a','b','c','d'])
# print(myvar)
# print(myvar['b'])


# // Key/value objects in Series
# import pandas as pd
# carprice={"swift":5000,"Scorpio":60000,"wagonr":40000}
# myvar=pd.Series(carprice)
# print(myvar)


# // index in Key/value series for select only some of data
# import pandas as pd
# carprice={"swift":5000,"Scorpio":60000,"wagonr":40000,"brezza":90000}
# myvar=pd.Series(carprice,index=["swift","wagonr"])
# print(myvar)


# //  Data frame: its usually likes multy dimensional tables
# import pandas as pd
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)

# print(myvar)


# // import data in dataframe
# import pandas as pd
# data = {
#     "swift": [45, 65, 70],
#     "scorpio": [50, 65, 75]
# }
# df = pd.DataFrame(data)
# df = pd.DataFrame (data, index=["d1", "d2", "d3"])
# print(df)
# print(df.loc["d2"])
# print(df.loc[1])
# print(df.loc[[0,1]])

# import pandas as pd
# df=pd.read_csv("data.csv")
# # print(df)
# #// .to_string to print entire data
# # print(df.to_string()) 
# print(pd.options.display.max_rows,2)
# print(df)

