import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)>25
df['overweight'] = df['overweight'].astype(int)
# 3
df['cholesterol'] = df["cholesterol"].apply(lambda x:0 if x ==1 else 1)
df['gluc'] = df["gluc"].apply(lambda x:0 if x ==1 else 1)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", 
    "smoke","alco", "active", "overweight" ])
    
    #df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size().reset_index(name='total')
    

    # 6
    #如果你希望分組結果直接保留為普通的 DataFrame 欄位，而不是索引，那麼使用 as_index=False 更方便。
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat).fig


    # 8
    #fig = None
    #fig.savefig('catplot.png')
    #return fig

    # 9
    fig.savefig('catplot.png')

    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    #(df['height'] >= df['height'].quantile(0.025)))

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', square=True, cmap='coolwarm', cbar_kws={"shrink": .5}, ax=ax)



    # 16
    fig.savefig('heatmap.png')
    
    return fig
