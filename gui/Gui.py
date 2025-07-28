import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Constants import currencys
from src.Currency_Convertor import get_exchange_rate, Convert_Currency
st.title(":dollar: Currency Convertor")
base_currency = st.selectbox('Base Currency:', currencys)
target_currency = st.selectbox('target Currency:', currencys)
amount = st.number_input('Enter amount : ', value=1.0,  min_value=0.0, max_value=1000000000.0)
try:
    if amount >= 0 and base_currency and target_currency:
            exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
            Convert_amount = Convert_Currency(amount, exchange_rate)
            st.success(f"\n {amount} {base_currency} = {Convert_amount:.2f} {target_currency}")
    else:
          st.error('Maybe the Api finished')
except Exception as e:
       st.error(f'An error occurred {e}')
