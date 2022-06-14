import random
from re import A


turn = 5
target_num = 10
loss_num = 2
alp_list = [chr(ord("A")+i) for i in range(26)]

def main():
    for i in range(turn):
        target,loss,display = BuildQ()
        if Kaitou(target,loss,display) == True:
            break

def BuildQ():
    target_char = list()
    loss_char = list()
    for i in range(target_num):
        target_r = random.randint(0,len(alp_list))
        target_char.append(alp_list[target_r])
    display_char = list(target_char)
    for j in range(loss_num):
        loss_r = random.randint(0,len(display_char))
        loss_char.append(display_char.pop(loss_r))
    
    return target_char,loss_char,display_char

def Kaitou(target,loss,display):
    print("対象文字：" + "".join(target))
    print("欠損文字：" + "".join(loss))
    print("表示文字：" + "".join(display))
    for i in range(loss_num):
        ans = input(f"{i+1}つ目の欠損文字を答えるんだ:")
        if ans in loss:
            loss.remove(ans)
            print("正解だ")
        else:
            print("出直してこい")
            break
    if len(loss) == 0:
        print("完全正解だ")
        return True
    else:
        return False
        
if __name__ == "__main__":
    main()





    




