package Java.unit6.ex.new_ex.unit6_3생성자.도전문제;
class Televison{
    private int channel;
    private int volume;
    private boolean onoff;

    public Televison(int channel, int volume,boolean onoff){
        this.channel = channel;
        this.volume = volume;
        this.onoff = onoff;
    }
    // 이것 외의 방법
    /* public Televison(int a,int b, boolean c){
        channel = a;
        volume = b;
        onoff = c;
    } 이렇게 해도 출력 가능.*/
    void print(){
        System.out.println("채널은 " + channel + "볼륨은 " + volume + "전원 상태는" + onoff);
    }
}
public class TelevisonTest {

    public static void main(String[] args) {
        Televison t = new Televison(20, 30, true);
        t.print();
        Televison yourtv = new Televison(14, 23, false);
        yourtv.print();
    }
    
}
