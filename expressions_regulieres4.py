import re 
exemple = '''
P1 is a product composed of P2 and P3
P2 is an elementary product
P5 is a product composed of P1 and P4
P4 is an elementary product
P9 is a product composed of P1 and P6 and P4
P10 is a product composed of P3 and P5
P11 is a product composed of P5 and P3
'''
pattern_produits_elementaires = r'P\d+ is an elementary product'
produits_elementaires = re.findall(pattern_produits_elementaires,exemple)

print("-The elementary product :")
print(produits_elementaires)


pattern_produits_compose = r'P\d+ is a product composed of P\d+ and P\d+ and P\d+'
produit_compose = re.findall(pattern_produits_compose,exemple)

print("-Products composed of three products: ")
#for produit in produit_compose:
print(produit_compose)

pattern_produits_P3_P5 = r'P\d+ is a product composed of P3 and P5|P\d+ is a product composed of P5 and P3' 
produit2 = re.findall(pattern_produits_P3_P5,exemple)

print("-The products composed of P3 and P5 are: ")
print(produit2)

pattern_produits_P9 = r'P\d+ is a product composed of (P\d+) and (P\d+) and (P\d+)'
produitP9 = re.findall(pattern_produits_P9,exemple)

print("-P9 is composed of 3 products are:")
print(produitP9)

