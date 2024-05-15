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

main.py - Source code for web-scrapping https://blog.hubspot.com/ and searching relevant blogs, as well as count the characters and keywords on most recent ones.
requirements.txt - File with listed all the dependencies needed to setup development environment.
Dockerfile - Text file that contains a set of instructions used to build a Docker image for easier deployment.

### How to run

In order to run the script, pull the repository and run this command in Bash:
```
docker run app X Y
```
Where X is the number of blogs we want to check and Y is the number of most common occurences of words/keyphrases

## Task 2 (Technical Writer)

PL: Napisz artykuł na bloga na temat: "Jak się zintegrować z API stripe.com korzystając z udostępnionego przez stripe SDK dla Pythona"

ENG: "Write a blog article on the topic: 'How to integrate with the stripe.com API using the Stripe SDK for Python'"

## Task 2 - explanation

The entire proposed blog is stored in the "BLOG.md" file with all the teoretical explanations and steps to setup.