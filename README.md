# Behavior_Tree_LLama
Generation of Behavior tree by LLama 2 in XML format

This project uses the LLaMA 2 model to generate behavior trees in XML format based on given instructions.

## Description

The script prompts the user for input, generates a response using a pre-trained model, formats the result into XML, and saves it to a file named `output.xml`.

## Instalation   

```bash
   pip install -r requirements.txt
```   

## Usage
1. Download model [weights](https://disk.yandex.ru/d/TXDoM55A4Tp-xQ)
1. Make sure you have the LLaMA 2 model available at the path `model/checkpoint-50`.
2. Run the main script:

   
```bash
   python main.py <INPUT_TASK>
```  

The generated response will be saved in `output.xml`.
