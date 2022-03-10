function check(form){
    if(form.userid.value == "giicha2" && form.userpassword.value == 1234){
        window.open('target.htm')
    }
    else if(form.userid.value == "giicha2" && form.userpassword.value != 1234){
        alert('비밀번호가 틀렸져 똥똥아!!')
    }else if(form.userid.value != "giicha2" && form.userpassword.value ==1234){
        alert('아이디가 틀렸져!!')
    }else{
        alert('모모모모모모모모!!!')
    }
}