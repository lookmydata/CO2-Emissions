import streamlit as st

presentacion = st.container()
with presentacion:
    st.header("Look My Data")
    st.write(" Somos LookMyData el dia de hoy le vamos a plantear nuestros objetivos seria describir la relación entre el consumo y generación de energía, y las emisiones de CO2 a nivel global, como así también su impacto sobre la salud humana, generando herramientas para su estudio en forma analítica y visual.")
    st.write(" Tambien planteamos estudiar la relación entre consumo/generación de energía, emisiones de CO2 y PBI: permitirá establecer un punto de partida para el análisis determinando el grado de dependencia entre actividad económica y la demanda de energía, con las emisiones asociadas")

    st.write(" Estudiar la relación entre emisiones de CO2 y frecuencia de desastres ambientales relacionados al clima.")
    st.write(" Estudiar la relación entre emisiones de CO2 y prevalencia de enfermedades respiratorias en los países con mayor nivel de emisiones")
    st.write(" Estudiar la relación entre emisiones de CO2 y PBI de principales países. Esto nos permitirá conocer la forma en la que varía la emisión de CO2  con respecto a la actividad económica. Al mismo tiempo, tomando como KPI la cantidad de m3 por 1M USD de PBI para cada país, podremos tener un parámetro comparativo de cuán “limpio” es su actividad económica.")
    
    st.write("### Los KPI que vamos a utilizar para realizar algunos de los objetivos son:")
    st.markdown("__Ranking de países según participación de energías limpias en la matriz energética__")
    st.markdown("__Ranking países según m3 CO2/ 1M USDPBI__")
    st.markdown("__Evolución histórica de generación de energía y emisión de CO2  en top 10 países emisores de CO2__")
    st.markdown("__Emisión CO2 por fuente de energía__")


