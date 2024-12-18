def main ():
    in_call,out_call,city_call,in_message,out_message=inputs()#基本條件輸入
    cost_183=type_183(in_call,out_call,city_call,in_message,out_message)
    cost_383=type_383(in_call,out_call,city_call,in_message,out_message)
    cost_983=type_983(in_call,out_call,city_call,in_message,out_message)
    '''
    Line 2~4 基本條件試算
    '''
    tel_cost=[int(cost_183),int(cost_383),int(cost_983)]
    tel_plan=[183,383,983]
    '''
    Line 9、10 設定矩陣
    '''
    if tel_cost[0]<tel_cost[1] :
        outputs(tel_cost[0],tel_plan[0])
    elif tel_cost[1]<tel_cost[2] :
        outputs(tel_cost[1],tel_plan[1])
    else :
        outputs(tel_cost[2],tel_plan[2])
    '''
    Line 14~19 輸出控制
    '''

def inputs() :
    tel_data=[int(input()),int(input()),int(input()),int(input()),int(input())]
    in_call,out_call,city_call,in_message,out_message=tel_data[0],tel_data[1],tel_data[2],tel_data[3],tel_data[4]
    return in_call,out_call,city_call,in_message,out_message

def type_183(in_call,out_call,city_call,in_message,out_message):
    unit=[0.08,0.1393,0.1349,1.1287,1.4803]
    cost_type_183=in_call*unit[0]+out_call*unit[1]+city_call*unit[2]+in_message*unit[3]+out_message*unit[4]
    if cost_type_183<183:cost_type_183=183
    return cost_type_183

def type_383(in_call,out_call,city_call,in_message,out_message):
    unit=[0.07,0.1304,0.1217,1.1127,1.2458]
    cost_type_383=in_call*unit[0]+out_call*unit[1]+city_call*unit[2]+in_message*unit[3]+out_message*unit[4]
    if cost_type_383<383:cost_type_383=383
    return cost_type_383

def type_983(in_call,out_call,city_call,in_message,out_message):
    unit=[0.06,0.1087,0.1018,0.9572,1.1243]
    cost_type_983=in_call*unit[0]+out_call*unit[1]+city_call*unit[2]+in_message*unit[3]+out_message*unit[4]
    if cost_type_983<983:cost_type_983=983
    return cost_type_983

def outputs(cost,plan):
    print(cost)
    print(plan)
main()