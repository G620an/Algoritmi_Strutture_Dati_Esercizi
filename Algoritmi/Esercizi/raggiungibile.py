def raggiungibile(g, x1, x2, x3):
    rag1 = visitaInAmpiezza(g, x1)
    if x3 not in rag1:
        return False
    elif x2 not in rag1:
        return False


#Complessità lista di adiacenza
#CTM(m,n) = Il primo nodo è isolato e quindi devo visitare in ampiezza solamente tetha di n
#CTP(m,n)= Il primo nodo è collegato sia a x2 che x3 quindi costo della visita tetha di n+m
#CSP=CSM = Sermpre vettore dei visitati quindi tetha di n
