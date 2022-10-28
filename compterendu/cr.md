# Détection de plaque

## Introduction

Dans le cadre du projet d'Image en I2FA, nous avons décider de travailler sur l'isolation et la détection des plaques d'immatriculations.  
Nous devons donc répondre au besoin de pouvoir obtenir un fichier texte contenant l'immatriculation à partir d'une photo d'une voiture avec sa plaque d'immatriculation.  

## Outils utilisés

Le langage que nous avons adopté est Python, celui-ci est simple à prendre en main et permets l'accès à des outils puissants facilement et intuitivement.  
Les outils utilisés sont assez simple et limité, on utilise OpenCV une librairie permettant l'édition et la transformation d'image.  
Requests afin de pouvoir faire des requetes http. L'api OCR SPACE afin de pouvoir effetuer la transformation image vers texte à partir de l'extraction de la plaque.  

## Fonctionnememnt

Le fonctionnement se découpe en plusieurs étapes.
Dans un premier temps on demande à l'utilisateur quel image contenant une plaque il veut traiter en demandant son numéro.

On va par la suite charger l'image, la redimenssioner à une taille standart pour nous et la passer en nuance de gris

Par la suite on va filtrer l'image en appliquant un filtre bilinéaire, il a pour but d'accentuer les bordures et réduire le flou en faisant une moyenne pondéré des intensités des pixels voisins.  
On va donc avoir des contours plus marqué et donc détectables par un algorithme de détection de bords

On va donc vouloir utiliser l'algorithme de Canny pour faire la detection des bordure.

OpenCV nous rends alors un objets contenants l'ensemble des contours qu'il a détecté, on va pouvoir requeter chacun d'entre eux leur coordonnées et par la suite les trié par 


## Gestion du projet

## Repartition des taches 

## Axes d'améliorations 
