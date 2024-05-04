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
        subprocess.call(['pip3', 'install', library])

    subprocess.call("pip3 install -U pip setuptools wheel", shell=True)
    subprocess.call("git clone https://github.com/explosion/spaCy", shell=True)
    subprocess.call("cd spaCy", shell=True)
    subprocess.call("pip3 install -r requirements.txt", shell=True)
    subprocess.call("pip3 install --no-build-isolation --editable .", shell=True)
    subprocess.call("python3 -m spacy download it_core_news_sm", shell=True)
if __name__ == "__main__":
    install_libraries()
