package Java.unit6.ex.new_ex.unit6_4생성자_오버로딩.랩;

class Time{
    private int hour;
    private int minute;
    private int second;

     Time(){
        this(0,0,0);
    }

     Time(int h,int m,int s){
        hour = h;
        minute = m;
        second = s;
    }

    public String toString(){
        return hour + ":" + minute + ":" + second;
    }
}


public class TimeClass_266 {
    public static void main(String[] args) {
        Time t1 = new Time();
        Time t2 = new Time(23,50, 30);
        System.out.println("첫번째 생성자 " + t1);
        System.out.println("두번째 생성자 " + t2);
    }
}
