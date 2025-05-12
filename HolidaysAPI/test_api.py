import requests

def test_colormind():
    try:
        response = requests.post('http://colormind.io/api/', json={'model': 'default'})
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_colormind()