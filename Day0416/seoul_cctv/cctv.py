import pandas as pd
ctx='../Data/'
filename=ctx+'CCTV_in_Seoul.csv'
seoul_cctv=pd.read_csv(filename, encoding='UTF-8')
# print(seoul_cctv.head())
seoul_cctv_idx =seoul_cctv.columns

#print(seoul_cctv_idx)
"""
   기관명    소계  2013년도 이전  2014년  2015년  2016년
"""

seoul_cctv.rename(columns={seoul_cctv.columns[0]:'구별'},inplace=True)


seoul_pop=pd.read_excel(ctx + 'population_in_Seoul.xls', encoding="ITF-8",
                        header=2,usecols='B,D,G,J,N')

seoul_pop.rename(columns={seoul_pop.columns[0]:'구별'
                            ,seoul_pop.columns[1]:'인구수'
                            ,seoul_pop.columns[2]:'한국인'
                            ,seoul_pop.columns[3]:'외국인'
                            ,seoul_pop.columns[4]:'고령자'},inplace=True)
seoul_cctv.sort_values(by='소계',ascending=True).head(5)
seoul_pop.drop([0],inplace=True)
seoul_pop['구별'].unique()
# print(seoul_pop)

seoul_pop['구별'].isnull
seoul_pop.drop([26],inplace=True)
print(seoul_pop)



