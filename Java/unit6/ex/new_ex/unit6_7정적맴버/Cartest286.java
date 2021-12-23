package Java.unit6.ex.new_ex.unit6_7정적맴버;

class Car{
    private String model;
    private String color;
    private int speed;

    private int id;
    static int numbers; // Car객체를 위한 정적 변수.

    public Car(String m, String c, int s){
        model = m;
        color = c;
        speed = s;
        id = ++numbers;
    }
}


public class Cartest286 {
    public static void main(String[] args) {
        Car c1 = new Car("E500","blue",80);
        Car c2 = new Car("E500", "blue", 20);
        int n = Car.numbers; // car 객체를 위한 정적변수가 몇번 호출 되었는지.
        System.out.println("지금까지 생성된 자동차 수 = " + n);
    }
}
