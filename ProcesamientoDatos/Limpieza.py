import pandas as pd

siniestros = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="SINIESTROS")
actorVial = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="ACTOR_VIAL")
vehiculos = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="VEHICULOS")
hipotesis = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="HIPOTESIS")
diccionario = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="DICCIONARIO")

historico = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\historico_siniestros_bogota_d.c_-.csv")