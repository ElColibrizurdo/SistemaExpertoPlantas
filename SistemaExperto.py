from experta import *

# Definimos la clase base para el hecho Planta
class Planta(Fact):
    tipo_cultivo = Field(str)
    clima = Field(str, default=None)  # Opcional
    edad = Field(str, default=None)   # Opcional
    sintomas = Field(list)  # Obligatorio
    zona_afectada = Field(str, default=None)  # Opcional
    partes_afectadas = Field(str, default=None)  # Opcional
    signos = Field(list, default=None)  # Opcional
    variedad = Field(str, default=None)  # Opcional
    historial_terreno = Field(str, default=None)  # Opcional
    manejo_agronomico = Field(str, default=None)  # Opcional
    presencia_vectores = Field(str, default=None)  # Opcional

class DiagnosticoPlagas(KnowledgeEngine):

    # Definimos la plaga 1: Hongo en tomate
    @Rule(Planta(tipo_cultivo="tomate", sintomas=MATCH.s))
    def hongo_en_tomate(self, s):
        sintomas_esperados = {"manchas en hojas", "hojas amarillas", "crecimiento lento"}
        sintomas_usuario = set(s)

        sintomas_encontrados = sintomas_esperados.intersection(sintomas_usuario)

        if len(sintomas_encontrados) >= len(sintomas_esperados) - 1:  # Permite que falte 1 síntoma
            print("Diagnóstico: Hongo en tomate.")
            print(f"Síntomas detectados: {sintomas_encontrados}")
        else:
            print("No se detectaron suficientes síntomas para un diagnóstico claro.")

    # Definimos la plaga 2: Insectos en pepino
    @Rule(Planta(tipo_cultivo="pepino", sintomas=MATCH.s))
    def insectos_en_pepino(self, s):
        sintomas_esperados = {"hojas mordidas", "presencia de insectos", "exudados pegajosos"}
        sintomas_usuario = set(s)

        sintomas_encontrados = sintomas_esperados.intersection(sintomas_usuario)

        if len(sintomas_encontrados) >= len(sintomas_esperados) - 1:  # Permite que falte 1 síntoma
            print("Diagnóstico: Insectos en pepino.")
            print(f"Síntomas detectados: {sintomas_encontrados}")
        else:
            print("No se detectaron suficientes síntomas para un diagnóstico claro.")

    # Definimos la plaga 3: Moho en plantas jóvenes
    @Rule(Planta(tipo_cultivo="tomate", edad="joven", sintomas=MATCH.s))
    def moho_en_planta_joven(self, s):
        sintomas_esperados = {"hojas arrugadas", "moho blanco", "crecimiento débil"}
        sintomas_usuario = set(s)

        sintomas_encontrados = sintomas_esperados.intersection(sintomas_usuario)

        if len(sintomas_encontrados) >= len(sintomas_esperados) - 1:  # Permite que falte 1 síntoma
            print("Diagnóstico: Moho en planta joven.")
            print(f"Síntomas detectados: {sintomas_encontrados}")
        else:
            print("No se detectaron suficientes síntomas para un diagnóstico claro.")

    # Definimos la plaga 4: Podredumbre en raíz (planta adulta)
    @Rule(Planta(tipo_cultivo="tomate", edad="adulta", sintomas=MATCH.s))
    def podredumbre_en_raiz(self, s):
        sintomas_esperados = {"raices oscuras", "presencia de humedad excesiva", "hojas amarillas"}
        sintomas_usuario = set(s)

        sintomas_encontrados = sintomas_esperados.intersection(sintomas_usuario)

        if len(sintomas_encontrados) >= len(sintomas_esperados) - 1:  # Permite que falte 1 síntoma
            print("Diagnóstico: Podredumbre en raíz.")
            print(f"Síntomas detectados: {sintomas_encontrados}")
        else:
            print("No se detectaron suficientes síntomas para un diagnóstico claro.")


if __name__ == "__main__":
    engine = DiagnosticoPlagas()
    engine.reset()

    #Daatos de prueba
    sintomas_observados = [
        "raices oscuras",
        "presencia de humedad excesiva",
        "hojas amarillas",
        "tallo muerto"
    ]

    engine.declare(Planta(
        sintomas=sintomas_observados,
        tipo_cultivo="tomate",
        clima = "Humedo",
        edad = "adulta"
    ))

    engine.run()