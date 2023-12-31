#prova modifica
from pathlib import Path

import pandas as pd
import seaborn as sns

import shiny.experimental as x
from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
from htmltools import HTML
from fasttrees import *

print("FIRST LINE")


# HTML content
html_home = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #444;
            text-align: center;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        footer {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Shiny FFTrees!</h1>
    </header>

    <nav>
        <a href="#">Home</a>

    </nav>

    <main>
        <h2>About this site</h2>
        <p>Shiny FFTrees is a Shiny application that allows you to create fast-and-frugal decision trees (FFTs) using the FFTrees Python package in a web-browser. The app is a companion to the following article:
         <li>Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368</li>.</p>

    </main>
    <main>
        <h2>How to use it</h2>
        <p>You should navigate this site using the header tabs in order:

        <li>Data: Select a dataset and binary criterion</li>
        <li>Create: Create FFTs, either with a built-in algorithm, or by hand.</li>
        <li>Visualize: Plot FFTs along with accuracy statistics</li></p>
    </main>
    <main>
        <h2>Contact </h2>
        <p>
        This site is being maintained by Salvatore Stile, co-creator of the FFTrees python package.
        If you have comments, suggestions, or bug reports you'd like to share, please post an issue on GitHub and or send me an email by clicking one of the icons below.</p>
    </main>


    <footer>
        &copy; 2023 Fast&Frugal Trees Python implementation
    </footer>
</body>
</html>

"""

html_intro ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #444;
            text-align: center;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        footer {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>INTRO</h1>
    </header>

    <nav>
        <a href="#">Home</a>

    </nav>

    <main>
        <h2>What is a decision tree?</h2>
        <p>Formally, a decision tree is comprised of a sequence of nodes, representing questions, branches, representing answers to questions, and leaves, representing decisions. Informally, a decision tree is a set of ordered, conditional rules in the form 'If A, then B' that are applied sequentially until a decision is reached.

Unlike compensatory algorithms such as regression and random forests, decision trees typically use very little information, and guide decision makers in their information search process. </p>

    </main>
    <main>
        <h2>Fast-and-frugal-tree (FFT)</h2>
        <p>A fast-and-frugal tree (FFT) is an extremely simple decision tree with exactly two branches under each node, where one (or both) branches is an exit branch (Martignon et al., 2008). In other words, in an FFT one answer (or in the case of the final node, both answers) to every question posed by a node will trigger an immediate decision. Because FFTs have an exit branch on every node, they typically make decisions faster than standard decision trees.</p>
    </main>
    <footer>
        &copy; 2023 Fast&Frugal Trees Python implementation
    </footer>
</body>
</html>

"""

html_data = """
<!DOCTYPE html>
<html lang="it">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>La Mia Pagina Web</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           background-color: #f2f2f2;
           margin: 0;
           padding: 0;
       }

       header {
           background-color: #333;
           color: #fff;
           text-align: center;
           padding: 20px;
       }

       nav {
           background-color: #444;
           text-align: center;
           padding: 10px;
       }

       nav a {
           color: #fff;
           text-decoration: none;
           margin: 0 10px;
       }

       main {
           max-width: 800px;
           margin: 20px auto;
           background-color: #fff;
           padding: 20px;
           border-radius: 5px;
           box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
       }

       footer {
           text-align: center;
           background-color: #333;
           color: #fff;
           padding: 10px;
       }

       /* Aggiunta dello stile per il box con il pulsante "Create" */
       .create-box {
           background-color: #e6e6e6;
           padding: 15px;
           border-radius: 5px;
           margin-top: 20px;
       }

       .create-button {
           display: block;
           margin: 10px auto;
           padding: 10px 20px;
           background-color: #4caf50;
           color: #fff;
           text-decoration: none;
           border-radius: 5px;
           text-align: center;
       }
   </style>
</head>
<body>
   <header>
       <h1>Benvenuto su Shiny FFTrees!</h1>
   </header>

   <nav>
       <a href="#">Home</a>
   </nav>

   <main>
       <h2>Informazioni sul sito</h2>
       <p>Shiny FFTrees è un'applicazione Shiny che ti consente di creare alberi decisionali veloci e frugali (FFT) utilizzando il pacchetto FFTrees Python in un browser web. L'app è un complemento al seguente articolo:</p>
       <li>Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368.</li>
   </main>

   <main>
       <h2>Come utilizzarlo</h2>
       <p>Si consiglia di navigare su questo sito utilizzando le schede dell'intestazione nell'ordine seguente:</p>
       <li>Dati: Seleziona un set di dati e un criterio binario</li>
       <li>Crea: Crea FFT, sia con un algoritmo incorporato, sia manualmente.</li>
       <li>Visualizza: Traccia FFT insieme a statistiche di accuratezza</li>
   </main>

   <main>
       <h2>Contatto </h2>
       <p>Questo sito è gestito da Salvatore Stile, co-creatore del pacchetto FFTrees Python. Se hai commenti, suggerimenti o segnalazioni di bug da condividere, pubblica un problema su GitHub o inviami una email cliccando su una delle icone sottostanti.</p>
   </main>

   <!-- Nuova sezione con il box "Create" -->
   <main class="create-box">
       <h2>Select Data</h2>
       <p>Utilizza il pulsante qui sotto per iniziare:</p>
       <a href="#" class="create-button">Select</a>
   </main>

   <footer>
       &copy; 2023 Implementazione in Python di Fast&Frugal Trees
   </footer>
</body>
</html>
"""
html_create = """
 <!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Mia Pagina Web</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #444;
            text-align: center;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        footer {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
        }

        /* Aggiunta dello stile per il box con il pulsante "Create" */
        .create-box {
            background-color: #e6e6e6;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }

        .create-button {
            display: block;
            margin: 10px auto;
            padding: 10px 20px;
            background-color: #4caf50;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>Benvenuto su Shiny FFTrees!</h1>
    </header>

    <nav>
        <a href="#">Home</a>
    </nav>

    <main>
        <h2>Informazioni sul sito</h2>
        <p>Shiny FFTrees è un'applicazione Shiny che ti consente di creare alberi decisionali veloci e frugali (FFT) utilizzando il pacchetto FFTrees Python in un browser web. L'app è un complemento al seguente articolo:</p>
        <li>Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368.</li>
    </main>

    <main>
        <h2>Come utilizzarlo</h2>
        <p>Si consiglia di navigare su questo sito utilizzando le schede dell'intestazione nell'ordine seguente:</p>
        <li>Dati: Seleziona un set di dati e un criterio binario</li>
        <li>Crea: Crea FFT, sia con un algoritmo incorporato, sia manualmente.</li>
        <li>Visualizza: Traccia FFT insieme a statistiche di accuratezza</li>
    </main>

    <main>
        <h2>Contatto </h2>
        <p>Questo sito è gestito da Salvatore Stile, co-creatore del pacchetto FFTrees Python. Se hai commenti, suggerimenti o segnalazioni di bug da condividere, pubblica un problema su GitHub o inviami una email cliccando su una delle icone sottostanti.</p>
    </main>

    <!-- Nuova sezione con il box "Create" -->
    <main class="create-box">
        <h2>Create FFTS!</h2>
        <p>Utilizza il pulsante qui sotto per iniziare:</p>
        <button id="create-button" onclick="myFunction()" class="create-button">Create</button>
    </main>
    <script>
    function myFunction() {
        // Imposta il contenuto dell'elemento con ID "demo"
        document.getElementById("demo").innerHTML = "Hello World";

        // Reindirizza la pagina a www.google.it
        window.location.href = "http://www.google.it";
    }

    // Aggiungi un gestore di eventi al bottone
    document.getElementById("create-button").addEventListener("click", myFunction);
</script>

    <footer>
        &copy; 2023 Implementazione in Python di Fast&Frugal Trees
    </footer>
</body>
</html>
"""
html_visualize = """
<!DOCTYPE html>
<html lang="it">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>La Mia Pagina Web</title>
   <style>
       body {
           font-family: Arial, sans-serif;
           background-color: #f2f2f2;
           margin: 0;
           padding: 0;
       }

       header {
           background-color: #333;
           color: #fff;
           text-align: center;
           padding: 20px;
       }

       nav {
           background-color: #444;
           text-align: center;
           padding: 10px;
       }

       nav a {
           color: #fff;
           text-decoration: none;
           margin: 0 10px;
       }

       main {
           max-width: 800px;
           margin: 20px auto;
           background-color: #fff;
           padding: 20px;
           border-radius: 5px;
           box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
       }

       footer {
           text-align: center;
           background-color: #333;
           color: #fff;
           padding: 10px;
       }

       /* Aggiunta dello stile per il box con il pulsante "Create" */
       .create-box {
           background-color: #e6e6e6;
           padding: 15px;
           border-radius: 5px;
           margin-top: 20px;
       }

       .create-button {
           display: block;
           margin: 10px auto;
           padding: 10px 20px;
           background-color: #4caf50;
           color: #fff;
           text-decoration: none;
           border-radius: 5px;
           text-align: center;
       }
   </style>
</head>
<body>
   <header>
       <h1>Benvenuto su Shiny FFTrees!</h1>
   </header>

   <nav>
       <a href="#">Home</a>
   </nav>

   <main>
       <h2>Informazioni sul sito</h2>
       <p>Shiny FFTrees è un'applicazione Shiny che ti consente di creare alberi decisionali veloci e frugali (FFT) utilizzando il pacchetto FFTrees Python in un browser web. L'app è un complemento al seguente articolo:</p>
       <li>Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368.</li>
   </main>

   <main>
       <h2>Come utilizzarlo</h2>
       <p>Si consiglia di navigare su questo sito utilizzando le schede dell'intestazione nell'ordine seguente:</p>
       <li>Dati: Seleziona un set di dati e un criterio binario</li>
       <li>Crea: Crea FFT, sia con un algoritmo incorporato, sia manualmente.</li>
       <li>Visualizza: Traccia FFT insieme a statistiche di accuratezza</li>
   </main>

   <main>
       <h2>Contatto </h2>
       <p>Questo sito è gestito da Salvatore Stile, co-creatore del pacchetto FFTrees Python. Se hai commenti, suggerimenti o segnalazioni di bug da condividere, pubblica un problema su GitHub o inviami una email cliccando su una delle icone sottostanti.</p>
   </main>

   <!-- Nuova sezione con il box "Create" -->
   <main class="create-box">
       <h2>Create FFTS!</h2>
       <p>Utilizza il pulsante qui sotto per iniziare:</p>
       <a href="#" class="create-button">Visualiza FFT tree</a>
   </main>

   <footer>
       &copy; 2023 Implementazione in Python di Fast&Frugal Trees
   </footer>
</body>
</html>
"""
html_article = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #444;
            text-align: center;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        footer {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1></h1>
    </header>

    <nav>
        <a href="#"></a>

    </nav>

    <main>
        <h2>FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees</h2>
        <p>Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368.
        <a href="https://econpsychbasel.shinyapps.io/shinyfftrees/"> https://econpsychbasel.shinyapps.io/shinyfftrees/</a></p>


    </main>
    <footer>
        &copy; 2023 Fast&Frugal Trees Python implementation
    </footer>
</body>
</html>

"""
html_learn = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        nav {
            background-color: #444;
            text-align: center;
            padding: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        main {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }

        footer {
            text-align: center;
            background-color: #333;
            color: #fff;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1></h1>
    </header>

    <nav>
        <a href="#"></a>

    </nav>

    <main>
        <h2>Fast-and-frugal trees (FFT)</h2>
        <p>A fast-and-frugal tree (FFT) was defined by Martignon et al. (2008) as a decision tree with exactly two branches from each node, where one branch (or in the case of the final node, both branches) is exit branch leading to a terminal leaf.

FFTs have been successfully used to both describe decision processes and to provide prescriptive guides for effective real-world decision making in a variety of domains, including medical (Fischer et al., 2002; Jenny, Pachur, Williams, Becker & Margraf, 2013; Super, 1984; Wegwarth, Gaissmaier & Gigerenzer, 2009), legal (Dhami, 2003; Dhami & Ayton, 2001; Dhami & Harries, 2001), financial (Aikman et al., 2014; Woike, Hoffrage & Petty, 2015) and managerial (Luan & Reb, 2017) decision making.</p>

    </main>
    <main>
        <h2>Algorithms</h2>
        <p>A fast-and-frugal tree construction algorithm accomplishes the following tasks (not necessarily in this order):

    Select cues
    Determine the order of cues
    Determine a decision threshold for each cue
    Determine the exit (positive or negative) for eaach cue

FFTrees contains four different tree construction algorithms that solve these four tasks in different ways. Here is a brief description of how the four different algorithms in FFTrees solve these tasks. For a full description, consult Martignon et al. (2008) and Phillips et al. (2017).

<li>Max and Zig-zag (Martignon et al., 2008)</li>

The Max and Zig-Zag algorithms were created by Martignon and colleagues (2008) as extremely simple algorithms that could in principle be applied 'in the head' of a person with a pencil, paper and calculator.

They begin by calculating a decision threshold for each cue. For numeric cues, the median value is used, while for nominal cues, dummy coded values of individual cue values are used.

For the Max algorithm, decision thresholds are then ranked according to the maximum value of their positive predictive value (ppv) and negative predictive value (npv). Finally, each cue is given the exit corresponding to whether their negative or positive predictive values are higher.
<li>Ifan and Dfan (Phillips et al., 2017)</li>

The ifan and dfan algorithms were created by Phillips and colleagues (2017). They were inspired by max and zig-zag, but are more flexible and computationally demanding than max and zig-zag.

The ifan algorithm works as follows. First, a decision threshold is calculated for each cue that maximizes the goal.chase statistic (default is 'bacc'). Next, cues are rank ordered by goal.chase. The top max.levels cues are then selected and all remaining cues are discarded. The ifan algorithm then creates a 'fan' of all possible trees that could be created from those those max.levels cues. Finally, the tree with the highest value of the goal statistic (default is 'bacc') is selected as the final tree.

The dfan algorithm works similarly to ifan. However, rather than calculating decision thresholds for each cue only once based on all data, it recursively calculates new thresholds for cues based on unclassified cases as the trees are grown. Thus, dfan tries to optimize decision thresholds for different subsets of cases. For this reason it is computationally much more demanding than the other three algorithms.</p>


<p><h3>References</h3>

Martignon, L., Katsikopoulos, K. V., & Woike, J. K. (2008). Categorization with limited resources: A family of simple heuristics. Journal of Mathematical Psychology, 52(6), 352–361.

Phillips, N, D., Neth, Hansjörg, Woike, J. K., & Gaissmaier, W. (2017). FFTrees: A FFTrees: A toolbox to create, visualize, and evaluate fast-and-frugal decision trees. Judgment and Decision Making, 12(4), 344-368.</p>
    </main>
    <footer>
        &copy; 2023 Fast&Frugal Trees Python implementation
    </footer>
</body>
</html>

"""

html_prova= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestione Evento</title>
</head>
<body>

<button id="myButton">Premi per gestire l'evento</button>

<script>
    // Aggiungi un gestore di eventi al bottone
    document.getElementById("myButton").addEventListener("click", function() {

    cancer = load_breast_cancer()

    # Estrai le features e le etichette di classe
    X_cancer, y_cancer = cancer.data, cancer.target

    # Suddividi il dataset in set di addestramento e test
    X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(
        X_cancer, y_cancer, test_size=0.4, random_state=42)

        # Fit and test fitted tree
        fftc = FastFrugalTreeClassifier()
        fftc.fit(X_train_cancer, y_train_cancer)
        print(fftc.score(X_test_cancer, y_test_cancer))
        alert("Evento gestito");
    });
</script>

</body>
</html>
"""

# Part 1: ui ----
app_ui = app_ui = ui.page_fluid(
    # style ----
    ui.navset_tab(
        # elements ----
        #ui.nav("HOME", ui.div("Welcome!")),
        ui.nav("HOME", HTML(html_home)),
        ui.nav("Intro", HTML(html_intro)),
        ui.nav("Data", HTML(html_data)),
        ui.nav("Create", HTML(html_create)),
        ui.nav("Visualize", HTML(html_visualize)),
        ui.nav("Article", HTML(html_article)),
        ui.nav("Learn", HTML(html_prova))
    )
)

# Part 2: server ----
def server(input, output, session):
    def data_output():
        ui.input_select("data_output", HTML("<i class='fa fa-table'></i> Choose a dataset"),["apple", "banana", "cherry", "date", "fig"])


# Combine into a shiny app.
# Note that the variable must be "app".
app = App(app_ui, server)
