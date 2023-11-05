package ECommerce;
import java.util.ArrayList;
import java.util.List;

public class Carrito {
    private List<Producto> productos_por_comprar= new ArrayList<>(); //ya infiere que es ArrayList<Producto>
    private double precios=0;
    private double pesos=0;
    private double tiempos_descargas=0;
    private double tiempos_servicios=0;
    private double costo_envio=0;

    public Carrito(){
        this.precios=precios;
        this.pesos=pesos;
        this.tiempos_descargas=tiempos_descargas;
        this.tiempos_servicios=tiempos_servicios;
        this.costo_envio=costo_envio;
        this.productos_por_comprar=productos_por_comprar;
    }

    public void agregar_carrito(Producto producto){ //no tengo que inicalizar el producto? Lo pongo en el constructo?

        if (producto instanceof ProductoDigital) {
            this.tiempos_descargas += producto.get_download_time();
            this.precios += producto.get_price();
            this.productos_por_comprar.add(producto);
        }
        else if(producto instanceof ProductoFisico){ //está tomando producto como si fuera de la clase padre
            if (producto.inventario>=1) {
                this.productos_por_comprar.add(producto);
                this.costo_envio += producto.get_shipping_cost();
                this.pesos += producto.get_weight();
                producto.inventario -= 1;
            }
            else {
                throw new IllegalArgumentException("No hay stock");
            }
        }
        else if(producto instanceof Servicio){
            this.productos_por_comprar.add(producto);
            this.tiempos_servicios+=producto.get_service_time();
        }
    }
    public List eliminar_carrito(Producto producto){
        int pos=productos_por_comprar.indexOf(producto); //--> método de colección ArrayList!!!
        if (pos!=-1){
            productos_por_comprar.remove(pos);
        }
        return productos_por_comprar;
    }

    public double get_precio_maximo() { //no sabía si obtener precio del producto del for o el que pasaba como parametro
        double precio_maximo = 0;
        for (Producto producto : productos_por_comprar) {
            double m = producto.get_price();
            if (m > precio_maximo) {
                precio_maximo = m;
            }
        }
        return precio_maximo;
    }

    public double get_eso_maximo() {
        double peso_maximo = 0;
        for (Producto producto : productos_por_comprar) {
            double m = producto.get_weight();
            if (m > peso_maximo) {
                peso_maximo = m;
            }
        }
        return peso_maximo;
    }
    public double get_tiempo_descarga() {
        double tiempo_descarga_maxima = 0;
        for (Producto producto : productos_por_comprar) {
            double m = producto.get_download_time();
            if (m > tiempo_descarga_maxima) {
                tiempo_descarga_maxima = m;
            }
        }
        return tiempo_descarga_maxima;
    }

    public double get_tiempo_servicio_maximo() {
        double tiempo_servicio_maximo = 0;
        for (Producto producto : productos_por_comprar) {
            double m = producto.get_service_time();
            if (m > tiempo_servicio_maximo) {
                tiempo_servicio_maximo = m;
            }
        }
        return tiempo_servicio_maximo; //si el return dentro del for, en el caso en que productos por comprar vacío, no lo ejecuta y defino que si o si devuelve double
    }

}
