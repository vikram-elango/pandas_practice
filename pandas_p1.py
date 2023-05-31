import pandas as pd
df = pd.read_csv('data/survey_results_public.csv')   # read csv method with path

print(df.shape)   # gives us the number of rows and columns (rows, columns)

print(df.info())    #gives information on the data, number of entries, list of all the columns along with their data type

pd.set_option('display.max_columns',79)  #displays all the data without cutting it out

print(df)

schema_df= pd.read_csv('data/survey_results_schema.csv')  #gives information on each column
print(schema_df)


print(df.head(5))   #this is to see the number of rows default df.head() shows first 5 rows but you can specifiy
                    #the number of rows you want to see for each row