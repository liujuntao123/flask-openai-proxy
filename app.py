from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:match>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(match):
    url = f'https://api.openai.com/{match}'
    headers = {key: value for (key, value) in request.headers if key != 'Host'}
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        params=request.args,
        cookies=request.cookies,
        stream=True,
    )

    response = Response(resp.content, resp.status_code, resp.raw.headers.items())
    return response

if __name__ == '__main__':
    app.run(debug=True)
