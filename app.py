from flask import Flask, request, jsonify
from rdkit import Chem
from rdkit.Chem import Draw
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_structure():
    try:
        user_input = request.json.get('drug_property', 'CCO')
        mol = Chem.MolFromSmiles(user_input)
        if not mol:
            return jsonify({'error': 'Invalid structure'})

        img = Draw.MolToImage(mol)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({'image': img_str})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
