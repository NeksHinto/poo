package ECommerce;
import java.util.List;

abstract class Producto {
    private float price=0;

    public Producto(float price){
        this.price=price;
    }
    public float get_price(){
        return this.price;
    }
    abstract double get_weight();
    abstract double get_service_time();
    abstract double get_shipping_cost();
    abstract double get_download_time();
}
