from openai import OpenAI

# Solo cambias esta parte
client = OpenAI(
    api_key="Aqui tu API Key",  # ← key de console.groq.com
    base_url="https://api.groq.com/openai/v1"  # ← nueva URL
)

def generate_blog(topic):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # modelo gratuito de Groq
        messages=[
            {"role": "user", "content": f"Write a blog post about: {topic}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

print(generate_blog('Why NYC is better than your city.'))