import random

def main():
    seikai = shutudai()
    kaitou(seikai)

def shutudai():
    #Q1 = "サザエの旦那の名前は？"
    #Q2 = "カツオの妹の名前は？"
    #Q3 = "タラオはカツオから見てどんな関係？"
    #A1 = ["マスオ","ますお"]
    #A2 = ["ワカメ","わかめ"]
    #A3 = ["甥","おい","甥っ子","おいっこ"]
    QAs = [["サザエの旦那の名前は？",["マスオ","ますお"]],["カツオの妹の名前は？",["ワカメ","わかめ"]],["タラオはカツオから見てどんな関係？",["甥","おい","甥っ子","おいっこ"]]]
    r = random.randint(0,2)
    print(QAs[r][0])
    return QAs[r][1]

def kaitou(seikai):
    ans = input("答えるんだ:")
    if ans in seikai:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()

    





    
