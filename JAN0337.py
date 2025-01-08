def inputs():
    user={}
    for _ in range(int(input())):
        class_id,term,n=input().split()
        class_id,term,n=int(class_id),int(term),int(n)
        xcx={}
        if str(class_id)[:3] in ['101','201']:
            for _ in range(n):
                student_id,class_point,test_point=input().split()
                student_id,class_point,test_point=int(student_id),int(class_point),int(test_point)
                xcx[student_id]=class_point*0.7+test_point*0.3
        else:
            for _ in range(n):
                student_id,class_point=input().split()
                student_id,class_point=int(student_id),int(class_point)
                xcx[student_id]=class_point
        user[class_id]=[term,xcx]
        
