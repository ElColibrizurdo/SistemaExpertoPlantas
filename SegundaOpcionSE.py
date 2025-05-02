from experta import *
import json

class Plaga(Fact):
    nombre = Field(str)
    tipo_cultivo = Field(str)
    edad = Field(str, default=None)
    sintomas = Field(list)

class PlantaObservada(Fact):
    tipo_cultivo = Field(str)
    edad = Field(str, default=None)
    sintomas = Field(list)

class DiagnosticoPlagas(KnowledgeEngine):

    @Rule(
        AS.planta << PlantaObservada(tipo_cultivo=MATCH.tc, edad=MATCH.edad, sintomas=MATCH.sintomas_usuario),
        AS.plaga << Plaga(tipo_cultivo=MATCH.tc, edad=MATCH.edad, sintomas=MATCH.sintomas_plaga) 
    )
    def comprar_sintomas(self, planta, plaga, sintomas_usuario, sintomas_plaga):
        sintomas_usuario = set(sintomas_usuario)
        sintomas_plaga = set(sintomas_plaga)

        coincidencias = sintomas_usuario.intersection(sintomas_plaga)
        umbral = len(sintomas_plaga) - 1

        if len(coincidencias) >= umbral:
            print(f"Diagnostico: Posible {plaga['nombre']}")
            print(f"Sintomas coincidencias: {coincidencias}")
        else:
            print(f"No hay suficientes coincidencias para {plaga['nombre']}")


if __name__ == "__main__":
    engine = DiagnosticoPlagas()
    engine.reset()

    engine.declare(Plaga(nombre="Hongo en tomate", tipo_cultivo="tomate", edad="joven", 
                         sintomas=["manchas en hojas", "hojas amarillas", "crecimiento lento"]))
    engine.declare(Plaga(nombre="Moho en tomate", tipo_cultivo="tomate", edad="joven", 
                         sintomas=["hojas arrugadas", "moho blanco", "crecimiento débil"]))
    engine.declare(Plaga(nombre="Insectos en pepino", tipo_cultivo="pepino", edad="adulta", 
                         sintomas=["hojas mordidas", "presencia de insectos", "exudados pegajosos"]))
    engine.declare(Plaga(nombre="Podredumbre en raíz", tipo_cultivo="tomate", edad="adulta", 
                         sintomas=["raices oscuras", "presencia de humedad excesiva", "hojas amarillas"]))

    # Declaramos la planta observada
    engine.declare(PlantaObservada(tipo_cultivo="tomate", edad="joven", 
                                   sintomas=["moho blanco", "hojas arrugadas", "crecimiento débil"]))

    engine.run()