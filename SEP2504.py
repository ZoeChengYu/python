def main() :
    a_card,b_card,c_card,x_card,y_card,z_card=inport()
    a_point,b_point,c_point,x_point,y_point,z_point=data_Card_Point(a_card),data_Card_Point(b_card),data_Card_Point(c_card),data_Card_Point(x_card),data_Card_Point(y_card),data_Card_Point(z_card)
    Home_point,Guest_point=Sum_point(a_point,b_point,c_point),Sum_point(x_point, y_point, z_point)
    Compares=Compare(Home_point,Guest_point)
    outport(Home_point, Guest_point,Compares)

def inport():
    card_a,card_b,card_c,card_x,card_y,card_z=input(),input(),input(),input(),input(),input()
    return card_a,card_b,card_c,card_x,card_y,card_z

def data_Card_Point(card):
    data_card=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    data_point=[1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
    index=data_card.index(card)#找輸入內容在第幾個元素
    unit_point=data_point[index]#輸出該元素代表值
    return unit_point

def Sum_point(i_point,j_point,k_point):
    Sum_point=i_point+j_point+k_point
    if Sum_point > 10.5:
        Sum_point = 0
    if Sum_point % 1==0:#避免出現2.0這種有小數點的整數
        Sum_point=int(Sum_point)
    return Sum_point

def Compare(Home_point,Guest_point):
    if (Home_point > Guest_point):
        Compare_Result=str('X Win')
    elif (Home_point < Guest_point):
        Compare_Result=str('Y Win')
    else:
        Compare_Result=str('Tie')
    return Compare_Result

def outport(Home_point,Guest_point,Compares):
    print(Home_point)
    print(Guest_point)
    print(Compares)

main()