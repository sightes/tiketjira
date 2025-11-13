# services/ai_service.py
import google.generativeai as genai

async def generate_task_description(motivo, bases, prompt, modelo, temperatura, k):
    genai.configure(api_key="AIzaSyBdPPzJSq7Kbch7iRxh3kBg67ZKneoEJgU")

    # Inyección de los parámetros del usuario en el prompt
    final_prompt = prompt.format(motivo=motivo, bases=bases)

    model = genai.GenerativeModel(model_name=modelo)

    response = model.generate_content(
        final_prompt,
        generation_config={
            "temperature": temperatura,
            "max_output_tokens": k
        }
    )
    return response.text
