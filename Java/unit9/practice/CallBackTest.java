package Java.unit9.practice;

interface ActionListner {
    void actionPerformed(ActionEvent event);
}

class Myclass implements ActionListner {
    public void actionPerformed(AtionEvent event) {
        System.out.println("beep");
    }
}

public class CallBackTest {

}
