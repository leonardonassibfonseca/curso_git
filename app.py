import streamlit as st
from src.extraction import load_data

st.set page_config(layout = 'wide')

def main():
    df_raw = load_data()
    st.dataframe(df_raw)
print('Teste problemas de merge')
if __name__ == '__main__':
    main()


print('Teste')
