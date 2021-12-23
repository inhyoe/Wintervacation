package Java.unit6.ex.new_ex.unit6_4생성자_오버로딩.예제;




public class Rectangle {

    private int x,y;
    private int width,height;

    public Rectangle(){
        this( 0 , 0 , 1 , 1);
    }

    Rectangle(int width, int height){
        this(0,0,width,height);
    }

    public Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height =height;
    }
}
