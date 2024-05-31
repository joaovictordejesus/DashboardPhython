#João Vitor de Jesus PDITA015
import streamlit as st 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("obesidade.csv")

#Aqui escolhi apenas 6 dados para serem analisados, aqueles que tinham menos variações, pois estes davam retronos mais precisos que geravam gráficos mais fáceis de serem observados pelo usuário. filter_columns = }"Gênero","Habito de Fumar", "Histórico familiar de sobrepeso,"Status" 
filter_columns = ["Status","Habito_de_Fumar","Histórico_familiar_de_sobrepeso","Gênero","Meio_de_Transporte","Come_algum_alimento_entre_refeições"] 

#Aqui eu coloco dois quadros com informações fixas que julguei importante, sendo elas o total de pessoas que participaram da pesquisa e a idade média delas. 
total_pessoas = df.shape[0]
idade_media = df["Idade"].mean() if 'Idade' in df.columns else None 

#Nessa parte eu importo o arquivo CSS 
with open ('style.css') as f: 
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True) 
    
#Aqui temos nossa barra interativa 
st.sidebar.header("Filtros para os Gráficos")

#Primeiro Gráfico em Barras:
bar_col1 = st.sidebar.selectbox("1° Gráfico de Barras",filter_columns)

#Segundo Gráfico em Barras:
bar_col2 = st.sidebar.selectbox("2° Gráfico de Barras",filter_columns)

#Gráfico de Rosca:
donut_col = st.sidebar.selectbox("Gráfico de Rosca",filter_columns) 

#Gráfico de Pizza 
pie_col = st.sidebar.selectbox("Grágico de Pizza",filter_columns)

st.sidebar.markdown('<p class="joao-text">João Victor de Jesus Augusto PDITA015</p>',unsafe_allow_html=True)

#Gerar os Gráficos de acordo com as seleções definidas acima
fig1 = px.bar(df, x=bar_col1,title=f"1° Gráfico de Barras Verticais de {bar_col1}", color_discrete_sequence=['blue'])
fig2 = px.bar(df, x=bar_col2, title=f"2° Gráfico de Barras Verticais de {bar_col2}", color_discrete_sequence=['red'])
fig3 = px.pie(df, names=donut_col, title=f"Gráfico de Rosca de {donut_col}", hole=0.3, color_discrete_sequence=['green'])
fig4 = px.pie(df, names=pie_col, title=f"Pizza de {pie_col}", color_discrete_sequence=['orange']) 

#Ajustando Tamanho dos Gráficos 
fig1.update_layout(height=250)
fig2.update_layout(height=250)
fig3.update_layout(height=250)
fig4.update_layout(height=250) 

#Título:
st.header("Dashboard de Análise de Obesidade") 

#Quadros com informações importantes: 
col1,col2 = st.columns(2) 
with col1:
    st.metric("Número Total de Participantes",total_pessoas)
with col2: 
    st.metric("Idade Média dos Participantes",f"{idade_media:.2f}"if idade_media is not None else"N/A")

#Gráficos:
with st.container():
   col1,col2 = st.columns(2)
   with col1:
     st.plotly_chart(fig1,use_container_width=True)
   with col2:
     st.plotly_chart(fig2,use_container_width=True) 
     
with st.container():
   col3,col4 = st.columns(2)
   with col3:
     st.plotly_chart(fig3,use_container_width=True)
   with col4:
     st.plotly_chart(fig4,use_container_width=True)