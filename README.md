# z3x-recruitment-tasks

## Task 1 (Junior Python Developer)

PL: Proszę o napisanie skryptu w Python (v3), odpalanego w konsoli. Skrypt ten powinien pobrać 3 ostatnio opublikowane artykuły ze strony https://blog.hubspot.com/ Następnie powinien sparsować każdy z nich i dla każdego w konsoli wyświetlić:
1. Liczbę słów użytych w artykule
2. Liczbę liter użytych w artykule
3. Pięć najczęściej używanych fraz kluczowych w artykule (frazy kluczowe mogą zawierać jedno słowo, dwa lub trzy), posortować od najczęściej używanej do najrzadziej używanej

ENG: Please write a Python (v3) script that runs in the console. This script should fetch the 3 most recently published articles from the https://blog.hubspot.com/ website. Then, it should parse each of them and display the following in the console for each article:

1. The number of words used in the article
2. The number of letters used in the article
3. The five most frequently used keywords in the article (keywords can consist of one word, two words, or three words), sorted from most frequently used to least frequently used.

## Task 1 - explanation

### Files associated with Task 1:

`main.py` - Source code for web-scrapping https://blog.hubspot.com/ and searching relevant blogs, as well as count the characters and keywords on most recent ones.\
`requirements.txt` - File with listed all the dependencies needed to setup development environment.\
`Dockerfile` - Text file that contains a set of instructions used to build a Docker image for easier deployment.

### How to run:

### Using "install.sh" (works only for Linux)

First, it's necessary to gather all dependencies needed for project. Open terminal and navigate to project directory. Type in Bash:

```
source install.sh
```
If using IDE such as VS Code, use "ctrl+shift+p" in order to clear Python cache and reload window.

### Manually creating the environment (for Windows users)

Create Python virtual environment, typing in terminal (must be inside project directory):

```
python -m venv .z3x_dev
```
Where ".z3x_dev" is the name of virtual environment

Activate the environment:

```
. .\.z3x_dev\Scripts\activate
```

Clear Python cache and reload window ("ctrl+shift+p" in VS Code)

Install the dependencies from `requirements.txt` file:

```
pip install -r .\requirements.txt
```

#### Running the script

In order to run the script, type in terminal:

```
python3 main.py X Y
```
Where X is the number of blogs we want to check and Y is number of most common occurences of words and keyphrases.
If we ommit the arguments, the default values are 3 for blogs and 5 for occurences.

### Using Docker

Check if Docker is installed on current system. Open command line and navigate to project directory. Type command below
```
docker build -t app .
```

In order to run the script, run this command:
```
docker run app
```
This approach uses default values for number of blogs we want to check and most common occurences of words and keyphrases.

## Task 2 (Technical Writer)

PL: Napisz artykuł na bloga na temat: "Jak się zintegrować z API stripe.com korzystając z udostępnionego przez stripe SDK dla Pythona"

ENG: "Write a blog article on the topic: 'How to integrate with the stripe.com API using the Stripe SDK for Python'"

## Task 2 - explanation

The entire proposed blog is stored in the "BLOG.md" file with all the teoretical explanations and steps to setup.