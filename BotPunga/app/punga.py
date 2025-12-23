import discord
import random
from discord.ext import commands

def diversos():
    diversos1=random.randint(1,100)
    if diversos1<=10:
        diversos2="Alaude élfico"
        return diversos2
    elif 11<=diversos1<=19:
        diversos2="Algemas"
        return diversos2
    elif 20<=diversos1<=28:
        diversos2="Caixa de voz"
        return diversos2
    elif 29<=diversos1<=37:
        diversos2="Coleção de livros"
        return diversos2
    elif 38<=diversos1<=46:
        diversos2="Corda de teia"
        return diversos2
    elif 47<=diversos1<=55:
        diversos2="Estojo de disfarces"
        return diversos2
    elif 56<=diversos1<=64:
        diversos2="Flauta mística"
        return diversos2
    elif 65<=diversos1<=73:
        diversos2="Luneta"
        return diversos2
    elif 74<=diversos1<=82:
        diversos2="Maleta de medicamentos"
        return diversos2
    elif 83<=diversos1<=91:
        diversos2="Organizador de pergaminhos"
        return diversos2
    elif 92<=diversos1<=100:
        diversos2="Sela"
        return diversos2

def consumivel():
    consumivel1=random.randint(1,100)
    if consumivel1==1:
        consumivel2="Ácido"
        return consumivel2
    elif consumivel1==2:
        consumivel2="Agua benta"
        return consumivel2
    elif 3<=consumivel1<=4:
        consumivel2="Baga-de-fogo"
        return consumivel2
    elif 5<=consumivel1<=9:
        consumivel2="Bálsamo de drogadora"
        return consumivel2
    elif 10<=consumivel1<=13:
        consumivel2="4x Bálsamo restaurador"
        return consumivel2
    elif consumivel1==14:
        consumivel2="Beladona"
        return consumivel2
    elif 15<=consumivel1<=16:
        consumivel2="2x Bomba de fumaça"
        return consumivel2
    elif 17<=consumivel1<=19:
        consumivel2="Bomba"
        return consumivel2
    elif consumivel1==20:
        consumivel2="Bruma sonolenta"
        return consumivel2
    elif 21<=consumivel1<=23:
        consumivel2="Cicuta"
        return consumivel2
    elif consumivel1==24:
        consumivel2="Corrosivo mineral"
        return consumivel2
    elif 25<=consumivel1<=26:
        consumivel2="Cosmético"
        return consumivel2
    elif 27<=consumivel1<=28:
        consumivel2="Dente-de-dragão"
        return consumivel2
    elif 29<=consumivel1<=30:
        consumivel2="Elixir do amor"
        return consumivel2
    elif 31<=consumivel1<=32:
        consumivel2="Elixir quimérico"
        return consumivel2
    elif 33<=consumivel1<=34:
        consumivel2="Esporos de cogumelo"
        return consumivel2
    elif consumivel1==35:
        consumivel2="Essência abissal"
        return consumivel2
    elif 36<=consumivel1<=39:
        consumivel2="2x Essência de mana"
        return consumivel2
    elif 40<=consumivel1<=41:
        consumivel2="Essência de sombra"
        return consumivel2
    elif 42<=consumivel1<=44:
        consumivel2="Éter elemental"
        return consumivel2
    elif 45<=consumivel1<=47:
        consumivel2="2x Fogo alquímico"
        return consumivel2
    elif consumivel1==48:
        consumivel2="Gelo extremo"
        return consumivel2
    elif consumivel1==49:
        consumivel2="Gema de Força"
        return consumivel2
    elif 50<=consumivel1<=52:
        consumivel2="Isca putrefata"
        return consumivel2
    elif 53<=consumivel1<=54:
        consumivel2="Lágrima pétrea"
        return consumivel2
    elif 55<=consumivel1<=56:
        consumivel2="Líquen lilás"
        return consumivel2
    elif 57<=consumivel1<=58:
        consumivel2="Musgo púrpura"
        return consumivel2
    elif 59<=consumivel1<=60:
        consumivel2="Névoa tóxica"
        return consumivel2
    elif 61<=consumivel1<=62:
        consumivel2="Óleo de baleia"
        return consumivel2
    elif 63<=consumivel1<=64:
        consumivel2="Óleo de besouro"
        return consumivel2
    elif 65<=consumivel1<=66:
        consumivel2="Ossos de monstro"
        return consumivel2
    elif consumivel1==67:
        consumivel2="Peçonha anciã"
        return consumivel2
    elif consumivel1==68:
        consumivel2="Peçonha comum"
        return consumivel2
    elif 69<=consumivel1<=70:
        consumivel2="Peçonha concentrada"
        return consumivel2
    elif consumivel1==71:
        consumivel2="Peçonha irritante"
        return consumivel2
    elif consumivel1==72:
        consumivel2="Peçonha potente"
        return consumivel2
    elif 73<=consumivel1<=74:
        consumivel2="Pedaço de língua"
        return consumivel2
    elif 75<=consumivel1<=78:
        consumivel2="Pó azul"
        return consumivel2
    elif 79<=consumivel1<=81:
        consumivel2="2x Pó de cristal"
        return consumivel2
    elif 82<=consumivel1<=84:
        consumivel2="2x Pó de giz"
        return consumivel2
    elif consumivel1==85:
        consumivel2="Pó de lich"
        return consumivel2
    elif 86<=consumivel1<=87:
        consumivel2="Pó de desaparecimento"
        return consumivel2
    elif consumivel1==88:
        consumivel2="Raio cristalizado"
        return consumivel2
    elif 89<=consumivel1<=90:
        consumivel2="Ramo verdejante"
        return consumivel2
    elif consumivel1==91:
        consumivel2="Riso de Nimb"
        return consumivel2
    elif 92<=consumivel1<=93:
        consumivel2="Saco de sal"
        return consumivel2
    elif 94<=consumivel1<=96:
        consumivel2="2x Seixo de âmbar"
        return consumivel2
    elif 97<=consumivel1<=98:
        consumivel2="Terra de cemitério"
        return consumivel2
    else:
        consumivel2="Veneno batráquio"
        return consumivel2

def possao():
    possao1=random.randint(1,100)
    if possao1==1:
        possao2="Abençoar Alimentos (óleo)"
        return possao2
    elif 2<=possao1<=3:
        possao2="Área Escorregadia (granada)"
        return possao2
    elif 4<=possao1<=6:
        possao2="Arma Mágica (óleo)"
        return possao2
    elif possao1==7:
        possao2="Compreensão"
        return possao2
    elif 8<=possao1<=15:
        possao2="Curar Ferimentos (2d8+2 PV)"
        return possao2
    elif 16<=possao1<=18:
        possao2="Disfarce Ilusório"
        return possao2
    elif 19<=possao1<=20:
        possao2="Escuridão (óleo)"
        return possao2
    elif 21<=possao1<=22:
        possao2="Luz (óleo)"
        return possao2
    elif 23<=possao1<=24:
        possao2="Névoa (granada)"
        return possao2
    elif 25<=possao1<=26:
        possao2="Primor Atlético"
        return possao2
    elif 27<=possao1<=28:
        possao2="Proteção Divina"
        return possao2
    elif 29<=possao1<=30:
        possao2="Resistência a Energia"
        return possao2
    elif 31<=possao1<=32:
        possao2="Sono"
        return possao2
    elif possao1==33:
        possao2="Suporte Ambiental"
        return possao2
    elif possao1==34:
        possao2="Tranca Arcana (óleo)"
        return possao2
    elif possao1==35:
        possao2="Visão Mística"
        return possao2
    elif possao1==36:
        possao2="Vitalidade Fantasma"
        return possao2
    elif 37<=possao1<=38:
        possao2="Escudo da Fé (aprimoramento para duração cena)"
        return possao2
    elif 39<=possao1<=40:
        possao2="Alterar Tamanho"
        return possao2
    elif 41<=possao1<=42:
        possao2="Aparência Perfeita"
        return possao2
    elif possao1==43:
        possao2="Armamento da Natureza (óleo)"
        return possao2
    elif 44<=possao1<=49:
        possao2="Bola de Fogo (granada)"
        return possao2
    elif 50<=possao1<=51:
        possao2="Camuflagem Ilusória"
        return possao2
    elif 52<=possao1<=53:
        possao2="Concentração de Combate (aprimoramento para duração cena)"
        return possao2
    elif 54<=possao1<=62:
        possao2="Curar Ferimentos (4d8+4 PV)"
        return possao2
    elif 63<=possao1<=66:
        possao2="Físico Divino"
        return possao2
    elif 67<=possao1<=68:
        possao2="Mente Divina"
        return possao2
    elif 69<=possao1<=70:
        possao2="Metamorfose"
        return possao2
    elif 71<=possao1<=75:
        possao2="Purificação"
        return possao2
    elif 76<=possao1<=77:
        possao2="Velocidade"
        return possao2
    elif 78<=possao1<=79:
        possao2="Vestimenta da Fé (óleo)"
        return possao2
    elif possao1==80:
        possao2="Voz Divina"
        return possao2
    elif 81<=possao1<=82:
        possao2="Arma Mágica (óleo; aprimoramento para bônus +3)"
        return possao2
    elif 83<=possao1<=88:
        possao2="Curar Ferimentos (7d8+7 PV)"
        return possao2
    elif possao1==89:
        possao2="Físico Divino (aprimoramento para três atributos)"
        return possao2
    elif 90<=possao1<=92:
        possao2="Invisibilidade (aprimoramento para duração cena)"
        return possao2
    elif 93<=possao1<=96:
        possao2="Bola de Fogo (granada; aprimoramento para 10d6 de dano)"
        return possao2
    else:
        possao2="Curar Ferimentos (11d8+11 PV)"
        return possao2

def equipamentos(a):
    if a==1:
        arma1=random.randint(1,100)
        if arma1<=2:
            arma2=["Açoite finntroll","Corpo a corpo"]
            return arma2
        elif arma1==3:
            arma2=["Adagas","Corpo a corpo"]
            return arma2
        elif arma1==4:
            arma2=["Alabarda","Corpo a corpo"]
            return arma2
        elif 5<=arma1<=7:
            arma2=["Alfange","Corpo a corpo"]
            return arma2
        elif arma1==8:
            arma2=["Arcabuz","Disparo"]
            return arma2
        elif 9<=arma1<=11:
            arma2=["Arco curto","Disparo"]
            return arma2
        elif 12<=arma1<=14:
            arma2=["Arco longo","Disparo"]
            return arma2
        elif 15<=arma1<=16:
            arma2=["Arpão","Corpo a corpo"]
            return arma2
        elif arma1==17:
            arma2=["Bacamarte","Corpo a corpo"]
            return arma2
        elif 18<=arma1<=20:
            arma2=["Besta leve","Disparo"]
            return arma2
        elif 21<=arma1<=22:
            arma2=["Besta pesada","Disparo"]
            return arma2
        elif 23<=arma1<=24:
            arma2=["Manopla","Corpo a corpo"]
            return arma2
        elif 25<=arma1<=26:
            arma2=["Garra Feroz","Corpo a corpo"]
            return arma2
        elif 27<=arma1<=28:
            arma2=["Cimitarra","Corpo a corpo"]
            return arma2
        elif 29<=arma1<=30:
            arma2=["Corrente de espinhos","Corpo a corpo"]
            return arma2
        elif 31<=arma1<=32:
            arma2=["Espada bastarda","Corpo a corpo"]
            return arma2
        elif 33<=arma1==35:
            arma2=["Espada curta","Corpo a corpo"]
            return arma2
        elif 36<=arma1<=38:
            arma2=["Espada longa","Corpo a corpo"]
            return arma2
        elif 39<=arma1<=41:
            arma2=["Espada Vespa","Corpo a corpo"]
            return arma2
        elif 42<=arma1<=44:
            arma2=["Florete","Corpo a corpo"]
            return arma2
        elif arma1==45:
            arma2=["Foice","Corpo a corpo"]
            return arma2
        elif 46<=arma1<=47:
            arma2=["Gadanho","Corpo a corpo"]
            return arma2
        elif 48<=arma1<=50:
            arma2=["Gladio","Corpo a corpo"]
            return arma2
        elif 51<=arma1<=53:
            arma2=["Katana","Corpo a corpo"]
            return arma2
        elif arma1==54:
            arma2=["Lança","Corpo a corpo"]
            return arma2
        elif arma1==55:
            arma2=["Lança de fogo","Disparo"]
            return arma2
        elif arma1==56:
            arma2=["Lança montada","Corpo a corpo"]
            return arma2
        elif 57<=arma1<=58:
            arma2=["Maça","Corpo a corpo"]
            return arma2
        elif arma1==59:
            arma2=["Machadinha","Corpo a corpo"]
            return arma2
        elif 60<=arma1<=61:
            arma2=["Machado anão","Corpo a corpo"]
            return arma2
        elif 62<=arma1<=64:
            arma2=["Machado de batalha","Corpo a corpo"]
            return arma2
        elif 65<=arma1<=67:
            arma2=["Machado de guerra","Corpo a corpo"]
            return arma2
        elif 68<=arma1<=70:
            arma2=["Machado táurico","Corpo a corpo"]
            return arma2
        elif arma1==71:
            arma2=["Mangual","Corpo a corpo"]
            return arma2
        elif 72<=arma1<=73:
            arma2=["Marreta","Corpo a corpo"]
            return arma2
        elif 74<=arma1<=75:
            arma2=["Martelo de guerra","Corpo a corpo"]
            return arma2
        elif 76<=arma1<=78:
            arma2=["Montante","Corpo a corpo"]
            return arma2
        elif 79<=arma1<=80:
            arma2=["Mordida do diabo","Corpo a corpo"]
            return arma2
        elif 81<=arma1<=82:
            arma2=["Mosquete","Corpo a corpo"]
            return arma2
        elif arma1==83:
            arma2=["Neko-te","Corpo a corpo"]
            return arma2
        elif arma1==84:
            arma2=["Picareta","Corpo a corpo"]
            return arma2
        elif 85<=arma1<=87:
            arma2=["Pistola","Disparo"]
            return arma2
        elif 88<=arma1<=89:
            arma2=["Pistola-Punhal","Disparo"]
            return arma2
        elif arma1==90:
            arma2=["Presa da serpente","Corpo a corpo"]
            return arma2
        elif 91<=arma1<=92:
            arma2=["2x Shuriken","Disparo"]
            return arma2
        elif 93<=arma1<=94:
            arma2=["Tetsubo","Corpo a corpo"]
            return arma2
        elif 95<=arma1<=97:
            arma2=["Traque","Disparo"]
            return arma2
        elif 98<=arma1<=99:
            arma2=["Tridente","Corpo a corpo"]
            return arma2
        else:
            arma2=["Zarabatana","Disparo"]
            return arma2
    elif a==2:
        esotéricos1=random.randint(1,100)
        if esotéricos1<=9:
            esotéricos2=["Ankh solar"]
            return esotéricos2
        elif 10<=esotéricos1<=18:
            esotéricos2=["Bolsa de pó"]
            return esotéricos2
        elif 19<=esotéricos1<=24:
            esotéricos2=["Cajado arcano"]
            return esotéricos2
        elif 25<=esotéricos1<=32:
            esotéricos2=["Cetro elemental"]
            return esotéricos2
        elif 33<=esotéricos1<=41:
            esotéricos2=["Costela de lich"]
            return esotéricos2
        elif 42<=esotéricos1<=48:
            esotéricos2=["Dedo de ente"]
            return esotéricos2
        elif 49<=esotéricos1<=55:
            esotéricos2=["Luva de ferro"]
            return esotéricos2
        elif 56<=esotéricos1<=63:
            esotéricos2=["Medalhão de prata"]
            return esotéricos2
        elif 64<=esotéricos1<=71:
            esotéricos2=["Orbe cristalino"]
            return esotéricos2
        elif 72<=esotéricos1<=80:
            esotéricos2=["Tomo de guerra"]
            return esotéricos2
        elif 81<=esotéricos1<=88:
            esotéricos2=["Tomo do rancor"]
            return esotéricos2
        elif 89<=esotéricos1<=94:
            esotéricos2=["Tomo hermético"]
            return esotéricos2
        else:
            esotéricos2=["Varinha arcana"]
            return esotéricos2

def melhoria(a,b):
    melhora=[]
    item=equipamentos(a)
    resultado=item[0]+" com "
    while b>0:
        if a==1:
            melhora1=random.randint(1,100)
            if melhora1<=5:
                melhora2="Atroz"
                melhora3="Cruel"
                if melhora2 not in melhora and melhora3 not in melhora and b>=2:
                    melhora+=[melhora3]
                    melhora+=[melhora2]
                    b=b-2
                elif melhora2 not in melhora and melhora3 in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 6<=melhora1<=10:
                melhora2="Banhada a ouro"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 11<=melhora1<=19:
                melhora2="Certeira"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 20<=melhora1<=24:
                melhora2="Cravejada de gemas"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 25<=melhora1<=33:
                melhora2="Cruel"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 34<=melhora1<=38:
                melhora2="Discreta"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 39<=melhora1<=47:
                melhora2="Equilibrada"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 48<=melhora1<=56:
                melhora2="Injeção alquímica"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 57<=melhora1<=61:
                melhora2="Macabra"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 62<=melhora1<=71:
                melhora2="Maciça"
                if melhora2 not in melhora and "Precisa" not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 72<=melhora1<=75 and b>=2:
                c=random.randint(0,8)
                melhora2=["Aço-Rubi", "Adamante", "Casco de Monstro", "Gelo Eterno", "Lanajuste", "Madeira de Tollon", "Máteria Vermelha", "Mitral", "Prata"]
                me=True
                for i in range(len(melhora2)):
                    if melhora2[i] in melhora:
                        me=False
                    i+=1
                if me:
                    melhora+=[melhora2[c]]
                    b=b-2
            elif 76<=melhora1<=80:
                melhora2="Mira telescópica"
                if melhora2 not in melhora and item[1]=="Disparo":
                    melhora+=[melhora2]
                    b=b-1
            elif 81<=melhora1<=85:
                melhora2="Penetrante"
                melhora3="Cruel"
                if melhora2 not in melhora and melhora3 not in melhora and b>=2:
                    melhora+=[melhora3]
                    melhora+=[melhora2]
                    b=b-2
                elif melhora2 not in melhora and melhora3 in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 86<=melhora1<=95:
                melhora2="Precisa"
                if melhora2 not in melhora and "Maciça" not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            else:
                melhora2="Pungente"
                melhora3="Certeira"
                if melhora2 not in melhora and melhora3 not in melhora and b>=2:
                    melhora+=[melhora3]
                    melhora+=[melhora2]
                    b=b-2
                elif melhora2 not in melhora and melhora3 in melhora:
                    melhora+=[melhora2]
                    b=b-1
        elif a==2:
            melhora1=random.randint(1,100)
            if melhora1<=4:
                melhora2="Banhado a ouro"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 5<=melhora1<=24:
                melhora2="Canalizador"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 25<=melhora1<=28:
                melhora2="Cravejada de gemas"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 29<=melhora1<=32:
                melhora2="Discreto"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 33<=melhora1<=52:
                melhora2="Energético"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 53<=melhora1<=56:
                melhora2="Macabro"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            elif 57<=melhora1<=60 and b>=2:
                c=random.randint(0,8)
                melhora2=["Aço-Rubi", "Adamante", "Casco de Monstro", "Gelo Eterno", "Lanajuste", "Madeira de Tollon", "Máteria Vermelha", "Mitral", "Prata"]
                me=True
                for i in range(len(melhora2)):
                    if melhora2[i] in melhora:
                        me=False
                    i+=1
                if me:
                    melhora+=[melhora2[c]]
                    b=b-2
            elif 61<=melhora1<=80:
                melhora2="Poderoso"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
            else:
                melhora2="Vigilante"
                if melhora2 not in melhora:
                    melhora+=[melhora2]
                    b=b-1
    for i in range(len(melhora)):
        resultado+=melhora[i]
        if i+2<len(melhora):
            resultado+=", "
        elif i+1<len(melhora):
            resultado+=" e "
        i+=1
    return resultado

def magico(a,b):
    magia=[]
    resultado=""
    while b>0:
        if a==1:
            item=equipamentos(a)
            resultado=item[0]+" com "
            magia1=random.randint(1,100)
            if magia1<=5:
                magia2="Ameaçadora"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 6<=magia1<=10:
                magia2="Anticriatura"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 11<=magia1<=12:
                magia2="Arremesso"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 13<=magia1<=14:
                magia2="Assassina"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 15<=magia1<=16:
                magia2="Caçadora"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 17<=magia1<=21:
                magia2="Congelante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 22<=magia1<=23:
                magia2="Conjuradora"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 24<=magia1<=28:
                magia2="Corrosiva"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 29<=magia1<=30:
                magia2="Dançarina"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 31<=magia1<=34:
                magia2="Defensora"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 35<=magia1<=36:
                magia2="Destruidora"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 37<=magia1<=38:
                magia2="Dilacerante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 39<=magia1<=40:
                magia2="Drenante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 41<=magia1<=46:
                magia2="Elétrica"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 47<=magia1<=51:
                magia2="Energética"
                magia3="Formidável"
                if magia2 not in magia and magia3 not in magia and b>=2:
                    magia+=[magia3]
                    magia+=[magia2]
                    b=b-2
                elif magia2 not in magia and magia3 in magia:
                    magia+=[magia2]
                    b=b-1
            elif 52<=magia1<=53:
                magia2="Excruciante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 54<=magia1<=58:
                magia2="Flamejante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 59<=magia1<=68:
                magia2="Formidável"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 69<=magia1<=74:
                magia2="Lancinante"
                magia3="Dilacerante"
                if magia2 not in magia and magia3 not in magia and b>=2:
                    magia+=[magia3]
                    magia+=[magia2]
                    b=b-2
                elif magia2 not in magia and magia3 in magia:
                    magia+=[magia2]
                    b=b-1
            elif 75<=magia1<=82:
                magia2="Magnífica"
                magia3="Formidável"
                if magia2 not in magia and magia3 not in magia and b>=2:
                    magia+=[magia3]
                    magia+=[magia2]
                    b=b-2
                elif magia2 not in magia and magia3 in magia:
                    magia+=[magia2]
                    b=b-1
            elif 83<=magia1<=84:
                magia2="Piedosa"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 85<=magia1<=86:
                magia2="Profana"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 87<=magia1<=88:
                magia2="Sagrada"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 89<=magia1<=90:
                magia2="Sanguinária"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 91<=magia1<=92:
                magia2="Trovejante"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 93<=magia1<=94:
                magia2="Tumular"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            elif 95<=magia1<=98:
                magia2="Veloz"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
            else:
                magia2="Venenosa"
                if magia2 not in magia:
                    magia+=[magia2]
                    b=b-1
        elif a==2 and b==1:
            magia1=random.randint(1,100)
            if magia1<=2:
                resultado="Anel do sustento"
                b=0
                return resultado
            elif 3<=magia1<=7:
                resultado="Bainha mágica"
                b=0
                return resultado
            elif 8<=magia1<=12:
                resultado="Corda da escalada"
                b=0
                return resultado
            elif 13<=magia1<=14:
                resultado="Ferraduras da velocidade"
                b=0
                return resultado
            elif 15<=magia1<=19:
                resultado="Garrafa da fumaça eterna"
                b=0
                return resultado
            elif 20<=magia1<=24:
                resultado="Gema da luminosidade"
                b=0
                return resultado
            elif 25<=magia1<=29:
                resultado="Manto élfico"
                b=0
                return resultado
            elif 30<=magia1<=34:
                resultado="Mochila de carga"
                b=0
                return resultado
            elif 35<=magia1<=40:
                resultado="Brincos da sagacidade"
                b=0
                return resultado
            elif 41<=magia1<=46:
                resultado="Luvas da delicadeza"
                b=0
                return resultado
            elif 47<=magia1<=52:
                resultado="Manoplas da força do ogro"
                b=0
                return resultado
            elif 53<=magia1<=59:
                resultado="Manto da resistência"
                b=0
                return resultado
            elif 60<=magia1<=65:
                resultado="Manto do fascínio"
                b=0
                return resultado
            elif 66<=magia1<=71:
                resultado="Pingente da sensatez"
                b=0
                return resultado
            elif 72<=magia1<=77:
                resultado="Torque do vigor"
                b=0
                return resultado
            elif 78<=magia1<=82:
                resultado="Chapéu do disfarce"
                b=0
                return resultado
            elif 83<=magia1<=84:
                resultado="Flauta fantasma"
                b=0
                return resultado
            elif 85<=magia1<=89:
                resultado="Lanterna da revelação"
                b=0
                return resultado
            elif 90<=magia1<=96:
                resultado="Anel da proteção"
                b=0
                return resultado
            elif 97<=magia1<=98:
                resultado="Anel do escudo mental"
                b=0
                return resultado
            else:
                resultado="Pingente da saúde"
                b=0
                return resultado
        elif a==2 and b==2:
            magia1=random.randint(1,100)
            if magia1<=4:
                resultado="Anel de telecinesia"
                b=0
                return resultado
            elif 5<=magia1<=8:
                resultado="Bola de cristal"
                b=0
                return resultado
            elif 9<=magia1<=10:
                resultado="Caveira maldita"
                b=0
                return resultado
            elif 11<=magia1<=14:
                resultado="Botas aladas"
                b=0
                return resultado
            elif 15<=magia1<=18:
                resultado="Braceletes de bronze"
                b=0
                return resultado
            elif 19<=magia1<=24:
                resultado="Anel da energia"
                b=0
                return resultado
            elif 25<=magia1<=30:
                resultado="Anel da vitalidade"
                b=0
                return resultado
            elif 31<=magia1<=34:
                resultado="Anel de invisibilidade"
                b=0
                return resultado
            elif 35<=magia1<=38:
                resultado="Braçadeiras do arqueiro"
                b=0
                return resultado
            elif 39<=magia1<=42:
                resultado="Brincos de Marah"
                b=0
                return resultado
            elif 43<=magia1<=46:
                resultado="Faixas do pugilista"
                b=0
                return resultado
            elif 47<=magia1<=50:
                resultado="Manto da aranha"
                b=0
                return resultado
            elif 51<=magia1<=54:
                resultado="Vassoura voadora"
                b=0
                return resultado
            elif 55<=magia1<=58:
                resultado="Símbolo abençoado"
                b=0
                return resultado
            elif 59<=magia1<=64:
                resultado="Amuleto da robustez"
                b=0
                return resultado
            elif 65<=magia1<=68:
                resultado="Botas velozes"
                b=0
                return resultado
            elif 69<=magia1<=74:
                resultado="Cinto da força do gigante"
                b=0
                return resultado
            elif 75<=magia1<=80:
                resultado="Coroa majestosa"
                b=0
                return resultado
            elif 81<=magia1<=86:
                resultado="Estola da serenidade"
                b=0
                return resultado
            elif 87<=magia1<=88:
                resultado="Manto do morcego"
                b=0
                return resultado
            elif 89<=magia1<=94:
                resultado="Pulseiras da celeridade"
                b=0
                return resultado
            else:
                resultado="Tiara da sapiência"
                b=0
                return resultado
    for i in range(len(magia)):
        resultado+=magia[i]
        if i+2<len(magia):
            resultado+=", "
        elif i+1<len(magia):
            resultado+=" e "
        i+=1
    return resultado

class PungaCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()

    @discord.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='diversos')
    async def diversos(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{diversos()}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='consumiveis')
    async def consumivel(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{consumivel()}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='pocoes')
    async def pocao(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{possao()}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='armas')
    async def armas(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{equipamentos(1)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='esotericos')
    async def esotericos(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{equipamentos(2)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='arma_superior')
    async def arma_superior(self, interaction, melhorias: discord.Option(int, choices=range(1, 5))):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{melhoria(1,melhorias)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='esoterico_superior')
    async def esoterico_superior(self, interaction, melhorias: discord.Option(int, choices=range(1, 5))):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{melhoria(2,melhorias)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='arma_encantada')
    async def arma_encantada(self, interaction, encantos: discord.Option(int, choices=range(1, 3))):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{magico(1,encantos)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='acessorio_menor')
    async def acessorio_menor(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{magico(2,1)}**.")

    @commands.slash_command(description='Use apenas após usar o comando "Punga" na mesma mas para ter outro resultado da mesma categoria.', name='acessorio_medio')
    async def acessorio_medio(self, interaction):
        await interaction.response.send_message(f"Parabéns você conseguiu pegar **{magico(2,2)}**.")

    @commands.slash_command(description='Só rode depois de passar no teste.')
    async def punga(self, interaction, punga: discord.Option(str, choices=["Dinheiro", "Item"]), nd: discord.Option(int, choices=range(1, 21))):
        if punga == "Dinheiro":
            numero=random.randint(1,20)
            dado=random.randint(1,10)
            if numero<3:
                din=dado*2*nd
            elif numero>=3 and numero<8:
                din=dado*3*nd
            elif numero>=8 and numero<14:
                din=dado*5*nd
            elif numero>=14 and numero<19:
                din=dado*8*nd
            else:
                din=dado*10*nd
            await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **T${din}**")
        elif punga == "Item":
            tabela1=random.randint(1,100)
            if nd<5:
                if tabela1<36:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{diversos()}**.")
                elif tabela1>=36 and tabela1<71:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{consumivel()}**.")
                elif tabela1>=71:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{equipamentos(a)[0]}**.")
            elif 5<=nd<11:
                if tabela1<21:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{diversos()}**.")
                elif tabela1>=21 and tabela1<41:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{consumivel()}**.")
                elif tabela1>=41 and tabela1<70:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{equipamentos(a)[0]}**.")
                elif tabela1>=70 and tabela1<85:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar uma Poção **{possao()}**.")
                elif tabela1>=85 and tabela1<100:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,1)}**.")
                else:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,2)}**.")
            elif 11<=nd<17:
                if tabela1<11:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{diversos()}**.")
                elif tabela1>=11 and tabela1<26:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{consumivel()}**.")
                elif tabela1>=26 and tabela1<61:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{equipamentos(a)[0]}**.")
                elif tabela1>=61 and tabela1<81:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar uma Poção **{possao()}**.")
                elif tabela1>=81 and tabela1<96:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,2)}**.")
                elif tabela1>=96 and tabela1<100:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,3)}**.")
                else:
                    a=random.randint(1,3)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{magico(a,1)}**")
            else:
                if tabela1<21:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{consumivel()}**.")
                elif tabela1>=21 and tabela1<46:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{equipamentos(a)[0]}**.")
                elif tabela1>=46 and tabela1<71:
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar uma Poção **{possao()}**.")
                elif tabela1>=71 and tabela1<91:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,3)}**.")
                elif tabela1>=91 and tabela1<96:
                    a=random.randint(1,2)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{melhoria(a,4)}**.")
                elif tabela1>=96 and tabela1<100:
                    a=random.randint(1,3)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{magico(a,1)}**")
                else:
                    a=random.randint(1,3)
                    await interaction.response.send_message(f"Parabéns seu ND é {nd} e você conseguiu pegar **{magico(a,2)}**")

def setup(bot: commands.Bot):
    bot.add_cog(PungaCommand(bot))
