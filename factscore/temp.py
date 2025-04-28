import requests


def get_stream():
    # s = requests.Session()
    url = 'http://localhost:11434/api/generate'
    data = '''{
      "model": "llama3.2-vision:11b",
      "prompt": "Why is the sky blue?",
      "stream": true 
    }'''

    # with s.post(url, data=data, stream=True) as res:
    #     for line in res.iter_lines():
    #         if line:
    #             print(line)

    r = requests.post(url, data=data, stream=True)
    for line in r.iter_lines():
        if line:
            print(line.decode('utf-8'))


def generate():
    url = 'http://localhost:11434/api/generate'

    model = "llama3.2-vision:11b"
    prompt = "Why is the sky blue?"
    data = f'''{{
        "model": "{model}",
        "prompt": "{prompt}",
        "stream": false
    }}'''

    r = requests.post(url, data=data, stream=False)
    if r.status_code == 200:
        print(r.json())
    else:
        print(f"Error: {r.status_code}")


def test_pickle():
    import pickle

    # Serialize (pickle) an object
    data = {"name": "Alice", "age": 30, "city": "New York", "complex": (1, 2, 'tupple', [1, 2, 3])}
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    # Deserialize (unpickle) the object
    with open("data.pkl", "rb") as f:
        loaded_data = pickle.load(f)

    print(loaded_data)  # Output: {'name': 'Alice', 'age': 30}
    print(loaded_data['complex'])


def main():
    # get_stream()
    generate()
    # test_pickle()


if __name__ == '__main__':
    main()
