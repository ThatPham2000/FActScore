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
    # data = f'''{{
    #     "model": "{model}",
    #     "prompt": "{prompt}",
    #     "stream": false
    # }}'''

    prompt2 = '''Please breakdown the following sentence into independent facts: He made his acting debut in the film The Moon is the Sun's Dream (1992), and continued to appear in small and supporting roles throughout the 1990s.
- He made his acting debut in the film.
- He made his acting debut in The Moon is the Sun's Dream.
- The Moon is the Sun's Dream is a film.
- The Moon is the Sun's Dream was released in 1992.
- After his acting debut, he appeared in small and supporting roles.
- After his acting debut, he appeared in small and supporting roles throughout the 1990s.

Please breakdown the following sentence into independent facts: He is also a successful producer and engineer, having worked with a wide variety of artists, including Willie Nelson, Tim McGraw, and Taylor Swift.
- He is successful.
- He is a producer.
- He is a engineer.
- He has worked with a wide variety of artists.
- Willie Nelson is an artist.
- He has worked with Willie Nelson.
- Tim McGraw is an artist.
- He has worked with Tim McGraw.
- Taylor Swift is an artist.
- He has worked with Taylor Swift.

Please breakdown the following sentence into independent facts: In 1963, Collins became one of the third group of astronauts selected by NASA and he served as the back-up Command Module Pilot for the Gemini 7 mission.
- Collins became an astronaut.
- Collins became one of the third group of astronauts.
- Collins became one of the third group of astronauts selected.
- Collins became one of the third group of astronauts selected by NASA.
- Collins became one of the third group of astronauts selected by NASA in 1963.
- He served as the Command Module Pilot.
- He served as the back-up Command Module Pilot.
- He served as the Command Module Pilot for the Gemini 7 mission.

Please breakdown the following sentence into independent facts: In addition to his acting roles, Bateman has written and directed two short films and is currently in development on his feature debut.
- Bateman has acting roles.
- Bateman has written two short films.
- Bateman has directed two short films.
- Bateman has written and directed two short films.
- Bateman is currently in development on his feature debut.

Please breakdown the following sentence into independent facts: Michael Collins (born October 31, 1930) is a retired American astronaut and test pilot who was the Command Module Pilot for the Apollo 11 mission in 1969.
- Michael Collins was born on October 31, 1930.
- Michael Collins is retired.
- Michael Collins is an American.
- Michael Collins was an astronaut.
- Michael Collins was a test pilot.
- Michael Collins was the Command Module Pilot.
- Michael Collins was the Command Module Pilot for the Apollo 11 mission.
- Michael Collins was the Command Module Pilot for the Apollo 11 mission in 1969.

Please breakdown the following sentence into independent facts: He was an American composer, conductor, and musical director.
- He was an American.
- He was a composer.
- He was a conductor.
- He was a musical director.

Please breakdown the following sentence into independent facts: She currently stars in the romantic comedy series, Love and Destiny, which premiered in 2019.
- She currently stars in Love and Destiny.
- Love and Destiny is a romantic comedy series.
- Love and Destiny premiered in 2019. 

Please breakdown the following sentence into independent facts: Michael Collins (born October 31, 1930) is a retired American astronaut and test pilot who was the Command Module Pilot for the Apollo 11 mission in 1969.
- Michael Collins was born on October 31, 1930.
- Michael Collins is retired.
- Michael Collins is an American.
- Michael Collins was an astronaut.
- Michael Collins was a test pilot.
- Michael Collins was the Command Module Pilot.
- Michael Collins was the Command Module Pilot for the Apollo 11 mission.
- Michael Collins was the Command Module Pilot for the Apollo 11 mission in 1969.

Please breakdown the following sentence into independent facts: Thierry Henry (born 17 August 1977) is a French professional football coach, pundit, and former player.'''


    normalized_prompt2 = "\\n".join(prompt2.splitlines())
    data = f'''{{
                    "model": "{model}",
                    "prompt": "{normalized_prompt2}",
                    "stream": false
                }}'''

    print(data)

    r = requests.post(url,
                      data=data,
                      stream=False, )

    if r.status_code == 200:
        print(r.json())
    else:
        print(f"Error: {r.status_code}")
        print(f'Text: {r.text}')
        print(f'Content: {r.content}')
        print(r.raise_for_status())


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
