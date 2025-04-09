from experta import *

class ProblemaPC(Fact):
    """Hechos sobre la computadora"""
    pass

class DiagnosticoPC(KnowledgeEngine):

    @Rule(ProblemaPC(no_enciende=True), ProblemaPC(ventilador=False))
    def fuente_poder_danada(self):
        print("⚠️ Diagnóstico: Fuente de poder dañada.")

    @Rule(ProblemaPC(enciende=True), ProblemaPC(imagen=False))
    def sin_imagen(self):
        print("⚠️ Diagnóstico: Fallo en tarjeta gráfica o RAM.")

    @Rule(ProblemaPC(pitidos=True))
    def fallo_ram(self):
        print("⚠️ Diagnóstico: Fallo en la memoria RAM.")

    @Rule(ProblemaPC(reinicia=True), ProblemaPC(calienta=True))
    def sobrecalentamiento(self):
        print("⚠️ Diagnóstico: Sobrecalentamiento o fuente inestable.")


engine = DiagnosticoPC()
engine.reset()

# Aquí defines los síntomas detectados
engine.declare(ProblemaPC(enciende=True, imagen=False))
engine.run()
