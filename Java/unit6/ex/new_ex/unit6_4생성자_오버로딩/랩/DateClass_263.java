package Java.unit6.ex.new_ex.unit6_4생성자_오버로딩.랩;


class Date{
    private int year ;
    private String month ;
    private int day  ;

    public Date(){
        this(1990,"1월",1);
    }


    public Date(int y){
        this(y,"1월",1);
    }

    public Date(int year, String month, int day){
        this.year = year;
        this.month = month;
        this.day = day;
    }
    /* public Date(int y, String m, int d){
        y = year;
        m = month;
        d = day;
        이렇게 할 시 왜 출력이 안될까?
        왜나하면 상위 상속자들이 this를 사용하기 때문이다.
    } */
   

    public String toString(){
        return "Date [ year = "+ year + ", month" +month +"월, "
        + "day = " +day + "]";
    }

}





public class DateClass_263 {
    public static void main(String[] args) {
        Date ymd = new Date(2015, "8월", 10);
        Date d = new Date();
        Date year = new Date(2020);
        
        System.out.println(ymd);
        System.out.println(year);
        System.out.println(d);

    }
}
