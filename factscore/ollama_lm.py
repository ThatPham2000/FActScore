from factscore.lm import LM
import requests
import ollama


class Ollama(LM):
    def __init__(self, model_name='llama3.2-vision:11b', cache_file=None):
        self.model_name = model_name
        self.save_interval = 100
        super().__init__(cache_file)

    def load_model(self):
        # Load the Ollama model
        self.model = self.model_name

    def _generate(self, prompt, max_sequence_length=2048, max_output_length=128):
        if self.add_n % self.save_interval == 0:
            self.save_cache()

        # Call the Ollama API to generate text
        response = call_via_ollama_package(prompt, model=self.model_name)

        # Get the output from the response
        output = response["response"]
        return output, response


def call_via_ollama_api(prompt, model):
    url = 'http://localhost:11434/api/generate'

    normalized_prompt = "\\n".join(prompt.splitlines())
    data = f'''{{
            "model": "{model}",
            "prompt": "{normalized_prompt}",
            "stream": false
        }}'''

    try:
        res = requests.post(url, data=data)
        res.raise_for_status()
        if res.status_code == 200:
            return res.json()
    except requests.exceptions.RequestException as e:
        print(f'Status code: {e.response.status_code}')
        print(f'Error: {e.response.text}')
        return None


def call_via_ollama_package(prompt, model):
    return ollama.generate(model=model, prompt=prompt)


if __name__ == "__main__":
    ollama_model = Ollama(model_name='llama3.2-vision:11b', cache_file='ollama_cache.pkl')

    # prompt = "Response with raw text (without md formatting): Why is the sky blue?"
    # output, response = ollama_model.generate(prompt)
    # print("add_n:", ollama_model.add_n)
    # print("Generated Output:", output)
    # print("Generated Response:", response)

    prompt2 = """Response with raw text (without md formatting): 
    - Why is the fire red?
    - Why is the sky blue?"""
    output2, response2 = ollama_model.generate(prompt2)
    print("add_n:", ollama_model.add_n)
    print("Generated Output:", output2)
    print("Generated Response:", response2)
