from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key as an environment variable for security
openai.api_key = os.getenv(
    "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"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_text():
    user_input = request.json.get("text", "")
    task = request.json.get("task", "grammar")  # 'grammar' or 'generation'

    try:
        if task == "grammar":
            # Grammar correction prompt
            prompt = f"Correct the grammar and enhance clarity:\n\n{user_input}"
        elif task == "generation":
            # Text generation prompt
            prompt = f"Generate a continuation of the following text:\n\n{user_input}"

        # OpenAI GPT call
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=150, temperature=0.7
        )

        result = response.choices[0].text.strip()
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/translate", methods=["POST"])
def translate_text():
    user_input = request.json.get("text", "")
    target_language = request.json.get("language", "English")  # Default to French

    try:
        prompt = f"Translate the following text to {target_language}:\n\n{user_input}"

        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=150, temperature=0.7
        )

        result = response.choices[0].text.strip()
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/adjust_tone", methods=["POST"])
def adjust_tone():
    user_input = request.json.get("text", "")
    tone = request.json.get("tone", "formal")

    try:
        prompt = f"Rewrite the following text in a {tone} tone:\n\n{user_input}"

        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=150, temperature=0.7
        )

        result = response.choices[0].text.strip()
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/summarize", methods=["POST"])
def summarize_text():
    user_input = request.json.get("text", "")

    try:
        prompt = f"Summarize the following text:\n\n{user_input}"

        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=100, temperature=0.7
        )

        result = response.choices[0].text.strip()
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
