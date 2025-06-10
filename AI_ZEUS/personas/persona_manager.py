class Persona:
    def __init__(self, name, specialties):
        self.name = name
        self.specialties = specialties

    def interpret(self, input_data):
        return {"intent": input_data["content"], "context": self.specialties}

class PersonaManager:
    def __init__(self):
        self.personas = {}

    def create_persona(self, name, specialties):
        persona = Persona(name, specialties)
        self.personas[name] = persona
        return persona

    def choose_best_persona(self, multimodal_input):
        return next(iter(self.personas.values()))

    def interpret(self, multimodal_input):
        persona = self.choose_best_persona(multimodal_input)
        return persona.interpret(multimodal_input)
