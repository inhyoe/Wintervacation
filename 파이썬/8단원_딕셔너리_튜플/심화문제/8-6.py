student_dic = {'211101':'강이안','211102':'박동민','211103':'김수정'}
print(student_dic['211101'])
print(student_dic['211102'])
print(student_dic['211103'])

new_student_dic = {'211101':['강이안','010-123-3333'],
                   '211102':['박동민','010-123-2222'],
                   '211103':['김수정','010-123-3333']}
search = input('학번을 입력하세요')
print(search,'학생은',new_student_dic[search][0],'이며,전화번호는 : '
      ,new_student_dic[search][1],'입니다.')