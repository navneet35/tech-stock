from flask import Flask, request, jsonify
from langchain_community.chat_models import AzureChatOpenAI
import base64
import os

app = Flask(__name__)

llm = AzureChatOpenAI(
    openai_api_key="hEeWCSWhjOY0ZZuJfPW4pMLk3uDCsBBUnZF10ps4YDe84XUumN1TJQQJ99BEACHYHv6XJ3w3AAAAACOGXfsx",
    azure_endpoint="https://navne-ma5lh7gl-eastus2.cognitiveservices.azure.com/",
    deployment_name="gpt-4.1",
    openai_api_version="2025-01-01-preview",
    openai_api_type="azure",
)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    image_data_url = data.get('image')
    if not image_data_url:
        return jsonify({'error': 'No image provided'}), 400

    # Extract base64 from data URL
    header, encoded = image_data_url.split(',', 1)
    image_bytes = base64.b64decode(encoded)

    # Prepare prompt for LLM (Vision model)
    prompt = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract all stock data (graph, PE ratio, etc) and provide technical analysis with buy/sell/hold advice."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{encoded}"}}
            ]
        }
    ]

    try:
        response = llm.invoke(prompt)
        return jsonify({'analysis': response.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test-llm', methods=['GET'])
def test_llm():
    prompt = [
        {
            "role": "user",
            "content": "What are the top places to visit in Redmond, Washington?"
        }
    ]
    try:
        response = llm.invoke(prompt)
        return jsonify({'response': response.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
