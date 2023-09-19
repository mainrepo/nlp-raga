# NLP RAGA - backend for [agent-parag](https://github.com/mainrepo/agent-parag)
The ***nlp-raga*** is ***R***etrieval ***A***ugmented ***G***eneration ***A***gent (**RAGA**) service for **NLP**. The simplest implementation of the **RAG** with OpenAI ChatGPT LLM directly.

## User Guidelines
Please use terminal for ***project installation**, **build** & **running locally** for **testing**. The **integrated terminal of vscode** can also be used. The vscode must have an appropriate extensions installed for development work. The main one being pylance language server. **Windows users can use Ubuntu or Al2 machines running on WSL 2***

After cloing the [nlp-raga](https://github.com/mainrepo/nlp-raga) repository; **cd** to the *nlp-raga* directory and fire below commands as required.

### <ins>Setup</ins>
A set of python versions can be installed using [pyenv](https://github.com/pyenv/pyenv). We will use 3.9 variant for it's stability. Otherwise direct installation of python 3.9 is also good for these basic samples.
```shell
# check the versions that can be installed
pyenv install -l | grep -v grep | grep 3.9

# install the 3.9 variant
pyenv install 3.9.xx

# check the installed python versions
pyenv versions

# make 3.9 variant as global python version
pyenv use 3.9

# create the 3.9 virtual environment
python -m venv /path/to/venv.d

# activate the 3.9 virtual environment
source /path/to/venv.d/bin/activate
```
___
The project uses [poetry](https://python-poetry.org/docs/#installation) as a python package manager.
```shell
# install the python dependencies
poetry install
```

### <ins>Running</ins>
Please set the environment variable ***OPENAI_API_KEY*** before running the service
```shell
# running the NLP for default pizza orders, an OpenAI ChatGPT agent
poetry run test-srv
```

## <ins>Vital Info</ins>
1. The project uses poetry (pyproject.toml) for python dependency management.
2. Here are screenshots of the running service.\
![Swagger](/images/swagger.png?raw=true) \
\
![Test](/images/test.png?raw=true)

3. The below screenshot is from the chat UI for this backend called ***[agent-parag](https://github.com/mainrepo/agent-parag)***.\
![BasicRun](/images/basic_run.png?raw=true)

## <ins>License</ins>
[MIT](https://choosealicense.com/licenses/mit/)