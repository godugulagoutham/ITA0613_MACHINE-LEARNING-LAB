import numpy as np
import pandas as pd
NUMERIC_COLUMNS=["Annual_Rainfall","Temperature","Humidity","Soil_pH","N","P","K","Fertilizer","Pesticide"]
MODEL_FEATURES=NUMERIC_COLUMNS+["GDD","Rainfall_Anomaly","Temperature_Range","Heat_Stress"]
def clean_and_engineer(df):
    df=df.copy()
    for c in NUMERIC_COLUMNS+["Yield","Area"]:
        if c in df.columns: df[c]=pd.to_numeric(df[c],errors="coerce")
    for c in NUMERIC_COLUMNS:
        df[c]=df[c].fillna(df.groupby("State")[c].transform("median")); df[c]=df[c].fillna(df[c].median())
    df["GDD"]=np.maximum(df["Temperature"]-10.0,0.0)*120.0
    state_mean=df.groupby("State")["Annual_Rainfall"].transform("mean")
    df["Rainfall_Anomaly"]=(df["Annual_Rainfall"]-state_mean)/(state_mean+1e-9)
    df["Temperature_Range"]=8.0; df["Heat_Stress"]=(df["Temperature"]>34.0).astype(int)
    return df
def time_split(df,train_end=2016,val_start=2017,val_end=2018):
    return df[df.Crop_Year<=train_end].copy(),df[(df.Crop_Year>=val_start)&(df.Crop_Year<=val_end)].copy(),df[df.Crop_Year>=val_end+1].copy()
def standardize(train,other_frames,features):
    mu=train[features].mean(); sd=train[features].std().replace(0,1.0).fillna(1.0)
    return (train[features]-mu).to_numpy(float),[(d[features]-mu).div(sd).to_numpy(float) for d in other_frames],mu,sd
