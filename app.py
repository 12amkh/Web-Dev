from fastapi import FastAPI, Request
import openai

app = FastAPI()

# Set your OpenAI API key
openai.api_key = "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"

@app.post("/summarize/")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    if text:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize this text: {text}"}
            ],
            max_tokens=100
        )
        return {"summary": response['choices'][0]['message']['content']}
    return {"error": "No text provided"}
