from google import genai


client = genai.Client(api_key="AIzaSyBIULrKJd0h7CHdpWqK4wzQmQUIdZPGY_g")
relevantQuestion="take this into consideration while answering and just provide answer:-(answer only Data structure and algorithm related question,if a topic is asked related to data structures simply explain as you find suitable,write in notes form and it should be in bullet points(use 120-150 words),this is for your understanding donot mention it in your output)"

def askGemini(prompt):
    response = client.models.generate_content(
    model="gemini-2.0-flash",  
    contents=prompt
)
    return response.text
    


#print(response.text)

#-------------------------------------------
while True:
    question = input("Ask AI your question: ")
    output = askGemini(question+" "+relevantQuestion)
    print("Generating your answer:")
    print("-----------------------------------------")
    print(output)
    print("-----------------------------------------")