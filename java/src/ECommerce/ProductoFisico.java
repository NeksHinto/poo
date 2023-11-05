package ECommerce;

class ProductoFisico extends Producto {
    private double peso;
    private String dimensiones;
    private Integer inventario;
    private double shipping_cost;

    public ProductoFisico(float price) {
        super(price);
        this.peso = peso;
        this.dimensiones = dimensiones;
        this.inventario = inventario;
        this.shipping_cost = shipping_cost;
    }

    @Override
    double get_weight() {
        return this.peso;
    }

    @Override
    double get_service_time() {
        return 0;
    }

    @Override
    double get_shipping_cost() {
        return this.shipping_cost;
    }

    @Override
    double get_download_time() {
        return 0;
    }
}
