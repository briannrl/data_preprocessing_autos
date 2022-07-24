import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import normalize

def open_file(PATH):
    df_ = pd.read_csv(PATH, encoding="ISO-8859-1")
    return df_

def rename_column_name(df_, dict_columns: dict):
    df_ = df_.rename(columns=dict_columns)
    return df_

def change_to_datetime(df_, columns: list):
    for elm in columns:
        df_[elm] = pd.to_datetime(df_[elm])
    return df_

def clean_odometer(df_):
    df_["odometer"] = df_["odometer"].str.replace(r"[,(km)]", "").astype("int64")
    return df_

def clean_price(df_):
    df_["price"] = df_["price"].str.replace(r"[$,]", "").astype("int64")
    return df_

def drop_columns(df_, columns: list):
    df_ = df_.drop(columns=columns)
    return df_

def filter_based_on_price(df_, lower_limit: int, upper_limit: int):
    df_ = df_.query(f"price >= {lower_limit} and price <= {upper_limit}")
    return df_

def impute_object(df_, columns: list):
    df_[columns] = df_[columns].apply(lambda col: col.fillna(col.mode()[0]), axis=0)
    return df_

def normalization(df_):
    df_[[col for col in df_.columns if df_[col].dtype == np.int64 and col != "price"]] = normalize(df_[[col for col in df_.columns if df_[col].dtype == np.int64 and col != "price"]], axis=0)
    return df_

def one_hot_encoding(df_):
    df_one_hot = (pd.get_dummies(df_[["abtest", "vehicle_type", "gearbox", "fuel_type", "brand", "unrepaired_damage"]], drop_first=True)
                        .assign(price=df_["price"],
                            registration_year=df_["registration_year"],
                            power_ps=df_["power_ps"],
                            odometer=df_["odometer"],
                            registration_month=df_["registration_month"],
                            ad_created=df_["ad_created"],
                            last_seen=df_["last_seen"]))
    df_one_hot.insert(0, "date_crawled", df_["last_seen"])
    return df_one_hot

def reset_index(df_):
    df_ = df_.reset_index(drop=True)
    return df_

