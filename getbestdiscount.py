# -*- coding: utf-8 -*-
#Preco c/d| Preco ao lt c/d| Preco s/d| preco ao lt s/d|
#-4 -> remove \n \r ' and ]

import codecs;

def getproducts() -> list:
    with codecs.open('bebidas2.db', 'r', encoding='utf-8', errors='ignore') as f:
        prods : list = f.readlines();
    return prods;

def discount_by_percentage(l) -> list:
    dscs : list = [];
    i : int;
    for i in range(len(l)):
        prod : list = l[i][2:-4].split(',');
        desc : str  = prod[-1];
        if ('%' in desc):
            desc : int = desc.replace('Desconto imediato:', '').replace('%', '').replace(' ', '');
            dscs.append(int(desc));
        else:
            dscs.append(1);
    return dscs;

def discount_by_money(l) -> list:
    dscs : list = [];
    print(len(l));
    i : int;
    for i in range(len(l)):
        prod : list = l[i][2:-4].split(',');
        desc : str = prod[-1];
        if ('%' not in desc):
            desc : float = desc.replace('Desconto imediato:', '').replace(' ', '');
            dscs.append(float(desc));
        else:
            dscs.append(0);
    return dscs;

def discount_by_subtraction(l) -> list:
    dscs : list = [];
    i : int;
    for i in range(len(l)):
        prod : list = l[i][2:-4].split(',');
        desc : str = prod[-1];
        if ('%' in desc):
            desc : int = desc.replace('Desconto imediato:', '').replace('%', '').replace(' ', '');
            ctm : float = '0.{}'.format(desc);
            #print(i, ctm)
            ctm : float = (float(prod[-3].replace('\n', '').replace('/kg', ''))) * float(ctm);
            #print(i, ctm)
            dscs.append(float(ctm));
        else:
            desc : float = desc.replace('Desconto imediato:', '').replace(' ', '');
            dscs.append(float(desc));
    return dscs;
            
            
#8424    
    

def maxdiscount(dscs, l)-> str:
    maior_desc : int = max(dscs);
    n : int = dscs.index(maior_desc);
    prodp : list = l[n][2:-4].split(',');
    descp = prodp[-1];
    pp : str  = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format(n, prodp[0], prodp[2], descp);
    return pp;

def betterten(dscs, l) -> list:
    melhores : list = [];
    i : int;
    for i in range(10):
        maior_desc : int = max(dscs);
        n : int = dscs.index(maior_desc);
        prodp : list = l[n][2:-4].split(',');
        descp = prodp[-1];
        pp : str  = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format(n, prodp[0], prodp[-5], descp);
        melhores.append([pp]);
        del dscs[n];
    return melhores;
        
        

l : list = getproducts();

m : list = discount_by_percentage(l);
f : list = discount_by_money(l);
p : list = discount_by_subtraction(l);

k : str  = maxdiscount(m, l);
r : str = maxdiscount(f, l);
u : str = maxdiscount(p, l);
g : list = betterten(p, l);
print(r);
print(k);
print(u);
print('----');
print(g);
for i in range(len(g)):
    print('{}\n'.format(g[i]))



















'''
prod : list = l[2252][2:-4].split(',');
prod_2 : list = l[3903][2:-4].split(',');
print(prod, prod_2);
desc : str = prod[-1];
desc_2 : str = prod_2[-1];
best : str = '';
desc   : int = desc.replace('Desconto imediato:', '').replace('%', '').replace(' ', '');
desc_2 : int = desc_2.replace('Desconto imediato:', '').replace('%', '').replace(' ', '');
if (int(desc) > int(desc_2)):
    best = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format('a', prod[0], prod[3], desc);
elif (int(desc) < int(desc_2)):
    best = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format('b', prod_2[0], prod_2[3], desc_2);
else:
    pass
print(best)
'''

            #print(desc, desc_2);
            #if (int(desc) > int(desc_2)):
            #    print('0')
                #best = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format(i, prod[0], prod[3], desc);
            #elif (int(desc) < int(desc_2)):
            #    print('1')
            #    best = 'linha = {}, produto = {}, preço = {}, desconto = {}'.format(i, prod_2[0], prod_2[3], desc_2);
            #else:
            #    print('@');
            #print(best);


#u ker u melor discont ? kom mas % o € ?
