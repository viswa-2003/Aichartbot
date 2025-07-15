import google.generativeai as ai

API_KEY = "proj_uwimvoAKLhWDkamBQhAecTI5"
ai.configure(api_key=API_KEY)

try:
    model = ai.GenerativeModel("gemini-pro")
    response = model.generate_content("Hello!")
    print("✅ API Key Works! Response:", response.text)
except Exception as e:
    print("❌ API Key is INVALID or model issue:", e)
