package ECommerce;

class Servicio extends Producto {
    private double duracion;
    private String proveedor;
    private double service_time;

    public Servicio(float price) {
        super(price);
        this.duracion = duracion;
        this.proveedor = proveedor;
        this.service_time = service_time;
    }

    public double get_duracion() {
        return this.duracion;
    }

    @Override
    double get_service_time() {
        return this.service_time;
    }

    @Override
    double get_weight() {
        return 0;
    }

    @Override
    double get_shipping_cost() {
        return 0;
    }

    @Override
    double get_download_time() {
        return 0;
    }


}
