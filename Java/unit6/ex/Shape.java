package Java.unit6.ex;;

class Shape1 {
    // int x , y 를 하지 않는 이유는 다른 곳에서도 쓰기 위함.
    private int x;
    private int y;
    public int getX(){
        return x;
    }
    public void setX(int x){
        this.x = x;
    }
    public int getY(){
        return y;
    }
    public void setY(int y){
        this.y = y;
    }
    void print(){
        System.out.println("도형의 위치는 \nx위치: "+x+
        "\n"+"y위치: "+y);
    }
}

class Rectangle extends Shape1{
    private int width;
    private int height;
    public int Getwidth(){
        return width;
    }
    public void Setwidth(int width){
        this.width = width;
    }
    
    public int Getheight(){
        return height;
    }
    public void Setheight(int height){
        this.height = height;
    }
    double area;
    void area(){
        area = width * height;
        System.out.println("도형의 넓이는: " +area);
    }
    void draw(){
        System.out.println("(" + this.getX()+","+this.getY()+
        ") 위치에 \n" + "가로: " + width + "세로: " + height );
    }
   

}


public class Shape {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.setX(15); 
        r.setY(15);
        r.Setwidth(25);
        r.Setheight(20);
        r.area();
        r.print();
        r.draw();
    }
}
