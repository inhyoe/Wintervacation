package Java.unit6.ex;
class Car{
    int speed;
    public void setSpeed(int speed){
        this.speed = speed;
    }
}

class SportCar extends Car{
    boolean turbo;
    public void setTurbo(boolean flag){
        turbo = flag;
    }
}

public class Cartest {
    public static void main(String[] args) {
        SportCar obj = new SportCar();
        obj.speed = 10;
        obj.setSpeed(60);
        obj.setTurbo(true);
    }
}
