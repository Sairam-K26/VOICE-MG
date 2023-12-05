# SpeechRecognition_vs_Whisper
An Complete Implementation over speech recognition and whisper to know their effiecncy in Speech to Text modules as with Runtime Audio Recording

SpeechRecognition.py is with SpeechRecognition module Code

w.py is with Whisper module Code

## 1) Download requiremts.txt 

```
pip install requirements.txt
```

## 2) Run the SpeechRecognition.py for SpeechRecognition module accuracy testing

```
streamlit run SpeechRecognition.py
```

## 3) Run the whisper.py for whisper module accuracy testing

```
streamlit run w.py
```
## Optional 

(you can run the recording.ipynb file for recording audio)

If needed Install chocolately in your system @ Powershell to run Whisper in Local System

#Grammer Checking of the transcripted text with Whisper,Llama 

## voice.py gives the entire code to make whisper transcript as input to llama local models input and check the grammer 

## For that you should first Install the following Dependencies and models in Local System:

1) https://visualstudio.microsoft.com/visual-cpp-build-tools/
2) https://huggingface.co/TheBloke/Llama-2-13B-GGML/blob/main/llama-2-13b.ggmlv3.q4_0.bin

## Then pip install llama cpp and llama index:
```
 pip install llama-cpp-python
 pip install llama_index
```

## Finally Run the Voice.py for the Execution 🔥:

```
 streamlit run voice.py 
```
