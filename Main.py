#initialisation de la valeur de sortie 
output = [0, 0, 0]

# Premiere neurone du reseau de neurone
# Valeurs en entrees d'une neurone du reseau de neurone (Premiere neurone)
inputsN = [1, 2, 3, 2.5]
# Valeurs du poids des resaux de neurones de cette neurone (Pewmiere neurone)
weightN1 = [0.2, 0.8, -0.5, 1]
# Valeur du biais d'une neurone du réseau de neurone (Pewmiere neurone)
biaisN1 = 2
# Valeur de sortie de la premiere neurone 
OutputN1 = inputsN[0] * weightN1[0] + inputsN[1] * weightN1[1] + inputsN[2] * weightN1[2] + inputsN[3] * weightN1[3] + biaisN1

# Deuxieme neurone du reseau de neurone

# Valeurs du poids des resaux de neurones de cette neurone (deuxieme neurone)
weightN2 = [0.5, -0.91, 0.26, -0.5]
# Valeur du biais d'une neurone du réseau de neurone (deuxieme neurone)
biaisN2 = 3
# Valeur de sortie de la deuxieme neurone
OutputN2 = inputsN[0] * weightN2[0] + inputsN[1] * weightN2[1] + inputsN[2] * weightN2[2] + inputsN[3] * weightN2[3] + biaisN2

# Deuxieme neurone du reseau de neurone

# Valeurs du poids des resaux de neurones de cette neurone (troisieme neurone)
weightN3 = [-0.26, -0.27, 0.17, 0.87]
# Valeur du biais d'une neurone du réseau de neurone (troisieme neurone)
biaisN3 = 0.5
# Valeur de sortie de la troisieme neurone
OutputN3 = inputsN[0] * weightN3[0] + inputsN[1] * weightN3[1] + inputsN[2] * weightN3[2] + inputsN[3] * weightN3[3] + biaisN3

# Assignation du vecteur de sorite du reseau de neurone
output[0] = OutputN1
output[1] = OutputN2
output[2] = OutputN3

print(output)