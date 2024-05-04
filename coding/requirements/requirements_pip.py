import subprocess

def install_libraries():
    libraries = [
        "Flask",
        "google-api-python-client",
        "google-auth-oauthlib",
        "transformers",
        "torch torchvision torchaudio",
        "tf-keras"
    ]
    
    for library in libraries:
        subprocess.call(['pip', 'install', library])

    subprocess.call("pip install -U pip setuptools wheel", shell=True)
    subprocess.call("git clone https://github.com/explosion/spaCy", shell=True)
    subprocess.call("cd spaCy", shell=True)
    subprocess.call("pip install -r requirements.txt", shell=True)
    subprocess.call("pip install --no-build-isolation --editable .", shell=True)
    subprocess.call("python -m spacy download en_core_web_sm", shell=True)
if __name__ == "__main__":
    install_libraries()
