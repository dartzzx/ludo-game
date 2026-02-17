#Tento skript vytvori sachovnicu pre hru Clovece nehnevaj sa 

n = int(input('Zadaj rozmer sachovnice (n - neparne cislo): '))
sachovnica=[]
n_mid = n//2 

# p_sachovnica(n) - Vytvori prazdnu sachovnicu pomocou zoznamov v zozname
# n - rozmer sachovnice 
def p_sachovnica(n):
    for a in range(n):
        riadok = []
        for b in range(n):
            riadok.append(' ')
        sachovnica.append(riadok)
        
#gen_sachovnica() - Do prazdnej sachovnice prida vsetky potrebne prvky a nakoniec vrati uplnu sachovnicu
def gen_sachovnica():
    p_sachovnica(n)
    sachovnica[n_mid].insert((n_mid),'X') #vlozi X do stredu sachovnice
    for riadok in sachovnica:
        for i in range(n): 
            if i !=0 and i!=n_mid and i!=n-1: #vlozi D (domceky)
                sachovnica[i][n_mid] = 'D'
                sachovnica[n_mid][i] = 'D'
                
            if sachovnica[n_mid][i] != 'D' and sachovnica[n_mid][i] != 'X':
                sachovnica[n_mid-1][i] = '*'
                sachovnica[n_mid][i] = '*'
                sachovnica[n_mid+1][i] = '*'
                
            if sachovnica[i][n_mid] != 'D' and sachovnica[i][n_mid] != 'X':
                sachovnica[i][n_mid-1] = '*'
                sachovnica[i][n_mid] = '*'
                sachovnica[i][n_mid+1] = '*'
            #predosle dva if podmienky pridaju * (hracie polia) okolo rohov D-ciek 
                
            if sachovnica[i][n_mid] == 'D':
                sachovnica[i][n_mid-1] = '*'
                sachovnica[i][n_mid+1] = '*'
                
            if sachovnica[n_mid][i] == 'D':
                sachovnica[n_mid-1][i] = '*'
                sachovnica[n_mid+1][i] = '*'
            
            #predosle dva if podmienky skontroluju ci su D-cka v strednych suradniciach, a ak ano, tak pridaju okolo nich * (hracie polia)
                
    return gen_sachovnica

#tlac_sachovnicu(gen_sachovnica) - na zaciatku si privola uplnu sachovnicu a potom ju upravi na krajsi/viac prakticky vzhlad a zaroven vyprintuje
def tlac_sachovnicu(gen_sachovnica):
    gen_sachovnica()
    for c in range(n):
        for d in range(n):
            print(sachovnica[c][d] + ' ' ,end='')
        print()

tlac_sachovnicu(gen_sachovnica)
  
#tento input som tu dal z dovodu, aby sa program hned nezavrel po spusteni  
input('Stlac ENTER na ukoncenie programu')

    







    
    
    
    
