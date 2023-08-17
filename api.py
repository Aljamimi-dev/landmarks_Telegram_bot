import openai

chatgpt_API_key = 'Enter your API key'
openai.api_key = chatgpt_API_key

# To connect with chatgpt API
def get_gpt_reply(prompt, max_tokens = 250):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'user' , 'content': f'what are the places that I can visit in {prompt} ?'}],
        max_tokens = max_tokens
    )
    
    # To get the generated message only 
    response_message = response.to_dict()['choices'][0]['message']['content']
    return response_message


print(get_gpt_reply('what is the most famous programming language?'))