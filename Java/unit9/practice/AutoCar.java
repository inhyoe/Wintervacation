package Java.unit9.practice;
// 추상메서드를 구현하는 이유가 무엇일까?

interface OperateCar {
    void start();
    void stop();
    void setSpeed(int speed);
    void turn(int degree);
}


public class AutoCar implements OperateCar{
    public void start(){
        System.out.println("자동차가 출발합니다");
    }
    public void stop(){
        System.out.println("자동차가 멈춥니다");
    }
    public void setSpeed(int speed){
        System.out.println("자동차가 속도를" + speed + "로 바꿉니다.");
    }
    public void turn(int degree){
        System.out.println("자동차가 " + degree +" 도 만큼 회전합니다");
    }

    public static void main(String[] args) {
        OperateCar obj = new AutoCar();
        obj.start();
        obj.setSpeed(30);
        obj.turn(70);
        obj.stop();
    }
}
