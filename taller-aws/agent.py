import os
from strands import Agent
import tools # Importamos tus funciones con @tool

SYSTEM_PROMPT = """Eres CloudArquitecto, experto en AWS. 
Ayudas a ingenieros de sistemas. Responde de forma técnica y breve."""

agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    tools=[], # Las dejamos vacías aquí para evitar el error de streaming
    model="meta.llama3-8b-instruct-v1:0"
)

def main():
    print("\n🚀 CLOUDARQUITECTO LISTO")
    while True:
        try:
            user_input = input("You: ").strip().lower()
            if not user_input or user_input in ["exit", "salir"]:
                break
            
            # Lógica para usar las herramientas de tools.py manualmente
            if "cuánto cuesta" in user_input or "costo" in user_input:
                # Extraemos el número (ej: 0.08)
                import re
                match = re.search(r"(\d+\.\d+|\d+)", user_input)
                precio = float(match.group(1)) if match else 0.05
                response = tools.calcular_costo_mensual(precio)
            elif "región" in user_input or "recomiendas" in user_input:
                response = tools.obtener_region_recomendada("latam")
            elif "estado" in user_input or "servicios" in user_input:
                response = tools.estado_servicios_aws()
            else:
                response = agent(user_input)

            print(f"\nCloudArquitecto: {response}\n")
            
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()