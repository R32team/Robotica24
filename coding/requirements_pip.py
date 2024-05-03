import subprocess

def install_libraries():
    libraries = [
        "Flask",
        "google-api-python-client",
        "google-auth-oauthlib",
        "transformers"
    ]
    
    for library in libraries:
        subprocess.call(['pip', 'install', library])

    subprocess.call("pip install -U pip setuptools wheel", shell=True)
    subprocess.call("pip install -U spacy", shell=True)
    subprocess.call("python -m spacy download it_core_news_sm", shell=True)

if __name__ == "__main__":
    install_libraries()
