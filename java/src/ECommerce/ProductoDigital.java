package ECommerce;

class ProductoDigital extends Producto {
    private String URL;
    private double tamaño;
    private double download_time;

    public ProductoDigital(float price) {
        super(price);
        this.URL = URL;
        this.tamaño = tamaño;
        this.download_time = download_time;
    }

    @Override
    double get_download_time() {
        return this.download_time;
    }

    @Override
    double get_weight() {
        return 0;
    }

    @Override
    double get_service_time() {
        return 0;
    }

    @Override
    double get_shipping_cost() {
        return 0;
    }
}
