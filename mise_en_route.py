i=1
somme=0
while i<=10:
    somme += i**2
    somme_form= i**2 + i*(i-1)*(2*i-1)/6
    print(i,"\t",i**2,"\t",somme,"\t",somme_form)
    i+=1
