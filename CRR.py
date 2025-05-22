from bigtree import Node, tree_to_dot

class CRR:

    def __init__(self, a, b ,p ,T):
        self.a = a
        self.b = b
        self.p = p
        self.T = T

    def calcula_crr(self):
        x = 1
        return self.v_t(x , 0)

    def h(self, x):
        valor =  10*x
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

if __name__  == '__main__':
    a = 0.5
    b = 0.75
    p = .4
    T = 5
    c1 = CRR(a,b,p,T)
    arbol, valor = c1.calcula_crr()
    graph = tree_to_dot(arbol, node_colour="gold")
    graph.write_png("tree.png")
    print('Calculando CRR: '+ str(valor))