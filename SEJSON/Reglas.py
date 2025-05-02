from experta import *
import json

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

    def __init__(self, plagas):
        super().__init__()
        self.plagas = plagas

    @Rule(Planta(tipo_cultivo=MATCH.tipo, edad=MATCH.edad, sintomas=MATCH.sintomas))
    def detectar_plagas(self, tipo, edad, sintomas):
        sintomas_usuarios = set(sintomas)

        for plaga in self.plagas:
            if plaga["tipo_cultivo"] != tipo:
                continue
            if plaga["edad"] != "cualquiera" and plaga["edad"] != edad:
                continue

            sintomas_plaga = set(plaga["sintomas"])
            coincidencias = sintomas_usuarios.intersection(sintomas_plaga)

            if len(coincidencias) >= len(sintomas_plaga) - 1:
                print(f"\n✅ Diagnóstico probable: {plaga['nombre']}")
                print(f"Coincidencias: {coincidencias}")
                return
            
        print("\n⚠️ No se encontró una plaga con suficientes coincidencias.")
            
print("Se empieza")

if __name__ == "__main__":
    print("Se empieza")
    with open("Hechos.json") as f:
        plagas = json.load(f)

    

    engine = DiagnosticoPlagas(plagas)
    engine.reset()

    engine.declare(Planta(
        tipo_cultivo="tomate",
        edad="joven",
        sintomas=["moho blanco", "hojas arrugadas"]
    ))

    engine.run()

print("Se empieza")
