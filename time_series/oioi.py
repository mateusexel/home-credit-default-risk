import pandas as pd
import numpy as np
import gc
credit_card_balance =  pd.read_csv('../data/credit_card_balance.csv')
POS_CASH_balance =  pd.read_csv('../data/POS_CASH_balance.csv')
installments_payments =  pd.read_csv('../data/installments_payments.csv')
installments_payments['MONTHS_BALANCE'] = (installments_payments['DAYS_INSTALMENT']/30).round().astype(int)
df = pd.merge(POS_CASH_balance, installments_payments,  left_on=(['SK_ID_PREV','SK_ID_CURR','MONTHS_BALANCE']), right_on=(['SK_ID_PREV','SK_ID_CURR','MONTHS_BALANCE']), how='outer')
df=pd.merge(df, credit_card_balance, how = 'outer')
del credit_card_balance, POS_CASH_balance ,installments_payments
gc.collect()
values = list(set(df.columns) - set(['SK_ID_PREV', 'SK_ID_CURR', 'MONTHS_BALANCE']))
df_pivot = df.pivot_table(values=values, index='SK_ID_CURR', columns='MONTHS_BALANCE').to_json('../treated_data/timeseries.json')
