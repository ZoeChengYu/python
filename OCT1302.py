def input_normal():
    RoundX=[int(input())]
    if RoundX[0] != 10:
        RoundX = RoundX + [int(input())]
    return RoundX

def input_last():
    RoundX=[int(input()),int(input())]
    if RoundX[0]+RoundX[1]>=10:
        RoundX = RoundX + [int(input())]
    return RoundX

def main():
    R1,R2,R3=input_normal(),input_normal(),input_last()
    Round_T=R1+R2+R3
    print(Score(Round_T))
    

def Score(data):
    score_total=0
    num=0
    for round_number in range(3):
        if round_number == 2 and (data[num]==10 or data[num]+data[num+1]==10):
            score_total += data[num]+data[num+1]+data[num+2]
        else:
            if(data[num]==10):
                score_total += data[num]+data[num+1]+data[num+2]
                num += 1
            elif(data[num]+data[num+1]==10):
                score_total += data[num]+data[num+1]+data[num+2]
                num += 2
            else:
                score_total += data[num]+data[num+1]
                num += 2
    return score_total
            
main()