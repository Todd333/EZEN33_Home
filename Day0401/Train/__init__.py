import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ctx = 'C:/Users/toddc/PycharmProjects/Day0401/data/'
train = pd.read_csv(ctx + 'train.csv')
test = pd.read_csv(ctx + 'test.csv')
# df = pd.DataFrame(train)
# print(df.columns)
"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

PassengerId 고객아이디      
Survived 생존여부     Survival    0 = No, 1 = Yes
Pclass 승선권 클래스    Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
Name 이름
Sex  성별  Sex    
Age  나이  Age in years    
SibSp  동반한 형제자매, 배우자 수  # of siblings / spouses aboard the Titanic    
Parch  동반한 부모, 자식 수  # of parents / children aboard the Titanic    
Ticket  티켓 번호  Ticket number    
Fare  티켓의 요금  Passenger fare    
Cabin  객실번호  Cabin number    
Embarked  승선한 항구명  Port of Embarkation  
  C = Cherbourg 쉐부로, Q = Queenstown 퀸스타운, S = Southampton 사우스햄톤
"""
f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'].value_counts().plot.pie(explode=[0, 0.1],
                                          autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')
# plt.show() 생존률 38.4% 사망률 61.6%
"""
데이터는 훈련데이터(train.csv) , 목적데이터(test.csv) 두가지로
제공됩니다. 
목적데이터에는 위 항목에서는  Survived 정보가 빠져있습니다.
그것은 답이기 때문입니다.
"""
# *************
# 성별
# *************
f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'][train["Sex"] == 'male'].value_counts().plot.pie(explode=[0, 0.1],
                                                                  autopct="%1.1f%%", ax=ax[0], shadow=True)
train['Survived'][train["Sex"] == 'female'].value_counts().plot.pie(explode=[0, 0.1],
                                                                    autopct="%1.1f%%", ax=ax[1], shadow=True)
ax[0].set_title('Survived(Male)')
ax[1].set_title('Survived(Female)')
# plt.show()
# 남성 생존률 18.9% 사망률 81.1%
# 여성 생존률 74.2% 사망률 25.8%
# *************
# 승선권 Pclass
# *************
df_1 = [train['Sex'], train['Survived']]
df_2 = train['Pclass']
df = pd.crosstab(df_1, df_2, margins=True)
# print(df.head())
"""
Pclass             1    2    3  All
Sex    Survived                    
female 0           3    6   72   81
       1          91   70   72  233
male   0          77   91  300  468
       1          45   17   47  109
All              216  184  491  891
"""
# Embarked 는 배를 탄 항구
f, ax = plt.subplots(2, 2, figsize=(20, 15))
sns.countplot('Embarked', data=train, ax=ax[0, 0])
ax[0, 0].set_title('No. Of Passengers Boarded')
sns.countplot('Embarked', hue='Sex', data=train, ax=ax[0, 1])
ax[0, 1].set_title('Male - Female for Embarked')
sns.countplot('Embarked', hue='Survived', data=train, ax=ax[1, 0])
ax[1, 0].set_title('Embarked vs Survived')
sns.countplot('Pclass', data=train, ax=ax[1, 1])
ax[1, 1].set_title('Embarked vs PClass')
# plt.show()
"""
위 데이터를 보면 절반 이상의 승객이 ‘Southampton’에서 배를 탔으며,
 여기에서 탑승한 승객의 70% 가량이 남성이었습니다.
 현재까지 검토한 내용으로는 남성의 사망률이 여성보다 
 훨씬 높았기에 자연스럽게 ‘Southampton’에서 
 탑승한 승객의 사망률이 높게 나왔습니다.
또한 ‘Cherbourg’에서 탑승한 승객들은 
1등 객실 승객의 비중 및 생존률이 높은 것으로 보아서 
이 동네는 부자동네라는 것을 예상할 수 있습니다.
"""
# 결측치 제거
# train.info()
"""
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
memory usage: 83.6+ KB
"""
print(train.isnull().sum())
"""
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
"""


def bar_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    df.plot(kind='bar', stacked=True, figsize=(10, 5))
    plt.show()


bar_chart('Sex')
bar_chart('Pclass')
bar_chart('SibSp')
bar_chart('Parch')
bar_chart('Embarked')