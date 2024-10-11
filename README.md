# XssFindr

XssFindr est un outil de pentest en Python permettant de tester la présence de failles XSS (Cross-Site Scripting) sur des pages web. Cet outil utilise Selenium pour injecter automatiquement des scripts malveillants dans les champs de saisie d'une page web afin de vérifier si une faille XSS est présente.
Fonctionnalités

    Injection automatique de plusieurs charges utiles XSS dans les champs de saisie des pages web.
    Détection des vulnérabilités XSS basées sur l'apparition d'alertes JavaScript.
    Génération d'un rapport avec le nombre de failles détectées.

Installation
Prérequis

Avant d'installer XssFindr, vous devez avoir :

    Python 3.x installé sur votre machine.
    Google Chrome installé, car le script utilise le WebDriver de Chrome pour l'automatisation.

Étape 1 : Cloner le dépôt GitHub

Commencez par cloner le dépôt GitHub de XssFindr :
```
git clone https://github.com/nathanbvn/XssFindr.git
cd XssFindr
```
Étape 2 : Installer les dépendances

Le script utilise Selenium pour interagir avec les pages web. Vous pouvez installer les dépendances nécessaires en exécutant la commande suivante :

```

pip install selenium

```

Étape 3 : Installer le ChromeDriver

XssFindr utilise Selenium et Google Chrome pour les tests. Vous devez donc installer ChromeDriver (le WebDriver pour Google Chrome).
Sur Linux/Mac

Vous pouvez installer ChromeDriver à l'aide des commandes suivantes :

```

# Télécharger ChromeDriver
wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip

# Décompresser l'archive
unzip chromedriver_linux64.zip

# Rendre le fichier exécutable
chmod +x chromedriver

# Déplacer ChromeDriver dans le répertoire `/usr/local/bin`
sudo mv chromedriver /usr/local/bin/

```

Sur Windows

Téléchargez ChromeDriver correspondant à la version de Google Chrome installée, décompressez-le et ajoutez le répertoire contenant chromedriver.exe à la variable d'environnement PATH.
Utilisation

Pour lancer l'outil, exécutez le script Python comme suit :

```

python3 xssfindr.py
```
Ensuite, entrez l'URL de la page à tester lorsqu'il est demandé.

![image](https://github.com/nathanbvn/XssFindr/assets/94560509/7666eedc-8e2b-4656-8ee7-6a5113bce23e)
