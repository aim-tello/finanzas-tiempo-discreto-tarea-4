from bigtree import Node, tree_to_dot
import numpy as np
import matplotlib.pyplot as plt

class CRR:

    def __init__(self, a, b ,p ,T):
        self.a = a
        self.b = b
        self.p = p
        self.T = T

    def calcula_estrat_crr(self):
        x = 1
        return self.v_t(x , 0)

    def h(self, x):
        valor =  10*x # Función de Payoff
        nodo = Node(str(valor))
        return nodo, valor

    def v_t(self, x, t):
        #print('Ejecutando nivel: '+ str(t))
        if t < self.T:
            hijo_1, valor_p_1 = self.v_t(x * self.b, t+1)
            hijo_2, valor_p_2 =  self.v_t(x * self.a, t + 1)
            valor_a =   self.p * valor_p_1+ (1 - self.p) *valor_p_2
            hijos = [hijo_1,hijo_2]
        else :
            hijo, valor_a = self.h(x)
            hijos = [hijo]
        nodo = Node(str(valor_a))
        nodo.children = hijos
        #print('valor en la iteracion: ' + str(valor_a))
        return nodo, valor_a

    def construye_trayectorias(self,n,t):
        return np.random.randint(2, size=(n, t))

    def ejecuta_crr(self):
        n = 5 #Numero de trayectorias
        t = 10 #Numero de intervalos
        trayectorias = self.construye_trayectorias(n,t)
        S_0 = 10 #Precio base del activo
        matriz_inicial = np.zeros((n,t+1))
        matriz_inicial[:,0]= np.full((1,n),S_0)
        print(matriz_inicial)
        print(trayectorias)
        for col in range(trayectorias.shape[1]):
            matriz_inicial[:,col+1] = np.multiply(matriz_inicial[:,col],(self.b)*trayectorias[:,col]) + np.multiply(matriz_inicial[:,col],(self.a)*(1-trayectorias[:,col]))
        for i in range(matriz_inicial.shape[0]):
            plt.plot(matriz_inicial[i], label=f'Trayectoria {i + 1}')

        plt.xlabel('t')
        plt.ylabel('Value')
        plt.title('Distintas trayectorias ')
        plt.legend()
        plt.show()

if __name__  == '__main__':
    a = 0.5 #Valor de bajada
    b = 1.75 #Valor de subida
    p = .4 #Probabilidad de a
    T = 5 #Iteraciones
    c1 = CRR(a,b,p,T)
    arbol, valor = c1.calcula_estrat_crr()
    #graph = tree_to_dot(arbol, node_colour="gold") #<--- activar este para generar la imagen que se ve en tree.png, con más de 5 ciclos, se atora
    #graph.write_png("tree.png")
    print('Calculando CRR: '+ str(valor))

    c1.ejecuta_crr()